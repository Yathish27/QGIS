"""
gee_logic.py
Contains only pure Earth Engine code. Safe for headless environments and Git tracking.
"""
import ee

def get_elevation_model(lon, lat, buffer_meters=20000):
    """
    Fetches the SRTM Digital Elevation Model for a given area.
    """
    # Define an Area of Interest (AOI)
    point = ee.Geometry.Point(lon, lat)
    aoi = point.buffer(buffer_meters)
    
    # Load the SRTM elevation dataset
    dem = ee.Image("USGS/SRTMGL1_003").clip(aoi)
    
    # Define visualization parameters for the DEM
    vis_params = {
        'min': 0,
        'max': 150, 
        'palette': ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']
    }
    
    return dem, vis_params
