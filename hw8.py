import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("Penguins Data.csv")

print(data.head())

print(data.info())

print(data.isnull().sum())

data = data.dropna()

sns.set_theme(style="white")

plt.scatter(data=data, x="Culmen Length (mm)", y="Body Mass (g)",)
plt.show()

plt.scatter(data=data, x="Culmen Depth (mm)", y="Body Mass (g)")
plt.show()

sns.pairplot(data=data, x_vars=["Culmen Length (mm)", "Culmen Depth (mm)"], y_vars=["Body Mass (g)"],  height=5, aspect=1)
plt.show()

data.plot.area(figsize=(8, 4), color="skyblue", alpha=0.5, legend=False)

plt.title("Culmen Length vs Body Mass")
plt.ylabel("Culmen Length (mm)")
plt.xlabel("Body Mass (g)")
plt.show()


print("i did this all by myself no chatgpt no copilot no google")