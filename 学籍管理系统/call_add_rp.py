import sys
import pymysql
from datetime import datetime
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from add_rp import Ui_Form
import os
 
class Add_rpUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Add_rpUIForm, self).__init__(parent)
        self.setupUi(self)
        #添加登录按钮信号
        self.commit_Button.clicked.connect(self.Insert)
        self.back_Button.clicked.connect(self.back)

    def Insert(self):
        rp_ID = self.lineEdit_1.text()
        rp_stu_ID = self.lineEdit_2.text()
        rp_name = self.lineEdit_3.text()
        rp_period = self.lineEdit_4.text()
        try:
            if rp_ID != "":
                rp_ID_int = int(rp_ID)
            if rp_stu_ID != "":
                rp_stu_ID_int = int(rp_stu_ID)
        except (ValueError or TypeError) as err_message:
            print(err_message)
            return
        if rp_ID == "" or rp_stu_ID == "" or rp_name == "" or rp_period == "":
            print("请输入完整信息！")
        else:
            conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
            cursor = conn.cursor()
            sql = "use student_sys_db"
            cursor.execute(sql)
            sql = "select * from rewards_punishment where rpid = " + rp_ID
            cursor.execute(sql)
            data = cursor.fetchall()
            row = len(data)
            if row != 0:
                print("信息重复！请重新输入或退出！")
                return
            sql = "select * from student where sid = " + rp_stu_ID
            cursor.execute(sql)
            data = cursor.fetchall()
            row = len(data)
            if row == 0:
                print("学生不存在！请检查输入！")
                return
            sql = "insert into rewards_punishment(rpid, sid, rpname, rpperiod) values(" + rp_ID + ", " + rp_stu_ID + ", '" + rp_name + "', '" + rp_period + "')"
            cursor.execute(sql)
            conn.commit()
            self.close()
            os.system("python call_stu_rp.py")

    def back(self):
        self.close()
        os.system("python call_stu_rp.py")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = Add_rpUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
