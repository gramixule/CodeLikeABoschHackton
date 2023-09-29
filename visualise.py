import pandas as pd
import matplotlib.pyplot as plt

#Load filtered and normalized data
data = pd.read_excel('FilteredAndNormalizedData.xlsx', engine='openpyxl')

#Select relevant columns for visual
relevant_data = data[['FirstObjectDistance_X', 'FirstObjectDistance_Y', 'VehicleSpeed', 'Timestamp']]

#Calculate speed of the vehicle

time_interval = data['Timestamp'].diff() #Calculate time interval between timestampe
vehicle_speed = data['FirstObjectDistance_X'].diff() / time_interval

#Calculate longitudinal and alteral distances

longitudinal_distance = data['FirstObjectDistance_X'] - data['VehicleSpeed'] * time_interval
lateral_distance = data['FirstObjectDistance_Y']


#Create a figure and subplots for visualisation
fig , axs  =plt.subplots(4, 1, figsize=(10, 12))

#Plot vehicle and object positions
axs[0].plot(data['Timestamp'], data['FirstObjectDistance_X'], label='Object Position')
axs[0].plot(data['Timestamp'], data['VehicleSpeed'], label='Vehicle Position')
axs[0].set_xlabel('Timestamp')
axs[0].set_ylabel('Position')
axs[0].set_title('Vehicle and Object Positions')
axs[0].legend()

# Plot vehicle and object speeds
axs[1].plot(data['Timestamp'], vehicle_speed, label='Vehicle Speed')
axs[1].plot(data['Timestamp'], data['FirstObjectSpeed_X'], label='Object Speed')
axs[1].set_xlabel('Timestamp')
axs[1].set_ylabel('Speed (m/s)')
axs[1].set_title('Vehicle and Object Speeds')
axs[1].legend()

# Plot longitudinal distance
axs[2].plot(data['Timestamp'], longitudinal_distance)
axs[2].set_xlabel('Timestamp')
axs[2].set_ylabel('Longitudinal Distance (m)')
axs[2].set_title('Longitudinal Distance')

# Plot lateral distance
axs[3].plot(data['Timestamp'], lateral_distance)
axs[3].set_xlabel('Timestamp')
axs[3].set_ylabel('Lateral Distance (m)')
axs[3].set_title('Lateral Distance')

plt.tight_layout()
plt.show()
