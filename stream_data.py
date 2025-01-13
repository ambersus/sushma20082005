import csv
import time

# File to stream data from
file_name = "health_data.csv"

def stream_data(file_name, delay=2):
    with open(file_name, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)  # Simulate sending the row to Pathway
            time.sleep(delay)  # Wait before sending the next row (real-time simulation)

# Stream the data
stream_data(file_name)
