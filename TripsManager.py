from cli_decorator import cli
import pandas as pd
from Trips import Trip


@cli
class TripsManager:

    def __init__(self, file_path):
        try:
            self.list_of_trips = []
            self.df = pd.read_csv(file_path)
            for index, row in self.df.iterrows():
                trip = Trip(
                    row['City'], row['Product Type'], row['Trip or Order Status'], row['Request Time'],
                    row['Begin Trip Time'], row['Begin Trip Lat'], row['Begin Trip Lng'], row['Begin Trip Address'],
                    row['Dropoff Time'], row['Dropoff Lat'], row['Dropoff Lng'], row['Dropoff Address'],
                    row['Distance (miles)'], row['Fare Amount'], row['Fare Currency']
                )
                self.list_of_trips.append(trip)
            print("Trips data loaded successfully.")
        except Exception as e:
            print(f"An error occurred while loading the trips data: {e}")
            return

    def get_all_money_spent(self, currency):
        total_money_spent = sum([x.fare_amount for x in self.list_of_trips if x.fare_currency == currency])
        return {
            f"Total money spent in {currency}": total_money_spent,
        }

    def get_all_trips(self):
        return {
            "Total COMPLETED trips": len([x for x in self.list_of_trips
                                          if x.trip_or_order_status == "COMPLETED"]),
            "Total FARE SPLIT trips": len([x for x in self.list_of_trips
                                           if x.trip_or_order_status == "FARE_SPLIT"]),
            "Total CANCELED trips": len([x for x in self.list_of_trips
                                         if x.trip_or_order_status == "CANCELED"]),
            "Total UNFULFILLED trips": len([x for x in self.list_of_trips
                                            if x.trip_or_order_status == "UNFULFILLED"]),
        }

    def get_all_trips_by_year(self, year):
        return {
            f"Total trips from {year}": len([x for x in self.list_of_trips if x.year == year]),
        }

    def get_all_trips_by_month(self, month):
        return {
            f"Total trips from {month}": len([x for x in self.list_of_trips if x.month == month]),
        }

    def get_all_trips_by_city(self, city):
        return {
            f"Total trips from {city}": len([x for x in self.list_of_trips if x.city == city]),
        }

    def get_all_distance_travelled(self):
        total_distance = sum(
            [x.distance for x in self.list_of_trips if pd.notnull(x.distance) and isinstance(x.distance, (int, float))])
        return {
            "Total distance travelled in km": round(float(total_distance), 2) if pd.notnull(total_distance) else 0,
        }

    def get_all_trips_by_product_type(self, product):
        return {
            f"Total trips by {product}": len([x for x in self.list_of_trips if x.product_type == product]),
        }

    def get_total_time_spent_on_trips(self):
        total_time_spent = sum([x.time_spent_on_trip for x in self.list_of_trips if x.time_spent_on_trip > 0])
        days, remainder = divmod(total_time_spent, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        return {
            "Total time spent on trips": f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"
        }

    def get_the_shortest_trip(self):
        shortest_trip = min(x.distance for x in self.list_of_trips if x.distance > 0)
        return {
            "The shortest trip": f"{shortest_trip} km"
        }

    def get_the_longest_trip(self):
        longest_trip = max(x.distance for x in self.list_of_trips)
        return {
            "The longest trip": f"{longest_trip} km"
        }


    def print_all_stats_the_hardcoded_way(self):
        print(self.get_all_money_spent("RON"))
        print(self.get_all_money_spent("GBP"))
        print(self.get_all_money_spent("EUR"))
        print(self.get_all_trips())
        print(self.get_all_trips_by_year(2017))
        print(self.get_all_trips_by_year(2018))
        print(self.get_all_trips_by_year(2019))
        print(self.get_all_trips_by_year(2020))
        print(self.get_all_trips_by_year(2021))
        print(self.get_all_trips_by_year(2022))
        print(self.get_all_trips_by_year(2023))
        print(self.get_all_trips_by_year(2024))
        print(self.get_all_trips_by_month(1))
        print(self.get_all_trips_by_month(2))
        print(self.get_all_trips_by_month(3))
        print(self.get_all_trips_by_month(4))
        print(self.get_all_trips_by_month(5))
        print(self.get_all_trips_by_month(6))
        print(self.get_all_trips_by_month(7))
        print(self.get_all_trips_by_month(8))
        print(self.get_all_trips_by_month(9))
        print(self.get_all_trips_by_month(10))
        print(self.get_all_trips_by_month(11))
        print(self.get_all_trips_by_month(12))
        print(self.get_all_trips_by_city("Bucharest"))
        print(self.get_all_trips_by_city("Cluj"))
        print(self.get_all_trips_by_city("Paris"))
        print(self.get_all_trips_by_city("London"))
        print(self.get_all_distance_travelled())
        print(self.get_all_trips_by_product_type("UberX"))
        print(self.get_all_trips_by_product_type("Comfort"))
        print(self.get_all_trips_by_product_type("Black"))
        print(self.get_total_time_spent_on_trips())
        print(self.get_the_shortest_trip())
        print(self.get_the_longest_trip())

if __name__ == '__main__':
    data = TripsManager()
    data.print_all_stats()
