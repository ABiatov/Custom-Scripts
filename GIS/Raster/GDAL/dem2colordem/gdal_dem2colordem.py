from osgeo import gdal
import gdal_calc # need to import path to gdal_calc.py or add  gdal_calc.py to work folder
from uuid import uuid4

colors_palette = "colors_palette.txt"

grey_dem = 'dem.tif'
color_dem = 'color_dem.tif'
color_shade_dem = 'color_shade_dem.tif'

color_gtiff_mem = "/vsimem/" + uuid4().hex
hillshade_gtiff_mem = "/vsimem/" + uuid4().hex
gamma_hillshade_gtiff_mem = "/vsimem/" + uuid4().hex

gdal.DEMProcessing(
    destName=color_gtiff_mem, 
    srcDS=grey_dem, 
    processing="color-relief", 
    addAlpha=True, 
    colorFilename=colortable_file, 
    format='GTiff')


hillshade_options = gdal.DEMProcessingOptions(
    band=1,
    zFactor=1.0,
    scale=1.0,
    azimuth=315.0,
    altitude=45.0
)

gdal.DEMProcessing(
    destName=hillshade_gtiff_mem,
    srcDS=grey_dem,
    processing="hillshade",
    options=hillshade_options,
    format="GTiff"
)

gdal_calc.Calc(
    calc="uint8(((A / 255.)**(1/0.5)) * 255)",
    overwrite=True,
    A=hillshade_gtiff_mem,
    A_band=1,
    outfile=gamma_hillshade_gtiff_mem,
    NoDataValue=0,
    format="GTiff"
)

gdal_calc.Calc(
    calc="uint8( ( 2 * (A/255.)*(B/255.)*(A<128) + ( 1 - 2 * (1-(A/255.))*(1-(B/255.)) ) * (A>=128) ) * 255 )",
    overwrite=True,
    A=gamma_hillshade_gtiff_mem,
    A_band=1,
    B=color_dem,
    allBands="B",
    outfile=colorized_hillshade_file,
    NoDataValue=0,
    format="GTiff"
)

