import csv
import random
from datetime import datetime, timedelta

# Simulation parameters
num_records = 100  # Number of data points to simulate
start_time = datetime.now() - timedelta(days=1)  # Start time for simulation

# File to save the simulated data
file_name = "health_data.csv"

# Generate random data for heart rate, steps, calories, and sleep
def generate_data():
    data = []
    for i in range(num_records):
        timestamp = start_time + timedelta(minutes=i * 15)  # 15-minute intervals
        heart_rate = random.randint(60, 120)  # Simulate heart rate (BPM)
        steps = random.randint(0, 10000)      # Simulate daily steps
        calories = random.randint(800, 2500)  # Simulate calories burned
        sleep_hours = random.uniform(4, 9)   # Simulate sleep hours (random float)
        data.append([timestamp.isoformat(), heart_rate, steps, calories, round(sleep_hours, 1)])
    return data

# Save data to a CSV file
def save_to_csv(data, file_name):
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "heart_rate", "steps", "calories", "sleep_hours"])  # Header
        writer.writerows(data)

# Generate and save the data
simulated_data = generate_data()
save_to_csv(simulated_data, file_name)
print(f"Simulated data saved to {file_name}")


