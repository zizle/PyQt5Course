# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/10

# 做一个小测试程序，猜猜你是谁？

import sys
import sip
import re

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QDesktopWidget,
    QPushButton,
    QProgressBar,
    QVBoxLayout, QHBoxLayout,
    QLabel,
    QRadioButton,
    QButtonGroup,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QBasicTimer, Qt, QMargins

QUESTIONS = {
    # '4': {'Q': '', 'A': 'A  ', 'B': 'B  ', 'C': 'C  ', 'D': 'D  '}
    '1': {'Q': '1. 早上起床之后通常吃什么当早点?', 'A': 'A  蛋和面包', 'B': 'B  麦片', 'C': 'C  汽水', 'D': 'D  什么都不吃'},
    '2': {'Q': '2. 如果你可以选任何一样你想吃的东西当早点, 你会选择什么?', 'A': 'A  蛋和吐司', 'B': 'B  蛋糕', 'C': 'C  汽水', 'D': 'D  其他别的东西'},
    '3': {'Q': '3. 午餐时，你会？', 'A': 'A  不吃东西因为太忙或担心体重', 'B': 'B  吃你想了一个早上想吃的东西', 'C': 'C  吃自己带来的食物', 'D': 'D  问朋友要吃什么再一起去吃'},
    '4': {'Q': '4. 一位朋友请你吃一些她/他带来的食物你会？', 'A': '  吃一小口因为实在太饿了', 'B': '  为了保持礼貌只吃一小口', 'C': '  拒绝他/她的好意因为你正在减肥', 'D': '  吃两口'},
    '5': {'Q': '5. 你未来的男/女朋友请你吃一样东西，你想那会是什么?', 'A': 'A  一块蛋糕', 'B': 'B  一颗苹果', 'C': 'C  一片披萨', 'D': 'D  一个胡萝卜'}
}


