import psycopg2
from psycopg2 import sql
import os
import rasterio
import numpy as np

def calculate_and_save_statistics(image_path):
    """
    Calculate statistics (Min, Max, Mean, Median, Standard Deviation) for spectral indices in a raster image.

    Parameters:
    - image_path (str): Path to the raster image file.

    Returns:
    - dict: Dictionary containing calculated statistics.
    """
    with rasterio.open(image_path) as src:
        # Read the image bands
        red_band = src.read(3)
        nir_band = src.read(4)
        green_band = src.read(2)

        # Calculate NDVI (Normalized Difference Vegetation Index)
        ndvi = (nir_band - red_band) / (nir_band + red_band)

        # Calculate other indices (replace with your formulas)
        # ndwi = ...

        # Calculate statistics for each index
        indices = {'NDVI': ndvi, 'NDWI': ndwi}  # Add other indices as needed

        statistics = {}
        for index_name, index_values in indices.items():
            statistics[index_name] = {
                "min": np.nanmin(index_values),
                "max": np.nanmax(index_values),
                "mean": np.nanmean(index_values),
                "median": np.nanmedian(index_values),
                "std_dev": np.nanstd(index_values),
            }

        return statistics

def create_table(cursor):
    """
    Create a PostgreSQL table.

    Parameters:
    - cursor (psycopg2.extensions.cursor): PostgreSQL database cursor.

    Returns:
    - None
    """
    create_table_query = """
    CREATE TABLE IF NOT EXISTS test_roi_tbl (
        image_date DATE,
        min FLOAT,
        max FLOAT,
        mean FLOAT,
        median FLOAT,
        std_dev FLOAT
    );
    """
    cursor.execute(create_table_query)

def insert_values(cursor, image_date, statistics):
    """
    Insert values into the PostgreSQL table.

    Parameters:
    - cursor (psycopg2.extensions.cursor): PostgreSQL database cursor.
    - image_date (str): Date associated with the image.
    - statistics (dict): Dictionary containing calculated statistics.

    Returns:
    - None
    """
    insert_query = sql.SQL("""
    INSERT INTO test_roi_tbl (image_date, min, max, mean, median, std_dev)
    VALUES (%s, %s, %s, %s, %s, %s);
    """)

    for index_name, index_stats in statistics.items():
        cursor.execute(insert_query, (
            image_date,
            index_stats["min"],
            index_stats["max"],
            index_stats["mean"],
            index_stats["median"],
            index_stats["std_dev"],
        ))

def main():
    # Specify the path to the raster image
    image_path = "/path/to/your/image.jp2"

    # Connect to the PostgreSQL database
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    try:
        # Create a cursor
        with connection.cursor() as cursor:
            # Calculate statistics
            statistics = calculate_statistics(image_path)

            # Create the table
            create_table(cursor)

            # Insert values into the table
            image_date = "2023-01-01"  # Replace with the actual date
            insert_values(cursor, image_date, statistics)

        # Commit the changes
        connection.commit()

        # Print the values in the table
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM test_roi_tbl;")
            rows = cursor.fetchall()
            print("Values in test_roi_tbl:")
            for row in rows:
                print(row)

    finally:
        # Close the connection
        connection.close()

if __name__ == "__main__":
    main()
