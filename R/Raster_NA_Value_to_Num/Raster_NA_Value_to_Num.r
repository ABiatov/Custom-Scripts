library("raster")
library("rgdal")
library("snow")

# Set work directory
setwd("/home/<USER>/WorkDirectory/")

# Import image
img <- brick("my_raster.tif")

img <- brick("uch_3_bereg_cliped.tif")

# To set numbers for owerwriting 
My_Num <- 7


# Создадтим функцю по замене значений NA числом заданым в переменной mynum
fun_no_null <- function(x) {x[is.na(x)] <- My_Num; return(x) }

beginCluster()
Raster_no_NULL <- calc(img, fun_no_null)
endCluster()

# About dataType
# https://www.rdocumentation.org/packages/raster/versions/2.6-7/topics/dataType

# Экспортируем в GeoTIF полученный растр
writeRaster(Raster_no_NULL, filename="DEM_no_NULL.tif", format = "GTiff", datatype='FLT4S', overwrite=TRUE)

