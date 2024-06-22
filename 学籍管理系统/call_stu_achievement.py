#导入程序运行必须模块
import sys
import os
import pymysql
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from stu_achievement import Ui_Form

class Stu_achievementUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Stu_achievementUIForm, self).__init__(parent)
        self.setupUi(self)
        self.sqlset = ""
        self.pages = [0]
        self.pages[0] = 0
        if len(sys.argv) == 1:
            self.display(self.pages, 0)
        else:
            self.display_check()
        self.basic_BUTTON.clicked.connect(self.basicButton)
        self.class_BUTTON.clicked.connect(self.classButton)
        self.rp_BUTTON.clicked.connect(self.rpButton)
        self.achievement_BUTTON.clicked.connect(lambda: self.display(self.pages, -2000000))
        self.course_BUTTON.clicked.connect(self.courseButton)
        self.nextpage_BUTTON.clicked.connect(lambda: self.display(self.pages, 1))
        self.lastpage_BUTTON.clicked.connect(lambda: self.display(self.pages, -1))
        self.check_BUTTON.clicked.connect(self.checkButton)
        self.add_BUTTON.clicked.connect(self.addButton)
        self.avg_BUTTON.clicked.connect(self.avgButton)
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        if self.sqlset == "":
            sql = "select * from achievement"
        else:
            sql = self.sqlset
        cursor.execute(sql)
        data = cursor.fetchall()
        row = len(data)
        for k in range(1, min(9, row + 1)):
            button_local = f"change_Button{k}"
            button_obj = getattr(self, button_local, None)
            if button_obj is not None:
                button_obj.clicked.connect(lambda _, k = k: self.change(k))
        for k in range(1, min(9, row + 1)):
            button_local = f"delete_BUTTON{k}"
            button_obj = getattr(self, button_local, None)
            if button_obj is not None:
                button_obj.clicked.connect(lambda _, k = k: self.delete(k))

    def avgButton(self):
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        sql = "select csid, csname, func(csid) as average from course"
        cursor.execute(sql)
        data = cursor.fetchall()
        row = len(data)
        file = open('avg_score.txt', 'w', encoding = 'utf-8')
        for i in range(0, row):
            print("课程号：" + str(data[i][0]) + " 课程名称：" + data[i][1] + " 平均成绩：" + str(data[i][2]))
            file.write("课程号：" + str(data[i][0]) + " 课程名称：" + data[i][1] + " 平均成绩：" + str(data[i][2]) + '\n')
        file.close()

    def display(self, pages, sign):
        if sign == -2000000:
            self.sqlset = "" # achievement 信号
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        if self.sqlset == "":
            sql = "select * from achievement"
        else:
            sql = self.sqlset
        cursor.execute(sql)
        data = cursor.fetchall()
        row = len(data)
        self.pages[0] = self.pages[0] + sign
        if self.pages[0] * 8 < 0:
            self.pages[0] = 0
            num = 0
        elif self.pages[0] * 8 + 8 > row:
            self.pages[0] = self.pages[0] - 1
            num = max(row - 8, 0)
        else:
            num = self.pages[0] * 8
        str_pages = str(num)
        if self.sqlset == "":
            sql = "select student.sid, student.sname, course.csid, course.csname, achievement.score from student, course, achievement where student.sid = achievement.sid and course.csid = achievement.csid limit 8 offset " + str_pages
        else:
            sql = self.sqlset + " limit 8 offset " + str_pages
        cursor.execute(sql)
        data = cursor.fetchall()
        for j in range(1, min(9, row + 1)):
            for i in range(1, 6):
                local = i + (j - 1) * 5
                str_local = f"textBrowser_{local}"
                # 使用getattr动态获取对象
                textBrowser_obj = getattr(self, str_local, None)
                if textBrowser_obj is not None:
                # 确保对象存在且可被访问后进行操作
                    if i == 1 or i == 3 or i == 5:
                        textBrowser_obj.setText(str(data[j - 1][i - 1]))
                    else:
                        textBrowser_obj.setText(data[j - 1][i - 1])

    def change(self, local):
        text_local = f"textBrowser_{local * 5 - 4}"
        textBrowser_change_obj = getattr(self, text_local, None)
        stu_ID = textBrowser_change_obj.toPlainText()
        text_local2 = f"textBrowser_{local * 5 - 2}"
        textBrowser_change_obj2 = getattr(self, text_local2, None)
        course_ID = textBrowser_change_obj2.toPlainText()
        self.close()
        os.system("python call_change_achievement.py " + stu_ID + " " + course_ID)

    def delete(self, local):
        text_local = f"textBrowser_{local * 5 - 4}"
        textBrowser_change_obj = getattr(self, text_local, None)
        stu_ID = textBrowser_change_obj.toPlainText()
        text_local2 = f"textBrowser_{local * 5 - 2}"
        textBrowser_change_obj2 = getattr(self, text_local2, None)
        course_ID = textBrowser_change_obj2.toPlainText()
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        sql = "delete from achievement where sid = " + stu_ID + " and csid = " + course_ID
        cursor.execute(sql)
        conn.commit()
        self.close()
        os.system("python call_delete_hint.py call_stu_achievement")

    def basicButton(self):
        self.close()
        os.system("python call_stu_basic.py")

    def classButton(self):
        self.close()
        os.system("python call_stu_class.py")

    def courseButton(self):
        self.close()
        os.system("python call_stu_course.py")

    def rpButton(self):
        self.close()
        os.system("python call_stu_rp.py")

    def checkButton(self):
        self.close()
        os.system("python call_select_achievement.py")

    def addButton(self):
        self.close()
        os.system("python call_add_achievement.py")

    def display_check(self):
        # 由于 call_select_achievement.py 的限制，这里至少有一个参数
        sql = "select achievement.sid, student.sname, achievement.csid, course.csname, achievement.score from achievement, student, course where achievement.sid = student.sid and achievement.csid = course.csid "
        if sys.argv[1] != "achievement.sid=":
            sql = sql + " and " + sys.argv[1]
        if sys.argv[2] != "student.sname=''":
            tempargv = "student.sname like '%" + sys.argv[2][15:len(sys.argv[2]) - 1] + "%'"
            sql = sql + " and " + tempargv
        if sys.argv[3] != "achievement.csid=":
            sql = sql + " and " + sys.argv[3]
        if sys.argv[4] != "course.csname=''":
            tempargv = "course.csname like '%" + sys.argv[4][15:len(sys.argv[4]) - 1] + "%'"
            sql = sql + " and " + tempargv
        if sys.argv[5] != "achievement.score=":
            sql = sql + " and " + sys.argv[5]
        self.sqlset = sql
        self.display(self.pages, -1000000)

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = Stu_achievementUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
