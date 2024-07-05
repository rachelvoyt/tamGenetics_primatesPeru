## Script to sort out the best primer pairs... 
## 1) from those returned by BatchPrimer3 and then ranked by primer quality in FastPCR, then
## 2) then tested in silico via MFEPrimer

setwd("./primers")

############################################################################
### 1: Filter BatchPrimer3 Primer Set 1 results w/FastPCR quality scores ###
############################################################################

# Packages
library(tidyverse)

# Load data
primerSet1 <- read.csv(file = "./primers/primerSet1_fastpcrAnalysis_20Jan2022.csv")
View(primerSet1)

# Subset 1: Subset primer pairs whose FastPCR primer quality scores are >= 75% for both f and r
primers75 <- primerSet1 %>% group_by(bp3Index, bp3Rank) %>% # subsets into primer pair sets
  filter(all(Primer_Quality...>=75)) # chooses primer pair sets where both in set are >= 75%
View(primers75)

# How many sequences have primer pairs w/both f & r >= 75%?
length(unique(primers75$bp3Index)) # 119 sequences w/both f & r >= 75
setdiff(1:357,primers75$bp3Index) # view those missing

# Subset 2: Remove seqs where both f & r primers >= 75%, & from there subset those w/f & r >= 50%
# This means that we may get primer pairs where f or r is >= 75%, just not both - both
# *will* be >= 50% though
primers75_seqs <- unique(primers75$bp3Index) # creating list of sequences included in Subset 1
primers50 <- primerSet1[!primerSet1$bp3Index %in% primers75_seqs,] # removing those from full list

primers50 <- primers50 %>% group_by(bp3Index, bp3Rank) %>%
  filter(all(Primer_Quality...>=50))
View(primers50)

length(unique(primers50$bp3Index)) # 205 w/both primers >= 50% but < 75%

# Subset 3: Remove seqs where f & r =< 50%, leaving those w/f and/or r 
# primers w/quality scores < 50%
primersLowQ <- primerSet1[!primerSet1$bp3Index %in% unique(primers75$bp3Index),]
primersLowQ <- primersLowQ[!primersLowQ$bp3Index %in% unique(primers50$bp3Index),]
View(primersLowQ)

unique(primersLowQ$bp3Index) # only sequences 5, 34, 117, 305, 350 - not bad

# From there, get avg primer quality per pair in each subset & select the top primer pair per seq
primers75_top <- primers75 %>%
  group_by(bp3Index, bp3Rank) %>%
  summarise_at(vars(Primer_Quality...),
               list(pq = mean)) %>% # create new column w/avg quality of f & r of each primer pair
  group_by(bp3Index) %>% # regroup by bp3Index
  slice_max(order_by = pq, n = 1) %>% # take top primer pair per index
  distinct(bp3Index, .keep_all = T) # adding this b/c some primer pairs avg are the same; "distinct()" 
                                      # fxn will atuomatically choose the first in the set to keep
                                      # (so the top chosen by BatchPrimer3)
View(primers75_top)

primers50_top <- primers50 %>%
  group_by(bp3Index, bp3Rank) %>%
  summarise_at(vars(Primer_Quality...),
               list(pq = mean)) %>%
  group_by(bp3Index) %>%
  slice_max(order_by = pq, n = 1) %>%
  distinct(bp3Index, .keep_all = T)
View(primers50_top)

primersLowQ_top <- primersLowQ %>%
  group_by(bp3Index, bp3Rank) %>%
  summarise_at(vars(Primer_Quality...),
               list(pq = mean)) %>%
  group_by(bp3Index) %>%
  slice_max(order_by = pq, n = 1) %>%
  distinct(bp3Index, .keep_all = T)
View(primersLowQ_top)

# Then create final list of top primers from each set & merge
x <- c("bp3Index", "bp3Rank")
primers75_final <- merge(primerSet1, primers75_top[x], by=x) # selecting primer pairs from original set that match the top pairs selected above
primers50_final <- merge(primerSet1, primers50_top[x], by=x)
primersLowQ_final <- merge(primerSet1, primersLowQ_top[x], by=x)

primersTop <- rbind(primers75_final, primers50_final, primersLowQ_final)
View(primersTop)
length(primersTop$bp3Index) # should be 658 (329 seqs * 2 primers) - success
table(primersTop$primerFR) # double checking that have 329 forward & 329 reverse - success

write.csv(primersTop,"primerSet2_forInSilico_20Jan2022.csv", row.names = F)


#############################################################
### 2: Replace failed in silico primers from Primer Set 2 ###
#############################################################

