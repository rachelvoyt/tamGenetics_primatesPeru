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