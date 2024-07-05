## Script to identify samples for DNA extraction & sequencing
## Last updated: 14 June 2022 by R. Voyt

# Set wd
setwd("./sampleOrganization/")

# Packages
library(tidyverse)
library(readxl)
library(janitor)
library(lubridate)

# Load data
allCaptures <- read.csv(file = "AllCaptures_2019_rvCopy.csv")
View(allCaptures)
hairSamples <- read.csv(file = "./hairSamples_CICRA_2009-2019_MASTER.csv", header = T)
head(hairSamples)
bloodSamples <- read.csv(file = "./originalData/longmireLog_CICRA_2013-2019.csv", header = T)
head(bloodSamples)
fecalSamples <- read.csv(file = "./PoopLog11.9.21_forRachel_rvCopy.csv")
View(fecalSamples)

# Add trapID to hairSamples using allCaptures
acSubset <- allCaptures %>% select(TrappingID, AnimalID, Date) %>% 
  rename(trapID = TrappingID, animalID = AnimalID, captureDate = Date)
head(acSubset)

write.csv(acSubset,"acSubset.csv", row.names = F) # ended up just doing it on excel

# Find total unique individuals
allCaptures_unique <- filter(allCaptures, 
                      Species == "SFUS" | Species == "SIMP") %>%
  distinct(AnimalID, .keep_all = T)

View(allCaptures_unique)
count(allCaptures_unique, AnimalID) # 247 unique animal IDs

# List of unique animal IDs
animalID_unique <- allCaptures_unique$AnimalID
head(animalID_unique)

## HAIR SAMPLES ##
# Format date
hairSamples$captureDate <- mdy(hairSamples$captureDate)
View(hairSamples)

# Filter unique animalID; exclude hairType that is UNK or shaved, keep 
# the one UNK animalID
hairSamples_unique <- filter(hairSamples, 
                      species == "SFUS" | species == "SIMP", 
                      hairType == "plucked" | hairType == "NULL" | hairType == "UNK") %>%
  arrange(desc(captureDate)) %>%
  distinct(animalID, .keep_all = T)
  
View(hairSamples_unique)          
count(hairSamples_unique, animalID) # 239 total (incl. 1 UNK animalID)

write.csv(hairSamples_unique,"uniqueHair_CICRA_2009-2019_NEW.csv", row.names = F)

# Which individuals are missing from hairSamples_unique?
allCaptures_unique$AnimalID[!allCaptures_unique$AnimalID %in% hairSamples_unique$animalID]

# Missing: [1] 101 75 77 79 85 86 88 93 94 97

#### BLOOD SAMPLES ####
bloodSamples$captureDate <- mdy(bloodSamples$captureDate)
View(bloodSamples)

bloodSamples <- filter(bloodSamples, species == "SFUS" | species == "SIMP") %>%
  arrange(desc(captureDate)) %>%
  distinct(animalID, .keep_all = T)
View(bloodSamples)    

write.csv(bloodSamples,"uniqueLongmire_CICRA_2013-2019.csv", row.names = F)

# Do all blood samples have a hair sample to match? (any blood samples that
# do NOT show up in hair samples?)
bloodSamples$animalID[!bloodSamples$animalID %in% hairSamples$animalID]
hairSamples$animalID[!hairSamples$animalID %in% bloodSamples$animalID] # just to double check

######################################################################

#################
# FECAL SAMPLES #
#################

# Subset fecal samples to SFUS and SIMP only, then filter out any "NULL" rnaTubeNo. & adjust formatting
f <- filter(fecalSamples, 
            species == "SFUS" | species == "SIMP") %>%
  filter(., rnaTubeNo. != "NULL")
f$name <- sub('-', '/', f$name)
  
View(f)

# Info on fecalSamples to check against
length(f$rnaLog_ID) # 1041
length(unique(f$rnaLog_ID)) # 1038
f_dupes <- f %>%
  filter(duplicated(.[["rnaLog_ID"]]))
View(f_dupes) # dup log IDs = 1184, 1188, 1902 (2 of each, going to leave them in just in case)

# Subset & adjust formatting for AllCaptures_2019, ditch duplicate rows
allCaptures_subset <- allCaptures %>%
  select(c("animalID", "name", "captureYear", "sex")) %>%
  distinct()
allCaptures_subset$name <- sub('-', '/', allCaptures_subset$name)

View(allCaptures_subset)

# Add animalID & sex to poop log
fecalID <- merge(f, allCaptures_subset, by.x = c("yearCollected", "name"), 
                 by.y = c("captureYear", "name"), all.x = T) %>%
  relocate(no.) %>%
  relocate(animalID, .after = no.)
View(fecalID)

# Any individuals assigned multiple animal IDs? No ID?
fecalID_dups <- fecalID %>%
  group_by(no.) %>% filter(n()>1)
length(unique(fecalID_dups$no.)) # 62 individuals with multiple animal IDs
View(fecalID_dups)

fecalID_na <- fecalID %>%
  filter(is.na(animalID))
View(fecalID_na)

