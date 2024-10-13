#######################################################################################################################
#### Supplement S1 of "A New Mark-Recapture Approach for Abundance Estimation of Social Species"
#### Hickey, J., Sollmann, R., PlosOne

#### This script (Part A) simulates capture-recapture data for a group-structured population
#### First, groups are detected, then individuals within groups are detected, conditional
#### on group detection. Input parameters are motivated by a study on mountain gorillas.
#### Scenarios with varying levels of group detection (pg) and individual detection (pi)
#### are explored. Please see main text for further details. 
#### The script is followed by a script to analyze generated data with the Two-Step and One-Step models (Part B);
#### and finally, a script to summarize model output across iterations (Part C). 


#######################################################################################################################
#######################################################################################################################
####### PART A - DATA SIMULATION ######################################################################################

#### This is an example simulation script, keeping pi = 0.7 and varying pg from 0.3 to 0.9
#### To run remaining simulations discussed in the manuscript, set pg = 0.7 and vary pi from 0.3 to 0.9

library(actuar)

####set the parameters that are fixed for all iterations first

###total number of groups in the population
N<-40

##average group size 
n<-13

###augmentation parameter for number of groups; needs to be high enough so as to not bound the estimate of N
M<-60  

#levels of group detection probability 
P.long<-seq(0.3, 0.9, 0.2) 

##probability of detecting an individual
p<-0.7  

K<-2 ##sweep - detection level for groups
k<-3 ##nests - detection level for individuals within groups

## function to get possible combinations for capture histories
## this calculates in how many different ways a capture history can arise
## see Supplement S3 for more detail
get.nposs<-function(x){
  out=NULL
  for (j in 1:(x+1)){
    out[j]<-dim(combn(x,(j-1)))[2]
  }
  return(out)
}

nposs<-get.nposs(k)

## creates a matrix of all possible observable capture histories
poss.cap<-as.matrix(expand.grid(0:k, 0:k))[-1,c(2,1)]


n.iter<-1000 # number of iterations for your simulation

## first, loop over possible values of group detection probability
for (pp in 1:length(P.long)){

  set.seed(2013) 
  
  P<-P.long[pp] 
  
##Create folder to hold simulated data and models for each scenario
path<-paste(getwd(), "/TwostepSim_pg", P*10, "_pi", p*10, sep="")

if(file.exists(path)==FALSE) dir.create(path = path)


	for (iter in 1:n.iter){

		### generate group sizes
		n.eff<-rztpois(N, n) 

		#### calculate total population size
		ntotal<-sum(n.eff)

		### generate group level detection histories
		OBS<-matrix(NA, N, K)

			for (i in 1:N){
				OBS[i,]<-rbinom(K, 1, P)
			}

		## how many and which groups were observed at least once?		
		g.obs<-sum(apply(OBS, 1, sum)>0)
		seen<-which(apply(OBS, 1, sum)>0)

		###set up objects for:
		## detection history frequencies for each observed group
		obs<-matrix(NA, g.obs, ((k+1)^2-1))
 
		## individual detection probability conditional on group detection
		p.i.eff<-matrix(NA, g.obs, K)
		
		## multinomial cell probabilities for detection history frequencies
		pvec<-matrix(NA,g.obs, (k+1)^2)
		
		## probability of being detected at least once; number individuals observed per group
		p.star<-nobs<-NULL
		pmat<-array(NA,c(g.obs, (k+1), (k+1)) )

		### Generate individual detection data - see manuscript and S3 for more detail
			for (i in 1:g.obs){
  
 				p.i.eff[i,1]<- p*OBS[seen[i],1]   
  				p.i.eff[i,2]<- p*OBS[seen[i],2]  
  
  					for (kk in 1:(k+1)){

   						for (j in 1:(k+1)){
      							pmat[i,kk,j]<- p.i.eff[i,1]^(kk-1) * (1-p.i.eff[i,1])^(k-(kk-1)) * nposs[kk]*
        							       p.i.eff[i,2]^(j-1) * (1-p.i.eff[i,2])^(k-(j-1)) * nposs[j]
    						}
    						
						pvec[i, ((kk-1)*(k+1)+1):((kk-1)*(k+1)+(k+1))]<-pmat[i,kk,]
  					}

  					p.star[i]<-(1-pvec[i,1])  
  					nobs[i]<-rztbinom(1,n.eff[seen[i]], p.star[i]) 
  					obs[i,]<-as.vector(rmultinom(1,nobs[i], pvec[i,2:(k+1)^2]))
			}

		###now also format data for regular (One-Step) model, i.e, individual detected or not in occasion 1 and 2

		obs.onestep<-matrix(NA, nrow=0, ncol=K)
			for (i in 1:g.obs){

				for (j in 1:dim(poss.cap)[1]){
  					if (obs[i,j]==0) next
  					if (poss.cap[j,1]>0 & poss.cap[j,2]>0) 
    					   obs.onestep<-rbind(obs.onestep, matrix(c(1,1),obs[i,j],2,byrow=T ))
  					if (poss.cap[j,1]>0 & poss.cap[j,2]==0) 
    					   obs.onestep<-rbind(obs.onestep, matrix(c(1,0),obs[i,j],2,byrow=T ))
  					if (poss.cap[j,1]==0 & poss.cap[j,2]>0) 
   					   obs.onestep<-rbind(obs.onestep, matrix(c(0,1),obs[i,j],2,byrow=T ))
				}
			}


	####save data and generating parameters, as an R object
	dl<-list(OBS=OBS, obs=obs, obs.onestep=obs.onestep, N=N, M=M, n=n, p=p, P=P, K=K, k=k, n.eff=n.eff)
	dput(dl, paste(path, '/TwoStepData_pg', P*10, '_pi', p*10, "_", iter, '.R', sep=''))

	} #end loop for iterations

} ##end loop over values of P





