#导入程序运行必须模块
import sys
import pymysql
import os
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from change_department import Ui_Form

class change_departmentUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(change_departmentUIForm, self).__init__(parent)
        self.setupUi(self)
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        self.department_ID_before = ""
        self.department_name_before = ""
        self.if_change = 0
        if len(sys.argv) > 1:
            sql = "select * from Department where did = " + sys.argv[1]
            cursor.execute(sql)
            data = cursor.fetchall()
            self.did_lineEdit.setText(str(data[0][0]))
            self.dname_lineEdit.setText(data[0][1])
            self.department_ID_before = str(data[0][0])
            self.department_name_before = data[0][1]
            self.if_change = 1
        self.commitButton.clicked.connect(self.commit)
        self.rollbackButton.clicked.connect(self.rollback)

    def commit(self):
        if self.if_change == 0:
            return
        department_ID = self.did_lineEdit.text()
        department_name = self.dname_lineEdit.text()
        if department_ID == self.department_ID_before and department_name == self.department_name_before:
            return
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        if department_ID != self.department_ID_before:
            if department_ID.isdigit() == False:
                print("院系编号只能包含数字！")
                return
            sql = "select * from Department where did = " + department_ID
            cursor.execute(sql)
            data = cursor.fetchall()
            row = len(data)
            if row != 0:
                print("院系编号不可相同！")
                return
            sql = "call Update_Department(" + self.department_ID_before + "," + department_ID + ")"
            cursor.execute(sql)
        sql = "update department set dname = '" + department_name + "' where did = " + department_ID
        cursor.execute(sql)
        conn.commit()
        self.close()
        os.system("python call_department.py")

    def rollback(self):
        self.close()
        os.system("python call_department.py")


if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = change_departmentUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
