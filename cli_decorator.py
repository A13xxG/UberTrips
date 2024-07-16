import argparse
import os
import sys


def cli(func):
    def wrapper():
        parser = argparse.ArgumentParser(
            prog="UberTrips",
            description='This program will help you understand some of the Uber trips data',
            epilog='Enjoy the program!'
        )
        parser.add_argument(
            '-f', '--file',
            type=str,
            required=True,
            help='The path to the CSV file containing the data'
        )

        args = parser.parse_args()
        file_path = os.path.join(args.file)

        if os.path.isfile(file_path) and file_path.lower().endswith('.csv'):
            return func(file_path)
        else:
            print("File does not exist or is not a CSV file. Please provide a valid CSV file path.")

            for i in range(3, 0, -1):
                print("-" * 100)
                file_path = input(f"Please enter a valid CSV file path (you have {i} tries left): ")
                if os.path.isfile(file_path) and file_path.lower().endswith('.csv'):
                    break
                print(f"{file_path} is not a valid CSV file path.")

            if os.path.isfile(file_path) and file_path.lower().endswith('.csv'):
                return func(file_path)
            else:
                print("Failed to provide a valid CSV file path after 3 attempts.")
                return sys.exit(1)

    return wrapper