#######################################################################################################################
#######################################################################################################################
####### PART B - FITTING MODELS #######################################################################################

### example script for fitting the two-step model to the simulation scenario with individual detection probability 
### pi = 0.7 and group detection probability pg = 0.3

library(rjags)
library(jagsUI)
library(mcmc)

### some JAGS related things that are constant across iterations
## for Two-step
model.file='Supplement S3 TwoStepCR.txt'
params<-c('p.g','psi','p.ind','lam','Ngroups','Ntotal')

## for one-step
model2<-'Supplement S2 OneStepCR.txt'
params2<-c('p','psi.i','N')

n.iter=1000  

##function to get possible combinations for capture histories
## as in script above
get.nposs<-function(x){
  out=NULL
  for (j in 1:(x+1)){
    out[j]<-dim(combn(x,(j-1)))[2]
  }
  return(out)
}


###set scenario parameters

##varying group detection probability
P.long<-c(0.3, 0.5, 0.7, 0.9) 

##individual detection probability
p<-0.7 

for (xy in 1:length(P.long)){
  
	P<-P.long[xy]

	path<-paste(getwd(), "/TwostepSim_pg", P*10, "_pi", p*10, sep="")

	din<-paste(path, '/TwoStepData_pg', P*10, '_pi', p*10, "_", 1, '.R', sep='')

	##read in one example data set to set up some parameters that are constant across iterations/scenarios
	dat.ex<-dget(din)

	##make sure you read in right data
	if (P!=dat.ex$P | p!=dat.ex$p) print("WRONG SCENARIO OR DATA")

	N=dat.ex$N
	M=dat.ex$M ##size of augmented group detection data set
	K=dat.ex$K ##number of sweeps (detection level for groups)
	Kn=dat.ex$k ##number of nests (detection level for individuals)


		for(iter in 1:n.iter){
	
			print(iter)
  
			###read in data set
			dat<-dget(paste(path,'/TwoStepData_pg', P*10, '_pi', p*10, "_", iter, '.R', sep=''))

			## pull out group detection histories
			OBS<-dat$OBS  #groups

			## summarize how many groups were seen, and which were seen
			g.obs<-sum(apply(OBS, 1, sum)>0)
			seen<-which(apply(OBS, 1, sum)>0)

			## create augmented group detection data
			yg<-matrix(0, M, K)
			yg[1:g.obs,]<-OBS[seen, ] 

			## get possible combinations in which detection histories can arise (see S3)
			nposs<-get.nposs(Kn)

			## extracte frequencies of individual detection histories
			yind<-dat$obs

			## calculate total number of individuals observed per group
			n<-apply(yind,1,sum) 

			## set initial values for zg and group.N (see S3 for details)
			zg.in<-rep(0, M)
			zg.in[1:g.obs]<-1
			N.in<-c(n+1, rpois(M-g.obs, mean(dat$n)))

			## bundle data
			data1<-list(Kn=Kn, M=M, K=K, obs=yg, g.obs=g.obs, obsvec=yind, n=n, nposs=nposs, poss.hist=dim(yind)[2] )

			## compile initial values function
			inits<-function(){list( p.g=runif(1, 0.4, 0.7), psi=runif(1, 0.4, 0.7), p.ind=runif(1, 0.4, 0.7), 
                                                z.g=zg.in, lam=12, group.N=N.in   )}

			## run chains in parallel on 3 cores
			out<-jags(data1, inits, params, model.file,
     		                  n.chains=3, n.adapt=500, n.iter=5000, n.burnin=1000, n.thin=1,
     		                  factories=NULL, parallel=TRUE, n.cores=3, DIC=FALSE)

			## save the chains 
			dput(out$samples, paste(path, '/FullTwoStepMulti_Chains_', iter, '.R', sep=''))

			## save posterior summaries of monitored parameters
			sout<-out$summary
			write.csv(sout, paste(path, '/FullTwoStepMulti_Results_', iter, '.csv', sep=''))


			###############################################################################
			### now, fit one-step model

			## pull out detection histories 
  			obs1s<-dat$obs.onestep  
	
			## number of individuals observed
  			iseen<-dim(obs1s)[1] 

			## augment data set
			y<-matrix(0, 800, K)
			y[1:iseen,]<-obs1s
	
			## set initial values for z (see S2)
			zin<-rep(0, 800)
			zin[1:iseen]<-1

			## compile data
			data2<-list(obs=y, M=800, K=K)

			## write initial values function
			inits2<-function(){list(p=runif(1, 0.55, 0.85), psi.i=runif(1, 0.4, 0.7), z=zin)}  

			## run model in parallel on 3 cores
			out2<-jags(data2, inits2, params2, model2,  n.chains=3, n.adapt=500,n.iter=10000, n.burnin=1000,
				   parallel=TRUE, n.cores=3, DIC=FALSE)

			## save the chains 
			dput(out2$samples, paste(path, '/OneStepMulti_Chains_', iter, '.R', sep=''))

			## save posterior summaries
			sout2 <- out2$summary
			write.csv(sout2, paste(path, '/OneStep_Results_', iter, '.csv', sep=''))

		}  ## end iteration loop

} # end loop over group detection probability






