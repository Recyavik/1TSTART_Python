# Теперь попробуем перевести изображение в другое цветовое пространство, например, HSV. Для этого в OpenCV
# есть функция cv2.cvtColor(). Она принимает как минимум два параметра: исходное изображение и константу,
# указывающую, какое преобразование следует произвести. Эти константы начинаются с cv2.COLOR_ и содержат описание
# преобразования (например, cv2.COLOR_RGB2HLS).
#
# Важный момент: по умолчанию OpenCV использует цветовое пространство BGR, и изображения, захваченные с камеры,
# закодированы именно так. Следовательно, для перевода в пространство HSV надо использовать константу cv2.COLOR_BGR2HSV.

import cv2 # Импортируем библиотеку OpenCV для обработки изображений
import numpy as np # Импортируем библиотеку NumPy для работы с массивами данных

cap = cv2.VideoCapture(1) # Создаём объект захвата видео с камеры
while True: # Бесконечный цикл для обработки каждого кадра видео
   res, img = cap.read() # Считываем кадр из видеопотока
   cv2.imshow('image', img) # Отображаем захваченный кадр

   img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # Преобразуем цветовое пространство из RGB в HSV
   hue = img_hsv[:,:,0]  # Извлекаем канал оттенков изображения (хью)
   saturation = img_hsv[:,:,1]  # Извлекаем канал насыщенного изображения
   value = img_hsv[:,:,2] # Извлекаем канал яркости изображения
   cv2.imshow('hue', hue)  # Отображаем канал оттенка
   cv2.imshow('saturation', saturation) # Отображаем канал насыщенности
   cv2.imshow('value', value) # Отображаем канал яркости


   # Обработчик событий для выхода из цикла при нажатии клавиши "q".
   if cv2.waitKey(1) & 0xFF == ord('q'):
       break
# Для освобождения ресурсов камеры.
cap.release()

# Для закрытия всех окон OpenCV при завершении программы.
cv2.destroyAllWindows()

