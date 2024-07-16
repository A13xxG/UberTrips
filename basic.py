from datetime import datetime
import pytz
import numpy as np
from cli_decorator import cli
import pandas as pd


def get_trip_stats(df):
    temp_data = df

    def convert_to_seconds(datetime_str):
        datetime_format = '%Y-%m-%d %H:%M:%S %z %Z'
        dt = datetime.strptime(datetime_str, datetime_format)
        dt = dt.astimezone(pytz.utc)
        time_in_seconds = int(dt.timestamp())
        return time_in_seconds

    temp_data["Begin Trip Time In Seconds"] = temp_data["Begin Trip Time"].apply(convert_to_seconds)
    temp_data["Dropoff Time In Seconds"] = temp_data["Dropoff Time"].apply(convert_to_seconds)
    temp_data['Dropoff Time In Seconds'] = temp_data['Dropoff Time In Seconds'].where(
        df['Trip or Order Status'] == "COMPLETED")
    temp_data['Begin Trip Time In Seconds'] = temp_data['Begin Trip Time In Seconds'].where(
        df['Trip or Order Status'] == "COMPLETED")
    temp_data['Time Spent On Trip'] = temp_data['Dropoff Time In Seconds'] - df['Begin Trip Time In Seconds']
    return {
        "The longest trip": f"{temp_data['Time Spent On Trip'].max().astype(int)} seconds",
        "The shortest trip": f"{temp_data['Time Spent On Trip'].min().astype(int)} seconds",
        "The average trip duration": f"{temp_data['Time Spent On Trip'].mean().astype(int)} seconds",
        "The total time spent on trips": f"{temp_data['Time Spent On Trip'].sum().astype(int)} seconds"
    }


def get_total_trips(df):
    return {
        "Total trips": len(df),
        "Total trips completed": len(df[df['Trip or Order Status'] == "COMPLETED"]),
        "Total trips cancelled": len(df[df['Trip or Order Status'] == "CANCELED"]),
        "Total trips unfufilled": len(df[df['Trip or Order Status'] == "UNFULFILLED"]),
        "Total trips fare-split": len(df[df['Trip or Order Status'] == "FARE_SPLIT"]),
    }


def get_all_money_spent(df):
    return {
        "Total money spent in RON": float(df['Fare Amount'].where(df['Fare Currency'] == "RON").sum()),
        "Total money spent in GBP": float(df['Fare Amount'].where(df['Fare Currency'] == "GBP").sum()),
        "Total money spent in EUR": float(df['Fare Amount'].where(df['Fare Currency'] == "EUR").sum()),
    }


def get_all_trips_from_city(df, city):
    return {
        f"Total trips from {city}": len(df[df['City'] == city]),
    }


def get_all_trips_from_trip_by_year(df, year):
    # Convert 'Request Time' to datetime
    df['Request Time'] = df['Request Time'].str.replace(" UTC", "")
    df['Request Time'] = pd.to_datetime(df['Request Time'])

    # Extract year from 'Request Time'
    df['Year'] = df['Request Time'].dt.year

    # Filter rows where 'Year' is the given year and 'Trip or Order Status' is either 'COMPLETED' or 'FARE_SPLIT'
    filtered_df = df[(df['Year'] == year) & (df['Trip or Order Status'].isin(["COMPLETED", "FARE_SPLIT"]))]

    return {
        f"Total trips from {year}": len(filtered_df),
    }


def get_all_trips_by_month(df, month):
    # Ensure 'Request Time' is of string type
    df['Request Time'] = df['Request Time'].astype(str)

    # Remove " UTC" from 'Request Time'
    df['Request Time'] = df['Request Time'].str.replace(" UTC", "")

    # Convert 'Request Time' to datetime
    df['Request Time'] = pd.to_datetime(df['Request Time'])

    # Extract month from 'Request Time'
    df['Month'] = df['Request Time'].dt.month

    # Filter rows where 'Month' is the given month and 'Trip or Order Status' is either 'COMPLETED' or 'FARE_SPLIT'
    filtered_df = df[(df['Month'] == int(month)) & (df['Trip or Order Status'].isin(["COMPLETED", "FARE_SPLIT"]))]

    return {
        f"Total trips from {month}": len(filtered_df),
    }

def get_all_distance_travelled(df):
    return {
        "Total distance travelled in km": float((df['Distance (miles)'].sum() * 1.60934).round(2)),
    }

def get_trips_by_product_type(df, product):
    return {
        f"Total trips by {product}": len(df[df['Product Type'] == product].where(
            df['Trip or Order Status'] == ("COMPLETED" or "FARE_SPLIT")
        )),
    }


@cli
def main(file):
    columns = [
        "City", "Product Type", "Trip or Order Status", "Request Time", "Begin Trip Time",
        "Begin Trip Lat", "Begin Trip Lng", "Begin Trip Address", "Dropoff Time",
        "Dropoff Lat", "Dropoff Lng", "Dropoff Address", "Distance (miles)",
        "Fare Amount", "Fare Currency"
    ]
    df = pd.read_csv(file, usecols=columns)
    print(get_trip_stats(df))
    print(get_total_trips(df))
    print(get_all_money_spent(df))
    print(get_all_trips_from_city(df, "London"))
    print(get_all_trips_from_trip_by_year(df, 2024))
    print(get_all_trips_by_month(df, '5'))
    print(get_all_distance_travelled(df))
    print(get_trips_by_product_type(df, "Comfort"))


if __name__ == '__main__':
    main()
