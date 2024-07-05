# Code for reproducing the demographic analysis in Ozgul et al. 2023 (PNAS) - Destabilizing effect of climate change on the persistence of a short-lived primate

rm(list = ls(all = TRUE))

# setwd("/Users/arpat/dropbox/canavar/work/Microcebus/Analysis")
setwd("/home/rachelvoyt/Documents/UT-Grad/Development/repos/tamGenetics_primatesPeru/paper3_demographics/cmrModels/examples/Ozgul.etal_2023/")

library(RMark)
library(tidyverse)
library(gridExtra)
library(MuMIn)
library(ggthemes)
library(popbio)
library(stats)
library(truncnorm)

# Theme used for figures - Source: https://rdrr.io/github/HanjoStudy/quotidieR/man/theme_Publication.html

theme_Publication <- function(base_size = 14,
                              base_family = "sans") {
  library(grid)
  library(ggthemes)
  (
    theme_foundation(base_size = base_size, base_family = base_family)
    + theme(
      plot.title = element_text(
        face = "bold",
        size = rel(1.2),
        hjust = 0.5,
        margin = margin(0, 0, 20, 0)
      ),
      text = element_text(),
      panel.background = element_rect(colour = NA),
      plot.background = element_rect(colour = NA),
      panel.border = element_rect(colour = NA),
      axis.title = element_text(face = "bold", size = rel(1)),
      axis.title.y = element_text(angle = 90, vjust = 2),
      axis.title.x = element_text(vjust = -0.2),
      axis.text = element_text(),
      axis.line.x = element_line(colour = "black"),
      axis.line.y = element_line(colour = "black"),
      axis.ticks = element_line(),
      panel.grid.major = element_blank(),
      panel.grid.minor = element_blank(),
      legend.key = element_rect(colour = NA),
      legend.position = "bottom",
      legend.direction = "horizontal",
      legend.box = "vetical",
      legend.key.size = unit(0.5, "cm"),
      #legend.margin = unit(0, "cm"),
      legend.title = element_text(face = "italic"),
      plot.margin = unit(c(10, 5, 5, 5), "mm"),
      strip.background = element_rect(colour = "#f0f0f0", fill = "#f0f0f0"),
      strip.text = element_text(face = "bold")
    )
  )
  
}


# Data

load("CMR_data.Rda")
load("Covariate_data.Rda")


# Survival Analysis

microcebus.process = process.data(
  CMRdata,
  model = "Multistrata",
  begin.time = 1994,
  groups = "sex",
  strata.labels = c('J', 'A')
)
microcebus.ddl = make.design.data(microcebus.process, parameters = list(
  S = list(pim.type = "time"),
  p = list(pim.type = "time"),
  Psi = list(pim.type = "constant")
))
microcebus.ddl$Psi$fixed[microcebus.ddl$Psi$tostratum == "J"] = 0
microcebus.ddl$Psi$fixed[microcebus.ddl$Psi$tostratum == "A"] = 1
microcebus.ddl$p$fixed[microcebus.ddl$p$stratum == "J"] = 0

## Testing for time (categorical) and Time (continuous) effects

mod = mark(microcebus.process,
           microcebus.ddl,
           model.parameters = list(
             S = list(formula =  ~ (stratum + sex + time + Time) ^ 3),
             p = list(formula =  ~ (sex + time) ^ 2),
             Psi = list(formula =  ~ 1)
           ))

results1 = dredge(mod,
                  evaluate = F,
                  subset = !("S(time)" && "S(Time)"))
results1 = lapply(results1, eval)
save(results1, file = 'results1.Rda')
#load("results1.Rda")

modelset1 = subset(model.sel(results1), weight > 0.001, recalc.weights =
                     FALSE)

## Table S1

write.csv(data.frame(modelset1), "Table-S1.csv")

## Figure 1

selected = rownames(modelset1)[2]
null.model = results1[[selected]]
aa = get.real(null.model, "S", se = T)
aa$stratum = factor(aa$stratum, levels = c('J', 'A'))
bb = get.real(results1[['49228']], "S", se = T)
bb$stratum = factor(bb$stratum, levels = c('J', 'A'))
levels(aa$stratum) <- levels(bb$stratum) <- c('Juvenile', 'Adult')
levels(aa$sex) <- levels(bb$sex) <- c('Female', 'Male')

