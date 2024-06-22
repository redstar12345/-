import sys
import pymysql
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from change_all_login import Ui_Form
import os
 
class changeallUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(changeallUIForm, self).__init__(parent)
        self.setupUi(self)
        #添加登录按钮信号
        self.pages = [0]
        self.pages[0] = 0
        self.display(self.pages, 0)
        self.nextpage_Button.clicked.connect(lambda: self.display(self.pages, 1))
        self.lastpage_Button.clicked.connect(lambda: self.display(self.pages, -1))
        self.back_Button.clicked.connect(self.button2)
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        sql = "select * from login"
        cursor.execute(sql)
        data = cursor.fetchall()
        row = len(data)
        for k in range(1, min(9, row + 1)):
            button_local = f"change_Button{k}"
            button_obj = getattr(self, button_local, None)
            if button_obj is not None:
                button_obj.clicked.connect(lambda _, k = k: self.change(k))
        for k in range(1, min(9, row + 1)):
            button_local = f"delete_Button{k}"
            button_obj = getattr(self, button_local, None)
            if button_obj is not None:
                button_obj.clicked.connect(lambda _, k = k: self.delete(k))

    def display(self, pages, sign):
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        sql = "select * from login"
        cursor.execute(sql)
        data = cursor.fetchall()
        row = len(data)
        self.pages[0] = self.pages[0] + sign
        if self.pages[0] * 8 < 0:
            self.pages[0] = 0
            num = 0
        elif self.pages[0] * 8 + 8 > row:
            self.pages[0] = self.pages[0] - 1
            num = max(row - 8, 0)
        else:
            num = self.pages[0] * 8
        str_pages = str(num)
        sql = "select * from login limit 8 offset " + str_pages
        cursor.execute(sql)
        data = cursor.fetchall()
        for j in range(1, min(9, row + 1)):
            for i in range(1, 4):
                local = i + (j - 1) * 3
                str_local = f"textBrowser_{local}"
                # 使用getattr动态获取对象
                textBrowser_obj = getattr(self, str_local, None)
                if textBrowser_obj is not None:
                # 确保对象存在且可被访问后进行操作
                    textBrowser_obj.setText(data[j - 1][i - 1])

    def button2(self):
        self.close()
        os.system("python call_stu_basic.py")

    def change(self, local):
        text_local = f"textBrowser_{local * 3 - 2}"
        textBrowser_change_obj = getattr(self, text_local, None)
        username = textBrowser_change_obj.toPlainText()
        self.close()
        os.system("python call_change_login.py " + username)

    def delete(self, local):
        text_local = f"textBrowser_{local * 3 - 2}"
        textBrowser_change_obj = getattr(self, text_local, None)
        username = textBrowser_change_obj.toPlainText()
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        sql = "delete from login where username = '" + username + "'"
        cursor.execute(sql)
        conn.commit()
        self.close()
        os.system("python call_delete_hint.py call_change_all_login")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = changeallUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
