import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("FuelConsumption.csv")

print(data.head())

print(data.info())

print(data.isnull().sum())

data = data.dropna()

print(data["FUELTYPE"].value_counts())

sns.set_theme(style="white")

sns.countplot(data=data, x="FUELTYPE", color="blue")

plt.title("Vehicle Count by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Number of Vehicles")

plt.xticks(rotation=30)

sns.despine()

plt.show()