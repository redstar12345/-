import sys
import pymysql
from datetime import datetime
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from add_department import Ui_Form
import os
 
class Add_departmentUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Add_departmentUIForm, self).__init__(parent)
        self.setupUi(self)
        #添加登录按钮信号
        self.add_Button.clicked.connect(self.Insert)
        self.back_Button.clicked.connect(self.back)

    def Insert(self):
        department_ID = self.lineEdit_1.text()
        department_name = self.lineEdit_2.text()
        try:
            if department_ID != "":
                department_ID_int = int(department_ID)
        except (ValueError or TypeError) as err_message:
            print(err_message)
            return
        if department_ID == "" or department_name == "":
            print("请输入完整信息！")
        else:
            conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
            cursor = conn.cursor()
            sql = "use student_sys_db"
            cursor.execute(sql)
            sql = "select * from Department where did = " + department_ID
            cursor.execute(sql)
            data = cursor.fetchall()
            row = len(data)
            if row != 0:
                print("信息重复！请重新输入或退出！")
                return
            sql = "insert into Department(did, dname) values(" + department_ID + ", '" + department_name +  "')"
            cursor.execute(sql)
            conn.commit()
            self.close()
            os.system("python call_department.py")

    def back(self):
        self.close()
        os.system("python call_department.py")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = Add_departmentUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
