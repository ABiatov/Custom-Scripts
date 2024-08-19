# zona_stat_raster_classes

import rasterio
from rasterio.mask import mask
import pandas as pd
import geopandas as gpd
import numpy as np


path_to_your_tiff = "C:/Users/admin/Dropbox/MAPS/WD/Seliverstov_Oleg/Sviati_gory_burned/data/rasters/dNBR_classes_21_23.tif"

path_to_your_geopackage = "C:/Users/admin/Dropbox/MAPS/WD/Seliverstov_Oleg/Sviati_gory_burned/data/vectors/SgNP_3857.gpkg"

path_to_output_gpkg = "C:/Users/admin/Dropbox/MAPS/WD/Seliverstov_Oleg/Sviati_gory_burned/data/vectors/SgNP_3857_stat.gpkg"

raster = rasterio.open(path_to_your_tiff)
polygons = gpd.read_file(path_to_your_geopackage)




def get_stats(row, raster):
    geom = row.geometry
    out_image, out_transform = mask(raster, [geom], crop=True)
    unique, counts = np.unique(out_image, return_counts=True)
    return pd.Series(dict(zip(unique, counts)))


def count_pixels(row, raster):
    geom = row.geometry
    out_image, out_transform = mask(raster, [geom], crop=True)
    return out_image.size


df = polygons.apply(get_stats, axis=1, raster=raster)


polygons = pd.concat([polygons, df], axis=1)

polygons['total_pixels'] = polygons.apply(count_pixels, axis=1, raster=raster)

polygons.columns = polygons.columns.astype(str)

polygons.to_file(path_to_output_gpkg, driver='GPKG')


