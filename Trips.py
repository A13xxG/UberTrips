from datetime import datetime

import pandas as pd
import pytz


class Trip:
    def __init__(self, city, product_type, trip_or_order_status, request_time, begin_trip_time, begin_trip_lat,
                 begin_trip_lng, begin_trip_address, dropoff_time, dropoff_lat, dropoff_lng, dropoff_address, distance,
                 fare_amount, fare_currency):
        self.city = city
        self.product_type = product_type
        self.trip_or_order_status = trip_or_order_status
        self.request_time = request_time
        self.begin_trip_time = begin_trip_time
        self.begin_trip_lat = begin_trip_lat
        self.begin_trip_lng = begin_trip_lng
        self.begin_trip_address = begin_trip_address
        self.dropoff_time = dropoff_time
        self.dropoff_lat = dropoff_lat
        self.dropoff_lng = dropoff_lng
        self.dropoff_address = dropoff_address
        self.distance = distance * 1.60934
        self.fare_amount = fare_amount
        self.fare_currency = fare_currency

        self.time_spent_on_trip = self.convert_to_seconds(dropoff_time) - self.convert_to_seconds(begin_trip_time)

        self.request_time = self.request_time.replace(" UTC", "")
        self.year = pd.to_datetime(self.request_time).year
        if self.year == '1970':
            self.dropoff_time = self.begin_trip_time = self.request_time
        self.month = pd.to_datetime(self.request_time).month

    def convert_to_seconds(self, datetime_str):
        datetime_format = '%Y-%m-%d %H:%M:%S %z %Z'
        dt = datetime.strptime(datetime_str, datetime_format)
        dt = dt.astimezone(pytz.utc)
        time_in_seconds = int(dt.timestamp())
        return time_in_seconds
