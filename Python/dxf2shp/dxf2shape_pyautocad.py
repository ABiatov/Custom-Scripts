# reciept generated ChatGPT

# Install the required libraries:
# pip install pyautocad pyshp

# Import the necessary modules:
import pyautocad
import shapefile

# Read the DXF file using pyautocad:
def read_dxf_file(dxf_path):
    dwg = pyautocad.ACAD()
    dwg.read(dxf_path)
    entities = dwg.entities
    return entities

# Convert the DXF entities to Shapefile format using pyshp:
def convert_to_shapefile(dxf_entities, shp_path):
    shp_writer = shapefile.Writer(shp_path, shapeType=shapefile.POLYLINE)
    shp_writer.field("Name", "C")  # Add an attribute field if needed

    for entity in dxf_entities:
        if entity.dxftype() == "LWPOLYLINE" or entity.dxftype() == "POLYLINE":
            polyline = []
            for point in entity:
                polyline.append([point.x, point.y])
            shp_writer.line([polyline])  # Write the polyline to Shapefile
            shp_writer.record("Polyline")  # Record attributes if needed

    shp_writer.close()

# Call the functions to perform the conversion:
dxf_file_path = "C:/Users/admin/Dropbox/Bussines_DB/ABSpatial/projects/metasymbiont/data/DXF_202306015/DXF/vazuza_loc_1.dxf"
shp_file_path = "C:/Users/admin/Dropbox/Bussines_DB/ABSpatial/projects/metasymbiont/data/DXF_202306015/DXF/shp/vazuza_loc_1.dxf"


entities = read_dxf_file(dxf_file_path)
convert_to_shapefile(entities, shp_file_path)