survival_time = ggplot(NULL, aes(as.integer(as.character(time)), estimate, col =
                                   stratum)) +
  scale_color_colorblind() +
  scale_fill_colorblind() +
  geom_point(data = aa) +
  geom_line(data = bb, lty = 1) +
  geom_ribbon(
    data = bb,
    aes(ymin = lcl, ymax = ucl, fill = stratum),
    alpha = 0.1,
    lwd = 0
  ) +
  facet_grid(sex ~ .) +
  theme_Publication() + theme(
    legend.position = c(0.5, 0.5),
    legend.direction = 'horizontal',
    legend.title = element_blank(),
    plot.margin = margin(10, 10, 5, 4)
  ) +
  scale_x_continuous(breaks = seq(1980, 2030, 5)) +
  xlim(c(1995, 2020.5)) +
  labs(x = "", y = "Annual survival")

recruitment_time = ggplot(covs, aes(year, recf)) + geom_point(col = 4) +
  geom_smooth(
    method = 'gam',
    formula = y ~ s(x, k = 3),
    col = 4,
    fill = 4,
    alpha = 0.1
  ) +
  theme_Publication() + theme(
    legend.position = "top",
    legend.direction = 'horizontal',
    legend.title = element_blank(),
    plot.margin = margin(10, 40, 5, 10)
  ) +
  scale_x_continuous(breaks = seq(1980, 2030, 5)) +
  xlim(c(1995, 2020)) +
  labs(y = "Female recruitment", x = "")

att.rain  <- attributes(scale(covs$rain))
label.rain <- seq(0, 2000, 200)
break.rain <-
  scale(label.rain,
        att.rain$`scaled:center`,
        att.rain$`scaled:scale`)[, 1]

att.tmaxc <- attributes(scale(covs$tmaxc))
label.tmaxc <- seq(28, 36, 0.5)
break.tmaxc <-
  scale(label.tmaxc,
        att.tmaxc$`scaled:center`,
        att.tmaxc$`scaled:scale`)[, 1]

climate.plot = ggplot(data = covs, aes(x = year)) +
  geom_vline(xintercept = 2007.5,
             lty = 2,
             col = "darkgrey") +
  annotate(
    geom = "text",
    x = c(2000, 2014),
    y = 2.7,
    label = c("First half", "Second half"),
    color = "darkgrey",
    size = 5
  ) +
  geom_point(aes(y = scale(rain)), col = "blue", size = 2) +
  geom_smooth(
    method = 'gam',
    formula = y ~ s(x, k = 3),
    aes(y = scale(rain)),
    col = "blue",
    fill = 'blue',
    alpha = 0.2,
    size = 0
  ) +
  geom_point(aes(y = scale(tmaxc)), col = "red", size = 2) +
  geom_smooth(
    method = 'gam',
    formula = y ~ s(x, k = 3),
    aes(y = scale(tmaxc)),
    col = "red",
    fill = 'red',
    alpha = 0.2,
    size = 0
  ) +
  scale_y_continuous(
    labels = label.tmaxc,
    breaks = break.tmaxc,
    sec.axis = sec_axis( ~ . * att.rain$`scaled:scale` +
                           att.rain$`scaled:center`, name = 'Rainfall (mm)')
  ) +
  scale_x_continuous(breaks = seq(1980, 2030, 5)) +
  xlim(c(1995, 2020)) +
  theme_Publication() +
  theme(
    axis.title.y = element_text(colour = "red"),
    axis.title.y.right = element_text(colour = "blue"),
    plot.margin = margin(10, 0, 5, 5)
  ) +
  labs(y = "Max. temperature (Cº)", x = "")

grid.arrange(
  climate.plot,
  survival_time,
  recruitment_time,
  ncol = 1,
  layout_matrix = rbind(1, 2, 2, 3)
)

# ggsave("Fig1.tiff",grid.arrange(climate.plot,survival_time,recruitment_time,ncol=1,layout_matrix=rbind(1,2,2,3)),device='tiff',width=2000,height=4000,unit="px",dpi=300)


## Testing for the difference between first and second half of the study

microcebus.ddl$S$half = factor(ifelse(as.integer(microcebus.ddl$S$time) >
                                        13, "second", "first"))

mod = mark(microcebus.process,
           microcebus.ddl,
           model.parameters = list(
             S = list(formula =  ~ (sex + stratum + half) ^ 3),
             p = list(formula =  ~ time),
             Psi = list(formula =  ~ 1)
           ))

results2 = dredge(mod,
                  evaluate = F,
                  fixed = c("S(stratum)", "S(sex)", "p(time)"))

results2 = lapply(results2, eval)
save(results2, file = 'results2.Rda')
#load("results2.Rda")

surv.all.model = results2[['9']]
save(surv.all.model, file = "surv.all.model.Rda")
surv.half.model = results2[['32']]
save(surv.half.model, file = "surv.half.model.Rda")

