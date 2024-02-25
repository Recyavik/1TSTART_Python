# Загрузка нейронной сети в проект
from tensorflow import keras
# Библиотека векторов
import numpy as np
# Вывод на экран результата
import matplotlib.pyplot as plt
# Загрузка и подготовка данных

(X_train, y_train), (X_test, y_test) = keras.datasets.cifar10.load_data()
class_names = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0
y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

# Создание модели
model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), padding="same", activation="relu", input_shape=(32, 32, 3)),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), padding="same", activation="relu"),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(128, (3, 3), padding="same", activation="relu"),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

# Компиляция модели
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# Обучение модели
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Оценка производительности
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
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
predictions = model.predict(X_test)
predictions_classes = np.argmax(predictions, axis=1)

# Визуализация нескольких тестовых изображений и предсказанных классов
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(X_test[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[predictions_classes[i]])
plt.show()
