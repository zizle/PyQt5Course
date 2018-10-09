# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class Window(QWidget):
    def __init__(self):
        # 调用QWidget方法
        super().__init__()
        # 自定义的绘制方法
        self.ShowUI()

    def ShowUI(self):
        self.setGeometry(300, 300, 300, 200)
        # 设置标题
        self.setWindowTitle('有提示的窗口')
        # 设置图标
        self.setWindowIcon(QIcon('data/app.png'))
        # 设置显示工具提示的字体
        QToolTip.setFont(QFont('SimHei', 10))
        # 创建一个提示体， 鼠标进入窗口便会显示
        # notice = self.setToolTip('这是一个<b>提示体</b>窗口')
        # 创建一个用于展示提示体的按钮
        btn = QPushButton('放上鼠标提示', self)
        # 设置提示体, 可将上面的notice作为参数置入，这样只要鼠标移入窗口，便会显示提示体
        btn.setToolTip('这是一个<b>提示体</b>窗口')
        # 显示默认尺寸
        btn.resize(btn.sizeHint())
        # 移动位置
        btn.move(50, 50)

        # 设置一个关闭按钮
        qbtn = QPushButton('退出', self)
        # 点击关闭
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(btn.sizeHint())
        qbtn.move(150, 50)
        # 显示
        self.show()


if __name__ == '__main__':
    # 创建应用程序
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
