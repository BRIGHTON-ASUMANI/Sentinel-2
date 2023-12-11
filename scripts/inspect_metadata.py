import os
import rasterio

def inspect_image(image_path):
    """
    Inspects and prints metadata of a raster image.

    Parameters:
    - image_path (str): Path to the raster image file.

    Returns:
    - None
    """
    # Open the image
    with rasterio.open(image_path) as src:
        # Print the metadata
        print(src.meta)

if __name__ == "__main__":
    # Assuming the script is in the "action_folder"
    script_folder = os.path.dirname(__file__)
    
    # Relative path to the image file
    image_relative_path = "../GRANULE/IMG_DATA/T36NXF_20221127T075159_AOT_20m.jp2"
    
    # Construct the absolute path to the image file
    image_path = os.path.abspath(os.path.join(script_folder, image_relative_path))

    # Call the inspect_image function with the image path
    inspect_image(image_path)

# Sample Output
# {'driver': 'JP2OpenJPEG', 'dtype': 'uint16', 'nodata': None, 'width': 5490, 'height': 5490, 'count': 1, 'crs': CRS.from_epsg(32636), 'transform': Affine(20.0, 0.0, 600000.0,
#        0.0, -20.0, 100020.0)}
