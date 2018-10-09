# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QInputDialog, QFrame, QColorDialog
from PyQt5.QtGui import QColor


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        # 初始化QFrame的颜色
        col = QColor(0, 0, 0)

        self.btn = QPushButton('输入', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('输入对话框')
        self.show()

    def showDialog(self):

        text, ok = QInputDialog.getText(self, '正在输入', '输入您的名字:')
        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
