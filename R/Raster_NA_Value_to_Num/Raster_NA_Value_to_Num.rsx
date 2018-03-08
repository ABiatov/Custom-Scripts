# Rscript for QGIS Processing
# You need copy this file in `<USER>/.qgis2/processing/rscripts/` folder.

##img=raster
##My_Num=number 0
##output=output raster
# About dataType
# https://www.rdocumentation.org/packages/raster/versions/2.6-7/topics/dataType


library("raster")
# library("rgdal")
library("snow")

# Создадтим функцю по замене значений NA числом заданым в переменной mynum
fun_no_null <- function(x) {x[is.na(x)] <- My_Num; return(x) }

beginCluster()
Raster_no_NULL <- calc(img, fun_no_null)
endCluster()

output = Raster_no_NULL