## Testing for the effects of environmental covariates

mod = mark(microcebus.process,
           microcebus.ddl,
           model.parameters = list(
             S = list(formula =  ~ (
               stratum + sex + tmaxc + rain + pop1 + rain1 + tmaxh1
             ) ^ 2),
             p = list(formula =  ~ time),
             Psi = list(formula =  ~ 1)
           ))
results3 = dredge(
  mod,
  evaluate = F,
  m.lim = c(5, 9),
  fixed = c("S(stratum)", "S(sex)", "p(time)")
)

results3 = lapply(results3, eval)
save(results3, file = 'results3.Rda')
#load("results3.Rda")

modelset3 = subset(model.sel(results3),  weight > 0.001, recalc.weights =
                     FALSE)
select.mod = rownames(modelset3)[1]
surv.model = results3[[select.mod]]
save(surv.model, file = "surv.model.Rda")


## Table S2

climlist = data.frame(modelset3)
for (i in 1:32)
  climlist[, i] = ifelse(is.na(climlist[, i]), NA, names(climlist)[i])
tableS2 = cbind(modelname = sapply(apply(climlist[, 1:32], 1, \(x) x[!is.na(x)]), paste, collapse =
                                     '+'), climlist[, c("df", "logLik", "AICc", "delta", "weight")])
write.csv(tableS2, file = "TableS2.csv")


covit <- function(x, m = 0) {
  mincov = min(covs[x], na.rm = T)
  maxcov = max(covs[x], na.rm = T)
  if (m == 3)
    rep(mean(covs[x][, 1], na.rm = T), 31)
  else
    if (m == 2)
      rep(quantile(covs[x][, 1], na.rm = T)[2], 31)
  else
    if (m == 4)
      rep(quantile(covs[x][, 1], na.rm = T)[4], 31)
  else
    if (m == 0)
      mincov + (0:30) * (maxcov - mincov) / 30
}


## Figure 2

indices = c(1, 27, 53, 79)

bb = get.real(results1[['33976']], "S", se = T) # time model
bb$stratum = factor(bb$stratum, levels = c('J', 'A'))
bb = merge(bb,
           covs,
           by.x = 'time',
           by.y = 'year',
           all.x = TRUE)
bb$rainfall1 = ifelse(bb$rain1 > 1000, "High Rainfall at t-1", "Low Rainfall at t-1")
bb$popt1 = ifelse(bb$pop1 > 80, "High density at t-1", "Low density at t-1")
levels(bb$sex) = c('Female', 'Male')
levels(bb$stratum) = c('Juvenile', 'Adult')

newdata = data.frame(
  pop11994 = rep(covit('pop1'), 2),
  rain11994 = c(covit('rain1', 2), covit('rain1', 4)),
  tmaxc1994 = rep(covit('tmaxc', 3), 2)
)
aa = covariate.predictions(results3[[select.mod]], data = newdata, indices = indices)$estimates
aaa = merge(aa, microcebus.ddl$S[, c('model.index', 'stratum', 'sex')], by = 'model.index', all.x = TRUE)
aaa$stratum = factor(aaa$stratum, levels = c('J', 'A'))
aaa$rainfall1 = ifelse(aaa$rain11994 > 1000, "High Rainfall at t-1", "Low Rainfall at t-1")
levels(aaa$sex) = c('Female', 'Male')
levels(aaa$stratum) = c('Juvenile', 'Adult')

survival_rainpop1 = ggplot(aaa, aes(pop11994, estimate, col = stratum)) + geom_line() +
  scale_color_colorblind() +
  scale_fill_colorblind() +
  geom_ribbon(aes(ymin = lcl, ymax = ucl, fill = stratum),
              alpha = 0.1,
              lwd = 0) +
  geom_point(data = bb, aes(pop1, estimate, col = stratum)) +
  facet_grid(sex ~ rainfall1) +
  theme_Publication() + theme(legend.title = element_blank()) +
  labs(x = 'Density at t-1', y = "Annual Survival")

newdata = data.frame(
  pop11994 = c(covit('pop1', 2), covit('pop1', 4)),
  rain11994 = rep(covit('rain1'), 2),
  tmaxc1994 = rep(covit('tmaxc', 3), 2)
)
aa = covariate.predictions(results3[[select.mod]], data = newdata, indices = indices)$estimates
aaa = merge(aa, microcebus.ddl$S[, c('model.index', 'stratum', 'sex')], by = 'model.index', all.x = TRUE)
aaa$stratum = factor(aaa$stratum, levels = c('J', 'A'))
aaa$popt1 = ifelse(aaa$pop11994 > 80, "High density at t-1", "Low density at t-1")
levels(aaa$sex) = c('Female', 'Male')
levels(aaa$stratum) = c('Juvenile', 'Adult')

