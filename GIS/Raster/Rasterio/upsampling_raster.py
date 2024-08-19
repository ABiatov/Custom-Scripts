import rasterio
from rasterio.enums import Resampling
import numpy as np
sources_dir = f"C:/Users/admin/Dropbox/MAPS/WD/Seliverstov_Oleg/Indexes_20231105/data/MODIS/" 

temp_dir = 'C:/Users/admin/Dropbox/MAPS/WD/Seliverstov_Oleg/Indexes_20231105/data/MODIS/'
band = 'MODIS_ndmi_2000_2005_summer_Voznesensk'
fname = f'{sources_dir}{band}.tif' 

for pixel_size in [250, 100, 50]:
        with rasterio.open(fname) as dataset:
                # resample data to target shape
                data= dataset.read(out_shape=(dataset.count,
                                int((dataset.bounds[3]-dataset.bounds[1])//pixel_size),
                                int((dataset.bounds[2]-dataset.bounds[0])//pixel_size)),
                                resampling=Resampling.cubic_spline)
            
                shape=data.shape

                #mask=data==-3.4028234663852885981170418348451692544e+38
                #maxx=np.max(data[~mask])
                #minn=np.min(data[~mask])

                #data[~mask]=(data[~mask]-minn)/(maxx-minn)*65534+1
                #data[mask]=0

                fname = f'{temp_dir}{band}_{pixel_size}.tif'
            
                transform = dataset.transform * dataset.transform.scale((dataset.width / shape[-1]),(dataset.height / shape[-2]))                
                
                with rasterio.open(fname,'w',transform=transform,
                                   height=shape[-2],width=shape[-1],crs=dataset.crs,
                                   count=dataset.count,dtype=rasterio.float32,nodata=0,
                                   num_threads='all_cpus', compress='lzw', BIGTIFF = 'YES') as dst:#compress='lzw',
                        dst.write(data)
