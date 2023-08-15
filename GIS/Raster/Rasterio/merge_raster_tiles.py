# import os
import subprocess
import numpy as np

import glob

try:
    import rasterio.merge
except ImportError:
    print('rasterio package not installed. Installing ...')
    subprocess.check_call(["python", '-m', 'pip', 'install', 'rasterio'])
    import rasterio.merge

tiles_folder_path = "C:/maps/ndvi_tiles"
tile_type = "ndvi"
region_name = "My_region"
result_path = "C:/maps"

# r_dtype = None
# r_dtype = rasterio.int16
r_dtype = rasterio.float32
# r_dtype = rasterio.float64

# r_nodata = None
r_nodata = np.nan

def merge_tiles(INPUT_FOLDER, RASTER_TYPE, REGION_NAME):
    fnames=glob.glob(tiles_folder_path+"*.tif")
    print(fnames)
    #dummy list comprehention for rasterio handles for tiles
    datasets=[[] for _ in range(len(fnames))]
    #filling in the list with handles for tiles
    for i,f in enumerate(fnames):
        datasets[i] = rasterio.open(f,'r')
    print('datasets opened')
    #use of method rasterio.merge.merge. datasets - list created above
    dest, output_transform=rasterio.merge.merge(datasets,
                                                nodata=r_nodata,
                                                dtype=r_dtype) # dtype=None
    #copy metadata (geodata) from file "1.tif"
    with rasterio.open(fnames[0]) as src:
            out_meta = src.meta.copy()
    #update metadata (geodata) with "height", "width" and "transform" obtained
    #from dest - the output of rasterio.merge.merge"
    out_meta.update({"driver": "GTiff",
                     "compress": 'lzw',
                     "dtype": r_dtype,
                     "height": dest.shape[1],
                     "width": dest.shape[2],
                     "transform": output_transform,
                     "num_threads":'all_cpus',
                     "BIGTIFF":'YES'})
    #write result to disk under handle dest1
    result_file_name = result_path+"merged_"+RASTER_TYPE+"_"+REGION_NAME+".tif"
    with rasterio.open(result_file_name, "w", **out_meta) as dest1:
            dest1.write(dest)
    return print(result_file_name)


merge_tiles(tiles_folder_path, tile_type, region_name)

