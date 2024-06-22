import sys
import pymysql
import os
from datetime import datetime
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from change_student import Ui_Form

class changeUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(changeUIForm, self).__init__(parent)
        self.setupUi(self)
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        self.stu_ID_before = ""
        self.stu_name_before = ""
        self.stu_sex_before = ""
        self.stu_birth_before = ""
        self.stu_entry_before = ""
        self.stu_class_before = ""
        self.if_change = 0
        if len(sys.argv) > 1:
            sql = "select * from student left join class on student.cid = class.cid where student.sid = " + sys.argv[1]
            cursor.execute(sql)
            data = cursor.fetchall()
            self.lineEdit_1.setText(str(data[0][0]))
            self.lineEdit_2.setText(data[0][1])
            self.lineEdit_3.setText(data[0][2])
            self.lineEdit_4.setText(data[0][3].strftime("%Y-%m-%d"))
            self.lineEdit_5.setText(data[0][4].strftime("%Y-%m-%d"))
            self.lineEdit_6.setText(str(data[0][7]))
            self.stu_ID_before = str(data[0][0])
            self.stu_name_before = data[0][1]
            self.stu_sex_before = data[0][2]
            self.stu_birth_before = data[0][3].strftime("%Y-%m-%d")
            self.stu_entry_before = data[0][4].strftime("%Y-%m-%d")
            self.stu_class_before = data[0][7]
            self.if_change = 1
        self.commitButton.clicked.connect(self.commit)
        self.rollbackButton.clicked.connect(self.rollback)

    def commit(self):
        if self.if_change == 0:
            return
        stu_ID = self.lineEdit_1.text()
        stu_name = self.lineEdit_2.text()
        stu_sex = self.lineEdit_3.text()
        stu_birth = self.lineEdit_4.text()
        stu_entry = self.lineEdit_5.text()
        stu_class = self.lineEdit_6.text()
        if stu_ID == self.stu_ID_before and stu_name == self.stu_name_before and stu_sex == self.stu_sex_before and stu_birth == self.stu_birth_before and stu_entry == self.stu_entry_before and stu_class == self.stu_class_before:
            return
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        if stu_ID != self.stu_ID_before:
            if stu_ID.isdigit() == False:
                print("学号只能包含数字！")
                return
            sql = "select * from student where sid = " + stu_ID
            cursor.execute(sql)
            data = cursor.fetchall()
            row = len(data)
            if row != 0:
                print("学号不可相同！")
                return
            sql = "call Update_student(" + self.stu_ID_before + "," + stu_ID + ")"
            cursor.execute(sql)
        try:
            date_format = "%Y-%m-%d"
            student_birth_date = datetime.strptime(stu_birth, date_format)
            student_entry_date = datetime.strptime(stu_entry, date_format)
        except (ValueError or TypeError) as err_message:
            print(err_message)
            return
        sql = "update student set sname = '" + stu_name + "' where sid = " + stu_ID
        cursor.execute(sql)
        sql = "update student set sex = '" + stu_sex + "' where sid = " + stu_ID
        cursor.execute(sql)
        sql = "update student set birth = '" + stu_birth + "' where sid = " + stu_ID
        cursor.execute(sql)
        sql = "update student set entry = '" + stu_entry + "' where sid = " + stu_ID
        cursor.execute(sql)
        sql = "select * from class where cname = '" + stu_class + "'"
        cursor.execute(sql)
        data = cursor.fetchall()
        row = len(data)
        if row == 0:
            print("班级不存在！")
            return
        else:
            sql = "select cid, cname from class where cname = '" + stu_class + "'"
            cursor.execute(sql)
            data1 = cursor.fetchall()
            sql = "select cid, cname from class where cname = '" + self.stu_class_before + "'"
            cursor.execute(sql)
            data2 = cursor.fetchall()
            sql = "update student set student.cid = " + str(data1[0][0]) + " where student.cid = " + str(data2[0][0]) + " and student.sid = " + stu_ID
            cursor.execute(sql)
        conn.commit()
        self.close()
        os.system("python call_stu_basic.py")

    def rollback(self):
        self.close()
        os.system("python call_stu_basic.py")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = changeUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
