# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initWindow()

    def initWindow(self):
        # 创建一个事件
        exitAction = QAction(QIcon('data/exit.png'), '退出', self)
        exitAction.setShortcut('Ctrl+Q')
        # 退出的方法
        exitAction.triggered.connect(qApp.quit)

        # 添加一个工具栏
        self.toolbar = self.addToolBar('退出')
        self.toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('工具栏')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
