# _*_ coding:utf-8 _*_
# author: zizle
# last edited: 2018/10/09
"""
Qt库是最强大的GUI库之一。pyqt5的官方网站http://www.riverbankcomputing.co.uk/news。

pyqt5做为Python的一个模块，它有620多个类和6000个函数和方法。这是一个跨平台的工具包，它可以运行在所有主要的操作系统，包括UNIX，Windows，Mac OS。pyqt5是双重许可。开发者可以在GPL和商业许可之间进行选择。
pyqt5的类别分为几个模块，包括以下：
QtCore
QtGui
QtWidgets
QtMultimedia
QtBluetooth
QtNetwork
QtPositioning
Enginio
QtWebSockets
QtWebKit
QtWebKitWidgets
QtXml
QtSvg
QtSql
QtTest
QtCore:包含了核心的非GUI功能。此模块用于处理时间、文件和目录、各种数据类型、流、URL、MIME类型、线程或进程。
QtGui包含类窗口系统集成、事件处理、二维图形、基本成像、字体和文本。
qtwidgets模块包含创造经典桌面风格的用户界面提供了一套UI元素的类。
QtMultimedia包含的类来处理多媒体内容和API来访问相机和收音机的功能。
Qtbluetooth模块包含类的扫描设备和连接并与他们互动。描述模块包含了网络编程的类。这些类便于TCP和IP和UDP客户端和服务器的编码，使网络编程更容易和更便携。
Qtpositioning包含类的利用各种可能的来源，确定位置，包括卫星、Wi-Fi、或一个文本文件。
Enginio模块实现了客户端库访问Qt云服务托管的应用程序运行时。
Qtwebsockets模块包含实现WebSocket协议类。
QtWebKit包含一个基于Webkit2图书馆Web浏览器实现类。
Qtwebkitwidgets包含的类的基础webkit1一用于qtwidgets应用Web浏览器的实现。
QtXml包含与XML文件的类。这个模块为SAX和DOM API提供了实现。
QtSvg模块提供了显示SVG文件内容的类。可伸缩矢量图形（SVG）是一种描述二维图形和图形应用的语言。
QtSql模块提供操作数据库的类。
QtTest包含的功能，使pyqt5应用程序的单元测试

"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建app对象并接受从命令行输入的参数列表
    app = QApplication(sys.argv)
    # 创建一个window。 QWidget是所有用户界面对象的基类
    window = QWidget()
    # 调整窗口大小,宽X高，单位是px
    window.resize(250, 150)
    # 移动窗口到屏幕的位置，也就是初始想显示的位置, 不指定为显示在屏幕的中间
    # window.move(100, 300)
    # 设置标题
    window.setWindowTitle('这是第一个PyQt窗口')
    # 显示
    window.show()
    # 使用系统exit()确保程序干净退出
    sys.exit(app.exec())

