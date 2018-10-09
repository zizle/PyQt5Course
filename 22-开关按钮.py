# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QFrame,
    QPushButton
)
from PyQt5.QtGui import QColor


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        self.col = QColor(0, 0, 0)

        redb = QPushButton('红色', self)
        # 设置为开关
        redb.setCheckable(True)
        redb.move(10, 10)
        # 连接到方法，通过clicked信号操作一个布尔值
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('绿色', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('蓝色', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('开关按钮')
        self.show()

    def setColor(self, pressed):

        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "红色":
            self.col.setRed(val)
        elif source.text() == "绿色":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" %
                                  self.col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
