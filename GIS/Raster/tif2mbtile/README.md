# GeoTIFF to MBTiles

## Variant 1 (gdal_translate)

```{sh}
gdal_translate DNPWildFire1_Orthomosaic_export_TueOct10.tif DNPWildFire1_10oct.mbtiles -of MBTILES
gdaladdo -r average —config COMPRESS_OVERVIEW JPEG DNPWildFire1_10oct.mbtiles 2 4 8 16
```
or

```{sh}
gdal_translate DNPWildFire1_Orthomosaic_export_TueOct10.tif DNPWildFire1_10oct.mbtiles -of MBTILES && gdaladdo -r average —config COMPRESS_OVERVIEW JPEG DNPWildFire1_10oct.mbtiles 2 4 8 16
```

## Variant 2 (gdal2mbtiles)

[https://github.com/ecometrica/gdal2mbtiles](https://github.com/ecometrica/gdal2mbtiles)

```{sh}
gdal2mbtiles --format jpg --resampling near --zoom-offset 7  DNP_20170904_Canon_S100_transparent_mosaic_group1.tif DNP_20170904.mbtiles
```


## Variant 3 (gdalbuildvrt & gdal2mbt)

[https://github.com/icetan/gdal2mbt](https://github.com/icetan/gdal2mbt)

```{sh}
gdalbuildvrt ./DNPWildFire1_10oct.vrt ./DNPWildFire1_Orthomosaic_export_TueOct10.tif
```

mbt.json 

```{json}
{
    "source": "DNPWildFire1_10oct.vrt",
    "num_levels": 8,
    "metadata": {
        "name": "DNPWildFire1_10oct",
        "description": "Aerial photos wildfire in DNP 20171010"
    }
}
```

```{sh}
gdal2mbt create -c mbt.json DNPWildFire1_10oct.mbtiles
```


