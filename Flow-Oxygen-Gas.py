import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import scipy.stats as sciStats
import statistics as stats
import numpy as np
import seaborn as sns

# Read the csv file
# For those whoever need to runs the code, please change the file location accordingly.

df1 = pd.read_csv('C:/Users/aleis/Desktop\School\Year 2 Sem 2\Physics Lab III/DataAnalysis/Flow_Oxygen_Trial_5.csv')


# create figure and axis objects with subplots()
fig,ax = plt.subplots()

lns1 = plt.plot(df1['Time'], df1['Temperature'], 'orange', linewidth = 2,marker = 'o', markersize = '5', 
                markerfacecolor = 'cyan', mec = 'c', label = "Temperature")
plt.xlabel('Time (s)', size = 14)
plt.ylabel('Temperature ($^{o}C$)', size = 14)
plt.title('Temperature ($^{o}C$) and Pressure (Pa) vs Time (s) for flowing oxygen gas', size = 14)
plt.grid()

ax2 = ax.twinx()


lns2 = plt.plot(df1['Time'], df1['Pressure'], linewidth = 2, marker = 'x', markersize = '7',
                 markerfacecolor = 'black', mec = 'k', label = "Pressure")
plt.ylabel('Pressure (Pa)', size = 14)


# Adjust the graph
lns = lns1 + lns2 
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=9)

plt.grid()
plt.show()