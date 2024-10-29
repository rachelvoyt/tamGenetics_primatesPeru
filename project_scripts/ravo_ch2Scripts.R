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

#####################################
### RECODE ALLELE READS BY CUTOFF ###
#####################################

# readCounts: df with rownames = loci, colnames = samples
# coverageCutoff: integer w/desired coverage cutoff

get_readSum.Recode <- function(readCounts, coverageCutoff) {
  
  library(gsubfn)
  
  repl <- function(x) gsubfn("(\\d+),(\\d+)", ~ as.numeric(x) + as.numeric(y), paste(x))
  
  readSums <- replace(readCounts, TRUE, lapply(readCounts, repl)) %>%
    mutate(across(everything(), as.numeric))
  
  readCounts[readSums < coverageCutoff] <- NA
  
  return(readCounts)
}

##########################################
### GET OPTIONS FOR SAMPLE/LOCI COMBOS ###
##########################################

# This function returns the # of loci w/non-missing values for the specified 
# proportion of n samples ("propSamples") for subsets of 2 to total samples;
# function will optimize sample/loci combos based on paired data across 3 dfs,
# specifcally for paired blood, fecal, and hair samples

# Input file notes:
## **IMPORTANT:** The three input files must be formatted such that the rows 
## and columns are in the exact same order.
## all dfs should have rownames = loci and colnames = samples

getOptions_optSamplesLoci_bfh <- function(df_blood, df_fecal, df_hair, propSamples) {
  
  # Initialize an empty list to store results
  result_list <- list()
  
  # convert genos to binary matrix (NAs = 0, non-NAs = 1)
  matrix1 <- ifelse(is.na(df_blood), 0, 1)
  matrix2 <- ifelse(is.na(df_fecal), 0, 1)
  matrix3 <- ifelse(is.na(df_hair), 0, 1)
  
  # multiply matrices
  matrix_prod <- matrix1 * matrix2 * matrix3
  
  # create new combo df (turn 0 back to NA)
  df4 <- as.data.frame(matrix_prod) %>%
    mutate(across(everything(), ~na_if(., 0)))
  
  # identify sample/loci counts w/100% geno success
  for (n_samples in 2:ncol(df_blood)) {
    
    crossprod_vector <- crossprod(matrix_prod)
    col_sums <- colSums(crossprod_vector)
    
    x_df <- as.data.frame(df4)  # to get meaningful colnames
    
    # use colSums vector to select n columns;
    # will rank all columns and give the n first;
    # gives n columns w/the max number of non-NA rows
    res <- x_df[, rank(-col_sums, ties.method = "first") <= n_samples]
    
    # Store the result in the list
    result_list[[as.character(n_samples)]] <- c(n_samples, nrow(res[which(rowMeans(!is.na(res)) >= propSamples), ]))
  }
  
  # Convert the list to a dataframe
  result_df <- do.call(rbind, result_list) %>%
    as.data.frame()
  
  # Rename columns
  colnames(result_df) <- c("samples", "loci")
  
  return(result_df)
}

########################################
### SUBSET TO OPTIMIZED SAMPLES/LOCI ###
########################################

# For a given dataframe of genotypes or allele reads, this function returns
# an optimized set of genotypes for n_samples, where the number of samples
# and the proportion of those n samples successfully genotyped per locus (propSamples)
# is chosen based on the results of function 1 above

optimized_genos <- function(df, n_samples, propSamples) {
  matrix <- ifelse(is.na(df), 0, 1)
  crossprod_vector <- crossprod(matrix)
  col_sums <- colSums(crossprod_vector)
  
  x_df <- as.data.frame(df)
  res <- x_df[, rank(-col_sums, ties.method = "first") <= n_samples]
  
  result <- res[which(rowMeans(!is.na(res)) >= propSamples), ]
  return(result)
}

#########################################
### DOWNSAMPLE + GENOTYPE CONSISTENCY ###
#########################################

