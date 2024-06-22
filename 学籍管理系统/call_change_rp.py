import sys
import pymysql
import os
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from change_rp import Ui_Form

class changeUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(changeUIForm, self).__init__(parent)
        self.setupUi(self)
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        self.rp_ID_before = ""
        self.rp_stu_ID_before = ""
        self.rp_rpname_before = ""
        self.rp_period_before = ""
        self.if_change = 0
        if len(sys.argv) > 1:
            sql = "select * from rewards_punishment where rpid = " + sys.argv[1]
            cursor.execute(sql)
            data = cursor.fetchall()
            self.rpid_lineEdit.setText(str(data[0][0]))
            self.sid_lineEdit.setText(str(data[0][1]))
            self.rpname_lineEdit.setText(data[0][2])
            self.rpperiod_lineEdit.setText(data[0][3])
            self.rp_ID_before = str(data[0][0])
            self.rp_stu_ID_before = str(data[0][0])
            self.rp_rpname_before = data[0][2]
            self.rp_period_before = data[0][3]
            self.if_change = 1
        self.commitButton.clicked.connect(self.commit)
        self.rollbackButton.clicked.connect(self.rollback)

    def commit(self):
        if self.if_change == 0:
            return
        rp_ID = self.rpid_lineEdit.text()
        rp_stu_ID = self.sid_lineEdit.text()
        rp_rpname = self.rpname_lineEdit.text()
        rp_period = self.rpperiod_lineEdit.text()
        if rp_ID == self.rp_ID_before and rp_stu_ID == self.rp_stu_ID_before and rp_rpname == self.rp_rpname_before and rp_period == self.rp_period_before:
            return
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        if rp_ID != self.rp_ID_before:
            if rp_ID.isdigit() == False:
                print("奖惩编号只能包含数字！")
                return
            sql = "select * from rewards_punishment where rpid = " + rp_ID
            cursor.execute(sql)
            data = cursor.fetchall()
            row = len(data)
            if row != 0:
                print("奖惩编号不可相同！")
                return
        if rp_stu_ID.isdigit() == False:
            print("学号只能包含数字！")
            return
        sql = "update rewards_punishment set rpid = " + rp_ID + " where rpid = " + self.rp_ID_before
        cursor.execute(sql)
        sql = "update rewards_punishment set sid = " + rp_stu_ID + " where rpid = " + rp_ID
        cursor.execute(sql)
        sql = "update rewards_punishment set rpname = '" + rp_rpname + "' where rpid = " + rp_ID
        cursor.execute(sql)
        sql = "update rewards_punishment set rpperiod = '" + rp_period + "' where rpid = " + rp_ID
        cursor.execute(sql)
        conn.commit()
        self.close()
        os.system("python call_stu_rp.py")

    def rollback(self):
        self.close()
        os.system("python call_stu_rp.py")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = changeUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
