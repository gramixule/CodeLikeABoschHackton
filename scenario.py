import pandas as pd

# Load your data
data = pd.read_excel('FilteredAndNormalizedData.xlsx', engine='openpyxl')

# Define a threshold for distance and speed checks
distance_threshold = 0.2  # Adjust as needed
speed_threshold = 0.1  # Adjust as needed

# Initialize variables to track scenario conditions
obstacle_approaching = False

# Iterate through the dataset
for i in range(1, len(data)):
    # Calculate distance between vehicle and obstacle (assuming FirstObjectDistance_X and FirstObjectDistance_Y represent obstacle position)
    distance = ((data.at[i, 'FirstObjectDistance_X'] - data.at[i - 1, 'FirstObjectDistance_X']) ** 2 +
                (data.at[i, 'FirstObjectDistance_Y'] - data.at[i - 1, 'FirstObjectDistance_Y']) ** 2) ** 0.5

    # Check if the vehicle is approaching the obstacle
    if distance < distance_threshold and data.at[i, 'VehicleSpeed'] > speed_threshold:
        obstacle_approaching = True
        break  # You can break the loop when the condition is met

# Check the condition to estimate the scenario
if obstacle_approaching:
    print("Estimated Scenario: Vehicle is approaching an obstacle.")
else:
    print("Scenario not detected.")
