# pip install opencv-python

import cv2
import numpy as np

img = cv2.imread("py.png")
img_scaled = cv2.resize(img, None, fx=0.5, fy=0.5)
kernel = np.ones((5, 5), np.uint8) # Эрозия
# Эрозия и дилатация являются операциями морфологической обработки изображения и предназначены в OpenCV
# для размывания и расширения изображений.
#
# Морфологическая обработка OpenCV — это процедура изменения геометрической структуры изображения.
# Мы находим форму и размер или структуру объекта. Обе операции определены для бинарных изображений,
# но мы также можем использовать их для изображения в градациях серого.
# Они широко используются следующим образом:
erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)


cv2.imshow("Original", img)
cv2.imshow("Scale", img_scaled)
cv2.imshow("Erosion", erosion)
cv2.imshow("Delatation", dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()