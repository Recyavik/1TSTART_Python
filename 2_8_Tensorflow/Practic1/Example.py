"""
https://pypi.org/project/tensorflow/#files

python.exe -m pip install --upgrade pip
pip install tensorflow
pip install keras-core
pip install keras-nightly
pip install neptune-tensorflow-keras

""" #

import tensorflow as tf
print(tf.__version__)

from tensorflow import keras
import  numpy as np
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(32, 32, 3)),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(128, (3, 3), padding='same', activation='relu'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print('Тест точности', test_acc)
plt.plot(history.history['accuracy'], label='Точность')
plt.plot(history.history['val_accuracy'], label='Точность значений')
plt.xlabel('Эпоки')
plt.ylabel('Точность')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')
plt.show()

predictions = model.predict(x_test)
predicted_classes = np.argmax(predictions, axis=1)
# Визуализация нескольких тестовых изображений и предсказанных классов
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_test[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[predicted_classes[i]])
plt.show()

