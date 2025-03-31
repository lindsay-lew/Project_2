#PLOT 1
import json
files = [
    'Project2/US_PopulationData.json',
]
json_data = []  # Store JSON data separately
for file in files: 
    # Load JSON file
    if file.endswith('.json'):
        with open(file, encoding='utf8') as fin:
            raw_content = fin.read()  # Read raw content
            json_data = json.loads(raw_content)  # Load JSON data
            print(f'Type of json_data: {type(json_data)}')  # Check data structure type
            print("Keys in JSON data:", json_data[0].keys())  # Print the keys of the metadata

            # Extract the second item, which contains the actual population data
            if isinstance(json_data, list) and len(json_data) > 1:
                population_data = json_data[1]  # Access the second element (the list of records)
                print(f'Total entries in population data: {len(population_data)}')  # Print total entries

                # Optionally print a sample entry to inspect its structure
                if population_data:
                    print("Sample data entry:", population_data[0])  # Print the first entry

                # Extracting years and population values for plotting in ascending order
                # years = [entry['date'] for entry in population_data]  # Get years
                # population_values = [entry['value'] for entry in population_data]  # Get population values

                # Sort the data by year in ascending order
                years = [entry['date'] for entry in reversed(population_data)]
                population_values = [entry['value'] for entry in reversed(population_data)]

                # Plotting
                import matplotlib.pyplot as plt
                plt.figure(figsize=(12, 6))
                plt.plot(years, population_values, marker='o', linestyle='-', color='teal')
                plt.xlabel('Year')
                plt.ylabel('Population')
                plt.title('US Population Over Years')
                plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
                plt.tight_layout()
                plt.savefig('Population_Plot.png', bbox_inches='tight')
                plt.show()
            else:
                print("No valid population data found.")



#PLOT 2
import csv
from datetime import datetime
files = [
    'Project2/Beach_Water_Quality.csv',
]
csv_data = []  # Store CSV data separately

# Lists to hold timestamps and water temperatures for Ohio Street Beach
timestamps_Ohio = []
water_temps_Ohio = []
timestamps_Rainbow = []
water_temps_Rainbow = []

water_temp_min = 10
water_temp_max = 30

# Read CSV file
with open('Project2/Beach_Water_Quality.csv', 'r', encoding='utf8') as fin:
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

        except (ValueError, KeyError):  # Handle conversion errors
            continue  # Skip bad data


# Sort data by time for both beaches
sorted_data_Ohio = sorted(zip(timestamps_Ohio, water_temps_Ohio))
timestamps_Ohio, water_temps_Ohio = zip(*sorted_data_Ohio)

sorted_data_Rainbow = sorted(zip(timestamps_Rainbow, water_temps_Rainbow))
timestamps_Rainbow, water_temps_Rainbow = zip(*sorted_data_Rainbow)

# Plotting
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))

# Scatter plot for both beaches with smaller dot size
plt.scatter(timestamps_Ohio, water_temps_Ohio, label='Ohio Street Beach', color='teal', alpha=0.6, s=10)  # s=20 for smaller dots
plt.scatter(timestamps_Rainbow, water_temps_Rainbow, label='Rainbow Beach', color='magenta', alpha=0.6, s=10)  # s=20 for smaller dots

# Customizing the plot
plt.xlabel('Year')
plt.ylabel('Water Temperature (°C)')
plt.title('Water Temperature Over Time at Ohio Street and Rainbow Beach')
plt.xticks(rotation=45)
plt.ylim(water_temp_min, water_temp_max + 5)  # Set y-axis limits
plt.legend(fontsize=12)

# Adjust layout and show the plot
plt.tight_layout()
plt.savefig('Beach_Plot.png', bbox_inches='tight')
plt.show()



# import pprint
# pprint.pprint(csv_data[:5])  # Print only the first 5 records to avoid excessive output

# # Print column headers (categories) in the dataset
# print("Column headers in dataset:", csv_data[0].keys())

