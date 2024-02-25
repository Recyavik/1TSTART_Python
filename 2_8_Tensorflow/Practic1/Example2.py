import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6], dtype=np.float32)
y = np.array([120, 340, 380, 400, 500, 600], dtype=np.float32)

w = tf.Variable(0.0)
b = tf.Variable(0.0)

loss_fn = tf.keras.losses.mean_squared_error
optimizer = tf.keras.optimizers.SGD()

@tf.function
def train_step(X, y):
  with tf.GradientTape() as tape:
    y_pred = w * X + b
    loss = loss_fn(y, y_pred)
  gradients = tape.gradient(loss, [w, b])
  optimizer.apply_gradients(zip(gradients, [w, b]))

for epoch in range(50):
  train_step(x, y)
  print("Эпоха: %d, Потери: %f" % (epoch, loss_fn(y, w*x + b)))

plt.plot(x,y, 'bo', label='Тренировочные данные')
plt.plot(x, w * x + b, 'r-', label='Предсказание')
plt.legend()
plt.show()

