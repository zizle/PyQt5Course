# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        # 调用QWidget方法
        super().__init__()
        # 自定义的绘制方法
        self.ShowUI()

    def ShowUI(self):
        # 设置位置和大小,分别为距左，距上， 窗口宽， 窗口高
        self.setGeometry(400, 300, 300, 200)
        # 设置标题
        self.setWindowTitle('设置了图标的窗口')
        # 设置图标
        self.setWindowIcon(QIcon('data/app.png'))
        # 显示
        self.show()


if __name__ == '__main__':
    # 创建应用程序
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