# Create clean copy (without indivs with multiple/NA animal IDs)
fecalID_clean <- fecalID[!fecalID$no. %in% c(fecalID_dups$no., fecalID_na$no.),]
fecalID_clean %>%
  filter(duplicated(.[["no."]])) # 0 duplicated entries
View(fecalID_clean) # no NA animal IDs

# Export
write.csv(fecalID, "fecalLog_2009-2019_FULL.csv", row.names = F) # includes all individuals, including those with one ID assigned, multiple IDs assigned, and no ID assigned
write.csv(fecalID_clean, "fecalLog_2009-2019_CLEAN.csv", row.names = F) # individuals with one ID assigned
write.csv(fecalID_dups, "fecalLog_2009-2019_DUPS.csv", row.names = F) # individuals with multiple IDs assigned
write.csv(fecalID_na, "fecalLog_2009-2019_NA.csv", row.names = F) # individuals with NO ID assigned

############################
# FECAL SAMPLES TO EXTRACT #
############################
## First add total number of samples collected over the years to fecalID_clean
fecalTotals <- read.csv("./sampleOrganization/samplingHistory_fecal_CICRA_2009-2019_COUNTS.csv")
hairTotals <- read.csv("./sampleOrganization/samplingHistory_hair_CICRA_2009-2019_COUNTS.csv")
bloodTotals <- read.csv("./sampleOrganization/samplingHistory_blood_CICRA_2009-2019_COUNTS.csv")

fecalID_cleanCounts1 <- merge(fecalID_clean, fecalTotals, by = "animalID") %>%
  rename(totalFecal = 'totalCollected')
fecalID_cleanCounts2 <- merge(fecalID_cleanCounts1, hairTotals, by = "animalID") %>%
  rename(totalHair = 'totalCollected')
fecalID_cleanCounts3 <- merge(fecalID_cleanCounts2, bloodTotals, by = "animalID") %>%
  rename(totalBlood = 'totalCollected')
head(fecalID_cleanCounts3)

## Get separate lists of SFUS and SIMP and subset to unique animalIDs & those with more than 1 sample collected over the years
#fecalsClean_SFUS <- fecalID_cleanCounts3 %>%
#  filter(species == "SFUS") %>%
#  arrange(desc(yearCollected)) %>%
#  distinct(animalID, .keep_all = T) %>%
#  filter(totalFecal > 1)
#View(fecalsClean_SFUS)
#fecalsClean_SIMP <- fecalID_cleanCounts3 %>%
#  filter(species == "SIMP") %>%
#  arrange(desc(yearCollected)) %>%
#  distinct(animalID, .keep_all = T)  %>%
#  filter(totalFecal > 1)
#View(fecalsClean_SIMP)

## Random samples to extract
#samplesFecals_SFUS_f <- fecalsClean_SFUS[sample(which(fecalsClean_SFUS$sex == "F"),8),]
#View(samplesFecals_SFUS_f)
#samplesFecals_SFUS_m <- fecalsClean_SFUS[sample(which(fecalsClean_SFUS$sex == "M"),7),]
#View(samplesFecals_SFUS_m)

#samplesFecals_SIMP_f <- fecalsClean_SIMP[sample(which(fecalsClean_SIMP$sex == "F"),8),]
#View(samplesFecals_SIMP_f)
#samplesFecals_SIMP_m <- fecalsClean_SIMP[sample(which(fecalsClean_SIMP$sex == "M"),7),]
#View(samplesFecals_SIMP_m)

#fecals_toExtract <- rbind(samplesFecals_SFUS_f, samplesFecals_SFUS_m, 
 #                         samplesFecals_SIMP_f, samplesFecals_SIMP_m)
#View(fecals_toExtract)

# Export
#write.csv(fecals_toExtract, "./sampleOrganization/fecals_toExtract_initialList.csv", row.names = F)

fecalsClean_countsBOTH <- fecalID_cleanCounts3 %>%
  arrange(desc(yearCollected)) %>%
  distinct(animalID, .keep_all = T)
write.csv(fecalsClean_countsBOTH, "./sampleOrganization/fecalsUnique_plusCounts.csv", row.names = F)


########################
# Hair samples - Run 2 #
########################
fecalsToExtract_plusTubes <- read.csv("./fecalsToExtract_plusTubes.csv")
hairXtns <- read.csv("./sampleOrganization/tamGenetics_extractionsHair_master_11Jul2022.csv")
View(hairXtns)
View(fecalsToExtract_plusTubes)

hairRun2 <- hairXtns %>%
  filter(animalID %in% fecalsToExtract_plusTubes$animalID) %>%
  filter(located. == "yes")
View(hairRun2)

write.csv(hairRun2, "./sampleOrganization/hairToInclude_run2.csv", row.names = F)


#########################
# Blood samples - Run 2 #
#########################
bloodXtns <- read.csv("./sampleOrganization/tamGenetics_extractionsBlood_master_13Jul2022.csv")
View(bloodXtns)

bloodRun2 <- bloodXtns %>%
  filter(animalID %in% fecalsToExtract_plusTubes$animalID)
