# Up sampling rasters with GDAL in few steps
# Sctipt read all tif-files in source directory and create new files in result directory

import pathlib
from osgeo import gdal
from datetime import datetime


def upsample_raster(input_raster, target_resolution):
    gdal_translate_upsample_options = gdal.TranslateOptions(
        format="MEM",
        xRes=target_resolution,
        yRes=target_resolution,
        resampleAlg='lanczos'  # can be 'average','near','bilinear','cubic','cubicspline','lanczos','mode','max','min','med','Q1','Q3'
        # creationOptions=['COMPRESS=DEFLATE', 'PREDICTOR=2', 'ZLEVEL=9', 'BIGTIFF=YES'],
    )
    upsampled_tif = gdal.Translate(
        destName="",
        srcDS=input_raster,
        # format="GTiff",
        options=gdal_translate_upsample_options,
    )
    rasters.append(upsampled_tif)

    return upsampled_tif


BASE_DIR = pathlib.Path("C:/raster_data")
source_raster_dir = BASE_DIR.joinpath("source_rasters")
result_raster_dir = BASE_DIR.joinpath("result_rasters")

steps = [600, 450, 300, 200, 125, 75, 50]
result_resolution = steps[-1]

curent_files = []

currentPattern = "*.tif"
for currentFile in source_raster_dir.glob(currentPattern):
    curent_files.append(currentFile.name)

start = datetime.now()


for raster_file in curent_files :

    source_raster_path = source_raster_dir.joinpath(raster_file)
    # print(source_raster_path)
    # print(source_raster_path.stem)

    result_raster_path = result_raster_dir.joinpath(f"{source_raster_path.stem}_{str(result_resolution)}.tif").as_posix()



    rasters = []

        # Upsample the raster for each step in the list of steps
    output_ds = source_raster_path.as_posix()
    for step in steps:
        output_ds = upsample_raster(output_ds, step)


    rasters = [source_raster_path] + [upsample_raster(rasters[i], steps[i]) for i in range(len(steps))]

    #
    # print(rasters)
    #
    gdal_translate_tif_export_options = gdal.TranslateOptions(
        format="GTiff",
        creationOptions=['COMPRESS=DEFLATE', 'PREDICTOR=2', 'ZLEVEL=9', 'BIGTIFF=YES'],
    )
    result_tif = gdal.Translate(
        destName=f"{result_raster_path}",
        srcDS=rasters[-1],
        # format="GTiff",
        options=gdal_translate_tif_export_options,
    )

    del result_tif

    print(f"{result_raster_path} done")

    #
    #
end = datetime.now()
# find difference start and end time and display
td = (end - start).total_seconds() * 10 ** 3
print(f"The time of execution of above program is : {td:.03f}ms")


