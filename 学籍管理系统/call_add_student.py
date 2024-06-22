import sys
import pymysql
from datetime import datetime
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from add_student import Ui_Form
import os
 
class Add_studentUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Add_studentUIForm, self).__init__(parent)
        self.setupUi(self)
        #添加登录按钮信号
        self.pushButton.clicked.connect(self.Insert)
        self.pushButton_2.clicked.connect(self.back)

    def Insert(self):
        student_ID = self.lineEdit_1.text()
        student_name = self.lineEdit_2.text()
        student_sex = self.lineEdit_3.text()
        student_birth = self.lineEdit_4.text()
        student_entry = self.lineEdit_5.text()
        student_classname = self.lineEdit_6.text()
        try:
            if student_ID != "":
                student_ID_int = int(student_ID)
            date_format = "%Y-%m-%d"
            if student_birth != "":
                student_birth_date = datetime.strptime(student_birth, date_format)
            if student_entry != "":
                student_entry_date = datetime.strptime(student_entry, date_format)
        except (ValueError or TypeError) as err_message:
            print(err_message)
            return
        if student_ID == "" or student_name == "" or student_sex == "" or student_birth == "" or student_entry == "" or student_classname == "":
            print("请输入完整信息！")
        else:
            if student_sex != '男' and student_sex != '女':
                print("请输入正确的性别信息！")
                return
            conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
            cursor = conn.cursor()
            sql = "use student_sys_db"
            cursor.execute(sql)
            sql = "select * from student where sid = " + student_ID
            cursor.execute(sql)
            data = cursor.fetchall()
            row = len(data)
            if row != 0:
                print("信息重复！请重新输入或退出！")
                return
            sql = "select * from class where cname = '" + student_classname + "'"
            cursor.execute(sql)
            data = cursor.fetchall()
            row = len(data)
            if row == 0:
                print("班级不存在！请检查输入！")
                return
            else:
                class_ID = str(data[0][0])
            sql = "insert into student(sid, sname, sex, birth, entry, cid) values(" + student_ID + ", '" + student_name + "', '" + student_sex + "', '" + student_birth + "', '" + student_entry + "', '" + class_ID + "')"
            cursor.execute(sql)
            conn.commit()
            self.close()
            os.system("python call_stu_basic.py")

    def back(self):
        self.close()
        os.system("python call_stu_basic.py")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = Add_studentUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
