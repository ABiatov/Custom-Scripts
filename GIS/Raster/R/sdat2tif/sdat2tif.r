#!/usr/bin/env Rscript

library("raster")
# library("rgdal")

temp_raster <- raster("temp.sdat", package="raster")
writeRaster(temp_raster, filename="temp.tif", format = "GTiff", datatype='FLT4S', overwrite=TRUE)
