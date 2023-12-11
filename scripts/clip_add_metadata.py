import os
import rasterio
from rasterio.mask import mask
import geopandas as gpd

def clip_image_with_metadata(source_image_path, geojson_path, output_image_path):
    """
    Clips a raster image using a GeoJSON file, adds metadata, and saves the clipped image.

    Parameters:
    - source_image_path (str): Path to the source raster image.
    - geojson_path (str): Path to the GeoJSON file defining the region of interest.
    - output_image_path (str): Path to save the clipped image.

    Returns:
    - None
    """
    # Check if the GeoJSON file exists
    if not os.path.exists(geojson_path):
        print(f"Error: GeoJSON file not found at {os.path.abspath(geojson_path)}")
        return

    # Load GeoJSON file
    geojson = gpd.read_file(geojson_path)

    # Open the source image
    with rasterio.open(source_image_path) as src:
        try:
            # Clip the image to the GeoJSON shapes
            clipped_img, clipped_transform = mask(src, geojson["geometry"], crop=True)
            print("Image successfully clipped.")
        except ValueError:
            print("No valid intersection between GeoJSON shapes and raster. Skipping clipping.")
            return

        # Add metadata tag
        clipped_img.meta["region"] = "test roi"

        # Save the clipped image to a new file
        with rasterio.open(output_image_path, "w", **clipped_img.meta) as dest:
            dest.write(clipped_img)
            print(f"Clipped image saved to {os.path.abspath(output_image_path)}")

if __name__ == "__main__":
    # Specify paths
    script_folder = os.path.dirname(__file__)
    source_image_path = "/home/brighton/pp/Sentinel-2/GRANULE/IMG_DATA/T36NXF_20221127T075159_AOT_20m.jp2"
    geojson_path = os.path.abspath(os.path.join(script_folder, "region_of_interest.geojson"))
    output_image_path = "clipped_image/test.jp2"
    
    print(f"GeoJSON file path: {geojson_path}")

    # Call the function to perform the clipping and metadata addition
    clip_image_with_metadata(source_image_path, geojson_path, output_image_path)
    
# GeoJSON file path: /home/brighton/pp/Sentinel-2/scripts/region_of_interest.geojson
# Image successfully clipped.
# Clipped image saved to /home/brighton/pp/Sentinel-2/clipped_image/test.jp2


