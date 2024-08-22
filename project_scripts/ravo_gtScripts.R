######################
### ASSIGN SPECIES ###
######################

# input data should be formatted as follows:
## 1) genoFile:
### - rownames = loci
### - colnames = sampleIDs
### - alleles separated by comma
### - non-genotyped alleles can be in any format (e.g., NA, "0", "0,0")
## 2) mdFile: should include a column for "species" and "sampleID"
## 3) sampleID_colName: specify column name for sampleID

assignSpecies <- function(genoFile, mdFile, sampleID_colName) {
  
  # import speciesKey
  speciesKeyFile <- read.csv("./project_data/speciesKey.csv")
  
  # ensure sampleID colname is in correct format
  if(missing(sampleID_colName)) {
    "sampleID"
  } else {
    colnames(mdFile)[colnames(mdFile) == sampleID_colName] <- "sampleID"
  }
  
  # assign species
  result <- genoFile %>%
    t() %>%
    as.data.frame() %>%
    select(c(speciesKeyFile$locus)) %>%
    rownames_to_column("sampleID") %>%
    pivot_longer(!sampleID,
                 names_to = "locus",
                 values_to = "genotype") %>%
    left_join(speciesKeyFile, by = c("locus", "genotype")) %>%
    select(-genotype) %>%
    pivot_wider(names_from = sampleID,
                values_from = species) %>%
    column_to_rownames("locus") %>%
    t() %>%
    as.data.frame() %>%
    mutate(
      totalGenos_sp = (rowSums(. == "LWED", na.rm = TRUE) + rowSums(. == "SIMP", na.rm = TRUE)),
      propGenos_sp = totalGenos_sp / 12,
      propLWED = (rowSums(. == "LWED", na.rm = TRUE) / totalGenos_sp),
      propSIMP = (rowSums(. == "SIMP", na.rm = TRUE) / totalGenos_sp),
      propMismatch_species = (1 - abs(propLWED - propSIMP)),
      spAssigned = ifelse(propLWED == 1, "LWED", 
                          ifelse(propSIMP == 1, "SIMP", 
                                 ifelse(propLWED < 1 & propSIMP > 0, "MIX", NA)))
    ) %>%
    rownames_to_column("sampleID") %>%
    relocate(c(spAssigned, totalGenos_sp, propGenos_sp, propMismatch_species, propLWED, propSIMP), .after = sampleID) %>%
    merge(., mdFile[, c("sampleID", "species")], by = "sampleID") %>%
    dplyr::rename("mdSpecies" = "species") %>%
    mutate(
      mdMatch = case_when(
        spAssigned == mdSpecies ~ TRUE,
        spAssigned != mdSpecies ~ FALSE
      )
    ) %>%
    relocate(c(mdMatch, mdSpecies), .after = sampleID)
  
  return(result)
}

##################
### ASSIGN SEX ###
##################

# Input data should be formatted as follows:
## 1) genoFile:
### - rownames = loci
### - colnames = sampleIDs
### - alleles separated by comma
### - non-genotyped alleles can be in any format (e.g., NA, "0", "0,0")
## 2) mdFile: should include a column for "species" and "sampleID"
## 3) sampleID_colName: specify column name for sampleID ("colName")
## 4) exclude_nonTargetSp: specify ("yes" or "no") whether to include genos for sex loci that are specific to the non-target species 

