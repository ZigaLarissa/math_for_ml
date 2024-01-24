# prerequisite package imports

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# load the dataset into a pandas dataframe

df = pd.read_csv("fuel_econ.csv")
ten_rows = df.head(10)
# print the first 10 rows
print(ten_rows)


# HISTOGRAM DEPICTING DISTRIBUTION OF CO2
carbon = df['co2']
plt.xlabel('CO2 Distribution')
plt.ylabel('Frequency')
plt.title('CO2 Distribution Vs Frequency Histogram')

plt.hist(carbon, bins=20, edgecolor='black')
plt.show()


# HISTOGRAM DEPICTING CAR BRANDS WORKED ON
brands = df['make']
plt.xlabel('Car Brands')
plt.ylabel('Frequency')
plt.title('CAR BRANDS DEPICTION HISTOGRAM')

plt.hist(brands, bins=5, range=[0, 5], color='m', edgecolor='white')
plt.show()


# HISTOGRAM DEPICTING FUEL EFFICIENCY SCORE
fuel = df['feScore']
plt.xlabel('Fuel Efficiency Score')
plt.ylabel('Frequency')
plt.title('FUEL EFFICIENCY Vs Frequency Histogram')

plt.grid('True')
plt.hist(carbon, bins=100, color='yellow')
plt.show()


# CREATE THE SAME HEATMAP AS THE ONE PROVIDED IN THE ASSIGNMENT
data = df.drop(['make', 'model', 'VClass', 'drive', 'trans', 'fuelType'], axis=1)
heat_map = data.corr()
axis_corr = sns.heatmap(heat_map, vmin=-1, vmax=1, center=0, cmap = sns.diverging_palette(20, 220, n=500), square=True)
plt.show()