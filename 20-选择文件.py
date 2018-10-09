# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('data/app.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('打开一个新文件')
        openFile.triggered.connect(self.showDialog)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('文件')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('改变字体')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fname[0]:
            with open(fname[0], 'r') as f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
