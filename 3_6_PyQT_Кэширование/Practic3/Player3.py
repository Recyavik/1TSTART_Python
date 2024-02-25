# Класс QGraphicsScene предоставляет поверхность
# для управления большим количеством 2D-графических элементов.
#
# Он используется вместе с QGraphicsView
# для визуализации графических элементов на 2D-поверхности.
import sys
from PyQt5.QtCore import Qt, QUrl, QDir
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QGridLayout,
    QFrame, QGraphicsDropShadowEffect, QGraphicsView, QGraphicsScene, QLabel,
    QPushButton, QHBoxLayout, QListWidget, QFileDialog)

from PyQt5.QtGui import QGradient, QFont, QColor, QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist, QMediaMetaData


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt Музыкальный плейер')

        # Создание контейнеров
        btn_box = QHBoxLayout()
        btn_box2 = QHBoxLayout()
        container = QGridLayout()
        info_container = QGridLayout()
        frame = QFrame()
        frame.setFrameShape(QFrame.Box)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setLayout(info_container)

        # Создание переменных проигрывателя
        self.dir = f'{QDir.currentPath()}'
        self.url = QUrl()
        self.player = QMediaPlayer()
        self.content = QMediaContent()
        self.playlist = QMediaPlaylist(self.player)
        self.player.setPlaylist(self.playlist)

        # Используется для изменения, чтобы уведомить self.update о том,
        # что индекс списка воспроизведения изменился.
        # Обновит выделенную строку в списке
        self.playlist.currentIndexChanged.connect(self.update)

        # Сигнализирует о том, что метаданные изменились
        self.player.metaDataChanged.connect(self.meta_data)

        # Метки для информации о треке
        self.artist = QLabel('Артист: ')
        self.album_title = QLabel('Альбом: ')
        self.track_title = QLabel('Трек: ')
        self.released = QLabel('Версия: ')
        self.genre = QLabel('Жанр: ')
        self.art = QLabel()

        # Добавляем информацию о треке в информационный контейнер
        info_container.addWidget(self.artist, 0, 0, 1, 1)
        info_container.addWidget(self.album_title, 1, 0, 1, 1)
        info_container.addWidget(self.track_title, 2, 0, 1, 1)
        info_container.addWidget(self.released, 3, 0, 1, 1)
        info_container.addWidget(self.genre, 4, 0, 1, 1)
        info_container.addWidget(self.art, 5, 0, 1, 1)

        # Создание метки статуса трека
        self.status = QLabel('Статус: ')
        self.status.setFrameShape(QFrame.Box)
        self.status.setFrameShadow(QFrame.Sunken)

        self.track = QLabel('Трек: ')
        self.track.setFrameShape(QFrame.Box)
        self.track.setFrameShadow(QFrame.Sunken)

        # Определяем и создаём поле списка
        self.music_list = QListWidget()
        self.music_list.setFrameShape(QFrame.Box)
        self.music_list.setFrameShadow(QFrame.Sunken)
        self.music_list.setStyleSheet('background-color: snow;')

        # Воспроизведение трека при двойном щелчке
        self.music_list.itemDoubleClicked.connect(self.my_doubleclick)

        # Создание стилей кнопок
        btn_style = '''QPushButton{background-color: Thistle;}
                       QPushButton:hover{background-color: SandyBrown; color: Indigo; \
                       font-weight: bold;}'''

        # Создание кнопки для получения аудиофайлов и очистки списка воспроизведения
        file_btn = QPushButton('Добавить')
        file_btn.released.connect(self.my_files)
        file_btn.setCursor(Qt.PointingHandCursor)
        file_btn.setStyleSheet(btn_style)
        file_btn.setMaximumWidth(100)

        clear_btn = QPushButton('Очистить список')
        clear_btn.released.connect(self.my_clear)
        clear_btn.setCursor(Qt.PointingHandCursor)
        clear_btn.setStyleSheet(btn_style)
        clear_btn.setMaximumWidth(150)

        # Создание кнопок
        self.play_btn = QPushButton('Пуск')
        self.play_btn.released.connect(self.my_state)
        self.play_btn.setCursor(Qt.PointingHandCursor)
        self.play_btn.setStyleSheet(btn_style)

        self.prev_btn = QPushButton('Предыдущий')
        self.prev_btn.released.connect(self.my_prev)
        self.prev_btn.setCursor(Qt.PointingHandCursor)
        self.prev_btn.setStyleSheet(btn_style)

        self.next_btn = QPushButton('Следующий')
        self.next_btn.released.connect(self.my_next)
        self.next_btn.setCursor(Qt.PointingHandCursor)
        self.next_btn.setStyleSheet(btn_style)

        self.stop_btn = QPushButton('Стоп')
        self.stop_btn.released.connect(self.my_stop)
        self.stop_btn.setCursor(Qt.PointingHandCursor)
        self.stop_btn.setStyleSheet(btn_style)

        self.exit_btn = QPushButton('Выход')
        self.exit_btn.released.connect(sys.exit)
        self.exit_btn.setCursor(Qt.PointingHandCursor)
        self.exit_btn.setStyleSheet('QPushButton{background-color: firebrick;} \
                                    QPushButton:hover{background-color: DarkMagenta;'
                                    'color: white; font-weight: bold;}')

        # Добавить кнопки в макет
        btn_box.addWidget(file_btn)
        btn_box.addWidget(clear_btn)
        btn_box2.addWidget(self.play_btn)
        btn_box2.addWidget(self.prev_btn)
        btn_box2.addWidget(self.next_btn)
        btn_box2.addWidget(self.stop_btn)
        btn_box2.addWidget(self.exit_btn)

        # Добавить макет в контейнер макетов
        container.addWidget(self.my_header_footer(100, 100,
                                24,'МОЯ МУЗЫКА C PYQT'), 0, 0, 1, 3)
        container.addWidget(self.status, 1, 0, 1, 1)
        container.addWidget(self.track, 1, 1, 1, 1)
        container.addLayout(btn_box, 1, 2, 1, 1)
        container.addWidget(frame, 2, 0, 2, 1)
        container.addWidget(self.music_list, 2, 1, 1, 2)
        container.addLayout(btn_box2, 3, 1, 1, 2)
        container.addWidget(self.my_header_footer(40, 40,
        12, '1T Музыкальный проигрыватель на курсе НЕЙРО.PY'), 4, 0, 1, 3)

        # Создание виджета и добавление главного контейнера макетов
        widget = QWidget()
        widget.setLayout(container)
        self.setCentralWidget(widget)

    # Получить метаданные из музыкального файла
    def meta_data(self):
        if self.player.isMetaDataAvailable():
            self.artist.setText(f'Артист: {self.player.metaData(QMediaMetaData.AlbumArtist)}')
            self.album_title.setText(f'Альбом: {self.player.metaData(QMediaMetaData.AlbumTitle)}')
            self.track_title.setText(f'Трек: {self.player.metaData(QMediaMetaData.Title)}')
            self.released.setText(f'Версия: {self.player.metaData(QMediaMetaData.Year)}')
            self.genre.setText(f'Жанр: {self.player.metaData(QMediaMetaData.Genre)}')
            self.track.setText(f'Трек: {self.player.metaData(QMediaMetaData.Title)}')
            pixmap = QPixmap(self.player.metaData(QMediaMetaData.CoverArtImage))
            pixmap = pixmap.scaled(int(pixmap.width() / 3), int(pixmap.height() / 3))
            self.art.setPixmap(pixmap)

    # Создание заголовка
    def my_header_footer(self, minheight, maxheight, fontsize, text):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(3)
        shadow.setOffset(3, 3)

        scene = QGraphicsScene()

        view = QGraphicsView()
        view.setMinimumSize(1000, minheight)
        view.setMaximumHeight(maxheight)
        view.setScene(scene)

        gradient = QGradient(QGradient.RichMetal)

        scene.setBackgroundBrush(gradient)

        font = QFont('Calibri', fontsize, QFont.Bold)

        text = scene.addText(text)
        text.setDefaultTextColor(QColor(0, 255, 128))
        text.setFont(font)

        text.setGraphicsEffect(shadow)

        return view

    # Метод двойного нажатия на Пуск
    def my_doubleclick(self):
        self.playlist.setCurrentIndex(self.music_list.currentRow())
        self.player.play()

    # Метод очистки списка треков
    def my_clear(self):
        self.player.stop()
        self.music_list.clear()
        self.playlist.clear()
        self.play_btn.setText('Пуск')
        self.status.setText('Статус: ')
        self.track.setText('Трек: ')
        self.artist.setText('Артист: ')
        self.album_title.setText('Альбом: ')
        self.track_title.setText('Трек: ')
        self.released.setText('Релиз: ')
        self.genre.setText('Жанр: ')
        pixmap = QPixmap()
        self.art.setPixmap(pixmap)

    # Метод добавления треков в плейлист
    def my_files(self):
        files = QFileDialog.getOpenFileNames(None, 'Добавить аудиофайлы',
                                             filter='Форматы аудио файлов (*.mp3 *.ogg *.wav)')

        for file in files[0]:
            self.playlist.addMedia(QMediaContent(self.url.fromLocalFile(file)))
            file = file.split('/')
            self.music_list.addItem(f'{file[-1][:-4]}')

        self.music_list.setCurrentRow(0)
        self.playlist.setCurrentIndex(0)

    # Методы контроля клавиш проигрывателя
    def my_prev(self):
        if self.playlist.previousIndex() == -1:
            self.playlist.setCurrentIndex(self.playlist.mediaCount() - 1)
        else:
            self.playlist.previous()

    def my_next(self):
        self.playlist.next()
        if self.playlist.currentIndex() == -1:
            self.playlist.setCurrentIndex(0)
            self.player.play()

    def my_stop(self):
        self.player.stop()
        self.play_btn.setText('Пуск')
        self.playlist.setCurrentIndex(0)
        self.music_list.setCurrentRow(0)
        self.status.setText('Статус: Остановлен')

    def my_state(self):
        if self.playlist.mediaCount() > 0:
            if self.player.state() != QMediaPlayer.PlayingState:
                self.play_btn.setText('Пауза')
                self.status.setText('Статус: Воспроизведение')
                self.player.play()
            else:
                self.play_btn.setText('Пуск')
                self.player.pause()
                self.status.setText('Статус: Пауза')

    # Методы для обновления плейлиста и листбокса
    def update(self):
        self.music_list.setCurrentRow(self.playlist.currentIndex())
        if self.playlist.currentIndex() < 0:
            self.music_list.setCurrentRow(0)
            self.playlist.setCurrentIndex(0)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()