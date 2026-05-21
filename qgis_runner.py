"""
qgis_runner.py
Run this file inside the QGIS Python Console Editor.
It dynamically reloads changes from your Git repository without restarting QGIS.
"""
import sys
import os
import importlib
import ee
from ee_plugin import Map 

# 1. Dynamically add this repository to the QGIS Python path
repo_dir = os.path.dirname(__file__)
if repo_dir not in sys.path:
    sys.path.append(repo_dir)

# 2. Import your logic module and force a reload to clear the QGIS cache
import gee_logic
importlib.reload(gee_logic)

def main():
    try:
        # Example coordinates (New York City)
        nyc_lon = -74.0060
        nyc_lat = 40.7128
        
        # 3. Call your pure GEE logic
        dem_image, vis_params = gee_logic.get_elevation_model(nyc_lon, nyc_lat, buffer_meters=20000)
        
        # 4. Render directly to the QGIS Canvas
        Map.setCenter(nyc_lon, nyc_lat, 11)
        Map.addLayer(dem_image, vis_params, 'NYC Elevation (SRTM)')
        
        print("Successfully reloaded and rendered from Git repository!")

    except Exception as e:
        print(f"Error running GEE script: {e}")

if __name__ == '__main__':
    main()