survival_poprain1 = ggplot(aaa, aes(rain11994, estimate, col = stratum)) + geom_line() +
  scale_color_colorblind() +
  scale_fill_colorblind() +
  geom_ribbon(aes(ymin = lcl, ymax = ucl, fill = stratum),
              alpha = 0.1,
              lwd = 0) +
  geom_point(data = bb, aes(rain1, estimate, col = stratum)) +
  facet_grid(sex ~ popt1) +
  theme_Publication() + theme(legend.title = element_blank(),
                              legend.position = c(1000, 0)) +
  labs(x = 'Rainfall at t-1 (mm)', y = "")

newdata = data.frame(
  pop11994 = covit('pop1', 3),
  rain11994 = covit('rain1', 3),
  tmaxc1994 = covit('tmaxc')
)
aa = covariate.predictions(results3[[select.mod]], data = newdata, indices = indices)$estimates
aaa = merge(aa, microcebus.ddl$S[, c('model.index', 'stratum', 'sex')], by = 'model.index', all.x = TRUE)
aaa$stratum = factor(aaa$stratum, levels = c('J', 'A'))
levels(aaa$sex) = c('Female', 'Male')
levels(aaa$stratum) = c('Juvenile', 'Adult')

survival_tmaxc = ggplot(aaa, aes(tmaxc1994, estimate, col = stratum)) + geom_line() +
  scale_color_colorblind() +
  scale_fill_colorblind() +
  geom_ribbon(aes(ymin = lcl, ymax = ucl, fill = stratum),
              alpha = 0.1,
              lwd = 0) +
  geom_point(data = bb, aes(tmaxc, estimate, col = stratum)) +
  facet_grid(sex ~ .) +
  theme_Publication() + theme(
    legend.title = element_blank(),
    plot.margin = margin(10, 0, 15, 10),
    legend.position = "top"
  ) +
  labs(x = "Max. temperature (Cº)", y = "Annual survival")

grid.arrange(
  survival_tmaxc,
  survival_poprain1,
  ncol = 2,
  widths = c(1.5 / 4, 2.5 / 4)
)

#ggsave("Fig2.tiff",grid.arrange(survival_tmaxc,survival_poprain1,ncol=2,widths=c(1.5/4, 2.5/4)) ,device='tiff',width=3600,height=2100,unit="px",dpi=300)


# Reproduction Analysis

model0 = glm(recf ~ (tmaxc+popadf+pop+pop1+rain+rain1)^2, family=Gamma(link="log"), data=covs, na.action = "na.fail")
results4 = dredge(model0, trace=2, m.lim=c(0,6),subset = !(pop & pop1) & !(rain & rain1) & !(pop & popadf)  & !(pop1 & popadf))


## Table S3

modelset=subset(results4, weight > 0.01, recalc.weights=FALSE)

for (i in 2:22) modelset[,i]=ifelse(is.na(modelset[,i]),NA,names(modelset)[i])

modelset$delta = round(modelset$delta,2)
modelset$weight = round(modelset$weight,3)
modelset$logLik = round(modelset$logLik,1)

tableS3=cbind(modelname=sapply(apply(modelset[,2:22], 1, \(x) x[!is.na(x)]), paste, collapse='+'),modelset[,c(26,27,23,24)])

write.csv(tableS3,file="TableS3.csv")

covs$half = ifelse(covs$year>2006,'second','first')

rec.model = get.models(results4, subset = 1)[[1]]
ndat=expand.grid(tmaxc=28:33,popadf=40:90)
ndat$rec=predict(rec.model,ndat,type="response")
ggplot(ndat,aes(tmaxc,popadf,z=rec))+geom_contour_filled()

save(rec.model,file="rec.model.Rda")

covs$half=as.factor(ifelse(covs$year>2007,"second","first"))
rec.half.model = glm(recf ~ half, family=Gamma(link="log"), data=covs, na.action = "na.fail")
save(rec.half.model,file="rec.half.model.Rda")
rec.all.model = glm(recf ~ 1, family=Gamma(link="log"), data=covs, na.action = "na.fail")
save(rec.all.model,file="rec.all.model.Rda")


## Figure 3

