#!/usr/bin/env Rscript

rm(list = ls()) # Reset R`s brain
# setwd("~/R/timeseries") # Set workin girectory
df <- read.csv('data.csv') # read data from *.csv file

library(ggplot2) # Add package
p <- ggplot(df, aes(year,Area_ha)) # базовий ggplot-об'єкт

p+geom_smooth(colour = "blue", size = 1)+
  xlab("роки")+
  ylab("площа, тис. га")+
  theme_classic()

ggsave("time_seria_smooth.png", width=16, height=12, unit="cm", dpi=300)
