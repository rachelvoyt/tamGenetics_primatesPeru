######################
##### ASSIGN SEX #####
######################

assignSex <- function(genoFile, mdFile, sampleID_colName, exclude_nonTargetSex) {
  
  # import sexKey
  sexKeyFile <- read.csv("./tamAnalyses_generalFiles/sexKey.csv") %>%
    mutate(
      exclude_ntSex = exclude_nonTargetSex
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
    relocate(mdSex, .after = sampleID) %>%
    relocate(mdMatch, .after = sexAssigned)
  
  return(result)
}