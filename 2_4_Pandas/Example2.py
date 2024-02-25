import pandas as pd
import numpy as np

coding = "utf-8"


array = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
df = pd.DataFrame(array, columns=["A", "B", "C"])
print(df, "\n")
print(df.index, "\n")
print(df.columns, "\n")

data = {"name": ["Tanya", "Andrei", "Misha"],
        "age": [25, 30, 35],
        "city": ["Moscow", "Irkutsk", "Sochi"]}
df = pd.DataFrame(data)
print(df, "\n")
print(df["name"], "\n")
print(df.age, "\n")
print(df.loc[1], "\n")
print(df.loc[1, "city"], "\n")
print(df.iloc[0, 1], "\n")

fil = df[df["age"] >= 30]
print(fil, "\n")

df["city"] = "Владивосток"
print(df, "\n")
df.loc[1, "age"] = 31
print(df, "\n")

df.drop("age", axis=1, inplace=True)
print(df, "\n")

df.drop(0, inplace=True)
print(df, "\n")

data = {"name": ["Tanya", "Andrei", None, "Misha"],
        "age": [25, None, 30, 35],
        "city": ["Moscow", "Irkutsk", "Sochi", "Sochi"]}
df = pd.DataFrame(data)
print(df, "\n")

df["age"].fillna(df["age"].mean(), inplace=True)
grouped = df.groupby("city")
print(df, "\n")

print(grouped.describe())
