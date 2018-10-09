# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QTextEdit
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initWindow()

    def initWindow(self):
        # 创建一个文本编辑窗口
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QAction(QIcon('data/exit.png'), '退出', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('退出程序')

        # 鼠标指针悬停在该菜单的提示
        exitAction.triggered.connect(self.close)

        # 创建一个状态栏， 用于显示鼠标上放的状态
        self.statusBar()
        # 创建一个菜单栏
        menuBar = self.menuBar()
        # 添加菜单
        exitMenu = menuBar.addMenu('退出')
        # 添加事件
        exitMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('菜单工具栏')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
