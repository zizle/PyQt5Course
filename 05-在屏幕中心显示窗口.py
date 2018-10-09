# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class Window(QWidget):
    def __init__(self):
        # 调用QWidget方法
        super().__init__()
        # 自定义的绘制方法
        self.ShowUI()

    def ShowUI(self):
        # 设置大小才能设置到中心，坑！
        self.resize(250, 150)
        # 设置到中心
        self.center()

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

    def closeEvent(self, event):
        """默认的退出按钮提示，自己设置的按钮不提示"""
        reply = QMessageBox.question(self, '退出确认', '您确定要这么做吗？', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        """屏幕中心显示，使用见19-22行代码"""
        qr = self.frameGeometry()
        # 获得屏幕中心点
        center_point = QDesktopWidget().availableGeometry().center()
        # 显示到中心
        qr.moveCenter(center_point)
        self.move(qr.topLeft())


if __name__ == '__main__':
    # 创建应用程序
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
