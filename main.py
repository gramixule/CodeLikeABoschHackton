import pandas as pd


# Load EXCEL
data = pd.read_excel('DevelopmentData.xlsx', engine='openpyxl')



# Define the normalization factor
distance_factor = 128.0 # Convert ObjectDistance from arbitrary units to m
speed_factor = 256.0 # conver speed to m/s

#Normalize ObjectDistance (X and Y columns)

data['FirstObjectDistance_X'] /= distance_factor
data['FirstObjectDistance_Y'] /= distance_factor
data['SecondObjectDistance_X'] /= distance_factor
data['SecondObjectDistance_Y'] /= distance_factor
data['ThirdObjectDistance_X'] /= distance_factor
data['ThirdObjectDistance_Y'] /= distance_factor
data['FourthObjectDistance_X'] /= distance_factor
data['FourthObjectDistance_Y'] /= distance_factor

# Normalize VehicleSpeed

data['VehicleSpeed'] /= speed_factor

# Normalize ObjectSpeeds (X and Y columns)
data['FirstObjectSpeed_X'] /= speed_factor
data['FirstObjectSpeed_Y'] /= speed_factor
data['SecondObjectSpeed_X'] /= speed_factor
data['SecondObjectSpeed_Y'] /= speed_factor
data['ThirdObjectSpeed_X'] /= speed_factor
data['ThirdObjectSpeed_Y'] /= speed_factor
data['FourthObjectSpeed_X'] /= speed_factor
data['FourthObjectSpeed_Y'] /= speed_factor

#First collumn remove in new doc
if 'Unnamed: 0' in data.columns:
    data = data.drop(columns=['Unnamed: 0'])

# Export the filtered and normalized data to a new Excel file
data.to_excel('FilteredAndNormalizedData.xlsx', index=False, engine='openpyxl')




'''
You have to normalize the values: 
    ObjectDistance(X,Y) -> divide by 128 -> untill will be [m]
    VehicleSpeed -> divide by 256 -> unit will be [m/s]
    ObjectSpeeds(X,Y) -> divide by 256 -> unit will be [m/s]

'''

