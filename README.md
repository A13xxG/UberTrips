
# UberTrips Documentation

## Overview
UberTrips is a Python project designed to analyze Uber trips data from a CSV file. The project provides functionality to parse the data, perform various statistical analyses, and print the results.

## Files
- `basic.py`: Contains the main logic for processing and analyzing the trips data.
- `cli_decorator.py`: Provides a decorator to handle command-line arguments for specifying the path to the CSV file.
- `Trips.py`: Defines the `Trip` class to model individual trips.
- `TripsManager.py`: Defines the `TripsManager` class to handle a collection of trips and perform various aggregate analyses.

## Usage

### Running the Script
To run the script, use the following command in your terminal:
```bash
python basic.py -f /path/to/your/csvfile.csv
```
This command will initiate the analysis of the CSV file provided.

### Command-Line Arguments
The script expects a single argument:
- `-f` or `--file`: The path to the CSV file containing the Uber trips data. This argument is required.

### Example
```bash
python basic.py -f Data/uber_trips.csv
```

## Structure and Key Functions

### `cli_decorator.py`
This file defines a decorator function `cli` that is used to handle command-line arguments for the scripts. It ensures the provided file path is valid and prompts the user for a correct path if necessary.

### `Trips.py`
Defines the `Trip` class which represents an individual trip. Key attributes include:
- `city`
- `product_type`
- `trip_or_order_status`
- `request_time`
- `begin_trip_time`
- `begin_trip_lat`
- `begin_trip_lng`
- `begin_trip_address`
- `dropoff_time`
- `dropoff_lat`
- `dropoff_lng`
- `dropoff_address`
- `distance`
- `fare_amount`
- `fare_currency`

### `TripsManager.py`
Defines the `TripsManager` class which is responsible for managing a collection of `Trip` objects and performing aggregate analyses. Key methods include:
- `get_all_money_spent(currency)`
- `get_all_trips()`
- `get_all_trips_by_year(year)`
- `get_all_trips_by_month(month)`
- `get_all_trips_by_city(city)`
- `get_all_distance_travelled()`
- `get_all_trips_by_product_type(product)`
- `get_total_time_spent_on_trips()`
- `get_the_shortest_trip()`
- `get_the_longest_trip()`
- `print_all_stats_the_hardcoded_way()`

### `basic.py`
This file contains the main logic for reading the CSV file and performing analyses. Key functions include:
- `get_trip_stats(df)`
- `get_total_trips(df)`
- `get_all_money_spent(df)`
- `get_all_trips_from_city(df, city)`
- `get_all_trips_from_trip_by_year(df, year)`
- `get_all_trips_by_month(df, month)`
- `get_all_distance_travelled(df)`
- `get_trips_by_product_type(df, product)`

## Data Analysis
The project provides various functions to analyze the Uber trips data:
- **Trip Statistics**: Calculate the longest, shortest, average trip duration, and total time spent on trips.
- **Total Trips**: Count the total number of trips, including completed, cancelled, unfufilled, and fare-split trips.
- **Money Spent**: Calculate the total money spent in different currencies (RON, GBP, EUR).
- **Trips by City**: Count the total trips from a specific city.
- **Trips by Year/Month**: Count the total trips in a specific year or month.
- **Distance Travelled**: Calculate the total distance travelled in kilometers.
- **Trips by Product Type**: Count the total trips by product type (e.g., UberX, Comfort, Black).
