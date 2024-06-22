import sys
import pymysql
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from login import Ui_Form
import os

class LoginUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(LoginUIForm, self).__init__(parent)
        self.setupUi(self)
        #添加登录按钮信号
        self.pushButton.clicked.connect(self.button1)
        self.pushButton_2.clicked.connect(self.button2)

    def button1(self):
        username = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        if username == "root" and pwd == "Dth20030116":
            self.close()
            os.system("python call_stu_basic.py")
        else:
            conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
            cursor = conn.cursor()
            sql = "use student_sys_db"
            cursor.execute(sql)
            sql = "select * from login"
            cursor.execute(sql)
            data = cursor.fetchall()  # 获得表格数据（二维元组）
            user_number = len(data)
            for i in range(0, user_number):
                if username == data[i][0] and pwd == data[i][1]:
                    print("登录成功！")
                    self.close()
                    os.system("python call_stu_basic.py")

    def button2(self):
        self.close()
        os.system("python call_register.py")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = LoginUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