assignSex <- function(genoFile, mdFile, sampleID_colName, exclude_nonTargetSp) {
  
  # import sexKey
  sexKeyFile <- read.csv("./project_data/sexKey.csv") %>%
    mutate(
      exclude_ntSex = exclude_nonTargetSp
    )
  
  # ensure sampleID colname is in correct format
  if(missing(sampleID_colName)) {
    "sampleID"
  } else {
    colnames(mdFile)[colnames(mdFile) == sampleID_colName] <- "sampleID"
  }
  
  result <- genoFile %>%
    t() %>%
    as.data.frame() %>%
    select(c(sexKeyFile$locus)) %>%
    rownames_to_column("sampleID") %>%
    pivot_longer(!sampleID,
                 names_to = "locus",
                 values_to = "genotype") %>%
    left_join(sexKeyFile, by = c("locus", "genotype")) %>%
    
    mutate(
      sex = case_when(
        exclude_ntSex == "yes" & sampleID %in% mdFile[mdFile$species=="LWED", "sampleID"] & str_detect(locus, "SIMP") ~ genotype,
        exclude_ntSex == "yes" & sampleID %in% mdFile[mdFile$species=="SIMP", "sampleID"] & str_detect(locus, "LWED") ~ genotype,
        .default = sex
      )
    ) %>%
    
    select(-genotype, -exclude_ntSex) %>%
    pivot_wider(names_from = sampleID,
                values_from = sex) %>%
    column_to_rownames("locus") %>%
    t() %>%
    as.data.frame() %>%
    mutate(
      totalGenos_sex = (rowSums(. == "F", na.rm = TRUE) + rowSums(. == "M", na.rm = TRUE)),
      possibleGenos_sex = case_when(
        exclude_nonTargetSp == "no" ~ 11,
        rownames(.) %in% mdFile[mdFile$species=="LWED", "sampleID"] ~ 7,
        rownames(.) %in% mdFile[mdFile$species=="SIMP", "sampleID"] ~ 9,
        .default = 11
      ),
      propGenos_sex = round(totalGenos_sex / possibleGenos_sex, 2),
      propF = round((rowSums(. == "F", na.rm = TRUE) / totalGenos_sex), 2),
      propM = round((rowSums(. == "M", na.rm = TRUE) / totalGenos_sex), 2),
      propMismatch_sex = (1 - abs(propF - propM)),
      sexAssigned = ifelse(propF == 1, "F", 
                           ifelse(propM == 1, "M", 
                                  ifelse(propF < 1 & propM > 0, "MIX", NA)))
    ) %>%
    rownames_to_column("sampleID") %>%
    relocate(c(sexAssigned, totalGenos_sex, possibleGenos_sex, propGenos_sex, propMismatch_sex, propF, propM), .after = sampleID) %>%
    merge(., mdFile[, c("sampleID", "sex")], by = "sampleID") %>%
    dplyr::rename("mdSex" = "sex") %>%
    mutate(
      mdMatch = case_when(
        is.na(sexAssigned) ~ NA,
        sexAssigned == mdSex ~ TRUE,
        sexAssigned != mdSex ~ FALSE,
        .default = FALSE
      )
    ) %>%
    relocate(c(mdMatch, mdSex), .after = sampleID)
  
  return(result)
}

###############################
### DOWNSAMPLE ALLELE READS ###
###############################

# Input file = UNFILTERED allele reads
## rownames = loci
## colnames = samples
## allele read values = comma-separated (e.g., 4,23)

library(stringi)

downsample_alleleReads <- function(alleleReads_file, n_reads, n_iterations) {
  # reformat alleleReads file
  ds_alleleReads <- alleleReads_file %>%
    rownames_to_column("locus") %>%
    pivot_longer(!locus,
                 names_to = "sampleID",
                 values_to = "readCounts") %>%
    relocate(sampleID) %>%
    arrange(sampleID) %>%
    # obtain separate read counts for allele 1, allele 2, and their sum
    separate(readCounts, into = c("readCounts_a1", "readCounts_a2"), sep = ",") %>%
    mutate(
      readCounts_a1 = as.numeric(readCounts_a1),
      readCounts_a2 = as.numeric(readCounts_a2),
      readCounts_sum = readCounts_a1 + readCounts_a2
    ) %>%
    # create "a/b" character strings based on allele counts (separate for each allele at first)
    rowwise() %>%
    mutate(
      vec_a1 = paste(replicate(readCounts_a1, "a"), collapse = ""),
      vec_a2 = paste(replicate(readCounts_a2, "b"), collapse = "")
    ) %>%
    # randomly combine "a" and "b" allele strings "n_iterations" times & combine as a list
    mutate(
      vec_a1a2 = list(replicate(n_iterations, stri_rand_shuffle(str_c(vec_a1, vec_a2))))
    ) %>%
    # downsample by extracting the first "n_reads" characters from each string in the list
    mutate(
      ds_vec_a1a2 = list(substr(vec_a1a2, 1, n_reads))
    ) %>%
    # count the number of a's & b's in each string in the list,
    # then calculate the mean of those counts, rounding to nearest integer
    mutate(
      dsCounts_a1 = as.integer(round(mean(unlist(list(str_count(ds_vec_a1a2, "a")))))),
      dsCounts_a2 = as.integer(round(mean(unlist(list(str_count(ds_vec_a1a2, "b"))))))
    ) %>%
    # calculate the sum for the downsampled read counts,
    # recode as NA if sum < n_reads,
    # and combine the rest in "x,x" format
    mutate(
      ds_readCounts_sum = dsCounts_a1 + dsCounts_a2,
      ds_readCounts = case_when(
        ds_readCounts_sum < n_reads ~ "0,0",
        .default = str_c(dsCounts_a1, dsCounts_a2, sep = ",")
      )
    ) %>%
    # create new alleleReads dataframe,
    # can be saved as a txt file or used as input for GTscore genotyping function
    select(c(sampleID, locus, ds_readCounts)) %>%
    pivot_wider(id_cols = locus,
                names_from = sampleID,
                values_from = ds_readCounts) %>%
    column_to_rownames("locus")
  
  return(ds_alleleReads)
}

