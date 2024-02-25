from PIL import Image, ImageEnhance, ImageFilter

# загрузка изображения
image = Image.open("img.png")

# обрезка изображения
cropped_image = image.crop((0, 0, 300, 300))

# сохранение обрезанного изображения
cropped_image.save("cropped_image.jpg")

enhancer = ImageEnhance.Brightness(image)
bright_image = enhancer.enhance(1.5)

# сохранение увеличенного изображения
bright_image.save("bright_image.jpg")

# применение фильтра "Размытие"
blurred_image = image.filter(ImageFilter.BLUR)

# сохранение обработанного изображения
blurred_image.save("blurred_image.jpg")

