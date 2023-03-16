# Clip raster files by shp

import pathlib
from osgeo import gdal
from datetime import datetime
start = datetime.now()

BASE_DIR = pathlib.Path("C:/geodata")
source_raster_dir = BASE_DIR.joinpath("source_rasters")
result_raster_dir = BASE_DIR.joinpath("result_rasters")
aoi_path = BASE_DIR.joinpath("shp/aoi.shp")

curent_files = []

currentPattern = "*.tif"
for currentFile in source_raster_dir.glob(currentPattern):
    curent_files.append(currentFile.name)


for raster_file in curent_files :
    source_raster_path = source_raster_dir.joinpath(raster_file)
    result_raster_path = result_raster_dir.joinpath(f"{source_raster_path.stem}_clipped.tif").as_posix()
    print(f"result_raster_path: {result_raster_path}")

    gdal_warp_options = gdal.WarpOptions(
        format='GTiff',
        dstSRS='EPSG:3857', 
        cutlineDSName=aoi_path.as_posix(),
        cutlineLayer='aoi',
        cropToCutline=True,
        creationOptions=['COMPRESS=DEFLATE', 'PREDICTOR=2', 'ZLEVEL=9', 'BIGTIFF=YES'],
        )

    gdal.Warp(destNameOrDestDS=result_raster_path,
              srcDSOrSrcDSTab=source_raster_path.as_posix(),
              options=gdal_warp_options
              )


end = datetime.now()
# find difference start and end time and display
td = (end - start).total_seconds() * 10 ** 3
print(f"The time of execution of above program is : {td:.03f}ms")