####################
### GENO SUCCESS ###
####################

# Input data should be formatted as follows:
## 1) genoFile:
### - rownames = loci
### - colnames = sampleIDs
### - alleles separated by comma
### - non-genotyped alleles can be in any format (e.g., NA, "0", "0,0")
## 2) mdFile: should include a column for "species" and "sampleID"
## 3) sampleID_colName: specify column name for sampleID ("colName")
## 4) exclude_nonTargetSp: specify ("yes" or "no") whether to include genos for sex loci that are specific to the non-target species 

get_genoSuccess <- function(genoFile,
                            lociFile,
                            mdFile,
                            by = c("bySample", "byLocus"),
                            sampleID_colName,
                            exclude_nonTargetSp = c("yes", "no")) {
  
  # ensure sampleID colname is in correct format
  if(missing(sampleID_colName)) {
    "sampleID"
  } else {
    colnames(mdFile)[colnames(mdFile) == sampleID_colName] <- "sampleID"
  }
  
  # species-specific loci sets & sample lists
  lociList_dual <- lociFile %>%
    filter(!str_detect(Locus, "LWED")) %>%
    filter(!str_detect(Locus, "SIMP"))
  
  lociList_lwed <- lociFile %>%
    filter(!str_detect(Locus, "SIMP"))
  
  lociList_simp <- lociFile %>%
    filter(!str_detect(Locus, "LWED"))
  
  lociList_lwedSpec <- lociFile %>%
    filter(str_detect(Locus, "LWED"))
  
  lociList_simpSpec <- lociFile %>%
    filter(str_detect(Locus, "SIMP"))
  
  
  sampleList_lwed <- mdFile %>%
    filter(species == "LWED") %>%
    select(sampleID)
  
  sampleList_simp <- mdFile %>%
    filter(species == "SIMP") %>%
    select(sampleID)
  
  sampleList_pos <- mdFile %>%
    filter(species %in% c("LWED", "SIMP")) %>%
    select(sampleID)
  
  # genoSuccess byLocus
  if(by == "byLocus") {
    genoSuccess_byLocus <- genoFile %>%
      rownames_to_column("locus") %>%
      mutate(
        totalGenos = case_when(
          exclude_nonTargetSp == "yes" & locus %in% lociList_lwedSpec$Locus ~ rowSums(!is.na(select(., sampleList_lwed$sampleID))),
          exclude_nonTargetSp == "yes" & locus %in% lociList_simpSpec$Locus ~ rowSums(!is.na(select(., sampleList_simp$sampleID))),
          exclude_nonTargetSp == "yes" & locus %in% lociList_dual$Locus ~ rowSums(!is.na(select(., sampleList_pos$sampleID))),
          .default = rowSums(!is.na(select(., -locus)))
        ),
        possibleGenos = case_when(
          exclude_nonTargetSp == "yes" & locus %in% lociList_lwedSpec$Locus ~ nrow(sampleList_lwed),
          exclude_nonTargetSp == "yes" & locus %in% lociList_simpSpec$Locus ~ nrow(sampleList_simp),
          exclude_nonTargetSp == "yes" & locus %in% lociList_dual$Locus ~ nrow(sampleList_pos),
          .default = nrow(mdFile)
        ),
        genoSuccess = totalGenos / possibleGenos
      ) %>%
      select(locus, totalGenos, possibleGenos, genoSuccess)
    
    return(genoSuccess_byLocus)
    
  }
  
  # genoSuccess_bySample
  if(by == "bySample") {
    genoSuccess_bySample <- genoFile %>%
      t() %>%
      as.data.frame() %>%
      rownames_to_column("sampleID") %>%
      mutate(
        totalGenos = case_when(
          exclude_nonTargetSp == "yes" & sampleID %in% sampleList_lwed$sampleID ~ rowSums(!is.na(select(., lociList_lwed$Locus))),
          exclude_nonTargetSp == "yes" & sampleID %in% sampleList_simp$sampleID ~ rowSums(!is.na(select(., lociList_simp$Locus))),
          .default = rowSums(!is.na(select(., -sampleID)))
        ),
        possibleGenos = case_when(
          exclude_nonTargetSp == "yes" & sampleID %in% sampleList_lwed$sampleID ~ nrow(lociList_lwed),
          exclude_nonTargetSp == "yes" & sampleID %in% sampleList_simp$sampleID ~ nrow(lociList_simp),
          .default = nrow(lociFile)
        ),
        genoSuccess = totalGenos / possibleGenos
      ) %>%
      select(sampleID, totalGenos, possibleGenos, genoSuccess)
    
    return(genoSuccess_bySample)
    
  }
  
}

