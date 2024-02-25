# TensorFlow является одной из наиболее популярных и широко используемых библиотек машинного обучения.
# Она используется во многих областях, включая компьютерное зрение, обработку естественного языка, р
# екомендательные системы и другие.

# Keras является высокоуровневым API, построенным на TensorFlow,
# который позволяет быстро создавать и обучать модели машинного обучения,
# особенно для задач обработки изображений, звука и текста.

# python.exe -m pip install --upgrade pip
# pip install tensorflow
# pip install keras-core
# pip install keras-nightly
# pip install neptune-tensorflow-keras
# https://pypi.org/project/tensorflow/#files

import tensorflow as tf

print(tf.__version__)

from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Загрузка и подготовка данных
# Загружаем модель 70 000 изображений 60 000 тренировок и 10 000 тестов
(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
class_names = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
]
# Нормализация данных (упрощение и сведение к одному диапазону от 0 до 1 и от -1 до 1 сводим к диапазону от 0 до 1)
# Это сделано для того, чтобы помочь с масштабом математики, участвующей в создании прогноза для каждого изображения.
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0
# Классифицируем по категориям
y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)
# Создание модели
model = keras.Sequential(
    [
        # Используем сверточный слой нейройной сети с процентом штрафа на каждом уровне с размерами 32 * 32
        # Чтобы размерность карты после свертки оставалась той-же, добавляют padding: матрицу
        keras.layers.Conv2D(
            32, (3, 3), padding="same", activation="relu", input_shape=(32, 32, 3)
        ),
        # Уменьшаем масштаб в 2 раза
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), padding="same", activation="relu"),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(128, (3, 3), padding="same", activation="relu"),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Flatten(),
        # Другой вид слоя, который мы видим в модели, создан с использованием tf.keras.layers.Dense()который создает то,
        # что называется полностью связанным или плотно связанным слоем. Это можно сравнить с разреженным слоем,
        # и различие связано с тем, как информация передается между узлами в соседних слоях.
        # Здесь одна распространенная функция активации, и та, которая используется во случае Dense(),
        # называется «softmax».
        keras.layers.Dense(128, activation="relu"),
        keras.layers.Dense(10, activation="softmax")
        # Softmax берет логиты, вычисленные по взвешенной сумме активаций из предыдущего слоя,
        # и преобразует их в вероятности, которые составляют 1,0. Это делает его чрезвычайно полезной функцией
        # активации для использования в нашем выходном слое, поскольку она обеспечивает легко интерпретируемые результаты
    ]
)

# Компиляция модели
# Теперь, когда мы определили, как выглядит наша нейронная сеть,
# следующий шаг - рассказать Tensorflow, как ее тренировать.
# Компиляция модели (оптимизация функции потерь (насколько нейронка была менее точной предыдущей модели)
# Укажем конфигурацию обучения (оптимизатор, функция потерь, метрики)
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
# Определили метрику точности "accuracy"
# optimizer="Adam" - среднеквадратичное распределение
# Это важные особенности того, как нейронная сеть дает свои окончательные прогнозы.

# Наконец-то наступает время обучения модели, и с TensorFlow 2.0 это очень легко сделать.
history = model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))
# Эта строка кода довольно интуитивно понятна, она передает обучающие данные и правильные метки этих данных.
# Параметр эпохи в model.fit()функция - это количество раз, которое модель видит все данных обучения.
# Причина, по которой мы хотим, чтобы модель видела все обучающие данные несколько раз, состоит в том,
# что одного проходного действия может быть недостаточно для того, чтобы модель достаточно обновляла свои веса
# при вычислении взвешенных сумм для заметного улучшения предсказательной силы.

# Оценка производительности модели на тестовых данных
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print("Test accuracy:", test_acc)
# Построение графиков производительности
plt.plot(history.history["accuracy"], label="accuracy")
plt.plot(history.history["val_accuracy"], label="val_accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.ylim([0.5, 1])
plt.legend(loc="lower right")
plt.show()
# Предсказание классов для тестовых изображений
predictions = model.predict(x_test)
predicted_classes = np.argmax(predictions, axis=1)
# Визуализация нескольких тестовых изображений и предсказанных классов
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_test[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[predicted_classes[i]])
plt.show()

# Этот пример использует набор данных CIFAR-10, который состоит из 60 000 изображений размером 32x32 пикселя,
# разделенных на 10 классов. Модель состоит из нескольких сверточных слоев и полносвязных слоев,
# и обучается на тренировочных данных в течение 10 эпох.
