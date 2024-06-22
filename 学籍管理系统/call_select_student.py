#导入程序运行必须模块
import sys
from datetime import datetime
import os
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from select_student import Ui_Form

class Select_studentUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Select_studentUIForm, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.check)
        self.pushButton_2.clicked.connect(self.back)

    def check(self):
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
        if student_ID == "" and student_name == "" and student_sex == "" and student_birth == "" and student_entry == "" and student_classname == "":
            print("请输入信息！")
        else:
            self.close()
            student_ID = " student.sid=" + student_ID
            student_name = " student.sname='" + student_name + "'"
            student_sex = " student.sex='" + student_sex + "'"
            student_birth = " student.birth='" + student_birth + "'"
            student_entry = " student.entry='" + student_entry + "'"
            student_classname = " class.cname='" + student_classname + "'"
            os.system("python call_stu_basic.py" + student_ID + student_name +  student_sex + student_birth + student_entry + student_classname)

    def back(self):
        self.close()
        os.system("python call_stu_basic.py")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = Select_studentUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