newdata = data.frame(tmaxc = covit('tmaxc', 3), popadf = covit('popadf'))
aa = predict(rec.model, newdata, type = "response", se.fit = T)
newdata$recf = aa$fit
newdata$recf.se = aa$se.fit
rec_popadf = ggplot(newdata, aes(popadf, recf)) + geom_line(col = 4) +
  geom_ribbon(
    aes(ymin = recf - recf.se, ymax = recf + recf.se, ),
    lwd = 0,
    fill = 4,
    alpha = 0.1
  ) +
  geom_point(data = covs, aes(popadf, recf, col = year), size = 3) +
  theme_Publication() + theme(
    legend.position = c(0.9, 0.9),
    legend.direction = 'vertical',
    legend.title = element_blank()
  ) +
  labs(x = "Density of adult females", y = "Female recruitment")

newdata = data.frame(tmaxc = covit('tmaxc'), popadf = covit('popadf', 3))
aa = predict(rec.model, newdata, type = "response", se.fit = T)
newdata$recf = aa$fit
newdata$recf.se = aa$se.fit
rec_tmaxc = ggplot(newdata, aes(tmaxc, recf)) + geom_line(col = 4) +
  geom_ribbon(
    aes(ymin = recf - recf.se, ymax = recf + recf.se, ),
    lwd = 0,
    fill = 4,
    alpha = 0.1
  ) +
  geom_point(data = covs, aes(tmaxc, recf, col = year), size = 3) +
  theme_Publication() + theme(
    legend.position = "none",
    legend.direction = 'vertical',
    legend.title = element_blank()
  ) +
  labs(x = "Max. temperature (Cº)", y = "")


grid.arrange(rec_popadf, rec_tmaxc, ncol = 2)
# ggsave("Fig3.tiff", grid.arrange(rec_popadf, rec_tmaxc, ncol = 2), device = 'tiff', width = 1200, height = 600, unit = "px", dpi = 100)


# Population Model

Ff = 0.5 #pop_fem_ratio

surv.half = function(hal="all",rand=T){      # survival function for the whole period and first & second halves
  surv1 = surv.all.model$results$real
  surv2 = surv.half.model$results$real
  surv=rbind(surv1,surv2)
  surv = surv[grep("S s",rownames(surv)),]
  surv$half=c(rep('all',4),rep(c('first','second'),4))
  surv$sex=c(rep(c('female','male'),c(2,2)),rep(c('female','male'),c(4,4)))
  surv$stage=c(rep(c('juv','ad'),2),rep(c('juv','ad'),c(2,2)),rep(c('juv','ad'),c(2,2)))
  surv = subset(surv,half==hal)
  if (rand==T) rtruncnorm(nrow(surv),a=0,b=1,mean=surv$estimate,sd=surv$se+0.0001) else surv$estimate
}


rec.half = function(hal='all',rand=T){      # recruitment function for the whole period and first & second halves
  repro=rbind(as.data.frame(predict(rec.all.model,type="response",se.fit=T)),as.data.frame(predict(rec.half.model,type="response",se.fit=T)))
  repro=subset(repro,!duplicated(fit))
  repro$half=c('all','first','second')
  repro=subset(repro,half==hal)
  if (rand==T) rtruncnorm(length(repro$fit),a=0,b=3,mean=repro$fit,sd=repro$se.fit+0.0001) else repro$fit}


matrix.half <- function(hal="all",rand=T,all=F){      # function to build matrix model for the whole period and first & second halves
  Sfs = surv.half(hal,rand=rand)
  Rfs = rec.half(hal,rand=rand)
  micro.vr = list(S.jf = Sfs[1], S.af = Sfs[2], S.jm = Sfs[3], S.am = Sfs[4], F.f = Ff, R.f = Rfs[1])
  micro.el = expression(
    0, 0, S.jf*2*R.f*(1-F.f), S.af*2*R.f*(1-F.f),
    S.jm, S.am, 0, 0,
    0, 0, S.jf*2*R.f*F.f, S.af*2*R.f*F.f,
    0, 0, S.jf, S.af)
  B=round(matrix(sapply(micro.el, eval, micro.vr, NULL), nrow=sqrt(length(micro.el)), byrow=TRUE),4)
  if(all==T) list(B=B,Sfs=Sfs,Rfs=Rfs) else B
}

matrices = list(All=matrix.half("all",rand=F),
                FirstHalf=matrix.half("first",rand=F),
                SecondHalf=matrix.half("second",rand=F))

#save(matrices,file="matrices.Rda")

rates = data.frame(period=rep(c("all","first","second"),c(5,5,5)), rate=rep(c("Sjf","Saf","Sjm","Sam","Rec"),3),value=c(surv.half("all",rand=F),rec.half("all",rand=F),surv.half("first",rand=F),rec.half("first",rand=F),surv.half("second",rand=F),rec.half("second",rand=F)))
#save(rates,file="rates.Rda")


