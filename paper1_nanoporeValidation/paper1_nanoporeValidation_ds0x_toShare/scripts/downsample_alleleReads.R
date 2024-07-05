###############################
### DOWNSAMPLE ALLELE READS ###
###############################

# Input file = UNFILTERED allele reads file from GTscore
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