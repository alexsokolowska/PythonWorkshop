#Go to https://climate.nasa.gov/vital-signs/global-temperature/ and download the data. Save it in the .txt format. 
#Import all necessary libraries (numpy, matplotlib.pyplot, etc.).
import numpy as np, matplotlib.pyplot as plt

#Load and name each column of the file in your program. Use np.genfromtxt as in the example above.
data = np.genfromtxt("NASA_data.txt", names = ["year", "annual_mean", "fiveyr_mean"])

#Plot the data (x axis: years, y axis: temperature change).
plt.plot(data['year'], data['annual_mean'], color='red', marker='o', label="Annual mean")
plt.plot(data['year'], data['fiveyr_mean'], color='gray', marker='x', label="Five year mean")

#Label the axes. Add a legend.
plt.xlabel("Year")
plt.ylabel("Temperature anomaly (C)")
plt.legend(frameon=False, loc=2)
#Save your figure (look up online how to use plt.savefig).

plt.savefig("./NASA_temperature_anomaly.pdf")
#Now, edit the program to use functions. Write a function plot_data(data) that will do all instructions from (4):(6) when called on data.

def plot_data(data):
    """ this program will do all plots on the called data"""
    
    plt.plot(data['year'], data['annual_mean'], color='red', marker='o', label="Annual mean")
    plt.plot(data['year'], data['fiveyr_mean'], color='gray', marker='x', label="Five year mean")

    plt.xlabel("Year")
    plt.ylabel("Temperature anomaly (C)")
    plt.legend(frameon=False)
    plt.savefig("./NASA_temperature_anomaly.pdf")