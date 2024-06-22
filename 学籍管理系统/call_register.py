#导入程序运行必须模块
import sys
import pymysql
import os
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from register import Ui_Form

class registerUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(registerUIForm, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.register)
        self.pushButton_3.clicked.connect(self.back)
        self.success = False

    def register(self):
        username = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        pwd2 = self.lineEdit_3.text()
        if username is None:
            print("请输入用户名！")
        elif pwd != pwd2:
            print("两次输入密码不一致！")
        else:
            self.success = True
            conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
            cursor = conn.cursor()
            sql = "use student_sys_db"
            cursor.execute(sql)
            sql = "select * from login"
            cursor.execute(sql)
            data = cursor.fetchall()  # 获得表格数据（二维元组）
            user_number = len(data)
            for i in range(0, user_number):
                lower_username = username.lower()
                lower_data = data[i][0].lower()
                if  lower_username == lower_data and self.success == True:
                    print("用户名重复！")
                    self.success = False
            if self.success == True:
                # 注册用户操作
                sql = "insert into login(username, pwd) values (%s, %s)"
                data = (username, pwd)
                cursor.execute(sql, data)
                conn.commit()
                self.close()
                os.system("python call_login.py")

    def back(self):
        self.close()
        os.system("python call_login.py")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = registerUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
