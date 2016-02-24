#!/usr/bin/env Rscript

library("raster")
rrrrr <- raster("temp.tif", package="raster")
writeRaster(rrrrr, filename="rrrrr.asc", format = "ascii", datatype='FLT4S', overwrite=TRUE)
