import sys
import pymysql
from datetime import datetime
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from add_course import Ui_Form
import os
 
class Add_courseUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Add_courseUIForm, self).__init__(parent)
        self.setupUi(self)
        #添加登录按钮信号
        self.commit_Button.clicked.connect(self.Insert)
        self.back_Button.clicked.connect(self.back)

    def Insert(self):
        course_ID = self.lineEdit_1.text()
        course_name = self.lineEdit_2.text()
        course_cstime = self.lineEdit_3.text()
        course_credit = self.lineEdit_4.text()
        try:
            if course_ID != "":
                course_ID_int = int(course_ID)
            if course_cstime != "":
                course_cstime_int = int(course_cstime)
            if course_credit != "":
                course_credit_int = int(course_credit)
        except (ValueError or TypeError) as err_message:
            print(err_message)
            return
        if course_ID == "" or course_name == "" or course_cstime == "" or course_credit == "":
            print("请输入完整信息！")
        else:
            conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
            cursor = conn.cursor()
            sql = "use student_sys_db"
            cursor.execute(sql)
            sql = "select * from course where csid = " + course_ID
            cursor.execute(sql)
            data = cursor.fetchall()
            row = len(data)
            if row != 0:
                print("信息重复！请重新输入或退出！")
                return
            sql = "insert into course(csid, csname, cstime, credit) values(" + course_ID + ", '" + course_name + "', " + course_cstime + ", " + course_credit + ")"
            cursor.execute(sql)
            conn.commit()
            self.close()
            os.system("python call_stu_course.py")

    def back(self):
        self.close()
        os.system("python call_stu_course.py")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = Add_courseUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
