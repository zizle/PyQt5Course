# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/10

import sys
from PyQt5.QtWidgets import (
    QApplication, QLabel,
    QWidget, QComboBox

)
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):

        combo = QComboBox(self)
        combo.addItem("子鼠")
        combo.addItem("丑牛")
        combo.addItem("寅虎")
        combo.addItem("卯兔")
        combo.addItem("辰龙")
        combo.addItem("巳蛇")
        combo.addItem("午马")
        combo.addItem("未羊")
        combo.addItem("申猴")
        combo.addItem("酉鸡")
        combo.addItem("戌狗")
        combo.addItem("亥猪")
        combo.move(30, 10)

        self.lbl = QLabel(" ", self)
        self.lbl.move(50, 150)
        # 选中条目调用方法
        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('下拉列表')
        self.show()

    def onActivated(self, text):
        text = '您选择了: ' + text
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())