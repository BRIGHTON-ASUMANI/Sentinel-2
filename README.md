# Sentinel-2

# Zonal Statistics Calculation and Database Update
![Screenshot from 2023-12-11 15-46-08](https://github.com/BRIGHTON-ASUMANI/Sentinel-2/assets/36225890/e779073d-47f8-45e4-a864-04931cc05022)

This Python script performs zonal statistics calculation on raster images, adds calculated indices as bands to the original image, and updates the PostgreSQL database with the results.

## Features

- **Zonal Statistics Calculation:**
  - Calculates statistics (Min, Max, Mean, Median, Standard Deviation) for spectral indices in a raster image.
  - Supports various indices (e.g., NDVI) with easy extensibility.

- **Add Indices as Bands:**
  - Adds the calculated indices as bands to the original image.

- **PostgreSQL Database Update:**
  - Creates a PostgreSQL database and a table to store zonal statistics.
  - Updates the table with calculated statistics, including image date, minimum, maximum, mean, median, and standard deviation.

## Prerequisites

- Python 3.x
- PostgreSQL

## Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:BRIGHTON-ASUMANI/Sentinel-2.git
    cd Sentinel-2
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a PostgreSQL database and update the `.env` file with your database details.

4. Run the script:

    ```bash
    python calculate_spectral_index.py
    ```

## Usage

- Update the paths and parameters in `calculate_spectral_index.py` according to your data and requirements.
- Run the script to perform zonal statistics calculation, add indices as bands, and update the PostgreSQL database.

## Environment Variables

Create a `.env` file in the root directory with the following content:

```env
DB_HOST=your_host
DB_NAME=zonal_statistics_db
DB_USER=your_username
DB_PASSWORD=your_password
