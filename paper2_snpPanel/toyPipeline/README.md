# README: tamGenetics how-to guide for GT-seq data analysis

The tamGenetics toyPipeline is a step-by-step guide for the preparation, processing, genotyping, and analysis of Genotyping-in-Thousands by Sequencing (GT-seq) data from Illumina and/or Nanopore sequencing platforms. The guide is designed for those who are new to GT-seq analysis, but also includes additional details, tips, and scripts for those who are new to bioinformatic analyses in general.

The guide is divided into three sections:

-   Part 1 (tamGenetics_gtseqHowTo_pt1): Sequence preparation & quality analyses
-   Part 2 (tamGenetics_gtseqHowTo_pt2): Amplicon read counting & genotyping
-   Part 3 (tamGenetics_gtseqHowTo_pt3): Loci and sample performance analyses

For each of these sections, I've provided "toy data" if you'd just like to get a feel for the pipeline as well as directions for formatting and processing your own data.

Prior to working through this guide, I recommend creating and organizing directories as follows:

```         
├── project_name (e.g., toyPipeline)
│   ├── GTscore_sourceScripts
│   └── seqrun_name (e.g., toyRun)
|       ├── 00_toyRun_seqs
|       ├── 01_toyRun_interleaved
|       ├── 02_toyRun_qualityChecks
|           └── multiqc_data
|       ├── 03_toyRun_gtscore
|           ├── summaryFiles
|           └── toyRun_pipeline_pt1.Rmd
|       ├── 04_toyRun_genoAnalyses
|       └── toyRun_metadata.csv
├── project_name.Rproj
├── README.md
└── .gitignore
```
