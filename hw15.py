import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('IMDB Dataset.csv')
print(data.head(3))

print(data.tail(3))
print(data.info())

print(data.isnull().sum())
subset = data.head(41-75)

print(subset)
print(data.loc[data["No_of_Votes"].No_of_Votes()])

sns.boxplot(x='Runtime', y='IMDB_Rating', data=data)
plt.figure(figsize=(10, 6))

sns.scatterplot(x='Runtime', y='IMDB_Rating', data=data)
plt.title('Relationship between Runtime and IMDB Rating')

plt.xlabel('Runtime (minutes)')
plt.ylabel('IMDB Rating')
plt.show()


plt.figure(figsize=(10, 6))
sns.histplot(data['Runtime'], kde=True, bins=30, color='peach')
plt.title('Distribution of Runtime')
plt.xlabel('Runtime (minutes)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data['IMDB_Rating'], kde=True, bins=30, color='pink')
plt.title('Distribution of IMDB Rating')
plt.xlabel('IMDB Rating')
plt.ylabel('Frequency')
plt.show()

sns.countplot(x="IMDB_Rating", y="No_of_Votes", data=data)