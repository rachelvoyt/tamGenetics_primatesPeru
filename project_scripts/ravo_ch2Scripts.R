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
    adultsOnly = F # subset to adults only?
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
    if(adultsOnly == T){
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

##########################
### GET GENOS PER YEAR ###
##########################

get_genos_perYear <- function(
    genoData_df, # geno dataframe
    genos_startCol,
    popData,
    sampleRef,
    outputFormat = c("genind", "hierfstat", "related")
) {
  
  # Initialize list to store yearly genoData
  genoData_perYear <- list()
  
  for (year in names(popData)) {
    # Subset genoData_df for individuals present in the year as per popData
    year_data <- genoData_df %>%
      merge(., popData[[year]][, c("animalID", "groupName")], by = "animalID") %>%
      mutate(pop = groupName) %>%
      select(-groupName)
      #filter(animalID %in% popData[[year]]$animalID)
    
    # Check if year_data is empty and skip if no individuals are present
    if (nrow(year_data) == 0) next
    
    # Remove columns where all values are NA (no scored alleles)
    year_geno_data <- year_data[, c(genos_startCol:ncol(genoData_df))]
    year_geno_data <- year_geno_data[, colSums(is.na(year_geno_data)) < nrow(year_geno_data)]
    
    # Convert the subsetted data to the chosen format
    if (outputFormat == "genind") {
      # Create genind object for the year
      genind_obj <- adegenet::df2genind(
        X = year_geno_data,
        sep = ",",
        ind.names = year_data$sampleID,
        pop = year_data$pop,
        NA.char = "NA",
        ploidy = 2,
        type = "codom"
      )
      genind_obj@other$sex <- year_data$sex
      genind_obj@other$birthYear <- year_data$birthYear_est
      genind_obj@other$captureYear <- year_data$captureYear
      
      genoData_perYear[[year]] <- genind_obj
      
    } else if (outputFormat == "hierfstat") {
      # First create genind object for the year
      genind_obj <- adegenet::df2genind(
        X = year_geno_data,
        sep = ",",
        ind.names = year_data$sampleID,
        pop = year_data$pop,
        NA.char = "NA",
        ploidy = 2,
        type = "codom"
      )
      # Convert genind to hierfstat
      hierfstat_data <- genind2hierfstat(genind_obj) %>%
        rownames_to_column("sampleID") %>%
        merge(., sampleRef[, c("sampleID", "sex")], by = "sampleID") %>%
        arrange(pop, sampleID)
        
        #popData[[year]] %>%
        #rename(animalID = sampleID, pop = population) %>%
        #left_join(sampleRef[, c("animalID", "sex")], by = "animalID") %>%
        #left_join(genos, by = "animalID") %>%
        #arrange(pop, animalID)
      
      genoData_perYear[[year]] <- list(
        genoData = select(hierfstat_data, -sex),
        sexData = hierfstat_data$sex
      )
    } else if (outputFormat == "related") {
      # Process for related format
      related_data_temp <- year_data %>%
        mutate(animalID = str_c(str_sub(pop, 1, 2), animalID, sep = "_")) %>%
        select(-pop) %>%
        select(c(animalID, contains(c("INDID", "SPECIES", "SEX", "LWED", "SIMP"))))
      
      related_data_temp2 <- related_data_temp %>%
        select(-sex) %>%
        column_to_rownames("animalID")
      
      related_data <- names(related_data_temp2) %>%
        map_dfc(~ related_data_temp2 %>%
                  select(all_of(.x)) %>%
                  separate(.x,
                           into = paste0(.x, c("a", "b")),
                           sep = ",")
        ) %>%
        mutate_all(~ str_replace(., "A", "4")) %>%
        mutate_all(~ str_replace(., "T", "7")) %>%
        mutate_all( ~ str_replace(., "C", "3")) %>%
        mutate_all(~ str_replace(., "G", "6")) %>%
        rownames_to_column("animalID") %>%
        merge(., related_data_temp[, c("animalID", "sex")], by = "animalID") %>%
        relocate(sex, .after = animalID)
      
      genoData_perYear[[year]] <- list(
        genoData = select(related_data, -sex),
        sexData = related_data$sex
      )
    }
  }
  
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
## all dfs should have rownames = loci; colnames = samples

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

# Version for single dataframe:
getOptions_optSamplesLoci <- function(df, propWhat, propSuccess) {
  
  # Initialize an empty list to store results
  result_list <- list()
  
  for (n in 2:ncol(df)) {
    # create matrix where NAs are 0 and non-NAs are 1
    is_na_vector <- ifelse(is.na(df), 0, 1)
    
    crossprod_vector <- crossprod(is_na_vector)
    col_sums <- colSums(crossprod_vector)
    
    x_df <- as.data.frame(df)  # to get meaningful colnames
    
    # use colSums vector to select n columns;
    # will rank all columns and give the n first;
    # gives n columns w/the max number of non-NA rows
    res <- x_df[, rank(-col_sums, ties.method = "first") <= n]
    
    # Store the result in the list
    result_list[[as.character(n)]] <- c(n, nrow(res[which(rowMeans(!is.na(res)) >= propSuccess), ]))
  }
  
  # Convert the list to a dataframe
  result_df <- do.call(rbind, result_list) %>%
    as.data.frame()
  
  # Rename columns
  if (propWhat == "samples") {
    colnames(result_df) <- c("samples", "loci")
  }
  if (propWhat == "loci") {
    colnames(result_df) <- c("loci", "samples")
  }
  
  
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

##############################
### GROUPREL - MY VERSIONS ###
##############################

get_grouprel <- function (genotypes, estimatorname, usedgroups, iterations, outdir, prefix) 
{
  if (estimatorname == "trioml") {
    estimator = 5
  }
  if (estimatorname == "wang") {
    estimator = 6
  }
  if (estimatorname == "lynchli") {
    estimator = 7
  }
  if (estimatorname == "lynchrd") {
    estimator = 8
  }
  if (estimatorname == "ritland") {
    estimator = 9
  }
  if (estimatorname == "quellergt") {
    estimator = 10
  }
  if (estimatorname == "dyadml") {
    estimator = 11
  }
  if (estimatorname == "trioml") {
    relatives <- coancestry(genotypes, trioml = 1)
  }
  if (estimatorname == "wang") {
    relatives <- coancestry(genotypes, wang = 1)
  }
  if (estimatorname == "lynchli") {
    relatives <- coancestry(genotypes, lynchli = 1)
  }
  if (estimatorname == "lynchrd") {
    relatives <- coancestry(genotypes, lynchrd = 1)
  }
  if (estimatorname == "ritland") {
    relatives <- coancestry(genotypes, ritland = 1)
  }
  if (estimatorname == "quellergt") {
    relatives <- coancestry(genotypes, quellergt = 1)
  }
  if (estimatorname == "dyadml") {
    relatives <- coancestry(genotypes, dyadml = 1)
  }
  rels <- relatives$relatedness
  if (usedgroups[1] == "all") {
    groupsall <- 1:length(rels[, 1])
    for (i in 1:length(rels[, 1])) {
      groupsall[i] <- substr(rels[i, 2], 1, 2)
    }
    groups <- unique(groupsall)
  }
  else {
    groups <- usedgroups
  }
  within <- paste(groups, groups, sep = "")
  relvalues <- 1:length(within)
  sizes <- 1:length(within)
  cat("\n Calculating within-group r-values...\n")
  for (i in 1:length(within)) {
    holder <- 0
    counter1 <- 0
    for (j in 1:length(rels[, 1])) {
      if (rels[j, 4] == within[i]) {
        holder <- holder + rels[j, estimator]
        counter1 <- counter1 + 1
      }
    }
    relvalues[i] <- holder/counter1
    sizes[i] <- counter1
    cat(sprintf("Group %s \t %f\n", within[i], relvalues[i]))
  }
  overallobs <- sum(relvalues)/length(relvalues)
  cat(sprintf("Overall \t %f\n", overallobs))
  
  obsrel <- cbind(within, relvalues)
  write.csv(obsrel, paste(outdir, prefix, "observed-r.csv", sep = ""))
  
  simresults <- data.frame(matrix(nrow = iterations, ncol = (length(within) + 
                                                               1)))
  for (j in 1:iterations) {
    cat(sprintf("Iteration %d\n", j))
    randlist <- 1:length(genotypes[, 1])
    randlist <- sample(randlist, length(randlist), replace = FALSE)
    randgenos <- data.frame(matrix(nrow = length(randlist), 
                                   ncol = length(genotypes[1, ])))
    for (i in 1:length(randlist)) {
      randgenos[i, ] <- genotypes[randlist[i], ]
    }
    if (estimatorname == "trioml") {
      simrels <- coancestry(randgenos, trioml = 1)
    }
    if (estimatorname == "wang") {
      simrels <- coancestry(randgenos, wang = 1)
    }
    if (estimatorname == "lynchli") {
      simrels <- coancestry(randgenos, lynchli = 1)
    }
    if (estimatorname == "lynchrd") {
      simrels <- coancestry(randgenos, lynchrd = 1)
    }
    if (estimatorname == "ritland") {
      simrels <- coancestry(randgenos, ritland = 1)
    }
    if (estimatorname == "quellergt") {
      simrels <- coancestry(randgenos, quellergt = 1)
    }
    if (estimatorname == "dyadml") {
      simrels <- coancestry(randgenos, dyadml = 1)
    }
    counter1 <- 1
    counter2 <- 0
    for (k in 1:length(within)) {
      holder <- 0
      counter3 <- 0
      num <- sizes[k]
      counter2 <- num
      for (l in counter1:(counter2 + counter1 - 1)) {
        holder <- holder + simrels$relatedness[l, estimator]
        counter3 <- counter3 + 1
      }
      simresults[j, k] <- holder/counter3
      counter1 <- counter2 + counter1
    }
    simresults[j, length(within) + 1] <- sum(simresults[j, 
                                                        1:length(within)])/length(within)
  }
  
  write.csv(simresults, paste(outdir, prefix, "expectedrel.csv", sep = ""))
  minx <- 0
  maxx <- 0
  for (k in 1:length(within)) {
    if (min(simresults[, k]) < relvalues[k]) {
      minx <- min(simresults[, k]) - 0.2
    }
    else {
      minx <- relvalues[k] - 0.2
    }
    if (max(simresults[, k]) > relvalues[k]) {
      maxx <- max(simresults[, k]) + 0.2
    }
    else {
      maxx <- relvalues[k] + 0.2
    }
    hist(simresults[, k], main = within[k], xlim = c(minx, 
                                                     maxx), xlab = "Relatedness")
    arrows(x0 = relvalues[k], y0 = iterations * 0.15, x1 = relvalues[k], 
           y1 = 0, col = "red", lwd = 3)
    ptest <- signif(((sum(simresults[, k] >= relvalues[k]) + 
                        1)/iterations), 3)
    mtext(bquote(p < .(ptest)), side = 3)
  }
  if (min(simresults[, length(within) + 1]) < overallobs) {
    minx <- min(simresults[, length(within) + 1]) - 0.2
  }
  else {
    minx <- overallobs - 0.2
  }
  if (max(simresults[, length(within) + 1]) > overallobs) {
    maxx <- max(simresults[, length(within) + 1]) + 0.2
  }
  else {
    maxx <- overallobs + 0.2
  }
  hist(simresults[, length(within) + 1], main = "Overall", 
       xlim = c(minx, maxx), xlab = "Relatedness")
  arrows(x0 = overallobs, y0 = iterations * 0.15, x1 = overallobs, 
         y1 = 0, col = "red", lwd = 3)
  ptest <- signif(((sum(simresults[, length(within) + 1] >= 
                          overallobs) + 1)/iterations), 3)
  mtext(bquote(p < .(ptest)), side = 3)
  
  # Initialize list to store p-values for summary
  p_values <- list()
  
  # Collect p-values for each within group
  for (k in 1:length(within)) {
    ptest <- signif(((sum(simresults[, k] >= relvalues[k]) + 1) / iterations), 3)
    p_values[[within[k]]] <- list(relvalue = relvalues[k], ptest = ptest)
  }
  
  # Collect overall p-value
  overall_ptest <- signif(((sum(simresults[, length(within) + 1] >= overallobs) + 1) / iterations), 3)
  
  # Save output to observed-r and expectedrel CSVs
  write.csv(obsrel, paste(outdir, prefix, "observed-r.csv", sep = ""))
  write.csv(simresults, paste(outdir, prefix, "expectedrel.csv", sep = ""))
  
  # Return values for summary
  return(list(within_relvalues = p_values, overall_relvalue = overallobs, overall_ptest = overall_ptest))
  
}
