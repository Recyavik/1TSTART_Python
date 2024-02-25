# Matplotlib также поддерживает использование функционального интерфейса и объектно-ориентированного
# интерфейса для работы с данными Pandas. Вы можете использовать методы Pandas,
# такие как plot(), scatter(), для создания графиков непосредственно из DataFrame.
import matplotlib.pyplot as plt
import pandas as pd
# Создаем DataFrame из словаря
data = {'x': [1, 2, 3, 4, 5], 'y': [5, 2, 8, 3, 12]}
df = pd.DataFrame(data)
# Создаем график
plt.plot(df['x'], df['y'])
# Отображаем график
plt.show()

