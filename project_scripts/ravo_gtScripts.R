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
## 3) sampleID_colName: specify mdFile column name for sampleID

assignSpecies <- function(genoFile, mdFile, sampleID_colName) {
  
  # get list of species loci present in genoFile (just in case some were filtered out in previous analyses)
  genoFile_speciesLoci <- rownames(genoFile) %>%
    str_subset(pattern = "SPECIES")
  
  # import speciesKey, subset to loci in genoFile_speciesLoci
  speciesKeyFile <- read.csv("./project_data/speciesKey.csv") %>%
    filter(locus %in% genoFile_speciesLoci)
  
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
## 3) sampleID_colName: specify mdFile column name for sampleID ("colName")
## 4) exclude_nonTargetSp: specify ("yes" or "no") whether to include genos for sex loci that are specific to the non-target species 

assignSex <- function(genoFile, mdFile, sampleID_colName, exclude_nonTargetSp) {
  
  # get list of sex loci present in genoFile (just in case some were filtered out in previous analyses)
  genoFile_sexLoci <- rownames(genoFile) %>%
    str_subset(pattern = "SEXID")  

  # import sexKey, subset to loci in genoFile_sexLoci
  sexKeyFile <- read.csv("./project_data/sexKey.csv") %>%
    mutate(
      exclude_ntSex = exclude_nonTargetSp
    ) %>%
    filter(locus %in% genoFile_sexLoci)
  
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

############################
### ID DUPLICATE SAMPLES ###
############################

# RV modified version of the GTscore function; when creating genotypes_NAmatrix, added as.matrix() to...
# ...enable using geno dataframe vs. polygen output

#function to compare genotypes between all pairs of samples
#input format: rows are loci, columns are samples, alleles are 0 and 1, missing genotypes are NA
#heterozygous calls must be consistent within a locus, ie all 0/1, no 1/0
get_dupSamples <- function(genotypes,MAF=NULL){
  #function to calculate MAF
  calcMAF<-function(locusGenos){
    allele1Counts<-sum(str_count(locusGenos,"0"),na.rm=TRUE)
    allele2Counts<-sum(str_count(locusGenos,"1"),na.rm=TRUE)
    allele1Freq<-allele1Counts/sum(allele1Counts,allele2Counts)
    if(allele1Freq>0.5){
      MAF<-1-allele1Freq
    }else{
      MAF<-allele1Freq
    }
    return(MAF)
  }
  
  #filter loci using MAF if threshold is specified
  if(!is.null(MAF)){
    #calculate MAF
    message(paste("MAF threshold applied:",MAF,"MAF",sep=" "))
    message("calculating MAF")
    locusMAF<-pbapply(genotypes,1,calcMAF)
    #convert to dataframe
    locusMAF<-data.frame(locus_ID=names(locusMAF),MAF=locusMAF,row.names=NULL)
    locusMAF$locus_ID<-as.character(locusMAF$locus_ID)
    #filter loc based on MAF threshold
    genotypes<-genotypes[rownames(genotypes)%in%locusMAF$locus_ID[locusMAF$MAF>=MAF],]
  }else{
    message("No MAF threshold applied, using all loci")
  }
  
  #make matrix of called vs NA genotypes for faster counting of missing data
  genotypes_NAmatrix<-as.matrix(genotypes)
  genotypes_NAmatrix[!is.na(genotypes_NAmatrix)]<-0
  genotypes_NAmatrix[is.na(genotypes_NAmatrix)]<-1
  class(genotypes_NAmatrix)<-"numeric"
  
  #identify all unique pairs of samples
  allPairs<-combn(dim(genotypes)[2], 2)
  ncombo<-dim(allPairs)[2]
  nloci<-dim(genotypes)[1]
  message(paste("number of samples:",dim(genotypes)[2],sep=" "))
  message(paste("number of loci:",nloci,sep=" "))
  message(paste("number of sample pairs:",ncombo,sep=" "))
  #reshape into 2xn matrix
  allPairs<-matrix(allPairs,nrow=2)
  
  #function to compare genotypes
  compareGenos<-function(samplePair){
    #count number of loci that are genotyped in both samples
    NAcounts<-genotypes_NAmatrix[,samplePair[1]]+genotypes_NAmatrix[,samplePair[2]]
    sharedCounts<-nloci-(sum(NAcounts)-sum(NAcounts[NAcounts==2])/2)
    #count number of loci with genotypes that match in both samples
    genotypeMatches<-sum(genotypes[,samplePair[1]]==genotypes[,samplePair[2]],na.rm=TRUE)
    #return counts of genotype matches and shared loci
    return(c(genotypeMatches,sharedCounts))
  }
  
  #do all pairwise sample comparisons
  message("comparing genotypes")
  matches<-pbapply(allPairs,2,compareGenos)
  
  #make dataframe of results
  comparisonResults<-data.frame(matrix(NA,nrow=dim(allPairs)[2],ncol=7))
  colnames(comparisonResults)<-c("Sample1","Sample2","matchedGenotypes","commonGenotypes","proportionMatch","proportionCommon","totalLoci")
  comparisonResults$Sample1<-colnames(genotypes)[allPairs[1,]]
  comparisonResults$Sample2<-colnames(genotypes)[allPairs[2,]]
  comparisonResults$matchedGenotypes<-matches[1,]
  comparisonResults$commonGenotypes<-matches[2,]
  comparisonResults$proportionMatch<-comparisonResults$matchedGenotypes/comparisonResults$commonGenotypes
  comparisonResults$proportionCommon<-comparisonResults$commonGenotypes/nloci
  comparisonResults$totalLoci<-nloci
  return(comparisonResults)
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


get_gtseqGenos_v2 <- function(readCounts_df, lociInfo, mdFile, sampleID_colName = NULL, exclude_nonTargetSp = c("yes", "no")) {
  
  names(lociInfo) <- tolower(names(lociInfo))
  
  # ensure sampleID colname is in correct format
  if(missing(sampleID_colName)) {
    "sampleID"
  } else {
    colnames(mdFile)[colnames(mdFile) == sampleID_colName] <- "sampleID"
  }
  
  # species sample lists
  sampleList_lwed <- mdFile %>%
    filter(species == "LWED") %>%
    select(sampleID)
  
  sampleList_simp <- mdFile %>%
    filter(species == "SIMP") %>%
    select(sampleID)
  
  # assign genos
  geno_df <- readCounts_df %>%
    rownames_to_column("locus") %>%
    pivot_longer(!locus,
                 names_to = "sampleID",
                 values_to = "readCounts") %>%
    # calculate allele ratios
    separate(readCounts, into = c("a1", "a2")) %>%
    mutate(
      a1 = as.numeric(a1),
      a2 = as.numeric(a2),
      
      a1 = case_when(
        a1 == 0 ~ 0.1,
        .default = a1
      ),
      a2 = case_when(
        a2 == 0 ~ 0.1,
        .default = a2
      ),
      
      ratio = case_when(
        a1 + a2 < 10 ~ NA,
        .default = round(a1 / a2, 3)
      )
    ) %>%
    # assign genos
    merge(., lociInfo[, c("locus", "allele1", "allele2")], by = "locus") %>%
    mutate(
      genos = case_when(
        ratio >= 10 ~ str_c(allele1, allele1, sep = ","),
        ratio <= 0.1 ~ str_c(allele2, allele2, sep = ","),
        ratio <= 0.2 ~ NA_character_,
        ratio <= 5 ~ str_c(allele1, allele2, sep = ","),
        TRUE ~ NA_character_  # Default case
      )
    ) %>%
    select(sampleID, locus, genos) %>%
    # exclude non-target species if indicated
    mutate(
      genos = case_when(
        exclude_nonTargetSp == "yes" & sampleID %in% sampleList_lwed$sampleID & str_detect(locus, "(?i)simp") ~ NA,
        exclude_nonTargetSp == "yes" & sampleID %in% sampleList_simp$sampleID & str_detect(locus, "(?i)lwed") ~ NA,
        .default = genos
      )
    ) %>%
    pivot_wider(names_from = sampleID,
                values_from = genos) %>%
    column_to_rownames("locus")
  
  return(geno_df)
  
}

# 1) get_gtseqGenos_v2 - based on GTseq_Genotyper_v2.pl
## Inputs:
### - "readCounts" column name; readCounts should be formatted as "x,x"
### - "locus" column name; loci names should match those in the lociInfo file
### - "lociInfo" dataframe; with columns Locus, Allele1, Allele2

get_gtseqGenos_v2_OLD <- function(readCounts, locus, lociInfo) {
  
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

####################
### GENO COMPARE ###
####################

get_genoCompare <- function(genoFile1, genoFile2, sampleRef, lociInfo) {
  
  na_values <- c("0", "0,0", "00")
  
  genoSet1 <- genoFile1 %>%
    mutate(across(everything(), \(x) as.character(x))) %>%
    rownames_to_column("locus") %>%
    pivot_longer(!locus,
                 names_to = "sampleID",
                 values_to = "genos1") %>%
    mutate(genos1 = case_when(
      genos1 %in% na_values ~ NA,
      .default = genos1
    )) %>%
    merge(., sampleRef[, c("sampleID", "sampleRef", "sampleType")], by = "sampleID") %>%
    dplyr::rename("sampleType1" = "sampleType")
  
  genoSet2 <- genoFile2 %>%
    mutate(across(everything(), \(x) as.character(x))) %>%
    rownames_to_column("locus") %>%
    pivot_longer(!locus,
                 names_to = "sampleID",
                 values_to = "genos2") %>%
    mutate(genos2 = case_when(
      genos2 %in% na_values ~ NA,
      .default = genos2
    )) %>%
    merge(., sampleRef[, c("sampleID", "sampleRef", "sampleType")], by = "sampleID") %>%
    dplyr::rename("sampleType2" = "sampleType")
  
  genoCompare <- genoSet1 %>%
    merge(., genoSet2, by = c("sampleRef", "locus"), all.x = T) %>%
    select(-contains("sampleID")) %>%
    mutate(
      match = genos1 == genos2
    ) %>%
    # determine mismatchType
    mutate(
      callType1 = get_callType(locus, genos1, lociInfo),
      callType2 = get_callType(locus, genos2, lociInfo),
      
      mismatchType = case_when(
        match == FALSE & str_detect(callType1, "hom") & str_detect(callType2, "het") ~ "hom_het",
        match == FALSE & str_detect(callType1, "het") & str_detect(callType2, "hom") ~ "het_hom",
        match == FALSE & str_detect(callType1, "hom") & str_detect(callType2, "hom") ~ "hom_hom",
        match == FALSE & str_detect(callType1, "FA") ~ str_c(callType1, callType2, sep = "_"),
        match == FALSE & str_detect(callType2, "FA") ~ str_c(callType1, callType2, sep = "_"),
        .default = NA
      )
    ) %>%
    select(sampleRef, locus, match, mismatchType, genos1, genos2, callType1, callType2, sampleType1, sampleType2)
  
  return(genoCompare)
  
}


########################
### LITTLE FUNCTIONS ###
########################

get_readSum <- function(x) gsubfn("(\\d+),(\\d+)", ~ as.numeric(x) + as.numeric(y), paste(x))
# Input: column name
# Example usage: %>% mutate(readSums = get_readSum(readCounts))


get_callType <- function(locusCol, genoCol, lociInfo) {
  
  # function for single record
  get_callType_single <- function(locus, geno) {
    
    # Get corresponding alleles from lociInfo based on the locusCol
    a1_ref <- lociInfo$allele1[lociInfo$locus == locus]
    a2_ref <- lociInfo$allele2[lociInfo$locus == locus]
    
    # Split genoCol into a1_call and a2_call
    alleles <- unlist(strsplit(geno, ","))
    a1_call <- alleles[1]
    a2_call <- alleles[2]
    
    # Check for missing values in the reference alleles or allele calls
    if (is.na(a1_ref) | is.na(a2_ref) | is.na(a1_call) | is.na(a2_call)) {
      return(NA)  # Return NA if any of the values are missing
    }
    
    # Classify the genotype
    if (a1_call == a1_ref & a2_call == a1_ref) {
      return("a1hom")
    } else if (a1_call == a2_ref & a2_call == a2_ref) {
      return("a2hom")
    } else if ((a1_call == a1_ref & a2_call == a2_ref) | 
               (a1_call == a2_ref & a2_call == a1_ref)) {
      return("het")
    } else if ((a1_call != a1_ref & a1_call != a2_ref & a2_call == a1_ref & a2_call != a2_ref) | 
               (a1_call != a1_ref & a1_call != a2_ref & a2_call != a1_ref & a2_call == a2_ref)) {
      return("a1FA")
    } else if ((a1_call == a1_ref & a1_call != a2_ref & a2_call != a1_ref & a2_call != a2_ref) |
               (a1_call != a1_ref & a1_call == a2_ref & a2_call != a1_ref & a2_call != a2_ref)) {
      return("a2FA")
    } else if ((a1_call != a1_ref & a1_call != a2_ref & a2_call != a1_ref & a2_call != a2_ref)) {
      return("a12FA")
    } else {
      return(NA)  # Return NA if the genotype doesn't match any condition
    }
    
  }
  
  # Apply to all rows using mapply
  mapply(get_callType_single, locusCol, genoCol)
  
}



