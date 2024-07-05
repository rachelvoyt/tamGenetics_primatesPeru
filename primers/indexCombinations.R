library(tidyverse)

i5 <- c('S501',
        'S502',
        'S503',
        'S504',
        'S505',
        'S506',
        'S507',
        'S508',
        'S510',
        'S511',
        'S513',
        'S515',
        'S516',
        'S517',
        'S518',
        'S520',
        'S521',
        'S522')
i7 <- c('N701',
        'N702',
        'N703',
        'N704',
        'N705',
        'N706',
        'N707',
        'N708',
        'N709',
        'N710',
        'N711',
        'N712',
        'N714',
        'N715',
        'N716',
        'N718',
        'N719',
        'N720',
        'N721',
        'N722',
        'N723',
        'N724',
        'N726',
        'N727',
        'N728',
        'N729')
df <- expand.grid(i5, i7) %>%
  unite(combo, c('Var1', 'Var2'), sep = "_")
View(df) # 468 unique combos possible

sets <- read.csv("illuminaIndices_setsABCD.csv")
length(unique(sets$combo)) # 384 unique combos; success

# Which do we have left to play with?
combosRemaining <- df %>%
  filter(!combo %in% sets$combo) %>%
  arrange(combo) # 84 combos remaining
write.table(combosRemaining, "illuminaIndicies_extraCombos.xlsx", row.names = F)

