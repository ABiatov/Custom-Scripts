library("raster")
library("snow")

# Set work directory
setwd("/home/<USER>/WorkDirectory/")

# Import image
img <- brick("my_raster.tif")

# To set numbers for owerwriting 
My_Num <- 7


# Create a function to replace the values of `NA` by the number specified in the variable `My_Num`
fun_no_null <- function(x) {x[is.na(x)] <- My_Num; return(x) }

# We replace the NULL values by the number specified in the variable `My_Num`.
# We will use the `beginCluster` function for calculations on several processor cores
beginCluster()
Raster_no_NULL <- calc(img, fun_no_null)
endCluster()

# Save the raster to a `GeoTiff` file
# To reade about dataType : https://www.rdocumentation.org/packages/raster/versions/2.6-7/topics/dataType
writeRaster(Raster_no_NULL, filename="DEM_no_NULL.tif", format = "GTiff", datatype='FLT4S', overwrite=TRUE)

