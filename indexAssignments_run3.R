library(tidyverse)

redos <- read.csv("redos_run3.csv", header = T)
indAssign <- read.csv("indexAssignments_run3.csv", header = T)

# Assign indices to redos

redoIndices <- merge(redos, indAssign, by = "pcr1_original", all.x = T) %>%
  select(c("pcr1_original", "xtnLocation", "primerPool", "sampleType", "i5_index", "i7_index", "index_combo"))

colnames(redos)
colnames(indAssign)

write.csv(redoIndices, "redos_run3_indexed.csv")