bloodRun2$animalID <- as.numeric(bloodRun2$animalID)
View(bloodRun2)
length(bloodRun2$animalID) # why is this 29 and not 30

fecalsToExtract_plusTubes$animalID %in% bloodRun2$animalID # missing animalID 134

# Time to investigate
uniqueBlood <- read_excel("./sampleOrganization/uniqueLongmire_CICRA_2013-2019.xlsx") %>%
  as.data.frame()
View(uniqueBlood)

uniqueBlood2 <- uniqueBlood %>% # ditch samples that I couldn't find
  filter(located == "yes")

# Which animalID samples did I (apparently) find that haven't yet been extracted?
missingBloodIDs <- uniqueBlood$animalID[!uniqueBlood$animalID %in% bloodXtns$animalID] # 231  59 134  62 138 221 293

# ok so where are they?
missingBloodXtns <- uniqueBlood2 %>%
  filter(animalID %in% missingBloodIDs)
View(missingBloodXtns)

# Figured out that I just never extracted those 6 samples; have now fixed so let's do this again
bloodXtns <- read.csv("./tamGenetics_extractionsBlood_master_18Jul2022.csv")
View(bloodXtns)

bloodRun2 <- bloodXtns %>%
  filter(animalID %in% fecalsToExtract_plusTubes$animalID)
bloodRun2$animalID <- as.numeric(bloodRun2$animalID)
View(bloodRun2)
length(bloodRun2$animalID)

write.csv(bloodRun2, "./bloodToInclude_run2.csv", row.names = F)

##########################
# FULL SAMPLE LIST RUN 2 #
##########################
fecals <- read.csv("./fecalsToExtract_plusTubes.csv") %>%
  select(c("fecalXtnTube", "notes", "animalID", "name", "species",
           "sex", "totalFecal", "totalHair", "totalBlood")) %>%
  rename(animalName = "name")
View(fecals)

hairs <- hairRun2 %>%
  select(c("animalID", "xtnTube.", "xtnPlate.", "xtnRow", "xtnCol", "animalName", "species",
           "sex")) %>%
  rename(hairXtnTube = "xtnTube.",
         hairXtnPlate = "xtnPlate.",
         hairXtnRow = "xtnRow",
         hairXtnCol = "xtnCol")
hairs$animalName <- gsub("-", "/", hairs$animalName) # adjust name formatting
View(hairs)

bloods <- bloodRun2 %>%
  select(c("animalID", "xtnTube.", "xtnPlate.", "xtnRow", "xtnCol", "animalName", "species",
           "sex")) %>%
  rename(bloodXtnTube = "xtnTube.",
         bloodXtnPlate = "xtnPlate.",
         bloodXtnRow = "xtnRow",
         bloodXtnCol = "xtnCol")
bloods$animalName <- gsub("-", "/", bloods$animalName) # adjust name formatting
colnames(bloods)

mergeFecalsHairs <- merge(fecals, hairs,
                        by = c("animalID", "animalName", "species", "sex"))
run2SampleList <- merge(mergeFecalsHairs, bloods, 
                        by = c("animalID", "animalName", "species", "sex")) %>%
  relocate(totalFecal, .after = last_col()) %>%
  relocate(totalHair, .after = totalFecal) %>%
  relocate(totalBlood, .after = totalHair) %>%
  relocate(notes)
View(run2SampleList)                        

write.csv(run2SampleList, "./run2_sampleList.csv", row.names = F)

##################################
# ADDING METADATA TO RUN2 PLATES #
##################################
run2Metadata <- read.csv("./sampleOrganization/run2_fecalHairBlood/run2_sampleList.csv")
run2Plate1 <- read.csv("./sampleOrganization/run2_fecalHairBlood/run2_plate1_samples.csv")
View(run2Plate1)

run2Metadata_fecals <- run2Metadata %>%
  select(c("notes", "animalID", "animalName", "species", "sex", "fecalXtnTube")) %>%
  mutate(hairXtnTube = "NA",
         hairXtnPlate = "NA",
         hairXtnCol = "NA",
         hairXtnRow = "NA")
View(run2Metadata_fecals)

run2Metadata_hair <- run2Metadata %>%
  select(c("notes", "animalID", "animalName", "species", "sex", 
           "hairXtnTube", "hairXtnPlate", "hairXtnRow", "hairXtnCol")) %>%
  mutate(fecalXtnTube = "NA")
View(run2Metadata_hair)

run2Metadata_plate1Subset <- rbind.data.frame(run2Metadata_fecals, run2Metadata_hair)
View(run2Metadata_plate1Subset)

run2Plate1_metadata <- merge(run2Plate1, run2Metadata_plate1Subset, 
                                  by = c("fecalXtnTube", "hairXtnTube", "hairXtnPlate", "hairXtnRow", "hairXtnCol"),
                                  all.x = T) %>%
  relocate(pcr1Plate) %>%
  relocate(col, .after = pcr1Plate) %>%
  relocate(row, .after = col)
View(run2Plate1_metadata)

write.csv(run2Plate1_metadata, "./sampleOrganization/run2_fecalHairBlood/run2_plate1_metadata.csv", row.names = F)