## Calculate lambdas and CIs for the whole period and first & second halves
L_all=NULL
L_1half=NULL
L_2half=NULL
for(i in 1:1000){
  L_all[i]=eigen.analysis(matrix.half("all"))$lambda1
  L_1half[i]=eigen.analysis(matrix.half("first"))$lambda1
  L_2half[i]=eigen.analysis(matrix.half("second"))$lambda1
  print(i)}

Lambdas = data.frame(Period=c('All','1half','2half'))

Lambdas$mean_L[1]=eigen.analysis(matrices[[1]])$lambda1
Lambdas$mean_L[2]=eigen.analysis(matrices[[2]])$lambda1
Lambdas$mean_L[3]=eigen.analysis(matrices[[3]])$lambda1

Lambdas$LCI[1]=quantile(L_all, 0.025)
Lambdas$LCI[2]=quantile(L_1half, 0.025)
Lambdas$LCI[3]=quantile(L_2half, 0.025)

Lambdas$UCI[1]=quantile(L_all,   0.975)
Lambdas$UCI[2]=quantile(L_1half, 0.975)
Lambdas$UCI[3]=quantile(L_2half, 0.975)

indices = data.frame(model.index=c(1,27,53,79),
                     stratum=factor(c("J","A","J","A"),levels=c("J","A")),
                     sex=factor(c("F","F","M","M"),levels=c("F","M")))

p0=mean(covs$pop1,na.rm=T)
r0=mean(covs$rain1,na.rm=T)
c0=mean(covs$tmaxc,na.rm=T)
a0=mean(covs$pop,na.rm=T)


newdata0 = data.frame(pop1 = mean(covs$pop1,na.rm=T), # mean values of covariates
                      rain1 = mean(covs$rain1,na.rm=T),
                      tmaxc = mean(covs$tmaxc,na.rm=T),
                      popadf = mean(covs$popadf,na.rm=T))

Sf<-function(newdata=newdata0,rand=T){         # survival as a function of covariates
  ndata=newdata[,c("pop1","rain1","tmaxc")]
  names(ndata)[names(ndata)%in%c("pop1","rain1","tmaxc")] = c("pop11994","rain11994","tmaxc1994")
  surv = covariate.predictions(surv.model, data = ndata, indices = indices$model.index)$estimates
  surv = merge(surv, indices, all.x = TRUE)
  if (rand==T) rtruncnorm(nrow(surv),a=0,b=1,mean=surv$estimate,sd=surv$se+0.0001) else surv$estimate #a=surv.range[1],b=surv.range[2]
}

Rf<-function(newdata=newdata0,rand=T){         # recruitment as a function of covariates
  ndata=newdata[,c("popadf","tmaxc"),drop=F]
  repro=predict(rec.model,ndata,type="response",se.fit=T)
  if (rand==T) rtruncnorm(length(repro$fit),a=0,b=3,mean=repro$fit,sd=repro$se.fit+0.0001) else repro$fit
}

Sf()
Rf()


matrixit <- function(Covs,all=F){          # matrix model as a function of covariates
  Sfs = Sf(Covs)
  Rfs = Rf(Covs)
  micro.vr = list(S.jf = Sfs[1], S.af = Sfs[2], S.jm = Sfs[3], S.am = Sfs[4], F.f = Ff, R.f = Rfs[1])
  micro.el = expression(
    0, 0, S.jf*2*R.f*(1-F.f), S.af*2*R.f*(1-F.f),
    S.jm, S.am, 0, 0,
    0, 0, S.jf*2*R.f*F.f, S.af*2*R.f*F.f,
    0, 0, S.jf, S.af)
  B=round(matrix(sapply(micro.el, eval, micro.vr, NULL), nrow=sqrt(length(micro.el)), byrow=TRUE),4)
  if(all==T) list(B=B,Sfs=Sfs,Rfs=Rfs) else B
}


## Function for Population Projection

