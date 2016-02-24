#!/usr/bin/env Rscript

library("raster")
# setwd("/home/narwhale/Maps/WD/Diplom_Alin-wild_boar/TIF/")
rrrrr <- raster("temp.tif", package="raster")
writeRaster(rrrrr, filename="rrrrr.asc", format = "ascii", datatype='FLT4S', overwrite=TRUE)
