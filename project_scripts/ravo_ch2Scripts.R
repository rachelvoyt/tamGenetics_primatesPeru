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
    capPeriod_days = NA,
    nGroups = NA,
    nF = NA,
    nM = NA,
    nTotal = NA,
    nRecap = NA,
    nNew = NA,
    propRecap = NA,
    propNew = NA
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
    
    # get cap start, end, and duration (days)
    capPeriod_y <- data.frame(
      capPeriod_start = min(capData_y$captureDate),
      capPeriod_end = max(capData_y$captureDate)
    ) %>%
      mutate(
        capPeriod_days = as.double(
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
    if (y > min(capData$captureYear)) {
      capData_prev <- capData %>%
        filter(species == whichSpecies) %>%
        filter(captureYear == (y - 1))
      nNew_y <- sum(!capData_y$animalID %in% capData_prev$animalID)
      nRecap_y <- sum(capData_y$animalID %in% capData_prev$animalID)
    } else {
      nNew_y <- nrow(capData_y)  # all are new in the first year
      nRecap_y <- 0
    }
    
    # append data for each "y" to df
    df[df$captureYear == y, c("capPeriod_start", "capPeriod_end", "capPeriod_days", "nGroups", "nF", "nM", "nTotal", "nRecap", "nNew")] <- 
      c(capPeriod_y$capPeriod_start, capPeriod_y$capPeriod_end, capPeriod_y$capPeriod_days, basicCounts_y$nGroups, basicCounts_y$nF, basicCounts_y$nM, basicCounts_y$nTotal, nRecap_y, nNew_y)
  }
  
  # get propRecap & propNew
  df$propRecap <- round(ifelse(as.numeric(df$nTotal) > 0, as.numeric(df$nRecap) / as.numeric(df$nTotal), NA), 2)
  df$propNew <- round(ifelse(as.numeric(df$nTotal) > 0, as.numeric(df$nNew) / as.numeric(df$nTotal), NA), 2)
  
  return(df)
  
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