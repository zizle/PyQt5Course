# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget, QProgressBar, QPushButton
)
from PyQt5.QtCore import QBasicTimer



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        # QProgressBar构造方法
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('开始加载', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        # 使用定时器激活进度条
        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('进度条展示')
        self.show()

    def timerEvent(self, e):
        """重新实现timerEvent()时间处理"""
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('加载完成')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        """启动和停止定时器"""
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('开始加载')
        else:
            self.timer.start(100, self)
            self.btn.setText('暂停')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())