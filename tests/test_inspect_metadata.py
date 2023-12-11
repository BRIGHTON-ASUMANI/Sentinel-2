import os
import unittest
from tempfile import TemporaryDirectory
import rasterio
from scripts.inspect_metadata import inspect_image

class TestInspectImage(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.temp_dir = TemporaryDirectory()
        self.image_path = os.path.join(self.temp_dir.name, "GRANULE/IMG_DATA/T36NXF_20221127T075159_AOT_20m.jp2")

        # Create an empty image file (for testing purposes)
        with open(self.image_path, "w"):
            pass

    def tearDown(self):
        # Clean up the temporary directory
        self.temp_dir.cleanup()

    def test_inspect_image(self):
        # Call the inspect_image function with the test image path
        metadata = inspect_image(self.image_path)

        # Assert that the metadata is not empty
        self.assertTrue(metadata)

if __name__ == "__main__":
    # Run the unit tests
    unittest.main()
