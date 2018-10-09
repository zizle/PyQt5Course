# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09

import sys
from PyQt5.QtWidgets import (
    QApplication, QLabel,
    QWidget, QCalendarWidget
)
from PyQt5.QtCore import QDate


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        # 创建了一个日历控件
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        # 如果我们从部件选择一个日期,点击[QDate]发出信号。我们将这个信号连接到showDate()方法
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        # 检索所选日期通过调用selectedDate
        date = cal.selectedDate()
        # 转为字符串设置为小部件的标签
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())