################################################################################################
#                                                                                              #
#                                         POLYGEN                                              #
#                                                                                              #
################################################################################################

# This is my version of the GTscore polygen script; it modifies the original by
# adding the depthCutoff variable to define desired read depth cutoff for genotyping

#PolyGen is broken into two functions
#The first function (polyGen) combines the locus table and read counts into a single file and submits to the second function
#The second funtion (genoSetup) genotypes the data and returns the final genotypes to polyGen where it undergoes final formatting
polyGen_rv<-function(locusTable,readCounts,p_thresh=0.05,epsilon=0.01, depthCutoff=0){
  
  # apply read depth cutoff if specified
  if(depthCutoff > 0){
    # set up a function to sum the read counts per allele for each locus, using package gsubfn
    repl <- function(x) gsubfn("(\\d+),(\\d+)", ~ as.numeric(x) + as.numeric(y), paste(x))
    
    # then apply the function to readCounts to sum each set of allele reads for each locus
    readSums <- replace(readCounts, TRUE, lapply(readCounts, repl)) %>%
      mutate(across(everything(),as.numeric))
    
    # recode loci with < depthCutoff read to "0,0"
    readCounts[readSums < depthCutoff] <- "0,0"
  }
  
  #remove correction factor column from locusTable (if present)
  if("correctionFactors" %in% colnames(locusTable)){
    locusTable<-locusTable %>% select(-correctionFactors)
  }
  
  #combine locus information and read counts into single table
  combinedData<-cbind(locusTable,readCounts)
  #pbapply has integrated progress bar, use apply if pbapply cannot be installed
  results<-pbapply(combinedData,1,genoSetup,epsilon,p_thresh)
  #results<-pbapply(combinedData,1,genoSetup,epsilon=0.01)
  #results<-apply(combinedData,1,genoSetup,epsilon=0.01)
  results<-t(results)
  return(results)
}

genoSetup<-function(genoData,epsilon=0.01,p_thresh=0.05){
  readList<-genoData[4:length(genoData)]
  n_alleles<-strsplit(genoData[3],",")
  n_alleles<-length(n_alleles[[1]])
  #use numbers in place of actual alleles to allow haplotypes and other allele coding (indel, etc)
  #convert back to actual alleles later
  alleles=as.character(seq(1:n_alleles))
  ploidy=as.numeric(genoData[2])
  #set up possible genotypes
  alleleList<-substr(alleles,1,n_alleles)
  alleleList<-replicate(ploidy, alleleList) 
  #convert to vector, then sort numerically and convert back to text
  alleleList<-as.vector(alleleList)    
  alleleList<-sort(as.numeric(alleleList))
  alleleList<-as.character(alleleList)
  genoCombos<-utils::combn(alleleList,ploidy)
  #print(genoCombos)
  GenotypeList<-t(genoCombos)
  possibleGenotypes<-unique(GenotypeList)
  
  #make conversion table for genotypes
  realAlleles<-genoData[3]
  realAllelesOrder<-unlist(strsplit(realAlleles,",",perl=TRUE))
  
  #make table to convert numeric genotype codes to real genotypes
  numericGeno<-apply(possibleGenotypes,1,function(x) paste(x,collapse=","))
  realGenotypes<-apply(possibleGenotypes,2,function(x) realAllelesOrder[as.numeric(x)])
  realGeno<-apply(realGenotypes,1,function(x) paste(x,collapse=","))
  genoConvert<-as.data.frame(t(rbind(numericGeno,realGeno)))
  
  #function to generate allele dosage for each genotype
  generateDosage<-function(genos){
    #split genotype into each allele for dosage assignment
    #genoAlleles<-str_split_fixed(genos,",",2)
    genoAlleles<-str_split(genos,",",simplify=TRUE)
    
    #function to count number of times each possible allele is present in each possible genotype
    genoDosage<-function(singleGeno){
      #test vector of all possible alleles to see which allele matches the genotype
      #do this individually for each allele in the genotype
      matches<-t(sapply(singleGeno,function(x) as.numeric(alleles==x)))
      #sum vector of possible allele matches for each allele in genotype
      #this gives count of each possible allele in the genotype being tested
      matches<-apply(matches,2,function(x) sum(x))
      return(matches)
    }
    
    #count number of times each possible allele is present in each possible genotype
    genoMatches<-t(apply(genoAlleles,1,genoDosage))
    #divide count matrix by ploidy to get relative dosage of each allele
    dosage<-genoMatches/ploidy
    return(dosage)
  }
  
  relative_dosage<-generateDosage(numericGeno)
  
  #make matrix of read chances
  read_chances<-matrix(NA,nrow=1,ncol=ploidy)
  #read_chances<-(relative_dosage*(1-epsilon) + (1-relative_dosage)*epsilon)
  #updated error model dividing epsilon by 3 (n alleles -1) where n alleles is the number of possible bases (4, ATCG)
  read_chances<-(relative_dosage*(1-epsilon) + (1-relative_dosage)*epsilon/3)
  
  #make likelihood function
  likelihoodFunc<-function(reads){
    #convert reads to alleles
    #parse allele counts
    if(reads=="."){
      reads<-paste(as.character(replicate(n_alleles, 0)),collapse=",")
    }
    alleleCounts<-as.numeric(unlist(strsplit(reads,",")))
    initLikelihood<-log(1)
    likelihoodMatrix<-matrix(0,nrow=dim(possibleGenotypes)[1],ncol=ploidy)
    #likelihood calculation
    likelihoodMatrix<-t(initLikelihood+log(t(read_chances))*(alleleCounts))
    likelihood<-apply(likelihoodMatrix,1,sum)
    #genotypes<-apply(possibleGenotypes,1,function(x) paste(x,collapse=""))
    genotypes<-apply(possibleGenotypes,1,function(x) paste(x,collapse=",")) #this is original for reference
    
    #create likelihood results matrix
    like_of_geno<-as.data.frame(matrix(NA,nrow=dim(possibleGenotypes)[1],ncol=2))
    colnames(like_of_geno)<-c("genotype","likelihood")
    like_of_geno$genotype<-genotypes
    like_of_geno$likelihood<-likelihood
    
    #print(like_of_geno)
    
    #use a likelihood ratio test to determine the support for the 'best' genotype
    #order likelihoods
    geno_likes<-like_of_geno[order(-like_of_geno$likelihood),]
    #rename rows so they can be extracted in correct order
    rownames(geno_likes)<-1:nrow(geno_likes)
    #compare likelihood ratio of two most likely models
    LR<-2*(geno_likes[1,2]-geno_likes[2,2])
    #get p-value of likelihood ratio
    p<-1-pchisq(LR, 1)
    #if(p<0.05){
    if(p<p_thresh){
      genoResult<-geno_likes[1,1]
      genoResult<-genoConvert$realGeno[genoConvert$numericGeno==genoResult]
    }else{
      genoResult<-"0"
    }
    result<-as.character(genoResult)
    return(result)
  }
  
  likelihoods<-sapply(readList,likelihoodFunc)
  return(likelihoods)
}

