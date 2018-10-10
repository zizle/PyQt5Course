# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/10

import sys
from PyQt5.QtWidgets import (
    QApplication, QHBoxLayout,QVBoxLayout,
    QWidget, QFrame, QSplitter

)
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        # 水平布局
        hbox = QHBoxLayout(self)

        topLeft = QFrame(self)
        # 使用风格框架，可以看到Frame之间的小间隙
        topLeft.setFrameShape(QFrame.StyledPanel)

        topRight = QFrame(self)
        topRight.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        # 创建QSplitter和添加两个帧
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topLeft)
        splitter1.addWidget(topRight)

        splitter2 = QSplitter(Qt.Vertical)
        # 可以将一个QSplitter添加到另一个中
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('拖动控件改变大小')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())