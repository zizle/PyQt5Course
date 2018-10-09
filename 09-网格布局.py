# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        # 三个标签
        title = QLabel('标题')
        author = QLabel('作者')
        review = QLabel('内容')

        # 两个行编辑
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        # 一个文本编辑
        reviewEdit = QTextEdit()

        # 创建一个网格布局
        grid = QGridLayout()
        # 设置组件之间的距离
        grid.setSpacing(10)
        # 添加在第1行，第0列
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)
        # 添加在第2行第0 列
        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        # 第3行第1列，跨度5行,1列
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)
        self.setWindowTitle('评论')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())