################################################################################################
#
#                                         DATA SUMMARIES
#
################################################################################################

#CALCULATE AVERAGE READ DEPTH, GENOTYPE RATE, MINOR ALLELE FREQUENCY, AND MAJOR ALLELE FREQUENCY
summarizeGTscore<-function(alleleReads, locusTable, genotypes){
  #remove correction factor column from locusTable (if present)
  if("correctionFactors" %in% colnames(locusTable)){
    locusTable<-locusTable %>% select(-correctionFactors)
  }
  #calculate average read depth
  reads<-apply(alleleReads, 1:2, function(x) sum(as.numeric(unlist(str_split(x,",")))))
  totalReads<-apply(reads, 1, sum)
  #Average read depth is calculated by dividing my number of samples with non-zero reads
  #Is this appropriate?
  nonZeroSamples<-apply(reads, 1, function(x) {length(x)-sum(x=="0")})
  avgReads<-totalReads/nonZeroSamples
  calcReadDepth_results<-data.frame(keyName=names(avgReads), value=avgReads, row.names=NULL)
  colnames(calcReadDepth_results)<-c("Locus_ID","AvgReadDepth")
  
  #calculate genotype rate
  genotypeRate_results<-apply(genotypes,1,function(x){(length(x)-sum(x=="0"))/length(x)})
  genotypeRate_results<-data.frame(keyName=names(genotypeRate_results), value=genotypeRate_results,row.names=NULL)
  colnames(genotypeRate_results)<-c("Locus_ID","GenotypeRate")
  
  #calculate minor allele frequency and major allele frequency
  getAlleleFreqs<-function(alleleFreqsCombinedData){
    Locus_ID<-as.character(alleleFreqsCombinedData[1])
    #get unique alleles
    alleles<-unlist(str_split(unlist(alleleFreqsCombinedData[3]),","))
    #get counts and frequency for each unique allele
    alleleCounts<-unlist(lapply(alleles, function(x) sum(str_count(as.character(unlist(alleleFreqsCombinedData[4:length(alleleFreqsCombinedData)])),x))))
    alleleFreqs<-alleleCounts/sum(alleleCounts)
    #get minimum frequency and maximum frequency
    minFreq<-min(alleleFreqs)
    maxFreq<-max(alleleFreqs)
    #combine all frequencies into comma delimited string
    allFreqs<-paste(round(alleleFreqs,digits=2),collapse=",")
    #combine and return minFreq,maxFreq,allFreqs
    freqResults<-paste(Locus_ID,minFreq,maxFreq,alleleFreqsCombinedData[3],allFreqs,sep=" ")
    return(freqResults)
  }
  alleleFreqsCombinedData<-cbind(locusTable,genotypes)
  alleleFreqs_results<-as.data.frame(apply(alleleFreqsCombinedData,1,getAlleleFreqs),row.names=NULL)
  alleleFreqs_results<-data.frame(str_split_fixed(alleleFreqs_results[,1]," ",5))
  colnames(alleleFreqs_results)<-c("Locus_ID","minFreq","maxFreq","alleles","allFreqs")
  alleleFreqs_results
  
  
  ####################################################################################################
  
  #calculate contamination score, this applies a binomial test to read counts from heterozygous genotypes
  #the contamination score is the proportion of heterozygous genotypes that failed the binomial test for each sample
  
  #function to create hetMatrix, 1 is heterozygous, 0 is homozygous
  idHets<-function(genos){
    alleles<-str_split(genos,",")
    hetCount<-unlist(lapply(alleles,function(x) length(unique(x))))
    hetCount[hetCount!=2]<-0
    hetCount[hetCount==2]<-1
    return(hetCount)
  }
  
  #function to run binomial test
  binomTest<-function(reads){
    ########binomial test doesn't work for haplotypes as written
    #should be able to work for haplotypes as long as locus is diploid
    #work on fixing, for now check if there are more than two alleles and set all reads to 0 if that is the case_when
    #can't directly check for more than two alleles because splitting alleles previously into allele1 and allele2 forced
    #counts into two columns.
    #if more than two alleles, conversion to number in the second column results in NA.
    #check for NA and if present reset all A1 and A2 in this code to 0
    A1<-as.numeric(str_split_fixed(reads,",",2)[,1])
    A2<-as.numeric(str_split_fixed(reads,",",2)[,2])
    A1NA<-sum(is.na(A1))
    A2NA<-sum(is.na(A2))
    
    if(A1NA>0|A2NA>0){
      A1<-0
      A2<-0
    }
    
    tot<-A1+A2
    
    if(tot!=0){
      result<-binom.test(A1, tot, 0.5, alternative=c("two.sided"), conf.level = 0.95)
      return(result$p.value)
    }else{
      return(NA)
    }
  }
  
  #function to manage binomial test
  testHet<-function(reads){
    binomTest_results<-unlist(lapply(reads,binomTest))
    numOutlier<-sum(binomTest_results<=0.05,na.rm=TRUE)
    numHet<-sum(!is.na(binomTest_results))
    #result is number of genotypes that failed binomial test over total number of heterozygous genotypes for each sample
    result<-numOutlier/numHet
    return(result)
  }
  
  #make matrix where heterozygous genotypes are 1 and homozygous genotypes are 0
  hetMatrix<-apply(genotypes,1,function(x){idHets(x)})
  
  #######################################################
  #this step causes problems if loci have more than two alleles, work on fixing...
  
  #split reads into allele 1 and allele 2
  allele1<-apply(alleleReads,1,function(x) as.numeric(str_split_fixed(x,",",2)[,1]))
  allele2<-apply(alleleReads,1,function(x) as.numeric(str_split_fixed(x,",",2)[,2]))
  
  #multiply by het matrix to keep only counts from heterozygous genotypes
  allele1HetCounts<-allele1*hetMatrix
  allele2HetCounts<-allele2*hetMatrix
  
  
  #recombine counts so only heterozygous genotypes from original count data are retained
  combinedHetCounts<-paste(allele1HetCounts,allele2HetCounts,sep=",")
  #reset dimensions and reassign column names
  dim(combinedHetCounts)<-c(dim(allele1HetCounts)[1],dim(allele1HetCounts)[2])
  colnames(combinedHetCounts)<-colnames(allele1HetCounts)
  
  
  #run function to get heterozygous contamination score for all samples
  hetContaminationResults<-apply(combinedHetCounts,2,testHet)
  hetContaminationResults<-data.frame(Locus_ID=names(hetContaminationResults),conScore=hetContaminationResults,stringsAsFactors=FALSE,row.names=NULL)
  
  
  ####################################################################################################
  
  #combine results and return
  depth_geno<-merge(calcReadDepth_results, genotypeRate_results)
  all_combined<-merge(depth_geno,alleleFreqs_results)
  
  all_combined<-merge(all_combined,hetContaminationResults)
  
  all_combined$Locus_ID<-as.character(all_combined$Locus_ID)
  #ensure appropriate columns are numeric
  all_combined$AvgReadDepth<-as.numeric(as.character(all_combined$AvgReadDepth))
  all_combined$GenotypeRate<-as.numeric(as.character(all_combined$GenotypeRate))
  all_combined$minFreq<-as.numeric(as.character(all_combined$minFreq))
  all_combined$maxFreq<-as.numeric(as.character(all_combined$maxFreq))
  #set final column names
  colnames(all_combined)<-c("Locus_ID","AvgReadDepth","GenotypeRate","minAF","majAF","alleles","allFreqs","conScore")
  
  return(all_combined)
}
