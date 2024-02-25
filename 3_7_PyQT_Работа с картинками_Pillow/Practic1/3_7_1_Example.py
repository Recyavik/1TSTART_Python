from PIL import Image
import numpy as np


image = Image.open("img.png")

image_array = np.array(image)

height, width, channels = image_array.shape

for i in range(height):
    for j in range(width):
        r, g, b = image_array[i,j]
        gray = (r + g + b) // 3
        image_array[i,j] = [gray, gray, gray]

gray_image = Image.fromarray(image_array)
gray_image.save("gray_array.png")