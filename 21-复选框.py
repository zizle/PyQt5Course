# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QCheckBox
)
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        cb = QCheckBox('显示标题', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('复选框')
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('已选中')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