simulate <-
  function(siml, simn, rangeT=c(1994,2020)) {   #siml = sim time length, simn = sim number
    
    obsNN4 = as.matrix(covs[,c('popjuvm','popadm','popjuvf','popadf')])
    
    obsl = nrow(covs)
    
    obsdat = data.frame(
      year = covs$year,
      pop1 = covs$pop1,
      rain1 = covs$rain1,
      tmaxc = covs$tmaxc,
      pop = covs$pop,
      popadf = covs$popadf,
      VR = c(rep(NA, obsl)))
    
    
    simdat = NULL
    
    for (s in 1:simn) {
      sample_t = match(sample(rangeT[1]:rangeT[2], siml, replace = T), covs$year)
      
      simdat0 = rbind(obsdat,data.frame(
        year = 2021:(2020 + siml),
        pop1 = c(rep(NA, siml)),
        rain1 = covs$rain1[sample_t],
        tmaxc = covs$tmaxc[sample_t],
        pop = c(rep(NA, siml)),
        popadf = c(rep(NA, siml)),
        VR = c(rep(NA, siml))
      ))
      
      NN4 = rbind(obsNN4,matrix(NA, siml, 4))
      
      for (t in obsl+0:(siml-1)) {
        B = matrixit(simdat0[t, ],all=T)
        NN4[t+1,] = rpois(4,B$B %*% NN4[t, ]) #demog.stoc added
        simdat0$pop1[t+1] = simdat0$pop[t]
        simdat0$pop[t+1] = sum(NN4[t+1,])
        simdat0$popadf[t+1] = NN4[t+1,4]
        simdat0$VR[t+1] = paste(sprintf('%.2f',c(B$Sfs,B$Rfs)),collapse="_")
        
        print(paste(s, "-", siml-t+obsl))
      }
      
      simdat0$simn=s
      simdat = rbind(simdat, simdat0)
    }
    simdat  
  }


## Population Projections

nsim=1000
simdatAll = simulate(50,nsim)
simdat1half = simulate(50,nsim,c(1994,2006))
simdat2half = simulate(50,nsim,c(2009,2020))


## Figure 5

att.rain  <- attributes(scale(covs$rain))
label.rain <- seq(0,2000,200)
break.rain <- scale(label.rain, att.rain$`scaled:center`, att.rain$`scaled:scale`)[,1]

att.tmaxc <- attributes(scale(covs$tmaxc))
label.tmaxc <- seq(28,36,0.5)
break.tmaxc <- scale(label.tmaxc, att.tmaxc$`scaled:center`, att.tmaxc$`scaled:scale`)[,1]


climate.plot = ggplot(data = covs, aes(x=year)) +
  geom_vline(xintercept=2007.5,lty=2,col="darkgrey")+
  annotate(geom="text", x=c(2000,2014), y=2.7, label=c("First half","Second half"),color="darkgrey",size=5)+
  geom_point(aes(y=scale(rain)),col = "blue",size=2) +
  geom_smooth(method = 'gam', formula=y~s(x,k=3), aes(y=scale(rain)),col = "blue",fill='blue',alpha=0.2,size=0) +
  geom_point(aes(y=scale(tmaxc)),col = "red",size=2) +
  geom_smooth(method = 'gam', formula=y~s(x,k=3), aes(y=scale(tmaxc)),col = "red",fill='red',alpha=0.2,size=0) +
  scale_y_continuous(labels = label.tmaxc, breaks = break.tmaxc,
                     sec.axis = sec_axis(~.*att.rain$`scaled:scale`+att.rain$`scaled:center`,name='Rainfall (mm)')) +
  scale_x_continuous(breaks = seq(1980,2030,5)) +
  theme_Publication()+
  theme(axis.title.y = element_text(colour = "red"),axis.title.y.right = element_text(colour = "blue"))+
  labs(y = "Max. temperature (Cº)", x = "")  


extpopAll=subset(simdatAll,year>2020)  %>%
  group_by(year) %>%
  summarise(ext.prob=mean(pop==0))

coeff=1000

popAll = ggplot(simdatAll,aes(x=year))+
  annotate(geom="text", x=2055, y=300, label="Sampling all the years",color="black",size=5)+
  geom_vline(xintercept=2007.5,lty=2,col="darkgrey")+
  geom_line(aes(y=pop,group=simn),alpha=0.03)+
  geom_line(data=extpopAll,aes(year,ext.prob*coeff),col='red',size=2,alpha=0.6)+
  labs(y='Abundance',x='')+
  coord_cartesian(xlim=range(simdatAll$year),ylim=c(0,300))+
  theme_Publication()+
  theme(legend.title = element_blank(),legend.position = "none",axis.title.y.right = element_text(colour = "red"))+
  scale_y_continuous(sec.axis = sec_axis(~./coeff,name='Extinction risk'))+
  scale_x_continuous(breaks = seq(1980,2080,5))


extpop1half=subset(simdat1half,year>2020)  %>%
  group_by(year) %>%
  summarise(ext.prob=mean(pop==0))

