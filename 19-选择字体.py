# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFontDialog, QVBoxLayout, QSizePolicy


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        vbox = QVBoxLayout()
        btn = QPushButton('点击换字体', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.move(20, 20)
        vbox.addWidget(btn)
        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('我是将被你改变的字体', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        # 设置窗口主布局
        self.setLayout(vbox)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('改变字体')
        self.show()

    def showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