#######################################################################################################################
#######################################################################################################################
####### PART C - SUMMARIZING MODEL OUTPUT #############################################################################

###### this script reads in the summary results from the two step CR model and summarizes them across iterations

###set scenario parameters - only one example given here
P<-0.5 ## group detection
p<-0.7 ## individual detection

path<-paste(getwd(), "/TwostepSim_pg", P*10, "_pi", p*10, sep="")

din<-paste(path, '/TwoStepData_pg', P*10, '_pi', p*10, "_", 1, '.R', sep='')
dat.ex<-dget(din)

##make sure you read in right data
if (P!=dat.ex$P | p!=dat.ex$p) print("WRONG SCENARIO OR DATA")

N=dat.ex$N
M=dat.ex$M
K=dat.ex$K
Kn=dat.ex$k
n=dat.ex$n

##set number of iterations
n.iter=1000 

## set up tables to hold results

###table for number of groups
Ngtab<-matrix(NA, nrow=n.iter, ncol=5)
colnames(Ngtab)<-c('Mean','SE','Bias','CIcoverage', 'CV')

###table for total pop size
Ntab<-matrix(NA, nrow=n.iter, ncol=6)
colnames(Ntab)<-c('Mean','SE','Bias','CIcoverage', 'CV', 'True_N')

