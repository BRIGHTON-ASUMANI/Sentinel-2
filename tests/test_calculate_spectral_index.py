import os
import unittest
import rasterio
import numpy as np

class TestCalculateAndAddIndices(unittest.TestCase):
    def setUp(self):
        # Create a temporary output directory for test files
        self.temp_output_dir = "temp_output"
        os.makedirs(self.temp_output_dir, exist_ok=True)

    def tearDown(self):
        # Clean up temporary files
        if os.path.exists(self.temp_output_dir):
            for file_name in os.listdir(self.temp_output_dir):
                file_path = os.path.join(self.temp_output_dir, file_name)
                os.remove(file_path)
            os.rmdir(self.temp_output_dir)

    def test_calculate_and_add_indices(self):
        # Specify the paths
        script_folder = os.path.dirname(__file__)
        image_path = os.path.abspath(os.path.join(script_folder, "../GRANULE/IMG_DATA/T36NXF_20221127T075159_AOT_20m.jp2"))
        output_image_path = os.path.join(self.temp_output_dir, "test.jp2")

        # Call the function to calculate and add indices
        calculate_and_add_indices(image_path, output_image_path)

        # Check if the output file is created
        self.assertTrue(os.path.exists(output_image_path))

        # Additional assertions can be added based on specific requirements

if __name__ == "__main__":
    unittest.main()
