
# pip install fiona rasterio
# conda install -c conda-forge fiona
# conda install -c conda-forge rasterio
import fiona
import rasterio
from rasterio import features
from rasterio.transform import from_origin

input_dxf = "C:/Users/admin/Dropbox/Bussines_DB/ABSpatial/projects/metasymbiont/data/DXF_202306015/DXF/vazuza_loc_1.dxf"
output_geotiff = "C:/Users/admin/Dropbox/Bussines_DB/ABSpatial/projects/metasymbiont/data/DXF_202306015/DXF/vazuza_loc_1_output.tif"

with fiona.open(input_dxf, layer='entities') as src:
    geoms = [feature['geometry'] for feature in src]

min_x = min([geom.bounds[0] for geom in geoms])
min_y = min([geom.bounds[1] for geom in geoms])
max_x = max([geom.bounds[2] for geom in geoms])
max_y = max([geom.bounds[3] for geom in geoms])

pixel_size = 0.01  # Adjust as needed
width = int((max_x - min_x) / pixel_size)
height = int((max_y - min_y) / pixel_size)

transform = from_origin(min_x, max_y, pixel_size, pixel_size)
profile = {
    'driver': 'GTiff',
    'dtype': rasterio.uint8,  # Adjust data type as needed
    'width': width,
    'height': height,
    'count': 1,
    'crs': '+proj=latlong',
    'transform': transform
}

with rasterio.open(output_geotiff, 'w', **profile) as dst:
    dst.write_band(1, 0)  # Write an empty band to the raster

with rasterio.open(output_geotiff, 'r+', **profile) as dst:
    burn_value = 255  # Adjust as needed
    for geom in geoms:
        shapes = [(geom, burn_value)]
        burned = features.rasterize(
            shapes,
            out_shape=(height, width),
            fill=0,
            transform=dst.transform,
            dtype=rasterio.uint8
        )
        dst.write_band(1, burned)

