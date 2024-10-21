###########################
### GET CAPDATA SUMMARY ###
###########################

get_capData_summary <- function(capData, whichSpecies) {
  
  # initialize df
  df <- data.frame(
    species = whichSpecies,
    captureYear = min(capData$captureYear):max(capData$captureYear),
    capPeriod_start = NA,
    capPeriod_end = NA,
    capDuration_days = NA,
    nGroups = NA,
    nF = NA,
    nM = NA,
    nTotal = NA,
    nRecap = NA,
    nNew = NA,
    propRecap = NA,
    propNew = NA,
    capPeriod_mid = NA,
    capInterval_days = NA
  )
  
  # basic info
  for (y in df$captureYear) {
    
    # subset dataframe to captureYear "y"
    capData_y <- capData %>%
      filter(species == whichSpecies) %>%
      filter(captureYear == y) %>%
      # select only first capture event per animalID in year y
      arrange(captureDate) %>%
      group_by(animalID) %>%
      slice(1) %>%
      ungroup() %>%
      as.data.frame()
    
    # get cap start, end, duration (days), and cap mid
    capPeriod_y <- data.frame(
      capPeriod_start = min(capData_y$captureDate),
      capPeriod_end = max(capData_y$captureDate)
    ) %>%
      mutate(
        capDuration_days = as.double(
          difftime(
            as.Date(capPeriod_end),
            as.Date(capPeriod_start),
            units = c("days"))
        )
      )
    
    # count groups, indivs, and F/M captured
    basicCounts_y <- capData_y %>%
      summarise(
        nGroups = length(unique(groupName)),
        nF = length(unique(animalID[sex == "F"])),
        nM = length(unique(animalID[sex == "M"])),
        nTotal = length(unique(animalID))
      )
    
    # count number of new indivs captured
#    if (y > min(capData$captureYear)) {
#      capData_prev <- capData %>%
#        filter(species == whichSpecies) %>%
#        filter(captureYear == (y - 1))
      
      if (y > min(capData$captureYear)) {
        capData_prev <- capData %>%
          filter(species == whichSpecies) %>%
          # subset captureYear to all prior to current year y
          filter(captureYear %in% c(min(capData$captureYear):(y - 1)))
      nNew_y <- sum(!capData_y$animalID %in% capData_prev$animalID)
      nRecap_y <- sum(capData_y$animalID %in% capData_prev$animalID)
    } else {
      nNew_y <- nrow(capData_y)  # all are new in the first year
      nRecap_y <- 0
    }
    
    # append data for each "y" to df
    df[df$captureYear == y, c("capPeriod_start", "capPeriod_end", "capDuration_days", "nGroups", "nF", "nM", "nTotal", "nRecap", "nNew")] <- 
      c(capPeriod_y$capPeriod_start, capPeriod_y$capPeriod_end, capPeriod_y$capDuration_days, basicCounts_y$nGroups, basicCounts_y$nF, basicCounts_y$nM, basicCounts_y$nTotal, nRecap_y, nNew_y)
  }
  
  # get propRecap & propNew
  df$propRecap <- round(ifelse(as.numeric(df$nTotal) > 0, as.numeric(df$nRecap) / as.numeric(df$nTotal), NA), 2)
  df$propNew <- round(ifelse(as.numeric(df$nTotal) > 0, as.numeric(df$nNew) / as.numeric(df$nTotal), NA), 2)
  
  # get interval b/t capPeriod_start and preceding captureYear's capPeriod_end
  df <- df %>%
    mutate(
      capPeriod_mid = as.Date(capPeriod_start) + as.numeric(capDuration_days),
      capInterval_days = as.numeric(as.Date(capPeriod_mid) - lag(as.Date(capPeriod_mid)))
    ) %>%
    relocate(c(capPeriod_mid, capInterval_days), .before = capDuration_days)
  
  return(df)
  
}

############################
### GET POPDATA PER YEAR ###
############################

get_popData_byYear <- function(
    capData,
    whichSpecies = c("LWED", "SIMP"),
    whichYears, # e.g., 2009:2019
    whichAnimalIDs = c("all", "with_hairSamples"), # all in capData? or just those with hair samples for genetics?
    md_genoData = NULL,
    birthData = NULL,
    adultsOnly = NULL # subset to adults only?
    ) {
  
  # initialize list to store dataframes for each year
  popData_list <- list()
  
  # add birth data if provided
  if(!is.null(birthData)){
    capData <- merge(capData, birthData, by = "animalID", all.x = T)
  }else{
    capData <- capData %>%
      mutate(
        birthDate_est = NA,
        birthYear_est = NA
      )
  }
  
  # get list of animalIDs
  if(whichAnimalIDs == "all") {
    animalID.list <- capData %>%
      select(animalID) %>%
      filter(animalID != "UNK") %>% # remove any "UNK" animalIDs
      distinct() %>%
      pull()
  } else if(whichAnimalIDs == "with_hairSamples") {
    animalID.list <- md_genoData %>%
      filter(sampleType == "hair") %>%
      select(animalID) %>%
      distinct() %>%
      pull()
  }
  
  for (y in whichYears) {
    
    # create dataframe for population in captureYear "y"
    popData_y <- capData %>%
      filter(animalID %in% animalID.list) %>%
      filter(captureYear == y) %>%
      # select only first capture event per animalID in year y
      group_by(animalID) %>%
      slice_min(captureDate) %>%
      ungroup() %>%
      as.data.frame() %>%
      select(animalID, groupName, ageClass, birthDate_est, birthYear_est) %>%
      mutate(
        born_thisSeason = case_when(
          birthYear_est == y ~ TRUE,
          .default = FALSE
        )
      )
    
    # subset to adults only if desired
    if(!is.null(adultsOnly)){
      popData_y <- popData_y %>%
        filter(born_thisSeason == FALSE)
    }else{
      popData_y <- popData_y
    }
    
    # add each dataframe to list w/year as name
    popData_list[[as.character(y)]] <- popData_y
    
  }
  
  return(popData_list)
  
}

