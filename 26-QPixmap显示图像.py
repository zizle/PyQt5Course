# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/10

import sys
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout,
    QWidget, QLabel, QPushButton
)
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        # 设置按钮
        btn = QPushButton('立即查看', self)
        btn.setFixedSize(60,20)
        btn.setCheckable(True)
        # 连接到方法，通过clicked信号操作一个布尔值
        btn.clicked[bool].connect(self.setImage)

        # 纵向布局
        vbox = QVBoxLayout(self)
        # 标签
        self.lbl = QLabel(self)
        # 设置label的大小
        self.lbl.setFixedWidth(500)
        self.lbl.setFixedHeight(400)
        self.lbl.setScaledContents(True)

        vbox.addWidget(btn)
        vbox.addWidget(self.lbl)

        # 窗口显示
        self.setLayout(vbox)
        self.move(30, 30)
        self.setWindowTitle('看看你是谁？')
        self.show()

    def setImage(self, pressed):
        if pressed:
            # 图像对象
            pixMap = QPixmap("data/pig.jpg")
        else:
            pixMap = QPixmap()
            # 设置图像
        self.lbl.setPixmap(pixMap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())