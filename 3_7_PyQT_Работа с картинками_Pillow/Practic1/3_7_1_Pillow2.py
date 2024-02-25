from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PIL import Image

app = QApplication([])
window = QWidget()
window.setGeometry(100, 100, 590, 500)

# загружаем изображение с помощью библиотеки Pillow
img = Image.open('img.png')
resized_img = img.resize((300, 400))

resized_img.save('resized_image.jpg')

# изменяем цветовую палитру изображения
bw_img = img.convert('L')

# сохраняем измененное изображение в файл
bw_img.save('bw_image.jpg')
