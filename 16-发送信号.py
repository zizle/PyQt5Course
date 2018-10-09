# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
    closeApp = pyqtSignal()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        self.c = Communicate()
        # 自定义closeApp信号连接到QMainWindow的close槽
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('发送信号')
        self.show()

    def mousePressEvent(self, *args, **kwargs):
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