# Load data
failedPrimers <- read.csv(file = "./primers/primerSet2_failedInSilico_25Jan2022.csv")
View(failedPrimers)
bp3Originals <- read.csv(file = "./primers/primerSet1_bp3Output_formattingUpdated_20Jan2022.csv")
View(bp3Originals)
primerSet2 <- read.csv(file = "./primers/primerSet2_forInSilico_20Jan2022.csv")
primerSet2 <- data.frame(lapply(primerSet2, function(v) {
  if (is.character(v)) return(toupper(v))
  else return(v)
})) # ensuring everything is in all caps to match bp3Originals (for merging purposes)
View(primerSet2)

# Add bp3Index, bp3Rank, & primerFR from primerSet2 to failedPrimers by mfeIndex
failedPrimers <- merge(failedPrimers, 
                       primerSet2[,c("mfeIndex", "bp3Index", "bp3Rank", "primerFR")], 
                       by = "mfeIndex", all.x = T)
View(failedPrimers)

# Add mfeIndex from primerSet2 to bp3Originals by bp3Index, bp3Rank, and primerFR
bp3Originals <- merge(bp3Originals, 
                       primerSet2[,c("mfeIndex", "bp3Index", "bp3Rank", "primerFR")], 
                       by = c("bp3Index", "bp3Rank", "primerFR"), all.x = T) %>%
  relocate("mfeIndex")
View(bp3Originals)

# Indicate whether primer pairs from bp3Originals passed or failed the first in silico test
bp3Originals$inSilico <- ifelse(
  bp3Originals$mfeIndex %in% failedPrimers$mfeIndex,
  paste("FAIL"),
  ifelse(
    bp3Originals$mfeIndex %in% primerSet2$mfeIndex & !(bp3Originals$mfeIndex %in% failedPrimers$mfeIndex),
    paste("PASS"),
    NA))
bp3Originals <- bp3Originals %>% relocate("inSilico")

View(bp3Originals)

write.csv(bp3Originals, file = "./primers/primerSet2_passFail.csv")

# Create list of replacement primers for those that failed
## Create list of indices where primers failed
failedbp3 <- bp3Originals %>% 
  filter(inSilico == "FAIL") %>%
  select(inSilico, mfeIndex, bp3Index, primerFR)
View(failedbp3)

## Subset indices where a primer failed
replacementPrimers <- bp3Originals %>%
  filter(bp3Originals$bp3Index %in% failedbp3$bp3Index) %>%
  filter(is.na(inSilico)) %>%
  merge(., failedbp3[,c("mfeIndex", "bp3Index", "primerFR")],
                            by = c("bp3Index", "primerFR")) %>%
  select(-mfeIndex.x, -inSilico) %>%
  relocate(mfeIndex.y) %>%
  rename(mfeIndex = mfeIndex.y)

View(replacementPrimers)

write.csv(replacementPrimers,"primerSet2x_replacementPrimers_forInSilico_25Jan2022.csv", row.names = F)


#####################################################
### 3. Merge SNP master file w/primer master file ###
#####################################################

primerTracking <- read.csv("primerTracking.csv")
SNPmaster <- read.csv("Master_SNP_File_Sam_7Feb2022.csv") # downloaded from Sam's google sheet; edited col headings to match for merge
x <- c("bp3Index", "bp3Rank")

primerSNP_tracking <- merge(primerTracking, SNPmaster, by = x, all = T)
View(primerSNP_tracking)

write.csv(primerSNP_tracking, "primerSNP_tracking.csv", row.names = F) # will edit columns in excel


############################################################################
### 4. Filter BatchPrimer3 Primer Set 3 results w/FastPCR quality scores ###
############################################################################

# Packages
library(tidyverse)

# Load data
primerSet3 <- read.csv(file = "./primers/primerSet3_fastpcrAnalysis_22Feb2022.csv")
View(primerSet3)

# Subset 1: Subset primer pairs whose FastPCR primer quality scores are >= 75% for both f and r
primers75.set3 <- primerSet3 %>% group_by(uniqueIndex, bp3Rank) %>% # subsets into primer pair sets
  filter(all(Primer_Quality...>=75)) # chooses primer pair sets where both in set are >= 75%
View(primers75.set3)

# How many sequences have primer pairs w/both f & r >= 75%?
length(unique(primers75.set3$uniqueIndex)) # 13 sequences w/both f & r >= 75
setdiff(1:357,primers75.set3$uniqueIndex) # view those missing

# Subset 2: Remove seqs where both f & r primers >= 75%, & from there subset those w/f & r >= 50%
# This means that we may get primer pairs where f or r is >= 75%, just not both
# both *will* be >= 50% though
primers75.set3_seqs <- unique(primers75.set3$uniqueIndex) # creating list of sequences included in Subset 1
primers50.set3 <- primerSet3[!primerSet3$uniqueIndex %in% primers75.set3_seqs,] # removing those from full list

