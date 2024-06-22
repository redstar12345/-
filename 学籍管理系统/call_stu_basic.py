import sys
from datetime import date
import pymysql
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from stu_basic import Ui_Form
import os

class Stu_basicUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Stu_basicUIForm, self).__init__(parent)
        self.setupUi(self)
        self.sqlset = ""
        self.pages = [0]
        self.pages[0] = 0
        self.username = ""
        if len(sys.argv) == 1:
            self.display(self, -2000000)
        else:
            self.display_check()
        self.basic_BUTTON.clicked.connect(lambda: self.display(self.pages, -2000000))
        self.class_BUTTON.clicked.connect(self.classButton)
        self.rp_BUTTON.clicked.connect(self.rpButton)
        self.course_BUTTON.clicked.connect(self.courseButton)
        self.achievement_BUTTON.clicked.connect(self.achievementButton)
        self.nextpage_BUTTON.clicked.connect(lambda: self.display(self.pages, 1))
        self.lastpage_BUTTON.clicked.connect(lambda: self.display(self.pages, -1))
        self.check_BUTTON.clicked.connect(self.checkButton)
        self.add_BUTTON.clicked.connect(self.addButton)
        self.change_login_Button.clicked.connect(self.changeloginButton)
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        if self.sqlset == "":
            sql = "select * from student"
        else:
            sql = self.sqlset
        cursor.execute(sql)
        data = cursor.fetchall()
        row = len(data)
        for k in range(1, min(9, row + 1)):
            button_local = f"change_BUTTON{k}"
            button_obj = getattr(self, button_local, None)
            if button_obj is not None:
                button_obj.clicked.connect(lambda _, k = k: self.change(k))
        for k in range(1, min(9, row + 1)):
            button_local = f"delete_BUTTON{k}"
            button_obj = getattr(self, button_local, None)
            if button_obj is not None:
                button_obj.clicked.connect(lambda _, k = k: self.delete(k))

    def display(self, pages, sign):
        if sign == -2000000:
            self.sqlset = "" # basic 信号
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        if self.sqlset == "":
            sql = "select * from student"
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
            sql = "select student.sid, student.sname, student.sex, student.birth, student.entry, class.cname from student left join class on student.cid = class.cid limit 8 offset " + str_pages
        else:
            sql = self.sqlset + " limit 8 offset " + str_pages
        cursor.execute(sql)
        data = cursor.fetchall()
        for j in range(1, min(9, row + 1)):
            for i in range(1, 7):
                local = i + (j - 1) * 6
                str_local = f"textBrowser_{local}"
                # 使用getattr动态获取对象
                textBrowser_obj = getattr(self, str_local, None)
                if textBrowser_obj is not None:
                # 确保对象存在且可被访问后进行操作
                    if i == 1:
                        textBrowser_obj.setText(str(data[j - 1][i - 1]))
                    elif i == 4 or i == 5:
                        textBrowser_obj.setText(data[j - 1][i - 1].strftime("%Y-%m-%d"))
                    else:
                        textBrowser_obj.setText(data[j - 1][i - 1])

    def change(self, local):
        text_local = f"textBrowser_{local * 6 - 5}"
        textBrowser_change_obj = getattr(self, text_local, None)
        student_ID = textBrowser_change_obj.toPlainText()
        self.close()
        os.system("python call_change_student.py " + student_ID)
    
    def delete(self, local):
        text_local = f"textBrowser_{local * 6 - 5}"
        textBrowser_change_obj = getattr(self, text_local, None)
        student_ID = textBrowser_change_obj.toPlainText()
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        sql = "select * from achievement where sid = " + student_ID
        cursor.execute(sql)
        data = cursor.fetchall()
        row = len(data)
        if row != 0:
            print("外键约束！数据不可删除！")
            return
        sql = "select * from rewards_punishment where sid = " + student_ID
        cursor.execute(sql)
        data = cursor.fetchall()
        row = len(data)
        if row != 0:
            print("外键约束！数据不可删除！")
            return
        sql = "delete from student where sid = " + student_ID
        cursor.execute(sql)
        conn.commit()
        self.close()
        os.system("python call_delete_hint.py call_stu_basic")

    def achievementButton(self):
        self.close()
        os.system("python call_stu_achievement.py")

    def classButton(self):
        self.close()
        os.system("python call_stu_class.py")

    def rpButton(self):
        self.close()
        os.system("python call_stu_rp.py")

    def courseButton(self):
        self.close()
        os.system("python call_stu_course.py")

    def checkButton(self):
        self.close()
        os.system("python call_select_student.py")

    def addButton(self):
        self.close()
        os.system("python call_add_student.py")

    def changeloginButton(self):
        self.close()
        os.system("python call_login_in.py")

    def display_check(self):
        # 由于 call_select_student.py 的限制，这里至少有一个参数
        if_and = False
        sql = "select student.sid, student.sname, student.sex, student.birth, student.entry, class.cname from student left join class on student.cid = class.cid where "
        if sys.argv[1] != "student.sid=":
            if if_and == False:
                sql = sql + sys.argv[1]
                if_and = True
            else:
                sql = sql + " and " + sys.argv[1]
        if sys.argv[2] != "student.sname=''":
            if if_and == False:
                tempargv = "student.sname like '%" + sys.argv[2][15:len(sys.argv[2]) - 1] + "%'"
                sql = sql + tempargv
                if_and = True
            else:
                tempargv = "student.sname like'%" + sys.argv[2][15:len(sys.argv[2]) - 1] + "%'"
                sql = sql + " and " + tempargv
        if sys.argv[3] != "student.sex=''":
            if if_and == False:
                sql = sql + sys.argv[3]
                if_and = True
            else:
                sql = sql + " and " + sys.argv[3]
        if sys.argv[4] != "student.birth=''":
            if if_and == False:
                sql = sql + sys.argv[4]
                if_and = True
            else:
                sql = sql + " and " + sys.argv[4]
        if sys.argv[5] != "student.entry=''":
            if if_and == False:
                sql = sql + sys.argv[5]
                if_and = True
            else:
                sql = sql + " and " + sys.argv[5]
        if sys.argv[6] != "class.cname=''":
            if if_and == False:
                tempargv = "class.cname like '%" + sys.argv[6][13:len(sys.argv[6]) - 1] + "%'"
                sql = sql + tempargv
                if_and = True
            else:
                tempargv = "class.cname like'%" + sys.argv[6][13:len(sys.argv[6]) - 1] + "%'"
                sql = sql + " and " + tempargv
        self.sqlset = sql
        self.display(self.pages, -1000000)

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin =Stu_basicUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())