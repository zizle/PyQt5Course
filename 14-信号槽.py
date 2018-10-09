# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initWindow()

    def initWindow(self):
        # lcd = QLCDNumber(self)
        # sld = QSlider(Qt.Horizontal, self)
        #
        # vbox = QVBoxLayout()
        # vbox.addWidget(lcd)
        # vbox.addWidget(sld)
        #
        # self.setLayout(vbox)
        # # 将滚动条的valueChanged信号连接到lcd的display插槽
        # sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('信号槽')
        self.show()

        def keyPressEvent(self, QKeyEvent):
            """按下空格退出程序"""
            if QKeyEvent() == Qt.Key_Escape:
                self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