primers50.set3 <- primers50.set3 %>% group_by(uniqueIndex, bp3Rank) %>%
  filter(all(Primer_Quality...>=50))
View(primers50.set3)

length(unique(primers50.set3$uniqueIndex)) # 20 w/both primers >= 50% but < 75%

# Subset 3: Remove seqs where f & r =< 50%, leaving those w/f and/or r 
# primers w/quality scores < 50%
primersLowQ.set3 <- primerSet3[!primerSet3$uniqueIndex %in% unique(primers75.set3$uniqueIndex),]
primersLowQ.set3 <- primersLowQ[!primersLowQ$bp3Index %in% unique(primers50.set3$uniqueIndex),]
View(primersLowQ.set3)

unique(primersLowQ.set3$uniqueIndex) # none! which is good

# From there, get avg primer quality per pair in each subset & select the top primer pair per seq
primers75_top.set3 <- primers75.set3 %>%
  group_by(uniqueIndex, bp3Rank) %>%
  summarise_at(vars(Primer_Quality...),
               list(pq = mean)) %>% # create new column w/avg quality of f & r of each primer pair
  group_by(uniqueIndex) %>% # regroup by bp3Index
  slice_max(order_by = pq, n = 1) %>% # take top primer pair per index
  distinct(uniqueIndex, .keep_all = T) # adding this b/c some primer pairs avg are the same; "distinct()" 
# fxn will atuomatically choose the first in the set to keep
# (so the top chosen by BatchPrimer3)
View(primers75_top.set3)

primers50_top.set3 <- primers50.set3 %>%
  group_by(uniqueIndex, bp3Rank) %>%
  summarise_at(vars(Primer_Quality...),
               list(pq = mean)) %>%
  group_by(uniqueIndex) %>%
  slice_max(order_by = pq, n = 1) %>%
  distinct(uniqueIndex, .keep_all = T)
View(primers50_top.set3)

# ((no low quality sequences to subset))
# primersLowQ_top.set3 <- primersLowQ.set3 %>%
#   group_by(uniqueIndex, bp3Rank) %>%
#  summarise_at(vars(Primer_Quality...),
#               list(pq = mean)) %>%
#  group_by(uniqueIndex) %>%
#  slice_max(order_by = pq, n = 1) %>%
#  distinct(uniqueIndex, .keep_all = T)
# View(primersLowQ_top.set3)

# Then create final list of top primers from each set & merge
x <- c("uniqueIndex", "bp3Rank")
primers75_final.set3 <- merge(primerSet3, primers75_top.set3[x], by=x) # selecting primer pairs from original set that match the top pairs selected above
primers50_final.set3 <- merge(primerSet3, primers50_top.set3[x], by=x)
# primersLowQ_final.set3 <- merge(primerSet3, primersLowQ_top.set3[x], by=x)

primersTop.set3 <- rbind(primers75_final.set3, primers50_final.set3)
View(primersTop.set3)
length(primersTop.set3$uniqueIndex) # should be 66 (33 seqs * 2 primers) - success
table(primersTop.set3$primerFR) # double checking that have 329 forward & 329 reverse - success

write.csv(primersTop.set3,"primerSet4_forInSilico_22Feb2022.csv", row.names = F)

#############################################################
### 5: Replace failed in silico primers from Primer Set 4 ###
#############################################################

# Load data
failedPrimers.set4 <- c('358.2', '360.1', '361.3', '363.3', '364.1', '367.1', '368.3', '369.2', '372.2', 
                        '374.2', '376.1', '380.2', '381.3', '383.3', '384.1', '385.2', '388.1', '389.2', 
                        '390.3', '397.1', '399.3')
failedPrimers.set4 <- as.data.frame(failedPrimers.set4) %>%
  rename(uniqueIndex = failedPrimers.set4)
View(failedPrimers.set4)
bp3Originals.set3 <- read.csv(file = "primerSet3_bp3Output_newPrimers-only_23Feb2022.csv")
View(bp3Originals.set3)
primerSet4 <- read.csv(file = "primerSet4_forInSilico_22Feb2022.csv")
primerSet4 <- data.frame(lapply(primerSet4, function(v) {
  if (is.character(v)) return(toupper(v))
  else return(v)
})) # ensuring everything is in all caps to match bp3Originals (for merging purposes)
View(primerSet4)

# Add bp3Index, bp3Rank, & primerFR from primerSet2 to failedPrimers by mfeIndex
failedPrimers.set4 <- merge(failedPrimers.set4, 
                       primerSet4[,c("uniqueIndex", "bp3Rank", "primerFR")], 
                       by = "uniqueIndex", all.x = T)
View(failedPrimers.set4)


