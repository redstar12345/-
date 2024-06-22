#导入程序运行必须模块
import sys
import pymysql
import os
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from change_achievement import Ui_Form

class change_achievementUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(change_achievementUIForm, self).__init__(parent)
        self.setupUi(self)
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        self.stu_ID = ""
        self.course_ID = ""
        self.score_before = ""
        self.if_change = 0
        if len(sys.argv) > 1:
            sql = "select achievement.sid, student.sname, achievement.csid, course.csname, achievement.score from achievement, student, course where achievement.sid = student.sid and achievement.csid = course.csid and achievement.sid = " + sys.argv[1] + " and achievement.csid = " + sys.argv[2]
            cursor.execute(sql)
            data = cursor.fetchall()
            self.textBrowser.setText(str(data[0][0]))
            self.textBrowser_2.setText(data[0][1])
            self.textBrowser_3.setText(str(data[0][2]))
            self.textBrowser_4.setText(data[0][3])
            self.lineEdit_5.setText(str(data[0][4]))
            self.stu_ID = str(data[0][0])
            self.course_ID = str(data[0][2])
            self.score_before = str(data[0][4])
            self.if_change = 1
        self.pushButton.clicked.connect(self.commit)
        self.pushButton_2.clicked.connect(self.rollback)

    def commit(self):
        if self.if_change == 0:
            return
        score = self.lineEdit_5.text()
        if score == self.score_before:
            return
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        if score != self.score_before:
            if score.isdigit() == False:
                print("分数只能包含数字！")
                return
            if int(score) > 100 or int(score) < 0:
                print("分数值不符合区间[0, 100]！")
                return
            sql = "select * from achievement where sid = " + self.stu_ID + " and csid = " + self.course_ID
        sql = "update achievement set score = " + score + " where sid = " + self.stu_ID + " and csid = " + self.course_ID
        cursor.execute(sql)
        conn.commit()
        self.close()
        os.system("python call_stu_achievement.py")

    def rollback(self):
        self.close()
        os.system("python call_stu_achievement.py")


if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = change_achievementUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())