# Создайте DataFrame структуру библиотеки Pandas для словаря фигур представленного ниже примера.
# Удалите дубликаты фигур по названию и сохраните таблицу в двух форматах csv и excel.
# Увеличьте размер каждой фигуры в 2 раза и пересчитайте периметр.

import pandas as pd

shape = ({ "Фигура": ["Круг", "Квадрат", "Треугольник", "Квадрат"],
   "Цвет": ['red', 'green', 'blue', 'red'], "Размер": [50, 40, 60, 70], "Периметр": [314.16, 160, 180, 210]})

df_shape = pd.DataFrame(shape)
print(df_shape)
print("-------------------------------------")

df_shape.drop_duplicates(subset=["Фигура"], inplace=True)
print(df_shape)
print("-------------------------------------")

df_shape.to_excel("figures.xlsx", sheet_name="Фигуры DataFrame", index=False)
df_shape.to_csv("figures.csv", index=False)
df_shape['Размер'] = df_shape['Размер'] * 2
df_shape["Периметр"] = df_shape["Периметр"].apply(lambda x: x * 2)
print(df_shape)
