# TensorFlow – это мощный инструмент, который может использоваться для создания программ
# для решения широкого спектра задач машинного обучения. Он имеет множество возможностей
# и может быть использован для создания простых и сложных моделей машинного обучения.

# Вот пример простой линейной регрессии, который можно использовать для предсказания цены
# на жилье на основе количества комнат в доме:
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
# Создание набора данных для обучения модели
x = np.array([1, 2, 3, 4, 5, 6], dtype=np.float32)
y = np.array([100, 200, 300, 400, 500, 600], dtype=np.float32)
# Инициализация параметров модели
# Если же требуется объявить тензор с изменяемыми значениями, то для этого используется класс tf.Variable.
# Он имеет похожий набор параметров
w = tf.Variable(0.0)
b = tf.Variable(0.0)
# Определение функции потерь и оптимизатора
loss_fn = tf.keras.losses.mean_squared_error
optimizer = tf.keras.optimizers.SGD()
# Определение графа вычислений
# Tensorflow, использует частные производные, то есть, по сути, алгоритм градиентного спуска.
@tf.function
def train_step(X, y):
  with tf.GradientTape() as tape:
    y_pred = w * X + b
    loss = loss_fn(y, y_pred)
  gradients = tape.gradient(loss, [w, b])
  optimizer.apply_gradients(zip(gradients, [w, b]))
# Обучение модели
for epoch in range(50):
  train_step(x, y)
  print("Epoch: %d, Loss: %f" % (epoch, loss_fn(y, w*x + b)))
# Отображение результата
plt.plot(x, y, 'bo', label='Training data')
plt.plot(x, w*x + b, 'r-', label='Predictions')
plt.legend()
plt.show()
