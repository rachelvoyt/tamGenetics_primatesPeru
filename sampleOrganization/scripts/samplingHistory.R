# Creating sampling history records for blood, hair, and fecal samples
# from CICRA tamarins 2009-2019 - R. Voyt Nov 2021

setwd("/home/rachelvoyt/Documents/UT-Grad/Development/repos/tamarinGenetics_primatesPeru")

# Packages
library(tidyverse)
library(lubridate)

# Load in data
aging_individuals <- read.csv("./sampleOrganization/originalData/aging_individuals.csv")
juvenile_tamarins <- read.csv("./sampleOrganization/originalData/juvenile_tamarins.csv", sep = ",")
AllCaptures_InfancyPeriods <- read.csv("./sampleOrganization/allCaptures_infancyPeriods_2009-2019.csv")
longmireLog <- read.csv("./sampleOrganization/originalData/longmireLog_CICRA_2013-2019.csv")
hairLog <- read.csv("./sampleOrganization/hairSamples_CICRA_2009-2019_MASTER.csv")
# fecalLog <- read.csv("./sampleOrganization/originalData/PoopLog11.9.21_forRachel.csv")
fecalLog_clean <- read.csv("./sampleOrganization/fecalLog_2009-2019_CLEAN.csv")

# ID juveniles in aging_individuals.csv using juvenile_tamarins.csv dataset from Gideon
# colnames(aging_individuals)
# colnames(juveniles)
# aging_juveniles <- lh

# aging_juveniles$entryType <- ifelse("aging_individuals$AnimalID" == "juveniles$AnimalID", aging_juveniles$entryType == "birth", NA)
# View(aging_juveniles) # Not working??
# ifelse(aging_individuals$AnimalID == juveniles$AnimalID, "Yes", "No") # no matches--
# looking back at the csv files, looks like we're missing a lot of individuals

# Create new list of unique individuals based on AllCaptures_InfancyPeriods_2009-2019 (created by RV)
head(AllCaptures_InfancyPeriods)
uniqueIndivs <- AllCaptures_InfancyPeriods[,c(2,3,4,6,9,11,12,14,15,16)] # subset to clear out unneeded columns
head(uniqueIndivs)
uniqueIndivs <- uniqueIndivs[!duplicated(uniqueIndivs["animalID"]),] # ditch duplicates

# Recreate aging dataframe by combining new list of unique indivs w/aging_individuals.csv from Gideon
head(aging_individuals)
d <- aging_individuals[,c(2,6:17)] # subset to only animal ID and year presence/absence columns
head(d)
names(d)[1] <- "animalID"
captureHistory <- merge(uniqueIndivs, d, by.x = "animalID", all.x = T) # merge; all.x=T enters NA for any w/o presence/absence data
View(captureHistory)
head(captureHistory)

# Any individuals in juvenile_tamarins.csv that aren't in AllCaptures_InfancyPeriods?
juvenile_tamarins$animalID[!juvenile_tamarins$animalID %in% AllCaptures_InfancyPeriods$animalID]
# nope

# Create new entryType columns and ID individuals who were born into the population
captureHistory <- captureHistory %>%
  mutate(entryType = case_when(
    !is.na(infStart) ~ "birth"
  ))
View(captureHistory)

# Rename capture columns
names(captureHistory)[11:22] <- c("capture2009", "capture2010", "capture2011",
                                  "capture2012", "capture2013", "capture2014",
                                  "capture2015", "capture2016", "capture2017",
                                  "capture2018", "capture2019", "capture2021")
head(captureHistory)

# Create entryYear column
captureHistory$infStart <- mdy(captureHistory$infStart)
captureHistory$infEnd <- mdy(captureHistory$infEnd)

captureHistory <- captureHistory %>%
  mutate(entryYear = case_when(
    (capture2009 >= 1 & is.na(infStart)) ~ "2009",
    (capture2010 >= 1 & is.na(infStart)) ~ "2010",
    (capture2011 >= 1 & is.na(infStart)) >= 1 ~ "2011",
    (capture2012 >= 1 & is.na(infStart)) ~ "2012",
    (capture2013 >= 1 & is.na(infStart)) ~ "2013",
    (capture2014 >= 1 & is.na(infStart)) ~ "2014",
    (capture2015 >= 1 & is.na(infStart)) >= 1 ~ "2015",
    (capture2016 >= 1 & is.na(infStart)) >= 1 ~ "2016",
    (capture2017 >= 1 & is.na(infStart)) ~ "2017",
    (capture2018 >= 1 & is.na(infStart)) ~ "2018",
    (capture2019 >= 1 & is.na(infStart)) ~ "2019",
    (capture2021 >= 1 & is.na(infStart)) ~ "2021",
    TRUE ~ as.character(year(infStart))
  ))
View(captureHistory)


# Create df that only has individual info from captureHistory
indivInfo <- captureHistory[,c(1,2,3,4,5,6,7,8,9,10,23,24)]
head(indivInfo)

# Create new dfs for blood, hair, and fecal samples collected
## Blood samples
### Ensure date column is coded as such in longmireLog
head(longmireLog)
longmireLog$captureDate <- as.Date(longmireLog$captureDate, "%m/%d/%y")
class(longmireLog$captureDate)

### Count the number of times each individual was sampled in each year and create new dataframe
bloodCounts <- longmireLog %>%
  group_by(animalID) %>%
  group_by(year(captureDate), .add = T) %>%
  summarise(n())
