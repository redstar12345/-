import sys
import pymysql
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsPixmapItem, QGraphicsScene
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel

import tkinter as tk
from tkinter import filedialog

#导入designer工具生成的login模块
from change_login import Ui_Form
import os
 
class Change_loginUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Change_loginUIForm, self).__init__(parent)
        self.setupUi(self)
        #添加登录按钮信号
        self.username = ""
        self.pwd = ""
        self.avatar_path = ""
        self.if_change = 0
        if len(sys.argv) == 2:
            self.username = sys.argv[1]
            conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
            cursor = conn.cursor()
            sql = "use student_sys_db"
            cursor.execute(sql)
            sql = "select * from login where username = '" + self.username + "'"
            cursor.execute(sql)
            data = cursor.fetchall()  # 获得表格数据（二维元组）
            self.pwd = data[0][1]
            self.if_change = 1
            self.path_before = data[0][2]
            self.avatar_path = data[0][2]
        self.lineEdit.setText(self.username)
        self.lineEdit_2.setText(self.pwd)
        self.pushButton.clicked.connect(self.button)
        self.pushButton_2.clicked.connect(self.button2)
        self.pushButton_3.clicked.connect(self.button3)
        self.pushButton_4.clicked.connect(self.button4)

    def button(self):
        root = tk.Tk()
        root.withdraw()
        self.open_file()

    def open_file(self):
        # 打开文件对话框并获取用户选择的文件路径
        self.avatar_path = filedialog.askopenfilename()
        if self.avatar_path:  # 确保用户选择了文件
            print("选择的文件路径是:", self.avatar_path)

    def button2(self):
        if self.if_change == 0:
            return
        username = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        if username == self.username and pwd == self.pwd and self.path_before == self.avatar_path:
            return
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        if username != self.username:
            sql = "select * from login where username = '" + username + "'"
            cursor.execute(sql)
            data = cursor.fetchall()
            row = len(data)
            if row != 0:
                print("用户名不可相同！")
                return
            sql = "update login set login.username = '" + username + "' where login.username = '" + self.username + "'"
            cursor.execute(sql)
        sql = "update login set login.pwd = '" + pwd + "' where login.username = '" + username + "'"
        cursor.execute(sql)
        sql = "update login set login.avatar_path = '" + self.avatar_path + "' where login.username = '" + username + "'"
        cursor.execute(sql)
        conn.commit()
        self.close()
        os.system("python call_stu_basic.py")

    def button3(self):
        self.close()
        os.system("python call_stu_basic.py")

    def button4(self):
        if self.avatar_path != "":
            os.system("start " + self.avatar_path)

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = Change_loginUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
