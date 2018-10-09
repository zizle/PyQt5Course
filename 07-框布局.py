# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class Window(QWidget):
    def __init__(self):
        # 调用QWidget方法
        super().__init__()
        # 自定义的绘制方法
        self.ShowUI()

    def ShowUI(self):
        ok_button = QPushButton('确定')
        cancel_button = QPushButton('取消')

        # 水平布局
        hbox = QHBoxLayout()
        # 伸展因子，靠右显示
        hbox.addStretch(1)
        hbox.addWidget(ok_button)
        hbox.addWidget(cancel_button)

        # 垂直布局
        vbox = QVBoxLayout()
        # 伸展因子，靠下显示
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 550, 150)
        self.setWindowTitle('框布局展示')
        self.show()


if __name__ == '__main__':
    # 创建应用程序
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