get_dsReadCounts.genoConsistency <- function(
    alleleReads_file, locusTable, n_reads, n_iterations
) {
  
  library(stringi)
  source("./project_scripts/GTscore/GTscore_modified.R")
  
  # prep locus table & reformat locus names
  locusTable <- locusTable %>%
    mutate(locus = sub('[_][^_]+$', '', Locus_ID)) %>%
    filter(locus %in% row.names(alleleReads_file))
  alleleReads_file <- alleleReads_file %>%
    rownames_to_column("locus") %>%
    merge(., locusTable[, c("locus", "Locus_ID")], by = "locus") %>%
    column_to_rownames("Locus_ID") %>%
    select(-locus)
  locusTable <- locusTable %>%
    select(-locus)
  
  # set up a/b string version of read counts
  df1 <- alleleReads_file %>%
    rownames_to_column("locus") %>%
    pivot_longer(!locus,
                 names_to = "sampleID",
                 values_to = "readCounts") %>%
    relocate(sampleID) %>%
    arrange(sampleID) %>%
    # separate read counts for allele 1 and allele 2
    separate(readCounts, into = c("readCounts_a1", "readCounts_a2"), sep = ",") %>%
    mutate(
      readCounts_a1 = as.numeric(readCounts_a1),
      readCounts_a2 = as.numeric(readCounts_a2),
      
      # replace NA w/0
      readCounts_a1 = replace_na(readCounts_a1, 0),
      readCounts_a2 = replace_na(readCounts_a2, 0)
    ) %>%
    # create "a/b" character strings based on allele counts
    rowwise() %>%
    mutate(
      vec_a1 = case_when(
        readCounts_a1 > 0 ~ paste(replicate(readCounts_a1, "a"), collapse = ""),
        .default = NA),
      vec_a2 = case_when(
        readCounts_a2 > 0 ~ paste(replicate(readCounts_a2, "b"), collapse = ""),
        .default = NA
      )
    )
  
  # get downsampled read counts x n_iterations
  df3 <- data.frame() # initialize empty df
  
  for (i in 1:n_iterations) {
    
    df2 <- df1 %>%
      mutate(
        n_iter = i,
        # randomly combine "a" and "b" allele strings & combine as a list
        vec_a1a2 = stri_rand_shuffle(str_c(vec_a1, vec_a2)),
        # downsample by extracting the first "n_reads" characters
        # from each string in the list
        ds_vec_a1a2 = list(substr(vec_a1a2, 1, n_reads)),
        # count the number of a's & b's in each string in the list,
        # then convert to read counts
        ds_readCounts = str_c(str_count(ds_vec_a1a2, "a"),
                              str_count(ds_vec_a1a2, "b"),
                              sep = ",")
      ) %>%
      select(sampleID, locus, n_iter, ds_readCounts)
    
    # append data for each "i"
    df3 <- bind_rows(df3, df2)
    
  }
  
  # once we have have df with downsampled read counts for all n_iterations,
  # reformat for input into GTscore polygen function
  alleleReads_all.iter <- df3 %>%
    unite(sampleID, c("sampleID", "n_iter"), sep = "_") %>%
    pivot_wider(id_cols = locus,
                names_from = "sampleID",
                values_from = "ds_readCounts") %>%
    column_to_rownames("locus")
  alleleReads_all.iter[is.na(alleleReads_all.iter)] <- "0,0"
  
  # genotype w/polygen
  genos_all.iter <- polyGen(locusTable, alleleReads_all.iter) %>%
    as.data.frame()
  
  # compare genos
  ## get colnames for later
  colNames <- str_c("iter_", 1:n_iterations)
  
  genoCompare_all.iter <- genos_all.iter %>%
    t() %>%
    as.data.frame() %>%
    rownames_to_column("sampleID") %>%
    pivot_longer(-sampleID,
                 names_to = "locus",
                 values_to = "genos") %>%
    mutate(genos = na_if(genos, "0")) %>%
    separate(sampleID, into = c("sampleID", "n_iter"), sep = "_") %>%
    mutate(n_iter = str_c("iter_", n_iter)) %>%
    pivot_wider(id_cols = c(sampleID, locus),
                names_from = n_iter,
                values_from = genos) %>%
    merge(., locusTable, by.x = "locus", by.y = "Locus_ID") %>%
    # Set up genotypes to check against
    separate(alleles, into = c("allele1", "allele2"), sep = ",") %>%
    mutate(
      a1hom = str_c(allele1, allele1, sep = ","),
      a2hom = str_c(allele2, allele2, sep = ","),
      het = str_c(allele1, allele2, sep = ",")
    ) %>%
    # Generate the counts for each genotype category
    mutate(
      n_a1hom = rowSums(select(., all_of(colNames)) == a1hom, na.rm = TRUE),
      n_a2hom = rowSums(select(., all_of(colNames)) == a2hom, na.rm = TRUE),
      n_het = rowSums(select(., all_of(colNames)) == het, na.rm = TRUE),
      
      totalGenos = rowSums(across(c("n_a1hom", "n_a2hom", "n_het")), na.rm = TRUE),
      
      prop_a1hom = n_a1hom / totalGenos,
      prop_a2hom = n_a2hom / totalGenos,
      prop_het = n_het / totalGenos
    ) %>%
    # remove those w/zero genos assigned
    filter(totalGenos > 0) %>%
    # Calculate the max genotype class and proportion match
    rowwise() %>%
    mutate(
      max_genoClass = paste0(names(.[, c("n_a1hom", "n_a2hom", "n_het")])[c_across(n_a1hom:n_het) == max(c_across(n_a1hom:n_het))], collapse = '/'),
      max_propMatch = max(prop_a1hom, prop_a2hom, prop_het, na.rm = TRUE)
    ) %>%
    ungroup() %>%
    # Select final columns
    select(sampleID, locus, allele1, allele2, max_genoClass, max_propMatch, totalGenos, prop_a1hom, prop_a2hom, prop_het, n_a1hom, n_a2hom, n_het)
  
  
  return(genoCompare_all.iter)
  
}