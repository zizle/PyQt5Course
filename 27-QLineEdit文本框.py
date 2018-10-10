# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/10

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget, QLabel,
    QLineEdit
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        self.lbl = QLabel(self)
        self.lbl.move(60, 40)

        # 文本框
        line = QLineEdit(self)
        line.move(60, 100)
        # 文本框变化调用的方法
        line.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('文本框的使用')
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        # 将label空间的长度调整为文本的长度
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())