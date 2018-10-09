# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initWindow()

    def initWindow(self):
        # 创建一个状态栏并显示消息
        self.statusBar().showMessage('状态显示')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('状态栏')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
