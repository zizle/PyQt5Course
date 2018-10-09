# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initWindow()

    def initWindow(self):
        exitAction = QAction(QIcon('data/exit.png'), '退出', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('退出程序')

        # 鼠标指针悬停在该菜单的提示
        exitAction.triggered.connect(qApp.quit)

        # 创建一个状态栏， 用于显示鼠标上放的状态
        self.statusBar()
        # 创建一个菜单栏
        menuBar = self.menuBar()
        # 添加菜单
        fileMenu = menuBar.addMenu('退出')
        # 添加事件
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('状态栏')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
