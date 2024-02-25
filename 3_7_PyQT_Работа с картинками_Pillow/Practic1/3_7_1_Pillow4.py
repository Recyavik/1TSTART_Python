from PIL import Image, ImageDraw

# загрузка изображения
image = Image.open("img.png")

# создание объекта ImageDraw
draw = ImageDraw.Draw(image)

# рисование красной линии
draw.line((0, 0, image.size[0], image.size[1]), fill=(255, 0, 0), width=5)

# сохранение обработанного изображения
image.save("drawn_image.jpg") 
