# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/10

# 做一个小测试程序，猜猜你是谁？

import sys
import sip
import re

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QDesktopWidget,
    QPushButton,
    QProgressBar,
    QVBoxLayout,
    QLabel,
    QRadioButton,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QBasicTimer, Qt

QUESTIONS = [

    {'Q': '早上起床之后通常吃什么当早点?', 'A': 'A 蛋和面包', 'B': 'B 麦片', 'C': 'C 汽水', 'D': 'D 什么都不吃'},
    {'Q': '如果你可以选任何一样你想吃的东西当早点，你会选择什么?', 'A': 'A 蛋和吐司', 'B': 'B 蛋糕', 'C': 'C 汽水', 'D': 'D 其他别的东西'},
    {'Q': '午餐时，你会？', 'A': 'A 不吃东西因为太忙或担心体重', 'B': 'B 吃你想了一个早上想吃的东西', 'C': 'C 吃自己带来的食物', 'D': 'D 问朋友要吃什么再一起去吃'},

]


class Window(QMainWindow):
    """创建窗口类"""

    def __init__(self):
        self.ansList = []
        super().__init__()
        self.initWindow()

    def initWindow(self):
        """初始化窗口设置"""
        # 创建一个布局
        self.vbox = QVBoxLayout()

        # 设置图标
        self.setWindowIcon(QIcon('data/qst.png'))
        # 设置窗口大小
        self.resize(450, 350)
        # 获取屏幕中心点
        screenPoint = QDesktopWidget().availableGeometry().center()
        # 设置到中心
        self.frameGeometry().moveCenter(screenPoint)

        # 设置进度条
        self.proBar()

        # 添加布局
        self.setLayout(self.vbox)

        # 窗口标题
        self.setWindowTitle('测测你是谁？')
        self.show()

    def proBar(self):
        """进度条控件及开始按钮"""
        # 进度条
        self.prBar = QProgressBar(self)
        # 大小位置
        # self.prBar.resize(350, 20)
        self.prBar.setGeometry(70, 100, 350, 20)
        # 按钮
        self.startBtn = QPushButton('加载资源', self)
        self.startBtn.setGeometry(170, 180, 100, 25)
        self.startBtn.clicked.connect(self.doAction)

        self.vbox.addWidget(self.prBar)
        self.vbox.addWidget(self.startBtn)

        # 使用定时器激活进度条
        self.timer = QBasicTimer()
        self.step = 0

    def timerEvent(self, *args, **kwargs):
        """重写时间处理"""
        if self.step >= 100:
            self.timer.stop()
            self.startBtn.setText('加载完成')
            self.startBtn.setText('开始测试')

            return
        self.step += 50
        self.prBar.setValue(self.step)

    def doAction(self):
        """启动和停止定时器"""
        if self.timer.isActive():
            self.timer.stop()
            self.startBtn.setText('继续加载')
        else:
            if self.step >= 100:
                # 再点击按钮进入测试
                self.testQuestion()
            else:
                self.timer.start(20, self)
                self.startBtn.setText('暂停')

    def testQuestion(self):
        # 开始测试就删除进度条和按钮
        self.vbox.removeWidget(self.prBar)
        self.vbox.removeWidget(self.startBtn)
        sip.delete(self.prBar)
        sip.delete(self.startBtn)

        # 设置label显示问题
        self.qstLabel = QLabel(self)
        self.qstLabel.setText('')
        # 适应字体长度
        self.qstLabel.adjustSize()
        self.qstLabel.resize(450, 25)
        self.vbox.addWidget(self.qstLabel)
        self.qstLabel.show()

        # 设置选择框
        self.rb1 = QRadioButton('             ', self)
        self.rb2 = QRadioButton('             ', self)
        self.rb3 = QRadioButton('             ', self)
        self.rb4 = QRadioButton('             ', self)

        self.rb1.resize(200, 25)
        self.rb2.resize(200, 25)
        self.rb3.resize(200, 25)
        self.rb4.resize(200, 25)

        self.rb1.move(60, 60)
        self.rb2.move(260, 60)
        self.rb3.move(60, 100)
        self.rb4.move(260, 100)
        self.vbox.addWidget(self.rb1)
        self.vbox.addWidget(self.rb2)
        self.vbox.addWidget(self.rb3)
        self.vbox.addWidget(self.rb4)
        self.rb1.show()
        self.rb2.show()
        self.rb3.show()
        self.rb4.show()

        # 设置两个按钮
        preBtn = QPushButton('上一题', self)
        preBtn.resize(60, 22)
        preBtn.move(80, 300)
        preBtn.clicked.connect(self.preQuestion)
        self.vbox.addWidget(preBtn)

        nextBtn = QPushButton('下一题', self)
        nextBtn.resize(60, 22)
        nextBtn.move(250, 300)
        nextBtn.clicked.connect(self.nextQuestion)
        self.vbox.addWidget(nextBtn)

        self.setLayout(self.vbox)

        preBtn.show()
        nextBtn.show()

    # def removeRaioButton(self):
    #     self.vbox.removeWidget(self.rb1)
    #     self.vbox.removeWidget(self.rb2)
    #     self.vbox.removeWidget(self.rb3)
    #     self.vbox.removeWidget(self.rb4)
    #     sip.delete(self.rb1)
    #     sip.delete(self.rb2)
    #     sip.delete(self.rb3)
    #     sip.delete(self.rb4)
    #     return

    def getQstNum(self):
        """获取问题的序号"""
        # 获取label标签内容
        content = self.qstLabel.text()

        # 提取当前的问题序号
        numObj = re.match('\d', content)
        if numObj:
            num = numObj.group()
        else:
            num = len(QUESTIONS)
        return int(num)

    def setAnswers(self, questionData):
        aAns = questionData.get('A')
        bAns = questionData.get('B')
        cAns = questionData.get('C')
        dAns = questionData.get('D')
        self.rb1.setText(aAns)
        self.rb2.setText(bAns)
        self.rb3.setText(cAns)
        self.rb4.setText(dAns)

    def nextQuestion(self):
        qNum = self.getQstNum()
        if 0 <= qNum < len(QUESTIONS):
            # 设置问题
            questionData = QUESTIONS[qNum]  # {'':{}}
            question = questionData.get('Q')
            qNum += 1
            self.qstLabel.setText(str(qNum) + '、' + question)
            # 设置答案
            self.setAnswers(questionData)

        if qNum == len(QUESTIONS):
            self.qstLabel.setText(str(qNum) + '、没有问题了...')


    def preQuestion(self):
        qNum = self.getQstNum()
        if 0 < qNum <= len(QUESTIONS):
            # 设置问题
            questionData = QUESTIONS[qNum - 1]
            question = questionData.get('Q')
            qNum -= 1
            self.qstLabel.setText(str(qNum) + '、' + question)
            # 设置答案
            self.setAnswers(questionData)
        if qNum == 0:
            self.qstLabel.setText('0、没有问题了...')

        print('上一题')

    def selectAns(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('已选中')
        else:
            self.setWindowTitle(' ')

        # qstLabel.setText('问题一：呀呀呀呀呀。。。')


if __name__ == '__main__':
    # 创建一个程序
    app = QApplication(sys.argv)
    # 初始化窗口
    window = Window()
    # 退出
    sys.exit(app.exec_())