class Window(QWidget):
    """创建窗口类"""

    def __init__(self):
        self.answers = {}
        super(Window, self).__init__()
        #     self.initWindow()
        #
        # def initWindow(self):
        """初始化窗口设置"""
        # 设置图标
        self.setWindowIcon(QIcon('data/qst.png'))
        # 设置窗口大小
        self.resize(450, 350)
        # 获取屏幕中心点
        screen_point = QDesktopWidget().availableGeometry().center()
        # 设置到中心
        self.frameGeometry().moveCenter(screen_point)

        # 两个按钮，水平布局
        self.h_box = QHBoxLayout()
        self.h_box.addStretch(1)  # 伸缩因子，按钮置右
        self.pre_button = QPushButton('上一题')
        self.next_button = QPushButton('下一题')
        self.commit_button = QPushButton('确认提交')
        self.pre_button.setMaximumWidth(120)
        self.next_button.setMaximumWidth(120)
        self.commit_button.setMaximumWidth(120)
        # 按钮点击关联方法
        self.pre_button.clicked.connect(self.pre_question)
        self.next_button.clicked.connect(self.next_question)
        self.commit_button.clicked.connect(self.commit)

        # 按钮设置为不可用
        self.pre_button.setEnabled(False)
        self.next_button.setEnabled(False)
        self.commit_button.setEnabled(False)

        self.h_box.addWidget(self.pre_button, alignment=Qt.AlignBottom)
        self.h_box.addWidget(self.next_button, alignment=Qt.AlignBottom)
        self.h_box.addWidget(self.commit_button, alignment=Qt.AlignBottom)

        # 垂直布局
        self.v_box = QVBoxLayout()

        # 标签显示消息
        self.content_label = QLabel()
        # 自动换行设置
        # self.content_label.setWordWrap(True)
        self.content_label.setText('点击开始加载资源')
        # 设置标签大小

        # 进度条
        self.process_bar = QProgressBar()
        # 设置控件的大小，在布局Layout内resize方法已经不能使用，设置最大、最小、最高的参数来调整
        # process_bar.setMinimumSize(100, 25)
        # 定时器激活进度条
        self.timer = QBasicTimer()
        self.step = 0

        # 按钮
        self.start_btn = QPushButton('加载资源')
        self.start_btn.setMaximumSize(120, 25)
        # 按钮点击关联的方法
        self.start_btn.clicked.connect(self.start_downloader)

        # 答案按钮组与答案按钮
        self.ans_btn_group = QButtonGroup()
        # 关联方法
        self.ans_btn_group.buttonClicked.connect(self.saved_answer)

        self.btn_a = QRadioButton()
        self.btn_b = QRadioButton()
        self.btn_c = QRadioButton()
        self.btn_d = QRadioButton()
        # 添加到组中，并设置ID
        self.ans_btn_group.addButton(self.btn_a, id=1)
        self.ans_btn_group.addButton(self.btn_b, id=2)
        self.ans_btn_group.addButton(self.btn_c, id=3)
        self.ans_btn_group.addButton(self.btn_d, id=4)

        # 答案按钮布局
        v_ans_box = QVBoxLayout()
        v_ans_box.addWidget(self.btn_a, alignment=Qt.AlignLeft)
        v_ans_box.addWidget(self.btn_b, alignment=Qt.AlignLeft)
        v_ans_box.addWidget(self.btn_c, alignment=Qt.AlignLeft)
        v_ans_box.addWidget(self.btn_d, alignment=Qt.AlignLeft)
        # 设置按钮之间的距离
        v_ans_box.setSpacing(10)
        # 与外布局之间的距离，左，上，右，下
        v_ans_box.setContentsMargins(QMargins(100, 0, 0, 0))
        # 设置隐藏
        self.btn_a.hide()
        self.btn_b.hide()
        self.btn_c.hide()
        self.btn_d.hide()

        # 布局添加标签、进度条和按钮
        self.v_box.addWidget(self.content_label, alignment=Qt.AlignCenter)
        self.v_box.addWidget(self.process_bar)
        self.v_box.addWidget(self.start_btn, alignment=Qt.AlignCenter)

        # 设置控件距离
        self.v_box.setSpacing(5)

        # 将水平布局加入垂直布局
        self.v_box.addLayout(v_ans_box)
        self.v_box.addLayout(self.h_box)
        # 窗口展示布局
        self.setLayout(self.v_box)

        # 窗口标题
        self.setWindowTitle('测测你是谁？')
        self.show()

    def timerEvent(self, *args, **kwargs):
        """重写时间处理"""
        if self.step >= 100:
            self.timer.stop()
            self.content_label.setText('资源加载完成！')
            self.start_btn.setText('开始测试')
            return
        self.step += 5
        self.process_bar.setValue(self.step)

    def start_downloader(self):
        """开始加载资源"""
        if self.timer.isActive():
            self.timer.stop()
            self.start_btn.setText('继续加载')
        else:
            if self.step >= 100:
                # 加载完成再次点击可进入测试
                self.enter_test()

            else:
                self.timer.start(20, self)
                self.start_btn.setText('暂停')

    def enter_test(self):
        print('开始测试')
        # 进入测试界面发生改变
        # 上下题按钮设置为可用
        self.pre_button.setEnabled(True)
        self.next_button.setEnabled(True)
        # 去掉进度条和'开始测试'按钮
        self.v_box.removeWidget(self.process_bar)
        self.v_box.removeWidget(self.start_btn)
        sip.delete(self.process_bar)
        sip.delete(self.start_btn)

        # QLabel显示信息变为题目信息
        question_dict = QUESTIONS.get('1')
        # 设置内容
        self.set_content(question_dict)
        # 显示选项按钮
        self.btn_a.show()
        self.btn_b.show()
        self.btn_c.show()
        self.btn_d.show()

    def set_content(self, qd):
        if isinstance(qd, dict):
            question = qd.get('Q', 'No Question!')
            answer_a = qd.get('A', 'No Answer A')
            answer_b = qd.get('B', 'No Answer B')
            answer_c = qd.get('C', 'No Answer C')
            answer_d = qd.get('D', 'No Answer D')
            self.content_label.setText(question)
            # 答案按钮的添加内容并可见
            self.btn_a.setText(answer_a)
            self.btn_b.setText(answer_b)
            self.btn_c.setText(answer_c)
            self.btn_d.setText(answer_d)
        else:
            print("the params 'qd' of function set_content must be class dict")

    def match_sequence(self):
        q = self.content_label.text()
        result = re.match('\d', q)
        if result:
            sequence = result.group()
        else:
            sequence = 0
        return int(sequence)

    def pre_question(self):
        # 获取当前是第几条题目
        sequence = self.match_sequence()
        if 1 < sequence <= len(QUESTIONS):
            # 开启一题按钮
            self.next_button.setEnabled(True)
            # 获取上一题内容
            question_dict = QUESTIONS.get(str(sequence-1))
            # 设置内容到标签和按钮
            self.set_content(question_dict)
        else:
            # 将上一题按钮设置不可用
            self.pre_button.setEnabled(False)

    def next_question(self):
        # 获取当前是第几条题目
        sequence = self.match_sequence()
        if 1 <= int(sequence) < len(QUESTIONS):
            # 开启上一题按钮
            self.pre_button.setEnabled(True)
            # 获取下一题内容
            question_dict = QUESTIONS.get(str(sequence+1))
            # 设置内容
            self.set_content(question_dict)
        else:
            # 将下题按钮设置为不可用
            self.next_button.setEnabled(False)
            # 提交按钮可用
            self.commit_button.setEnabled(True)

    def commit(self):
        lock, key = self.checked_answer()
        if lock:
            print('提交成功')
        else:
            print('第{}题还没做！'.format(key))

    def checked_answer(self):
        for key in QUESTIONS:
            if not self.answers.get(key):
                return False, key
        return True, 1


    # def clear_checked(self):
    #     """清除按钮选中状态"""
    #     if self.btn_a.isChecked():
    #         self.btn_a.setChecked(True)
    #
    #     if self.btn_b.isChecked():
    #
    #         self.btn_b.setChecked(True)
    #     if self.btn_c.isChecked():
    #
    #         self.btn_c.setChecked(True)
    #     if self.btn_d.isChecked():
    #
    #         self.btn_d.setChecked(True)

    def saved_answer(self):
        if self.ans_btn_group.checkedId() == 1:
            print('您选择了A')
            # 获取当前题号
            sequence = str(self.match_sequence())
            self.answers[sequence] = 'A'

        elif self.ans_btn_group.checkedId() == 2:
            print('您选择了B')
            sequence = str(self.match_sequence())
            self.answers[sequence] = 'B'

        elif self.ans_btn_group.checkedId() == 3:
            print('您选择了C')
            sequence = str(self.match_sequence())
            self.answers[sequence] = 'C'

        else:
            print('您选择了D')
            sequence = str(self.match_sequence())
            self.answers[sequence] = 'D'


if __name__ == '__main__':
    # 创建一个程序
    app = QApplication(sys.argv)
    # 初始化窗口
    window = Window()
    # 退出
    sys.exit(app.exec_())




