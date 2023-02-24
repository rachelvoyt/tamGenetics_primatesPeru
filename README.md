# tamGenetics_primatesPeru

This repository contains all files and scripts associated with data analysis for my dissertation on saddleback and bearded emperor tamarins in Amazonian Peru. At present scripts and data are divided by sequencing run, including three on Illumina (all "tamRun" sections) and one on Nanopore (the "laLab" section). There's also a separate folder for the GTscore source scripts. 

**NOTE** that I have made small modifications to the original versions of two of the GTscore scripts:
* matchReads.pl - added an option to specify the "inDir" (lines 43, 45, 179 and 180)
* GTscore.R - added an option for "\\[ATGC\\]"="N" (lines 616 and 617) to replace brackets in probe
