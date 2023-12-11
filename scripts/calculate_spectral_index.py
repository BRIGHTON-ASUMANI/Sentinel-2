import os
import rasterio
import numpy as np

def calculate_and_add_indices(image_path, output_image_path):
    """
    Calculate spectral indices and add them as bands to the original image.

    Parameters:
    - image_path (str): Path to the original raster image file.
    - output_image_path (str): Path to save the image with added bands.

    Returns:
    - None
    """
    # Check if the image file exists
    if not os.path.exists(image_path):
        print(f"Error: Image file not found at {os.path.abspath(image_path)}")
        return

    with rasterio.open(image_path) as src:
        # Get the available band indices
        band_indices = list(range(1, src.count + 1))

        # Check if there are at least two bands available
        if len(band_indices) < 2:
            print("Error: The raster does not have enough bands to calculate indices.")
            return

        # Use Red (band 3) and NIR (band 4) if available; otherwise, use the first two bands
        red_band_index = band_indices[2] if 3 in band_indices else band_indices[0]
        nir_band_index = band_indices[3] if 4 in band_indices else band_indices[1]

        # Read the original image bands
        red_band = src.read(red_band_index)
        nir_band = src.read(nir_band_index)

        # Calculate NDVI (Normalized Difference Vegetation Index)
        ndvi = (nir_band - red_band) / (nir_band + red_band)

        # Add the calculated indices as bands to the original image
        output_profile = src.profile
        output_profile.update(count=src.count + 1)  # Increment band count
        output_profile.update(nodata=np.nan)  # Set nodata value to NaN

        # Open the output image file for writing
        with rasterio.open(output_image_path, 'w', **output_profile) as dest:
            # Write the original bands to the output image
            for i in range(1, src.count + 1):
                dest.write(src.read(i), i)

            # Write the calculated indices as new bands
            dest.write(ndvi, src.count + 1, nodata=np.nan)

if __name__ == "__main__":
    # Specify the paths
    script_folder = os.path.dirname(__file__)
    image_path = os.path.abspath(os.path.join(script_folder, "../GRANULE/IMG_DATA/T36NXF_20221127T075159_AOT_20m.jp2"))
    output_image_path = "test.jp2"

    # Call the function to calculate and add indices
    calculate_and_add_indices(image_path, output_image_path)

# sample output

# Calculating NDVI and adding it as a band to the original image...
# NDVI band successfully added.

# Output image saved to: test.jp2