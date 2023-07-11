import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import scipy.stats as sciStats
import statistics as stats
import numpy as np
import seaborn as sns

# Read the csv file
# For those whoever need to runs the code, please change the file location accordingly.

df1 = pd.read_csv('C:/Users/aleis/Desktop\School\Year 2 Sem 2\Physics Lab III/DataAnalysis/Calibration-for-T-P-InsidePipe-White.csv')
df2 = pd.read_csv('C:/Users/aleis/Desktop\School\Year 2 Sem 2\Physics Lab III/DataAnalysis/Calibration-for-T-P-InsidePipe-Yellow.csv')

# Clear the space between each string from csv file
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()


# Take the column of temperature and pressure from csv file
summary_stats_pressure_df1 = round(df1[["Pressure"]].describe(),3)
summary_stats_temperature_df1 = round(df1[["Temperature"]].describe(),3)

summary_stats_pressure_df2 = round(df2[["Pressure"]].describe(),3)
summary_stats_temperature_df2 = round(df2[["Temperature"]].describe(),3)

print(summary_stats_pressure_df1)
print(summary_stats_pressure_df2)
print(summary_stats_temperature_df1)
print(summary_stats_temperature_df2)

# Transform the string into float 
df1_pressure = (df1['Pressure'].astype(float))
df2_pressure = (df2['Pressure'].astype(float))
df1_temperature = (df1['Temperature'].astype(float))
df2_temperature = (df2['Temperature'].astype(float))

# Calculate the statistics parameter needed
mean_pressure_df1 = stats.mean(df1_pressure)
mean_pressure_df2 = stats.mean(df2_pressure)
mean_temperature_df1 = stats.mean(df1_temperature)
mean_temperature_df2 = stats.mean(df2_temperature)

std_pressure_df1 = stats.stdev(df1_pressure)
std_pressure_df2 = stats.stdev(df2_pressure)
std_temperature_df1 = stats.stdev(df1_temperature)
std_temperature_df2 = stats.stdev(df2_temperature)

# Plot histogram for Temperature
plt.subplot(1,2,1)
plt.hist(df1_temperature, bins = 10, alpha = 0.5, color='blue', label='Temperature')
plt.hist(df2_temperature, bins = 10, alpha = 0.5, color='green', label='Temperature')
plt.xlabel("Temperature ($^{o}C$)")
plt.ylabel("Counts of Data")
plt.title('Calibration of Temperature for Sensors', size = 14)
plt.legend(['Temperature for Sensor 1','Temperature for Sensor 2'],  loc='upper center')
plt.grid()


# Plot histogram for Pressure
plt.subplot(1,2,2)
plt.hist(df1_pressure, bins = 10, alpha = 0.5, color='blue', label='Pressure')
plt.hist(df2_pressure, bins = 10, alpha = 0.5, color='green', label='Pressure')
plt.xlabel("Pressure ($Pa$)")
plt.ylabel("Counts of Data")
plt.title('Calibration of Pressure for Sensors', size = 14)
plt.legend(['Pressure for Sensor 1','Pressure for Sensor 2'],  loc='upper center')
plt.grid()

plt.show()