# Indicate whether primer pairs from bp3Originals Set 3 passed or failed in silico test
bp3Originals.set3$inSilico <- ifelse(
  bp3Originals.set3$uniqueIndex %in% failedPrimers.set4$uniqueIndex,
  paste("FAIL"),
  ifelse(
    bp3Originals.set3$uniqueIndex %in% primerSet4$uniqueIndex & !(bp3Originals.set3$uniqueIndex %in% failedPrimers.set4$uniqueIndex),
    paste("PASS"),
    NA))
bp3Originals.set3 <- bp3Originals.set3 %>% relocate("inSilico")

View(bp3Originals.set3)

write.csv(bp3Originals.set3, file = "primerSet4_resultsInSilico_23Feb2022.csv", row.names = F)

# Create list of replacement primers for those that failed
## Create list of indices where primers failed
failed.set4 <- bp3Originals.set3 %>% 
  filter(inSilico == "FAIL") %>%
  select(inSilico, uniqueIndex, bp3Index, primerFR)
View(failed.set4)

## Subset indices where a primer failed # NEED TO UPDATE THIS SECTION (just did it manually to send to Sam)
replacementPrimers.set4 <- bp3Originals.set3 %>%
  filter(bp3Originals.set3$uniqueIndex %in% failed.set4$uniqueIndex) %>%
  filter(is.na(inSilico)) %>%
  merge(., failed.set4[,c("uniqueIndex", "bp3Index", "primerFR")],
        by = c("uniqueIndex", "primerFR")) %>%
  select(-mfeIndex.x, -inSilico) %>%
  relocate(mfeIndex.y) %>%
  rename(mfeIndex = mfeIndex.y)

View(replacementPrimers.set4)

write.csv(replacementPrimers,"primerSet2x_replacementPrimers_forInSilico_25Jan2022.csv", row.names = F)

#############################################################
### 6: Add pass/fail to in silico PCR 4 for primer set 4x ###
#############################################################
psTracking <- read.csv("./primers/primerSNP_tracking.csv") # from first sheet of primerSNP_tracking.xlsx
set4x_pass <- read.csv("./primers/primerSet4x_passInSilico_25Feb2022.csv")

psTracking$isPCR4_final <- ifelse(
  psTracking$uniqueIndex %in% set4x_pass$uniqueIndex,
  paste("PASS"),
  ifelse(
    psTracking$uniqueIndex %in% primerSet4$uniqueIndex &
      !(psTracking$uniqueIndex %in% set4x_pass$uniqueIndex),
    paste ("FAIL"),
    NA))

View(psTracking)

write.csv(psTracking, file = "./primers/psTracking_addtlPrimers_isResults.csv", row.names = F)

###################################################
### 7: Redo add pass/fail to all in silico PCRs ###
###################################################

pcr1 <- read.csv("./primers/isPCR1_results.csv") %>% drop_na("bp3Rank")
pcr1 <- pcr1[,c("uniqueIndex", "isPCR1_SIMP", "isPCR1_SIMP_failReason")]
pcr2 <- read.csv("./primers/isPCR2_results.csv") %>% drop_na("bp3Rank")
pcr2 <- pcr2[,c("uniqueIndex", "isPCR2_SIMP", "isPCR2_SIMP_failReason")]
pcr3 <- read.csv("./primers/isPCR3_results.csv") %>% drop_na("bp3Rank")
pcr3 <- pcr3[,c("uniqueIndex", "isPCR3_SIMP", "isPCR3_SIMP_failReason", 
                "isPCR3_LWED", "isPCR3_LWED_failReason", "isPCR3_final")]
pcr4 <- read.csv("./primers/isPCR4_results.csv") %>% drop_na("bp3Rank")
pcr4 <- pcr4[,c("uniqueIndex", "isPCR4_SIMP", "isPCR4_SIMP_failReason", 
                "isPCR4_LWED", "isPCR4_LWED_failReason", "isPCR4_final")]
pcr5 <- read.csv("./primers/isPCR5_results.csv") %>% drop_na("bp3Rank")
pcr5 <- pcr5[,c("uniqueIndex", "isPCR5_SIMP", "isPCR5_SIMP_failReason", 
                "isPCR5_LWED", "isPCR5_LWED_failReason", "isPCR5_final")]
psTrackingFile <- read.csv("./primers/primerSNP_tracking.csv") # from first sheet of primerSNP_tracking.xlsx

pst <- merge(psTrackingFile, pcr1, by = "uniqueIndex", all = T) %>%
  merge(pcr2, by = "uniqueIndex", all = T) %>%
  merge(pcr3, by = "uniqueIndex", all = T) %>%
  merge(pcr4, by = "uniqueIndex", all = T) %>%
  merge(pcr5, by = "uniqueIndex", all = T)
colnames(pst)

write.csv(pst, "./primers/primerSNP_tracking_checks_27Feb2022.csv")