################################
### GTSEQ PIPELINE FUNCTIONS ###
################################

# 1) get_gtseqGenos_v2 - based on GTseq_Genotyper_v2.pl
## Inputs:
### - "readCounts" column name; readCounts should be formatted as "x,x"
### - "locus" column name; loci names should match those in the lociInfo file
### - "lociInfo" dataframe; with columns Locus, Allele1, Allele2

get_gtseqGenos_v2 <- function(readCounts, locus, lociInfo) {
  
  # Get allele ratio and genotype for one entry
  getRatio_and_assignGeno <- function(rc, locus) {
    if (is.na(rc)) {
      return(NA_character_)
    }
    
    # Find the alleles corresponding to the locus
    alleles <- lociInfo[lociInfo$Locus == locus, c("Allele1", "Allele2")]
    
    if (nrow(alleles) == 0) {
      stop(paste("Locus", locus, "not found in lociInfo."))
    }
    
    Allele1 <- alleles$Allele1
    Allele2 <- alleles$Allele2
    
    # Split the input string into two numeric values
    counts <- as.numeric(unlist(strsplit(rc, ",")))
    
    # Replace 0 counts with 0.1
    counts[counts == 0] <- 0.1
    
    # Sum the read counts
    readSum <- sum(counts)
    
    # Check the sum and compute the ratio and genotype if appropriate
    if (readSum < 10) {
      return(NA_character_)
    } else {
      ratio <- round(counts[1] / counts[2], 3)
      
      # Determine genotype based on the ratio
      genotype <- case_when(
        ratio >= 10 ~ str_c(Allele1, Allele1, sep = ","),
        ratio <= 0.1 ~ str_c(Allele2, Allele2, sep = ","),
        ratio <= 0.2 ~ NA_character_,
        ratio <= 5 ~ str_c(Allele1, Allele2, sep = ","),
        TRUE ~ NA_character_  # Default case
      )
      
      return(genotype)
    }
  }
  
  # Apply the processing and genotype determination to each element in readCounts
  mapply(getRatio_and_assignGeno, readCounts, locus)
}

########################
### LITTLE FUNCTIONS ###
########################

get_readSum <- function(x) gsubfn("(\\d+),(\\d+)", ~ as.numeric(x) + as.numeric(y), paste(x))
# Input: column name
# Example usage: %>% mutate(readSums = get_readSum(readCounts))