####################################
### GET HIERFSTAT GENOS PER YEAR ###
####################################

get_genos_perYear_forHierfstat <- function(
    genoData_hf, # geno data already in hf format
    popData,
    sampleRef
) {
  
  # assign animalIDs to genoData
  genos <- genoData_hf %>%
    merge(sampleRef[, c("sampleID", "animalID")], by.x = 0, by.y = "sampleID") %>%
    relocate(animalID) %>%
    select(-Row.names, -pop)
  
  # append geno data to popData  
  genoData_perYear_temp <- lapply(popData, "[", 1:2) %>%
    map(., ~ .x %>%
          # rename cols
          set_names(c("animalID", "pop")) %>% 
          # add sex (code as factor)
          merge(sampleRef[, c("animalID", "sex")], by = "animalID", all.x = T) %>%
          mutate(sex = as.factor(sex)) %>%
          # add genos
          merge(genos, by = "animalID") %>%
          arrange(pop, animalID)
    )
  
  # Organize the results by year
  genoData_perYear <- map2(names(popData), genoData_perYear_temp, ~ {
    list(
      genoData = select(.y, -c(animalID, sex)), 
      sexData = .y$sex  
    )
  })
  
  # Name the list by years (assuming popData is named by years)
  names(genoData_perYear) <- names(popData)
  
  return(genoData_perYear)
}

#########################
### GET PARITY STATUS ###
#########################

get_parityStatus <- function(capData_file) {
  
  parityAssignments <- capData_file %>%
    filter(sex == "F") %>%
    select(animalID, species, captureDate, ageClass, nippleL_length, nippleR_length) %>%
    arrange(as.numeric(animalID), captureDate) %>%
    # calculate mean nipple length
    mutate(
      nippleL_length = case_when(
        str_detect(nippleL_length, "<") ~ "0",
        str_detect(nippleR_length, "small") ~ "0",
        .default = nippleL_length
      ),
      nippleR_length = case_when(
        str_detect(nippleR_length, "<") ~ "0",
        str_detect(nippleR_length, "small") ~ "0",
        .default = nippleR_length
      ),
      nippleL_length = as.numeric(nippleL_length),
      nippleR_length = as.numeric(nippleR_length)
    ) %>%
    rowwise() %>%
    mutate(
      nippleMean = mean(c_across(c(nippleL_length, nippleR_length)), na.rm = T),
      nippleMean = round(nippleMean, digits = 2)
    ) %>%
    # assign parity
    mutate(
      parity = case_when(
        is.na(nippleL_length) & is.na(nippleR_length) ~ "noMeasure",
        species == "LWED" & nippleMean >= 3 ~ "parous",
        species == "SIMP" & nippleMean >= 4 ~ "parous",
        .default = "nulliparous"
      ),
      parity2 = case_when(
        is.na(nippleL_length) & is.na(nippleR_length) ~ "noMeasure",
        species == "LWED" & nippleL_length >= 3 ~ "parous",
        species == "LWED" & nippleR_length >= 3 ~ "parous",
        species == "SIMP" & nippleL_length >= 4 ~ "parous",
        species == "SIMP" & nippleR_length >= 4 ~ "parous",
        .default = "nulliparous"
      )
    ) %>%
    arrange(as.numeric(animalID), captureDate)
  
  return(parityAssignments)
  
}

#######################
### READ FRANZ SIBS ###
#######################

read_franzSibs <- function(sibFile_path) {
  
  sibFile <- readLines(sibFile_path)
  
  colnames_sibs <- c("sample1",
                     "sample2",
                     "FS",
                     "PO",
                     "HS",
                     "pV_PO",
                     "pV_HS",
                     "pV_U",
                     "commonParents",
                     "commonLoci")
  
  # accepted dyads
  startLine_table1 <- grep("Genotype 1", sibFile)[1] + 2
  endLine_table1 <- grep("Rejected", sibFile)[1] - 5
  
  sibs_table1 <- sibFile[startLine_table1:endLine_table1] %>%
    as.data.frame() %>%
    dplyr::rename("temp" = ".") %>%
    mutate(
      temp = gsub(" ", "", temp),
      temp = str_sub(temp, 2, -2)
    ) %>%
    separate(temp, into = colnames_sibs, sep = "\\|") %>%
    mutate(dyadStatus = "accepted")
  
  
  # rejected dyads
  startLine_table2 <- grep("Rejected", sibFile)[1] + 2
  endLine_table2 <- grep("TOTAL \\(REJECTED!)", sibFile)[1] - 3
  
  sibs_table2 <- sibFile[startLine_table2:endLine_table2] %>%
    as.data.frame() %>%
    dplyr::rename("temp" = ".") %>%
    mutate(
      temp = gsub(" ", "", temp),
      temp = str_sub(temp, 2, -2)
    ) %>%
    separate(temp, into = colnames_sibs, sep = "\\|") %>%
    mutate(dyadStatus = "rejected")
  
  sibs_df <- rbind(sibs_table1, sibs_table2)
  
  return(sibs_df)
  
}