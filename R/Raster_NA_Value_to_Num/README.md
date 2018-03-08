# NULL value conversation to Numeric in OneBand Raster

## Step-by-step instruction

### Start R and load the packages
Start **R** in terminal
```{sh}
R
```

We will need these packages: `snow`, `sp`, `raster`.
You need to install the necessary packages, if they are not installed.
```{r}
install.packages(c("snow", "sp", "raster"), dependencies = TRUE)
```
Load the required packages.
```{r}
library("sp")
library("raster")
library("snow")
```

### Load the data in R
Set the working directory with the data
```{r}
setwd("~/WorkFolder/")
```
Load the raster file
```{r}
img <- brick("my_raster.tif")
```

To set numbers for owerwriting, example `7`
```{r}
My_Num <- 7
```

Create a function to replace the values of `NA` by the number specified in the variable `My_Num`
```{r}
fun_no_null <- function(x) {x[is.na(x)] <- My_Num; return(x) }
```

We replace the NULL values by the number specified in the variable `My_Num`.
We will use the `beginCluster` function for calculations on several processor cores.
```{r}
beginCluster()
Raster_no_NULL <- calc(img, fun_no_null)
endCluster()
```

Save the raster to a `GeoTiff` file
To reade about dataType : https://www.rdocumentation.org/packages/raster/versions/2.6-7/topics/dataType
```{r}
writeRaster(Raster_no_NULL, filename="DEM_no_NULL.tif", format = "GTiff", datatype='FLT4S', overwrite=TRUE)
```
Rscript for R or R-studio: https://github.com/ABiatov/Custom-Scripts/blob/master/R/Raster_NA_Value_to_Num/Raster_NA_Value_to_Num.r
Rscript for QGIS Processing: https://github.com/ABiatov/Custom-Scripts/blob/master/R/Raster_NA_Value_to_Num/Raster_NA_Value_to_Num.rsx





