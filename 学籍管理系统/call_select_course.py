#导入程序运行必须模块
import sys
from datetime import datetime
import os
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from select_course import Ui_Form

class Select_courseUIFORM(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Select_courseUIFORM, self).__init__(parent)
        self.setupUi(self)
        self.check_Button.clicked.connect(self.check)
        self.back_Button.clicked.connect(self.back)

    def check(self):
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
        if course_ID == "" and course_name == "" and course_cstime == "" and course_credit == "":
            print("请输入信息！")
        else:
            self.close()
            course_ID = " course.csid=" + course_ID
            course_name = " course.csname='" + course_name + "'"
            course_cstime = " course.cstime=" + course_cstime
            course_credit = " course.credit=" + course_credit
            os.system("python call_stu_course.py" + course_ID + course_name +  course_cstime + course_credit)

    def back(self):
        self.close()
        os.system("python call_stu_course.py")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = Select_courseUIFORM()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