View(bloodCounts)
names(bloodCounts)[2] <- "year"
names(bloodCounts)[3] <- "bloodSamples"
head(bloodCounts)

bloodCounts <- as.data.frame(bloodCounts)

bloodHistory <- pivot_wider(bloodCounts, 
                                names_from = year,
                                names_sort = T,
                                values_from = bloodSamples) %>%
  rename(
    blood2013 = '2013',
    blood2014 = '2014',
    blood2015 = '2015',
    blood2016 = '2016',
    blood2017 = '2017',
    blood2018 = '2018',
    blood2019 = '2019') %>%
  select(-"NA") %>% # ditching "NA" column
  filter(!row_number() %in% c(410)) %>%
  merge(., indivInfo, by = "animalID") %>% # adding indiv info
  arrange(as.numeric(animalID)) %>%
  relocate(c(entryYear, entryType), .after = animalID)
  
View(bloodHistory)

write.csv(bloodHistory,"samplingHistory_blood_CICRA_2013-2019.csv", row.names = F)

## Now hair samples
hairCounts <- hairLog %>%
  group_by(animalID) %>%
  group_by(year(mdy(captureDate)), .add = T) %>%
  summarise(n())
View(hairCounts)
names(hairCounts)[2] <- "year"
names(hairCounts)[3] <- "hairSamples"
head(hairCounts)

hairCounts <- as.data.frame(hairCounts)

hairHistory <- pivot_wider(hairCounts, 
                            names_from = year,
                            names_sort = T,
                            values_from = hairSamples) %>%
  rename(
    hair2009 = '2009',
    hair2010 = '2010',
    hair2011 = '2011',
    hair2013 = '2013',
    hair2014 = '2014',
    hair2015 = '2015',
    hair2016 = '2016',
    hair2017 = '2017',
    hair2018 = '2018',
    hair2019 = '2019') %>%
  select(-"NA") %>% # ditching "NA" column
  filter(!row_number() %in% c(370)) %>% # ditching animalID "NULL" (this was a ditched sample)
  merge(., indivInfo, by = "animalID") %>% # adding indiv info
  arrange(as.numeric(animalID))

View(hairHistory)
write.csv(hairHistory,"samplingHistory_hair_CICRA_2009-2019.csv", row.names = F)

## And last but not least, fecal samples
View(fecalLog_clean) # no animalID column

fecalCounts <- fecalLog_clean %>%
  group_by(animalID) %>%
  group_by(year(mdy(dateClean)), .add = T) %>%
  summarise(n())
View(fecalCounts)
names(fecalCounts)[2] <- "year"
names(fecalCounts)[3] <- "fecalSamples"
head(fecalCounts)

fecalCounts <- as.data.frame(fecalCounts)

fecalHistory <- pivot_wider(fecalCounts, 
                           names_from = year,
                           names_sort = T,
                           values_from = fecalSamples) %>%
  rename(
    fecal2009 = '2009',
    fecal2010 = '2010',
    fecal2011 = '2011',
    fecal2013 = '2013',
    fecal2014 = '2014',
    fecal2015 = '2015',
    fecal2016 = '2016',
    fecal2017 = '2017',
    fecal2018 = '2018',
    fecal2019 = '2019') %>%
  merge(., indivInfo, by = "animalID") %>% # adding indiv info
  arrange(as.numeric(animalID))

View(fecalHistory)
write.csv(fecalHistory,"./sampleOrganization/samplingHistory_fecal_CICRA_2009-2019.csv", row.names = F)

# Let's also write csv for total number of samples collected
fecalTotals <- fecalLog_clean %>%
  group_by(animalID) %>%
  summarise(n()) %>%
  rename(totalCollected = 'n()')
head(fecalTotals)

hairTotals <- hairLog %>%
  group_by(animalID) %>%
  summarise(n()) %>%
  rename(totalCollected = 'n()')
head(hairTotals)

bloodTotals <- longmireLog %>%
  group_by(animalID) %>%
  summarise(n()) %>%
  rename(totalCollected = 'n()')
head(bloodTotals)

# Export
write.csv(fecalTotals, "./sampleOrganization/samplingHistory_fecal_CICRA_2009-2019_COUNTS.csv", row.names = F)
write.csv(hairTotals, "./sampleOrganization/samplingHistory_hair_CICRA_2009-2019_COUNTS.csv", row.names = F)
write.csv(bloodTotals, "./sampleOrganization/samplingHistory_blood_CICRA_2009-2019_COUNTS.csv", row.names = F)

# And one more kind of visualization, where we see all tube numbers for each animalID
fecalTubes <- fecalLog_clean %>%
  group_by(animalID) %>%
  summarise(rnaTubeNos. = paste(sort(unique(rnaTubeNo.)), collapse = ", "))
View(fecalTubes)

# Export
write.csv(fecalTubes, "./sampleOrganization/samplingHistory_fecal_CICRA_2009-2019_tubes.csv", row.names = F)

# Let's add that info to our fecalsToExtract
fecalsToExtract <- read.csv("./sampleOrganization/fecalsToExtract.csv")
head(fecalsToExtract)

fecalsToExtract2 <- merge(fecalsToExtract, fecalTubes, by = "animalID")
View(fecalsToExtract2)

write.csv(fecalsToExtract2, "./sampleOrganization/fecalsToExtract_plusTubes.csv", row.names = F)
