import os
import rasterio
from rasterio.mask import mask
import geopandas as gpd
import unittest
from tempfile import TemporaryDirectory

class TestClipImageWithMetadata(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.temp_dir = TemporaryDirectory()
        self.source_image_path = os.path.join(self.temp_dir.name, "source_image.jp2")
        self.geojson_path = os.path.join(self.temp_dir.name, "region_of_interest.geojson")
        self.output_image_path = os.path.join(self.temp_dir.name, "clipped_image.jp2")

        # Create test files
        with open(self.source_image_path, "w") as src_file:
            src_file.write("Test source image content")

        with open(self.geojson_path, "w") as geojson_file:
            geojson_file.write('{"type": "FeatureCollection", "features": []}')

    def tearDown(self):
        # Clean up the temporary directory
        self.temp_dir.cleanup()

    def test_clip_image_with_metadata(self):
        # Call the function to test
        clip_image_with_metadata(self.source_image_path, self.geojson_path, self.output_image_path)

        # Check if the output file exists
        self.assertTrue(os.path.exists(self.output_image_path))

        # Check if the metadata tag is added
        with rasterio.open(self.output_image_path) as dest:
            self.assertIn("region", dest.meta)
            self.assertEqual(dest.meta["region"], "test roi")

if __name__ == "__main__":
    unittest.main()
