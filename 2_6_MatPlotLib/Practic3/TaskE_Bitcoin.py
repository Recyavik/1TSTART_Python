# https://www.blockchain.com/explorer/charts/price-market/

import matplotlib.pyplot as plt
import json
from datetime import datetime

# За представление структурированных данных на основе синтаксиса JavaScript отвечает стандартный текстовый формат
# под названием JSON, аббревиатура которого расшифровывается как JavaScript Object Notation.
# Многие среды разработки отлично справляются с его чтением и генерированием.
# JSON находится в состоянии строки, поэтому позволяет передавать информацию по сети.
# JSON обладает рядом преимуществ, которые и сделали его популярным:
# # Не занимает много места, является компактным в написании и быстро компилируется.
# # Создание текстового содержимого понятно человеку, просто в реализации,
# а чтение со стороны среды разработки не вызывает никаких проблем. Чтение может осуществляться и человеком, поскольку ничего сложного в представлении данных нет.
# # Структура преобразуется для чтения на любых языках программирования.
# # Практически все языки имеют соответствующие библиотеки или другие инструменты для чтения данных JSON.


def get_data_plot():
    with open("price-market.json") as file:
        data = json.load(file)
        return data


# Структура данных похожа на словарь
# x формат даты в Utc формате
# y стоимость биткоина


def data_plot():
    data = get_data_plot()
    x_list = list()
    y_list = list()
    count = 0
    for item in data.values():
        for el in item:
            if isinstance(el, dict):
                sec = int(el["x"] / 1000)
                data_obj = datetime.fromtimestamp(sec).strftime("%Y-%m-%d")
                x_list.append(data_obj)
                y_list.append(el["y"])
    return x_list, y_list


plt.title(
    "График рыночной стоимости BitCoin", fontsize=14, fontweight="bold", color="blue"
)
plt.xlabel("Период", fontsize=12, color="black")
plt.ylabel("Рыночная стоимость", fontsize=12, color="black")

x, y = data_plot()
plt.plot(x, y, label="Рыночная стоимость")
# plt.legend()
plt.grid()
plt.show()
