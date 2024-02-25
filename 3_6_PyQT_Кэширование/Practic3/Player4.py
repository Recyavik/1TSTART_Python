from functools import partial
import os
import sys
import mutagen
from PyQt5.QtCore import Qt, QUrl, QDir
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, \
    QFrame, QGraphicsDropShadowEffect, QGraphicsView, QGraphicsScene, QLabel, \
    QPushButton, QHBoxLayout, QStyle, QListWidget, QFileDialog, QSlider, QVBoxLayout, QDial
from PyQt5.QtGui import QGradient, QFont, QColor, QCursor, QIcon, QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist, \
    QMediaMetaData


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('PyQt5 Music Player')

        # Create some variables
        self.url = QUrl()
        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist(self.player)
        self.player.setPlaylist(self.playlist)

        # Create the status and track labels
        common_style = '''
                        font-weight: bold;
                        font-size: 10pt;
                       '''
        self.status = QLabel('Status: Now Stopped')
        self.status.setStyleSheet(common_style)
        self.status.setFrameShape(QFrame.Box)
        self.status.setFrameShadow(QFrame.Sunken)

        self.track = QLabel('Track: ')
        self.track.setStyleSheet(common_style)
        self.track.setFrameShape(QFrame.Box)
        self.track.setFrameShadow(QFrame.Sunken)

        # Labels for the track information
        artist = QLabel('Artist:')
        artist.setStyleSheet(common_style)
        album = QLabel('Album:')
        album.setStyleSheet(common_style)
        track = QLabel('Track:')
        track.setStyleSheet(common_style)
        released = QLabel('Album Release:')
        released.setStyleSheet(common_style)
        genre = QLabel('Genre:')
        genre.setStyleSheet(common_style)

        self.artist = QLabel()
        self.artist.setStyleSheet(common_style)
        self.album_title = QLabel()
        self.album_title.setStyleSheet(common_style)
        self.track_title = QLabel()
        self.track_title.setStyleSheet(common_style)
        self.released = QLabel()
        self.released.setStyleSheet(common_style)
        self.genre = QLabel()
        self.genre.setStyleSheet(common_style)
        self.art = QLabel()
        self.art.setContentsMargins(5, 170, 5, 5)

        # Timer Label
        self._timer = QLabel('Duration: 00:00:00 / 00:00:00')

        # Define and create the listbox
        self.musiclist = QListWidget()
        self.musiclist.setFrameShape(QFrame.Box)
        self.musiclist.setFrameShadow(QFrame.Sunken)
        self.musiclist.setStyleSheet('background-color: snow;')

        # Create some containers
        btn_box = QHBoxLayout()
        btn_box2 = QHBoxLayout()
        slider_box = QVBoxLayout()
        slider_box.setContentsMargins(5, 80, 5, 5)
        dial_box = QVBoxLayout()
        container = QGridLayout()
        info_container = QGridLayout()
        info_container.setSpacing(8)

        frame = QFrame()
        frame.setMinimumWidth(390)
        frame.setFrameShape(QFrame.Box)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setLayout(info_container)

        img_frame = QFrame()
        img_frame.setMinimumHeight(100)

        # Create slider frame and control
        slider_frame = QFrame()
        slider_frame.setFrameShape(QFrame.Box)
        slider_frame.setFrameShadow(QFrame.Sunken)
        slider_frame.setMinimumHeight(30)
        slider_frame.setLayout(slider_box)

        self.slider = QSlider(Qt.Horizontal)
        slider_box.addWidget(self._timer)
        slider_box.addWidget(self.slider)

        # Create volume frame and control
        dial_frame = QFrame()
        dial_frame.setFrameShape(QFrame.Box)
        dial_frame.setFrameShadow(QFrame.Sunken)
        dial_frame.setLayout(dial_box)

        self.dial = QDial()
        self.dial.setRange(0, 100)
        self.dial.setNotchesVisible(True)
        self.dial.setSliderPosition(70)
        self.dial.setValue(70)
        self.dial.setMinimumWidth(200)
        self.dial.setMaximumWidth(200)
        self.dial.setMinimumHeight(100)
        dial_box.addWidget(QLabel('Volume'))
        dial_box.addWidget(self.dial)

        # Used to update various aspects of gui
        self.playlist.currentIndexChanged.connect(self.update)
        self.dial.valueChanged.connect(self._volume, self.dial.value())
        self.player.metaDataChanged.connect(self.meta_data)
        self.musiclist.itemDoubleClicked.connect(self._doubleclick)
        self.player.positionChanged.connect(self.track_position)
        self.player.durationChanged.connect(self.duration)
        self.slider.valueChanged.connect(self.timer)

        # Add track information to the info container
        info_container.addWidget(artist, 0, 0, 1, 1)
        info_container.addWidget(self.artist, 0, 1, 1, 1)
        info_container.addWidget(album, 1, 0, 1, 1)
        info_container.addWidget(self.album_title, 1, 1, 1, 1)
        info_container.addWidget(track, 2, 0, 1, 1)
        info_container.addWidget(self.track_title, 2, 1, 1, 1)
        info_container.addWidget(released, 3, 0, 1, 1)
        info_container.addWidget(self.released, 3, 1, 1, 1)
        info_container.addWidget(genre, 4, 0, 1, 1)
        info_container.addWidget(self.genre, 4, 1, 1, 1)
        info_container.addWidget(self.art, 5, 0, 1, 2)

        # Create the control buttons & button styles
        btn_style = '''QPushButton{background-color: skyblue;}
                       QPushButton:hover{background-color: lightskyblue; color: dodgerblue; \
                       font-weight: bold;}'''

        # Create buttons for getting audio files and clearing playlist
        file_btn = QPushButton('Get Audio')
        file_btn.released.connect(self._files)
        file_btn.setCursor(Qt.PointingHandCursor)
        file_btn.setStyleSheet(btn_style)
        file_btn.setMaximumWidth(100)

        clear_btn = QPushButton('Clear List')
        clear_btn.released.connect(self._clear)
        clear_btn.setCursor(Qt.PointingHandCursor)
        clear_btn.setStyleSheet(btn_style)
        clear_btn.setMaximumWidth(100)

        # Create & style the control buttons
        self.play_btn = QPushButton('Play')
        self.play_btn.released.connect(self._state)
        self.play_btn.setCursor(Qt.PointingHandCursor)
        self.play_btn.setStyleSheet(btn_style)

        self.prev_btn = QPushButton('Prev')
        self.prev_btn.released.connect(self._prev)
        self.prev_btn.setCursor(Qt.PointingHandCursor)
        self.prev_btn.setStyleSheet(btn_style)

        self.next_btn = QPushButton('Next')
        self.next_btn.released.connect(self._next)
        self.next_btn.setCursor(Qt.PointingHandCursor)
        self.next_btn.setStyleSheet(btn_style)

        self.stop_btn = QPushButton('Stop')
        self.stop_btn.released.connect(self._stop)
        self.stop_btn.setCursor(Qt.PointingHandCursor)
        self.stop_btn.setStyleSheet(btn_style)

        self.exit_btn = QPushButton('Exit')
        self.exit_btn.released.connect(sys.exit)
        self.exit_btn.setCursor(Qt.PointingHandCursor)
        self.exit_btn.setStyleSheet('QPushButton{background-color: firebrick;} \
                                    QPushButton:hover{background-color: red; color: white; \
                                    font-weight: bold;}')

        # Add the buttons to layout
        btn_box.addWidget(file_btn)
        btn_box.addWidget(clear_btn)
        btn_box2.addWidget(self.play_btn)
        btn_box2.addWidget(self.prev_btn)
        btn_box2.addWidget(self.next_btn)
        btn_box2.addWidget(self.stop_btn)
        btn_box2.addWidget(self.exit_btn)

        # Add layouts to container layout
        container.addWidget(self._header_footer(100, 100, 40, 'PyQt5 Music Player'), 0, 0, 1, 3)
        container.addWidget(self.status, 1, 0, 1, 1)
        container.addWidget(self.track, 1, 1, 1, 1)
        container.addLayout(btn_box, 1, 2, 1, 1)
        container.addWidget(frame, 2, 0, 2, 1)
        container.addWidget(self.musiclist, 2, 1, 1, 2)
        container.addLayout(btn_box2, 3, 1, 1, 2)
        container.addWidget(slider_frame, 4, 0, 1, 2)
        container.addWidget(dial_frame, 4, 2, 1, 1)
        container.addWidget(self._header_footer(40, 40, 10, 'my-python.org - 10/16/2021'), 5, 0, 1, 3)

        # Create the widget and set layout to container
        widget = QWidget()
        widget.setLayout(container)
        self.setCentralWidget(widget)

    # Volume control
    def _volume(self, val=70):
        self.player.setVolume(val)

    # Sets position of slider
    def track_position(self, position):
        self.slider.setValue(position)

    # Duration of the track playing
    def duration(self, duration):
        self.slider.setRange(0, duration)

    # Updates duration of track playing
    def timer(self):
        total_milliseconds = self.player.duration()
        total_seconds, total_milliseconds = divmod(total_milliseconds, 1000)
        total_minutes, total_seconds = divmod(total_seconds, 60)
        total_hours, total_minutes = divmod(total_minutes, 60)

        elapsed_milliseconds = self.slider.value()
        elapsed_seconds, elapsed_milliseconds = divmod(elapsed_milliseconds, 1000)
        elapsed_minutes, elapsed_seconds = divmod(elapsed_seconds, 60)
        elapsed_hours, elapsed_minutes = divmod(elapsed_minutes, 60)

        self._timer.setText(
            f'Duration: {elapsed_hours:02d}:{elapsed_minutes:02d}:{elapsed_seconds:02d} / {total_hours:02d}:{total_minutes:02d}:{total_seconds:02d}')

    # Shorten text that may be too long
    def _truncate(self, text, length=25):
        if len(text) <= length:
            return text
        else:
            return f"{' '.join(text[:length + 1].split(' ')[0:-1])} ...."

    # Get music metadata
    def meta_data(self):
        if self.player.isMetaDataAvailable():
            # print(self.player.availableMetaData())
            if self.player.metaData(QMediaMetaData.AlbumArtist):
                self.artist.setText(self.player.metaData(QMediaMetaData.AlbumArtist))
            if self.player.metaData(QMediaMetaData.AlbumTitle):
                self.album_title.setText(self._truncate(self.player.metaData(QMediaMetaData.AlbumTitle)))
            if self.player.metaData(QMediaMetaData.Title):
                self.track_title.setText(self._truncate(self.player.metaData(QMediaMetaData.Title)))
            if self.player.metaData(QMediaMetaData.Year):
                self.released.setText(f'{self.player.metaData(QMediaMetaData.Year)}')
            if self.player.metaData(QMediaMetaData.Genre):
                self.genre.setText(self.player.metaData(QMediaMetaData.Genre))
            if self.player.metaData(QMediaMetaData.Title):
                self.track.setText(f'Track: {self._truncate(self.player.metaData(QMediaMetaData.Title), 20)}')
            if self.player.metaData(QMediaMetaData.CoverArtImage):
                pixmap = QPixmap(self.player.metaData(QMediaMetaData.CoverArtImage))
                pixmap = pixmap.scaled(int(pixmap.width() / 3), int(pixmap.height() / 3))
                self.art.setPixmap(pixmap)
                self.art.setContentsMargins(0, 32, 0, 5)

    # Create the header
    def _header_footer(self, minheight, maxheight, fontsize, text):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(3)
        shadow.setOffset(3, 3)

        scene = QGraphicsScene()

        view = QGraphicsView()
        view.setMinimumSize(800, minheight)
        view.setMaximumHeight(maxheight)
        view.setScene(scene)

        gradient = QGradient(QGradient.RichMetal)

        scene.setBackgroundBrush(gradient)

        font = QFont('comic sans ms', fontsize, QFont.Bold)

        text = scene.addText(text)
        text.setDefaultTextColor(QColor(250, 250, 250))
        text.setFont(font)

        text.setGraphicsEffect(shadow)

        return view

    # Method for double clicking a track and play
    def _doubleclick(self):
        self.playlist.setCurrentIndex(self.musiclist.currentRow())
        self.player.play()

    # Method for clearing the playlist and musiclist
    def _clear(self):
        self.player.stop()
        self.musiclist.clear()
        self.playlist.clear()
        self.play_btn.setText('Play')
        self.status.setText('Status: ')
        self.track.setText('Track: ')
        self.artist.setText('Artist: ')
        self.album_title.setText('Album: ')
        self.track_title.setText('Track: ')
        self.released.setText('Released: ')
        self.genre.setText('Genre: ')
        self.art.setContentsMargins(5, 170, 5, 50)
        pixmap = QPixmap()
        self.art.setPixmap(pixmap)
        self.dial.setSliderPosition(70)
        self.dial.setValue(70)

    # Method for adding tracks to the playlist and musiclist
    def _files(self):
        files = QFileDialog.getOpenFileNames(None, 'Get Audio Files',
                                             filter='Audio Files (*.mp3 *.ogg *.wav)')
        for file in files[0]:
            self.playlist.addMedia(QMediaContent(self.url.fromLocalFile(file)))
            try:
                track = mutagen.File(file)
                self.musiclist.addItem(str(track['TIT2']))
            except:
                track = self._truncate(file.rpartition("/")[2].rpartition(".")[0])
                self.musiclist.addItem(track)
                print("no header")

        self.musiclist.setCurrentRow(0)
        self.playlist.setCurrentIndex(0)

    # Methods for the control buttons
    def _prev(self):
        if self.playlist.previousIndex() == -1:
            self.playlist.setCurrentIndex(self.playlist.mediaCount() - 1)
        else:
            self.playlist.previous()

    def _next(self):
        self.playlist.next()
        if self.playlist.currentIndex() == -1:
            self.playlist.setCurrentIndex(0)
            self.player.play()

    def _stop(self):
        self.player.stop()
        self.play_btn.setText('Play')
        self.playlist.setCurrentIndex(0)
        self.musiclist.setCurrentRow(0)
        self.status.setText('Status: Now Stopped')

    def _state(self):
        if self.playlist.mediaCount() > 0:
            if self.player.state() != QMediaPlayer.PlayingState:
                self.play_btn.setText('Pause')
                self.status.setText('Status: Now Playing')
                self.player.play()
            else:
                self.play_btn.setText('Play')
                self.player.pause()
                self.status.setText('Status: Now Paused')

        else:
            pass

    # Method for updating the listbox when the playlist updates
    def update(self):
        self.musiclist.setCurrentRow(self.playlist.currentIndex())
        if self.playlist.currentIndex() < 0:
            self.musiclist.setCurrentRow(0)
            self.playlist.setCurrentIndex(0)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()