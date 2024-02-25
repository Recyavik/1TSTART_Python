from PIL import Image

# загрузка изображений
image1 = Image.open("img.png")
image2 = Image.open("elephant.png")

# создание нового изображения с размером обоих исходных изображений
new_image = Image.new("RGB", (image1.width + image2.width, image1.height))

# добавление первого изображения на новое изображение
new_image.paste(image1, (0, 0))

# добавление второго изображения на новое изображение
new_image.paste(image2, (image1.width, 0))

# сохранение нового изображения
new_image.save("merged_image.jpg") 