###table for avg group size
ntab<-matrix(NA, nrow=n.iter, ncol=5)
colnames(ntab)<-c('Mean','SE','Bias','CIcoverage', 'CV')

###table for group p
Pgtab<-matrix(NA, nrow=n.iter, ncol=5)
colnames(Pgtab)<-c('Mean','SE','Bias','CIcoverage', 'CV')

###table for individual p
Ptab<-matrix(NA, nrow=n.iter, ncol=5)
colnames(Ptab)<-c('Mean','SE','Bias','CIcoverage', 'CV')


for(iter in 1:n.iter){

	## read in data set
	dat<-dget(paste(path,'/TwoStepData_pg', P*10, '_pi', p*10, "_", iter, '.R', sep=''))

	## pull out true group sizes to calculate true total pop size
	ntotal<-sum(dat$n.eff)

	## read in summary results from two-step model
	res<-read.csv(paste(path, '/FullTwoStepMulti_Results_', iter, '.csv', sep=''), row.names = "X")

	## pull out estimates of Ngroups and ntotal with SEs, compare to true numbers
	## do the same for detection probs
	## names of parameters have to correspond with the names used in the res table

	##get mean and SE
	Ntab[iter, 1:2]<-unlist(res['Ntotal', 1:2])
	ntab[iter, 1:2]<-unlist(res['lam', 1:2])
	Ngtab[iter, 1:2]<-unlist(res['Ngroups', 1:2])
	Pgtab[iter, 1:2]<-unlist(res['p.g', 1:2])
	Ptab[iter, 1:2]<-unlist(res['p.ind', 1:2])

	## get relative bias
	Ntab[iter, 3]<-(Ntab[iter, 1] - ntotal)/ntotal
	ntab[iter, 3]<-(ntab[iter, 1] - n)/n
	Ngtab[iter, 3]<-(Ngtab[iter, 1] - N)/N
	Pgtab[iter, 3]<-(Pgtab[iter, 1] - P)/P
	Ptab[iter, 3]<-(Ptab[iter, 1] - p)/p

	## get CI coverage 
	Ntab[iter, 4]<- ifelse( res['Ntotal', 3]<= ntotal & res['Ntotal', 7]>=ntotal,1,0 ) #JRH's version
	ntab[iter, 4]<-ifelse( res['lam', 3]<= n & res['lam', 7]>=n,1,0 ) #JRH's version
	Ngtab[iter, 4]<-ifelse( res['Ngroups', 3]<= N & res['Ngroups', 7]>=N,1,0 ) #JRH's version
	Pgtab[iter, 4]<-ifelse( res['p.g', 3]<= P & res['p.g', 7]>=P,1,0 ) #JRH's version
	Ptab[iter, 4]<-ifelse( res['p.ind', 3]<= p & res['p.ind', 7]>=p,1,0 ) #JRH's version

	##get coefficient of variation
	Ntab[iter, 5]<-Ntab[iter, 2]/Ntab[iter, 1]
	ntab[iter, 5]<-ntab[iter, 2]/ntab[iter, 1]
	Ngtab[iter, 5]<-Ngtab[iter, 2]/Ngtab[iter, 1]
	Pgtab[iter, 5]<-Pgtab[iter, 2]/Pgtab[iter, 1]
	Ptab[iter, 5]<-Ptab[iter, 2]/Ptab[iter, 1]

	## add true N to Ntab
	Ntab[iter, 6]<-ntotal

}  ###end iteration loop

##automatically write out with data generating pg and pi
nam<-paste(path, "/Ntab_TwoStepCMRMulti_pg", P*10, "_pi", p*10, ".csv", sep="")
write.csv(Ntab, nam)



