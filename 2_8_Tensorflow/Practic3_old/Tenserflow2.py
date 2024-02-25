import tensorflow as tf
# Загрузка нейронной сети в проект
from tensorflow import keras
# Вывод на экран результата
import matplotlib.pyplot as plt


# Загрузка и подготовка данных
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0
y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

# Создание модели
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

# Компиляция модели
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# Обучение модели
history = model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# Построение графиков производительности
plt.plot(history.history["accuracy"], label="accuracy")
plt.plot(history.history["val_accuracy"], label="val_accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.show()

# Оценка производительности
test_loss, test_acc = model.evaluate(x_test, y_test)
print("Test accuracy:", test_acc)

# Распознавание цифр
predictions = model.predict(x_test)
for i in range(10):
    plt.imshow(x_test[i], cmap="gray")
    plt.title("Predicted: "+str(tf.argmax(predictions[i])))
    plt.show()


