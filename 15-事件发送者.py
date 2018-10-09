# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        btn1 = QPushButton("按钮 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("按钮 2", self)
        btn2.move(150, 50)

        # 两个按钮连接到了同一个插槽
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('事件发送者')
        self.show()

    def buttonClicked(self):
        # 使用sender来判断是哪个按钮发出的信号
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + '被点击了')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
