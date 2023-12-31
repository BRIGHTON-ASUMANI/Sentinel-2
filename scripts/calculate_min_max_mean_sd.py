import os
import rasterio
import numpy as np

def calculate_statistics(image_path):
    """
    Calculate statistics (Min, Max, Mean, Median, Standard Deviation) for the image band.

    Parameters:
    - image_path (str): Path to the raster image file.

    Returns:
    - None
    """
    # Check if the image file exists
    if not os.path.exists(image_path):
        print(f"Error: Image file not found at {os.path.abspath(image_path)}")
        return

    with rasterio.open(image_path) as src:
        # Print metadata
        print("Metadata of the image:")
        print(src.meta)

        # Read the image band (assuming it's a single-band image)
        band = src.read(1)

        # Calculate statistics for the band
        print("\nStatistics for the image band:")
        print(f"Min: {np.nanmin(band)}")
        print(f"Max: {np.nanmax(band)}")
        print(f"Mean: {np.nanmean(band)}")
        print(f"Median: {np.nanmedian(band)}")
        print(f"Standard Deviation: {np.nanstd(band)}")

if __name__ == "__main__":
    # Specify the path to the raster image
    script_folder = os.path.dirname(__file__)
    image_path = os.path.abspath(os.path.join(script_folder, "../GRANULE/IMG_DATA/T36NXF_20221127T075159_AOT_20m.jp2"))

    # Call the function to calculate statistics
    calculate_statistics(image_path)
    
# Sample output

# Metadata of the image:
# {'driver': 'JP2OpenJPEG', 'dtype': 'uint16', 'nodata': None, 'width': 5490, 'height': 5490, 'count': 1, 'crs': CRS.from_epsg(32636), 'transform': Affine(20.0, 0.0, 600000.0,
#        0.0, -20.0, 100020.0)}

# Statistics for the image band:
# Min: 47
# Max: 199
# Mean: 106.66590993394182
# Median: 108.0
# Standard Deviation: 8.283675389113222
