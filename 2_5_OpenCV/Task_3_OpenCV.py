# pip install opencv-python

import cv2
import numpy as np

img = cv2.imread("py.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
# В медианном размытии центральный пиксель изображения заменяется медианой всех пикселей в области ядра,
# в результате чего это размытие наиболее эффективно при удалении шума в стиле «соли».
# Для того, чтобы применить данный вид размытия, необходимо вызвать функцию medianBlur() и передать туда
# два параметра: изображение и размер ядра:
img_median = cv2.medianBlur(img_gray, 5)



cv2.imshow("Original", img)
cv2.imshow("Gray", img_gray)
cv2.imshow("Median", img_median)
cv2.imwrite("Median_py.jpg", img_median)
cv2.waitKey(0)
cv2.destroyAllWindows()