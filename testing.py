import csv
from datetime import datetime
import matplotlib.pyplot as plt

# File path
file_path = 'Project2/Beach_Water_Quality.csv'

# Lists to hold timestamps and water temperatures for each beach
timestamps_Ohio = []
water_temps_Ohio = []
timestamps_Rainbow = []
water_temps_Rainbow = []

water_temp_min = 0
water_temp_max = 30

# Read CSV file
with open(file_path, 'r', encoding='utf8') as fin:
    reader = csv.DictReader(fin)
    for row in reader:
        try:
            # Convert timestamp from format 'MM/DD/YYYY HH:MM:SS AM/PM'
            timestamp = datetime.strptime(row['Measurement Timestamp'], '%m/%d/%Y %I:%M:%S %p')
            water_temp = float(row['Water Temperature'])

            # Filter for Ohio Street Beach
            if row['Beach Name'] == 'Ohio Street Beach':
                if water_temp_min < water_temp < water_temp_max:
                    timestamps_Ohio.append(timestamp)
                    water_temps_Ohio.append(water_temp)

            # Filter for Rainbow Beach
            elif row['Beach Name'] == 'Rainbow Beach':
                if water_temp_min < water_temp < water_temp_max:
                    timestamps_Rainbow.append(timestamp)
                    water_temps_Rainbow.append(water_temp)

        except (ValueError, KeyError):
            continue  # Skip bad data

# Sort data by time for both beaches
sorted_data_Ohio = sorted(zip(timestamps_Ohio, water_temps_Ohio))
timestamps_Ohio, water_temps_Ohio = zip(*sorted_data_Ohio)

sorted_data_Rainbow = sorted(zip(timestamps_Rainbow, water_temps_Rainbow))
timestamps_Rainbow, water_temps_Rainbow = zip(*sorted_data_Rainbow)

# Plotting
plt.figure(figsize=(12, 6))

# Scatter plot for both beaches with smaller dot size
plt.scatter(timestamps_Ohio, water_temps_Ohio, label='Ohio Street Beach', color='blue', alpha=0.6, s=10)  # s=20 for smaller dots
plt.scatter(timestamps_Rainbow, water_temps_Rainbow, label='Rainbow Beach', color='orange', alpha=0.6, s=10)  # s=20 for smaller dots

# Customizing the plot
plt.xlabel('Time', fontsize=14)
plt.ylabel('Water Temperature (°C)', fontsize=14)
plt.title('Water Temperature Over Time at Ohio Street and Rainbow Beach', fontsize=16)
plt.xticks(rotation=45)
plt.ylim(water_temp_min, water_temp_max + 5)  # Set y-axis limits
plt.legend(fontsize=12)
plt.grid(alpha=0.3)  # Light grid for better readability

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
