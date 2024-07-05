######################
### ASSIGN SPECIES ###
######################

# data formatting should be as follows:
## genoFile: rownames = loci; colnames = sampleIDs; alleles separated by comma; non-genotyped alleles can be in any format
## mdFile: should include a column for "species" and "sampleID"
## sampleID_colName: specify column name for sampleID

assignSpecies <- function(genoFile, mdFile, sampleID_colName) {
  
  # import speciesKey
  speciesKeyFile <- read.csv("./tamAnalyses_generalFiles/speciesKey.csv")
  
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
    relocate(mdSpecies, .after = sampleID) %>%
    relocate(mdMatch, .after = spAssigned)
  
  return(result)
}