#### now produce summary across iterations

## set up table for summary results
summary.mat<-matrix(NA, 5, 8)
rownames(summary.mat)<-c('Ntotal','Avg.N','Ngroups','p.g','p.ind')
colnames(summary.mat)<-c('Avg est.', 'RMSE', 'Avg Bias', 'SD Bias', 'Min Avg Bias', 
			'Max Avg Bias', 'CI coverage', 'Avg CV')

###get average estimate across all iterations
summary.mat['Ntotal',1]<-mean(Ntab[,1])
summary.mat['Avg.N',1]<-mean(ntab[,1])
summary.mat['Ngroups',1]<-mean(Ngtab[,1])
summary.mat['p.g',1]<-mean(Pgtab[,1])
summary.mat['p.ind',1]<-mean(Ptab[,1])

###get root mean square error 
summary.mat['Ntotal',2]<-sqrt(sum((Ntab[,1]-Ntab[,6])^2)/n.iter) 
summary.mat['Avg.N',2]<-sqrt(sum((ntab[,1]-n)^2)/n.iter) 
summary.mat['Ngroups',2]<-sqrt(sum((Ngtab[,1]-N)^2)/n.iter) 
summary.mat['p.g',2]<-sqrt(sum((Pgtab[,1]-P)^2)/n.iter) 
summary.mat['p.ind',2]<-sqrt(sum((Ptab[,1]-p)^2)/n.iter)

###get average relative bias across all iterations
summary.mat['Ntotal',3]<-mean(Ntab[,3])
summary.mat['Avg.N',3]<-mean(ntab[,3])
summary.mat['Ngroups',3]<-mean(Ngtab[,3])
summary.mat['p.g',3]<-mean(Pgtab[,3])
summary.mat['p.ind',3]<-mean(Ptab[,3])

###get SD of relative bias across all iterations
summary.mat['Ntotal',4]<-sd(Ntab[,3])

###get minimum relative bias across all iterations
summary.mat['Ntotal',5]<-min(Ntab[,3])

###get maximum relative bias across all iterations
summary.mat['Ntotal',6]<-max(Ntab[,3])

###get confidence interval coverage
summary.mat['Ntotal',7]<-sum(Ntab[,4])/n.iter
summary.mat['Avg.N',7]<-sum(ntab[,4])/n.iter
summary.mat['Ngroups',7]<-sum(Ngtab[,4])/n.iter
summary.mat['p.g',7]<-sum(Pgtab[,4])/n.iter
summary.mat['p.ind',7]<-sum(Ptab[,4])/n.iter

###get average CV
summary.mat['Ntotal',8]<-mean(Ntab[,5])
summary.mat['Avg.N',8]<-mean(ntab[,5])
summary.mat['Ngroups',8]<-mean(Ngtab[,5])
summary.mat['p.g',8]<-mean(Pgtab[,5])
summary.mat['p.ind',8]<-mean(Ptab[,5])

## write resulting table as csv file
nam2<-paste("SummaryResults_TwoStepMultiCMR_pg", P*10, "_pi", p*10, ".csv", sep="")
write.csv(summary.mat, nam2)


###################################################################################################
######## now the same for one-step model results, for the same scenario of p (individual detection
######## and P (group detection)

#### IMPORTANT NOTE:
#### instead of comparing onde-step modelestimates of p directly to the individual level data generating pi
#### we need to compare it to the effective individual p (unconditional on group detection)
#### let's call that p.uncond, where "1-(1-p)^K" = detected at all across all K nests and "P" is group detection

p.uncond<-(1-(1-p)^K) * P

###make tables to hold your results

###table for total pop size
Ntab_1s<-matrix(NA, nrow=n.iter, ncol=6)
colnames(Ntab_1s)<-c('Mean','SE','Bias','CIcoverage', 'CV', 'True_N')

###table for p
Ptab_1s<-matrix(NA, nrow=n.iter, ncol=5)
colnames(Ptab_1s)<-c('Mean','SE','Bias','CIcoverage', 'CV')