pop1half = ggplot(simdat1half,aes(x=year))+
  annotate(geom="text", x=2055, y=300, label="Sampling the first half",color="black",size=5)+
  geom_vline(xintercept=2007.5,lty=2,col="darkgrey")+
  geom_line(aes(y=pop,group=simn),alpha=0.03)+
  geom_line(data=extpop1half,aes(year,ext.prob*coeff),col='red',size=2,alpha=0.6)+
  labs(y='',x='')+
  coord_cartesian(xlim=range(simdat1half$year),ylim=c(0,300))+
  theme_Publication()+
  theme(legend.title = element_blank(),legend.position = "none",axis.title.y.right = element_text(colour = "red"))+
  scale_y_continuous(sec.axis = sec_axis(~./coeff,name=''))+
  scale_x_continuous(breaks = seq(1980,2080,5))


extpop2half=subset(simdat2half,year>2020)  %>%
  group_by(year) %>%
  summarise(ext.prob=mean(pop==0))

pop2half = ggplot(simdat2half,aes(x=year))+
  annotate(geom="text", x=2055, y=300, label="Sampling the second half",color="black",size=5)+
  geom_vline(xintercept=2007.5,lty=2,col="darkgrey")+
  geom_line(aes(y=pop,group=simn),alpha=0.03)+
  geom_line(data=extpop2half,aes(year,ext.prob*coeff),col='red',size=2,alpha=0.6)+
  labs(y='',x='')+
  coord_cartesian(xlim=range(simdat2half$year),ylim=c(0,300))+
  theme_Publication()+
  theme(legend.title = element_blank(),legend.position = "none",axis.title.y.right = element_text(colour = "red"))+
  scale_y_continuous(sec.axis = sec_axis(~./coeff,name=''))+
  scale_x_continuous(breaks = seq(1980,2080,5))

grid.arrange(pop1half,popAll,pop2half,ncol=1)

##ggsave("Fig5c.tiff",grid.arrange(pop1half,popAll,pop2half,ncol=1),device='tiff',width=3000,height=3600,unit="px",dpi=300)


## Model Validation

validate <-
  function(simn, rangeT=c(1994,2020)) {
    siml = rangeT[2]-rangeT[1]+1
    
    obsNN4 = as.matrix(covs[,c('popjuvm','popadm','popjuvf','popadf')])
    
    obsl = nrow(covs)
    
    obsdat = data.frame(
      year = covs$year,
      pop1 = covs$pop1,
      rain1 = covs$rain1,
      tmaxc = covs$tmaxc,
      pop = covs$pop,
      popadf = covs$popadf,
      VR = c(rep(NA, obsl)))
    
    simdat = NULL
    
    for (s in 1:simn) {
      years=rangeT[1]:rangeT[2]
      sample_t = match(years, covs$year)
      
      simdat0 = obsdat
      
      NN4 = obsNN4
      
      for (t in 1:(siml-1)) {
        B = matrixit(simdat0[t, ],all=T)
        NN4[t+1,] = rpois(4,B$B %*% NN4[t, ]) #demog.stoc added
        simdat0$pop1[t+1] = simdat0$pop[t]
        simdat0$pop[t+1] = sum(NN4[t+1,])
        simdat0$popadf[t+1] = NN4[t+1,4]
        simdat0$VR[t+1] = paste(sprintf('%.2f',c(B$Sfs,B$Rfs)),collapse="_")
        
        print(paste(s, "-", siml-t))
      }
      
      simdat0$simn=s
      simdat = rbind(simdat, simdat0)
    }
    simdat  
  }

validatAll = validate(1000)

percs=NULL
for (t in 1994:2020){
  percs[t-1993]=ecdf(subset(validatAll,year==t)$pop)(covs$pop[match(t,covs$year)])}
cummean(percs)


## Figure S2

valipopAll = ggplot(validatAll,aes(x=year))+
  geom_vline(xintercept=2007.5,lty=2,size=1,col="darkgrey")+
  geom_line(aes(y=pop,group=simn,col="Simulations"),alpha=0.1)+
  geom_line(data=covs,aes(year,pop,col='All individuals'),size=1,alpha=0.6)+
  geom_line(data=covs,aes(year,poplocals,col='Local recruits'),size=1,alpha=0.6)+
  labs(y='Abundance',x='')+
  coord_cartesian(xlim=range(validatAll$year),ylim=c(0,200))+
  theme_Publication()+
  scale_x_continuous(breaks = seq(1980,2080,5))+
  scale_colour_manual(name="",values=c('All individuals'='red', 'Local recruits'='blue',"Simulations"="black"))+
  theme(legend.title = element_blank(),legend.position=c(0.26,0.9))


valipopAll
# ggsave("FigS2.jpeg",valipopAll,device='jpeg',width=900,height=600,unit="px",dpi=100)

