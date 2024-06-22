import sys
import pymysql
from datetime import datetime
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from add_achievement import Ui_Form
import os
 
class Add_achievementUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Add_achievementUIForm, self).__init__(parent)
        self.setupUi(self)
        #添加登录按钮信号
        self.add_Button.clicked.connect(self.Insert)
        self.back_Button.clicked.connect(self.back)

    def Insert(self):
        stu_ID = self.lineEdit_1.text()
        course_ID = self.lineEdit_2.text()
        score = self.lineEdit_3.text()
        try:
            if stu_ID != "":
                stu_ID_int = int(stu_ID)
            if course_ID != "":
                course_ID_int = int(course_ID)
            if score != "":
                score_int = int(score)
        except (ValueError or TypeError) as err_message:
            print(err_message)
            return
        if stu_ID == "" or course_ID == "" or score == "":
            print("请输入完整信息！")
        else:
            conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
            cursor = conn.cursor()
            sql = "use student_sys_db"
            cursor.execute(sql)
            sql = "select * from achievement where sid = " + stu_ID + " and csid = " + course_ID
            cursor.execute(sql)
            data = cursor.fetchall()
            row = len(data)
            if row != 0:
                print("信息重复！请重新输入或退出！")
                return
            sql = "select * from student where sid = " + stu_ID
            cursor.execute(sql)
            data = cursor.fetchall()
            row1 = len(data)
            sql = "select * from course where csid = " + course_ID
            cursor.execute(sql)
            data = cursor.fetchall()
            row2 = len(data)
            if row1 == 0:
                print("学生不存在！请检查输入！")
                return
            elif row2 == 0:
                print("课程不存在！请检查输入！")
                return
            sql = "insert into achievement(sid, csid, score) values(" + stu_ID + ", " + course_ID + " , " + score + ")"
            cursor.execute(sql)
            conn.commit()
            self.close()
            os.system("python call_stu_achievement.py")

    def back(self):
        self.close()
        os.system("python call_stu_achievement.py")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = Add_achievementUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
