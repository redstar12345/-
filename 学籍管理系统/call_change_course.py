#导入程序运行必须模块
import sys
import pymysql 
import os
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from change_course import Ui_Form

class change_courseUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(change_courseUIForm, self).__init__(parent)
        self.setupUi(self)
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        self.course_ID_before = ""
        self.courese_name_before = ""
        self.course_time_before = ""
        self.course_credit_before = ""
        self.if_change = 0
        if len(sys.argv) > 1:
            sql = "select * from course where csid = " + sys.argv[1]
            cursor.execute(sql)
            data = cursor.fetchall()
            self.lineEdit_1.setText(str(data[0][0]))
            self.lineEdit_2.setText(data[0][1])
            self.lineEdit_3.setText(str(data[0][2]))
            self.lineEdit_4.setText(str(data[0][3]))
            self.course_ID_before = str(data[0][0])
            self.courese_name_before = data[0][1]
            self.course_time_before = str(data[0][2])
            self.course_credit_before = str(data[0][3])
            self.if_change = 1
        self.pushButton.clicked.connect(self.commit)
        self.pushButton_2.clicked.connect(self.rollback)

    def commit(self):
        if self.if_change == 0:
            return
        course_ID = self.lineEdit_1.text()
        course_name = self.lineEdit_2.text()
        course_time = self.lineEdit_3.text()
        course_credit = self.lineEdit_4.text()
        if course_ID == self.course_ID_before and course_name == self.courese_name_before and course_time == self.course_time_before and course_credit == self.course_credit_before:
            return
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        if course_ID != self.course_ID_before:
            if course_ID.isdigit() == False:
                print("课程编号只能包含数字！")
                return
            sql = "select * from course where csid = " + course_ID
            cursor.execute(sql)
            data = cursor.fetchall()
            row = len(data)
            if row != 0:
                print("课程编号不可相同！")
                return
            sql = "call Update_course(" + self.course_ID_before + "," + course_ID + ")"
            cursor.execute(sql)
        sql = "update course set csname = '" + course_name + "' where csid = " + course_ID
        cursor.execute(sql)
        sql = "update course set cstime = '" + course_time + "' where csid = " + course_ID
        cursor.execute(sql)
        sql = "update course set credit = '" + course_credit + "' where csid = " + course_ID
        cursor.execute(sql)
        conn.commit()
        self.close()
        os.system("python call_stu_course.py")

    def rollback(self):
        self.close()
        os.system("python call_stu_course.py")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = change_courseUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
