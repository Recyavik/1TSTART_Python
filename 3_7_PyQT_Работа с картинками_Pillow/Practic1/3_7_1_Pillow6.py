from PIL import Image
import os

# создание списка изображений
image_list = ["img_1.png", "img_2.png", "img_3.png", "img_4.png"]

# создание папки для хранения уменьшенных копий изображений
if not os.path.exists("thumbnails"):
    os.makedirs("thumbnails")

# изменение размеров и сохранение уменьшенных копий изображений
for image_file in image_list:
    # загрузка изображения
    image = Image.open(image_file)

    # изменение размера изображения
    size = 128, 128
    image.thumbnail(size)

    # сохранение уменьшенной копии изображения
    thumb_file = os.path.join("thumbnails", image_file)
    image.save(thumb_file, "JPEG")

    # отображение уменьшенной копии изображения
    image.show()
