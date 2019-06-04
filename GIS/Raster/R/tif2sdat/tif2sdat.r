#!/usr/bin/env Rscript

library("raster")
# library("rgdal")

rrrrr <- raster("temp.tif", package="raster")
writeRaster(rrrrr, filename="rrrrr.sdat", format = "SAGA", datatype='FLT4S', overwrite=TRUE)
