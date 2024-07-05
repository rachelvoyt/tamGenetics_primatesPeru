# Determining which loci to ditch

setwd("/home/rachelvoyt/Documents/UT-Grad/Development/repos/tamarinGenetics_primatesPeru")

# Packages
library(tidyverse)
library(readxl)

######################################
## Compare GTseq vs GTscore results ##
######################################

# 30 June 2022

# Load data
gtseq_zeroReads <- read.table("gtseq_zeroReads.txt", header = F)
View(gtseq_zeroReads)
gtseq_under280 <- read.table("gtseq_under280reads.txt", header = F)
View(gtseq_under280)
gtscore_lsFull <- read.csv("./03_gtScore/summaryFiles/locusSummary_combined.csv")
View(gtscore_lsFull)

# Adjust gtscore formatting to match up with gtseq loci numbers (trimming down locus name to just the number)
gtscore_lsFull$Locus <- substr(gtscore_lsFull$Locus,0,nchar(gtscore_lsFull$Locus)-2)
gtscore_lsFull$Locus <- gsub("^.*\\_","", gtscore_lsFull$Locus)

# Get info just for loci that failed gtseq
seqFail_scoreInfo <- gtscore_lsFull %>%
  filter(Locus %in% gtseq_zeroReads$V1)
View(seqFail_scoreInfo)

# And info for loci that had under 280 reads in gtseq
seq280_scoreInfo <- gtscore_lsFull %>%
  filter(Locus %in% gtseq_under280$V1)
View(seq280_scoreInfo)

# Export
write.csv(seqFail_scoreInfo, "seqFail_scoreInfo.csv", row.names = F)
write.csv(seq280_scoreInfo, "seq280_scoreInfo.csv", row.names = F)


# Let's print out full gtscore results and just add a column saying how they did in gtseq
seq <- read.csv("gtseq_failedLoci_combined.csv")
View(seq)

seqScore <- merge(gtscore_lsFull, seq, by = "Locus", all.x = T) %>%
  relocate(gtseq_reads)
View(seqScore)

# Export 
write.csv(seqScore, "scoreAll_seqFail.csv", row.names = F)


#######################
## oPools assessment ##
#######################

# Which loci from the oPools order do we need to re-order?

# Load data
opools <- read_excel("./primers/01_primerOrders/tamarinGenetics_primerOrder2_oPools_224oligos.xlsx") %>%
  select("Sequence") %>%
  as.data.frame()
gtseq_finalChoices <- read.csv("./primers/03_lociChoices/Master SNP file - GTseq_googleSheet_10Jul2022.csv")
psTracking <- read_excel("./primers/primerSNP_tracking.xlsx") %>%
  select(c("uniqueIndex", "bp3Index", "bp3Rank", "seqID", "set", "finalPrimerseq")) %>%
  as.data.frame()
View(opools)
View(gtseq_finalChoices)
View(psTracking)

# Add loci names to opools sequences
opoolsNames <- merge(opools, psTracking, 
                     by.x = "Sequence", by.y = "finalPrimerseq", 
                     all.x = T, all.y = F)
View(opoolsNames)

# Subset gtseq_finalChoices to get a list of loci to remove
gtseq_removeLoci <- gtseq_finalChoices %>%
  filter(!To.be.removed.before.second.amplification.round. == "NO")
length(gtseq_removeLoci$SET) # 81 loci to remove from full pool
View(gtseq_removeLoci)

gtseq_keepLoci <- gtseq_finalChoices %>%
  filter(To.be.removed.before.second.amplification.round. == "NO")
length(gtseq_keepLoci$SET)

removeLoci_bp3Index <- gtseq_removeLoci$bp3_index..UNIQUE.
length(removeLoci_bp3Index) # 81

keepLoci_bp3Index <- gtseq_keepLoci$bp3_index..UNIQUE.
length(keepLoci_bp3Index) # 221

# Remove bp3error loci from oPools file - what do we have left?
opoolsToReorder <- opoolsNames %>%
  filter(bp3Index %in% keepLoci_bp3Index)
View(opoolsToReorder) # 142 remaining to order

# Export
write.csv(opoolsToReorder, "./primers/03_lociChoices/oPools_toReorder_142oligos.csv", row.names = F)

###################
## Plate primers ##
###################

# Load data & add bp3Index
plate1 <- read_excel("./primers/01_primerOrders/tamarinGenetics_primerOrder1_plate1_28Jan2022.xlsx") %>%
  as.data.frame() %>%
  mutate(plateNo. = "1") %>%
  relocate(plateNo.)
plate2 <- read_excel("./primers/01_primerOrders/tamarinGenetics_primerOrder1_plate2_28Jan2022.xlsx") %>%
  as.data.frame() %>%
  mutate(plateNo. = "2") %>%
  relocate(plateNo.)
plate3 <- read_excel("./primers/01_primerOrders/tamarinGenetics_primerOrder1_plate3_28Jan2022.xlsx") %>%
  as.data.frame() %>%
  mutate(plateNo. = "3") %>%
  relocate(plateNo.)
plate4 <- read_excel("./primers/01_primerOrders/tamarinGenetics_primerOrder1_plate4_28Jan2022.xlsx") %>%
  as.data.frame() %>%
  mutate(plateNo. = "4") %>%
  relocate(plateNo.)
  
platePrimers <- rbind(plate1, plate2, plate3, plate4)

platePrimers2 <- as.data.frame(platePrimers) %>%
  mutate(Name2 = Name) %>%
  separate(Name2, c("Tam", "bp3Index", "FR"), sep = "_") %>%
  select(-Tam, -FR)
platePrimers3 <- platePrimers2
platePrimers3$bp3Index <- substr(platePrimers3$bp3Index,1,nchar(platePrimers3$bp3Index)-2)
View(platePrimers3)
length(platePrimers3$Name) # 384

# Indicate which to exclude from pool & separate into letter/number
platePrimers4 <- platePrimers3 %>%
  filter(bp3Index %in% keepLoci_bp3Index) %>%
  rename(wellPosition = "Well Position")

platePrimers5 <- separate(platePrimers4, wellPosition, 
                                  into = c("row", "col"), 
                                  "(?<=[A-Z])(?=[0-9])")

platePrimers_toRepool <- platePrimers5 %>%
  relocate("col", .before = "row")
View(platePrimers_toRepool)
length(platePrimers_toRepool$Name) # 300

# small test to see diff b/t sorting by removeLoci vs. keepLoci
smallTest <- platePrimers3 %>%
  filter(!bp3Index %in% removeLoci_bp3Index)
smallTest$bp3Index[!smallTest$bp3Index %in% platePrimers_toRepool$bp3Index] # 71 & 126 >> we ditched these prior to running apparently?

opoolsToReorder$bp3Index %in% platePrimers_toRepool$bp3Index
platePrimers_toRepool$bp3Index %in% opoolsToReorder$bp3Index

#Export
write.csv(platePrimers_toRepool, "./primers/03_lociChoices/platePrimers_toRepool_poolA.csv", row.names = F)

###################
## Primer splits ##
###################

# Total primers to include
gtseq_keepLoci <- gtseq_finalChoices %>%
  filter(To.be.removed.before.second.amplification.round. == "NO")
length(gtseq_keepLoci$species) # 221 loci total; 442 oligos total 

# so need 110 & 111 loci (220 & 222 oligos) per split pool

# How many oligos are we re-ordering in oPools?
length(opoolsToReorder$bp3Index) # 142 oligos

# How many primers need to be added to the oPools set? 
220-142 # 78 oligos (39 loci)
