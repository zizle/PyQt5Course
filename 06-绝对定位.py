# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Window(QWidget):
    def __init__(self):
        # 调用QWidget方法
        super().__init__()
        # 自定义的绘制方法
        self.ShowUI()

    def ShowUI(self):
        label1 = QLabel('标签一', self)
        # 使用move()方法空置控件的位置
        label1.move(15, 10)

        label2 = QLabel('标签二', self)
        label2.move(35, 30)

        label3 = QLabel('标签三', self)
        label3.move(55, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('绝对定位展示')
        self.show()


if __name__ == '__main__':
    # 创建应用程序
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
