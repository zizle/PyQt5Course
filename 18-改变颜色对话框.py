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

        self.btn = QPushButton('点击换装', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('有颜色的输入对话框')
        self.show()

    def showDialog(self):
        # 弹出颜色选择窗
        col = QColorDialog.getColor()
        # 当点击的是确定才改变颜色
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
