#NumPy (Numerical Python) — это библиотека для языка Python,
# которая предоставляет многомерные массивы, матричные операции
# и функции для работы с ними. Она широко используется в научных и инженерных приложениях,
# а также в обработке данных и машинном обучении.
# Вместо обработки каждого пикселя изображения отдельно,
# мы можем использовать массивы NumPy, чтобы обработать всю картинку одновременно.
# Это может привести к значительному ускорению процесса обработки.

from PIL import Image
import numpy as np

# загрузка изображения
image = Image.open("img.png")

# преобразование в NumPy-массив
img_array = np.array(image)

# получение размера изображения
height, width, channels = img_array.shape

# преобразование в черно-белое
for i in range(height):
    for j in range(width):
        r, g, b = img_array[i, j]
        gray = (r + g + b) // 3
        img_array[i, j] = [gray, gray, gray]

# преобразование обратно в изображение и сохранение
gray_image = Image.fromarray(img_array)
gray_image.save("gray_image.jpg")