for(iter in 1:n.iter){

	## read in data set
	dat<-dget(paste(path, '/TwoStepData_pg', P*10, '_pi', p*10, "_", iter, '.R', sep=''))

	## extract true total pop size
	ntotal<-sum(dat$n.eff)

	## read in summary results from ONE-STEP model
	res_1s<-read.csv(paste(path, '/OneStep_Results_', iter, '.csv', sep=''), 
				row.names="X")
	res_1s<-as.matrix(res_1s)


	## pull out estimates of ntotal with SEs, compare to true numbers
	## do the same for detection probs
	## names of parameters have to correspond with the names used in the res_1s table

	##get mean and SE
	Ntab_1s[iter, 1:2]<-res_1s['N', 1:2]
	Ptab_1s[iter, 1:2]<-res_1s['p', 1:2]

	## get relative bias
	Ntab_1s[iter, 3]<-(Ntab_1s[iter, 1] - ntotal)/ntotal
	Ptab_1s[iter, 3]<-(Ptab_1s[iter, 1] - p.uncond)/p.uncond
       
	## get CI coverage
	Ntab_1s[iter, 4]<- ifelse( res_1s['N', 3]<= ntotal & res_1s['N', 7]>=ntotal,1,0 ) #JRH version
	Ptab_1s[iter, 4]<-ifelse( res_1s['p', 3]<= p.uncond & res_1s['p', 7]>=p.uncond,1,0 ) #JRH version

	## get coefficient of variation
	Ntab_1s[iter, 5]<-Ntab_1s[iter, 2]/Ntab_1s[iter, 1]
	Ptab_1s[iter, 5]<-Ptab_1s[iter, 2]/Ptab_1s[iter, 1]

	## add true N to Ntab
	Ntab_1s[iter, 6]<-ntotal

}  ###end iteration loop

##write table as csv
nam<-paste(path, "/Ntab_OneStepCMRMulti_pg", P*10, "_pi", p*10, ".csv", sep="")
write.csv(Ntab_1s, nam)


### now produce summary across iterations

summary_1s.mat<-matrix(NA, 2, 8)
rownames(summary_1s.mat)<-c('N','p')
colnames(summary_1s.mat)<-c('Avg est.', 'RMSE', 'Avg Bias', 'SD Bias', 'Min Avg Bias', 'Max Avg Bias', 
				'CI coverage', 'Avg CV')

###get average estimate across all iterations
summary_1s.mat['N',1]<-mean(Ntab_1s[,1])
summary_1s.mat['p',1]<-mean(Ptab_1s[,1])

###get root mean square error 
summary_1s.mat['N',2]<-sqrt(sum((Ntab_1s[,1]-Ntab_1s[,6])^2)/n.iter) 
summary_1s.mat['p',2]<-sqrt(sum((Ptab_1s[,1]-p.uncond)^2)/n.iter) 

###get average relative bias across all iterations
summary_1s.mat['N',3]<-mean(Ntab_1s[,3])
summary_1s.mat['p',3]<-mean(Ptab_1s[,3])

###get SD of relative bias across all iterations
summary_1s.mat['N',4]<-sd(Ntab_1s[,3])

###get minimum relative bias across all iterations
summary_1s.mat['N',5]<-min(Ntab_1s[,3])

###get maximum relative bias across all iterations
summary_1s.mat['N',6]<-max(Ntab_1s[,3])

###get confidence interval coverage 
summary_1s.mat['N',7]<-sum(Ntab_1s[,4])/n.iter
summary_1s.mat['p',7]<-sum(Ptab_1s[,4])/n.iter

###get average CV
summary_1s.mat['N',8]<-mean(Ntab_1s[,5])
summary_1s.mat['p',8]<-mean(Ptab_1s[,5])

## write results table
nam2<-paste("SummaryResults_OneStepMultiCMR_pg", P*10, "_pi", p*10, ".csv", sep="")
write.csv(summary_1s.mat,nam2)












