import pandas as pd  # type: ignore
import numpy as np

numbers = [11,  22, 33, 44, 55, 66]
print(numbers)
series = pd.Series(numbers)
print(series, "\n")

numbers = [11,  22, 33.0, 44, 55, 66]
series = pd.Series(numbers)
print(series, "\n")
vals = series.values
print(vals, "\n")
index = series.index
print(index, "\n")
tail_n = series.tail(3)
print(tail_n, "\n")
head_n = series.head(3)
print(head_n, "\n")

des = series.describe()
print(des, "\n")

numbers = [11,  22, 33, 44, 55, 66, 22, 22, 33, 66, 66, 66]
series = pd.Series(numbers)
print(series, "\n")
uniq = series.unique()
print(uniq, "\n")

print(series.count(), "\n")
print(series.value_counts(), "\n")

s = pd.Series(np.linspace(0, 1, 5))
print(s, "\n")

d = {"a": 11, "b": 12, "c": 13, "g":14}
sd = pd.Series(d)
print(sd, "\n")
print(pd.Series(d, index=["a", "b", "c", "d"]))

s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
print(s, "\n")
print(s["b"], "\n")
print(s[["b", "d"]], "\n")
print(s[1:])
print(s + s)

data = [70, 20 ,30, 40, 50, 60]
ind = ["a", "b", "c", "d", "e", "f"]
series = pd.Series(data, index=ind)
print(series, "\n")
print(series[2:6], "\n")

filtered_series = series[series > 30]
print(filtered_series, "\n")

new = series.drop("d")
print(new, "\n")

series["b"] = 35
print(series, "\n")
series[1:4] = 0
print(series, "\n")

