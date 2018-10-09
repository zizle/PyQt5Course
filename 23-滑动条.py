# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget, QSlider, QLabel
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        # 创建一个滑动条
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        # 创建一个标签
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('audio.ico'))
        self.label.setGeometry(110, 70, 160, 100)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('滑动条')
        self.show()

    def changeValue(self, value):
        if value == 0:
            self.label.setPixmap(QPixmap('data/audio.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('data/min.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('data/med.png'))
        else:
            self.label.setPixmap(QPixmap('data/max.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())