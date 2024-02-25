import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import (QPropertyAnimation, QSequentialAnimationGroup, QPoint, QSize)
# Эти отдельные анимационные кривые полезны сами по себе,
# но иногда вам может потребоваться объединить несколько анимаций вместе,
# чтобы создать более сложное поведение.
# Для поддержки этого Qt предоставляет QAnimationGroup,
# с помощью которой мы можем комбинировать несколько анимаций и контролировать,
# когда они запускаются и останавливаются.
# Существует два класса animation group, которые группируют анимации определенным образом

# - QParallelAnimationGroup группирует анимации для одновременного запуска
# - QSequentialAnimationGroup группирует анимации для последовательного запуска по порядку
# - QAnimationGroup это абстрактный класс, поэтому его нельзя использовать напрямую.

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color:red; border-radius: 15px;")
        self.child.resize(100, 100)
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setEndValue(QPoint(200, 200))
        self.anim.setDuration(1500)
        self.anim_2 = QPropertyAnimation(self.child, b"size")
        self.anim_2.setEndValue(QSize(250, 150))
        self.anim_2.setDuration(3500)
        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()