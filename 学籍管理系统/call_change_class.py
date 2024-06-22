#导入程序运行必须模块
import sys
import pymysql
import os
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from change_class import Ui_Form

class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        self.class_ID_before = ""
        self.class_name_before = ""
        self.class_pname_before = ""
        self.if_change = 0
        if len(sys.argv) > 1:
            sql = "select * from class left join pro on class.pid = pro.pid where class.cid = " + sys.argv[1]
            cursor.execute(sql)
            data = cursor.fetchall()
            self.cid_lineEdit.setText(str(data[0][0]))
            self.cname_lineEdit.setText(data[0][1])
            self.num_textBrowser.setText(str(data[0][2]))
            self.pname_lineEdit.setText(data[0][5])
            self.class_ID_before = str(data[0][0])
            self.class_name_before = data[0][1]
            self.class_pname_before = data[0][5]
            self.if_change = 1
        self.commitButton.clicked.connect(self.commit)
        self.rollbackButton.clicked.connect(self.rollback)

    def commit(self):
        if self.if_change == 0:
            return
        class_ID = self.cid_lineEdit.text()
        class_name = self.cname_lineEdit.text()
        class_pname = self.pname_lineEdit.text()
        if class_ID == self.class_ID_before and class_name == self.class_name_before and class_pname == self.class_pname_before:
            return
        conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
        cursor = conn.cursor()
        sql = "use student_sys_db"
        cursor.execute(sql)
        if class_ID != self.class_ID_before:
            if class_ID.isdigit() == False:
                print("班级编号只能包含数字！")
                return
            sql = "select * from class where cid = " + class_ID
            cursor.execute(sql)
            data = cursor.fetchall()
            row = len(data)
            if row != 0:
                print("班级编号不可相同！")
                return
            sql = "call Update_class(" + self.class_ID_before + "," + class_ID + ")"
            cursor.execute(sql)
        sql = "update class set cname = '" + class_name + "' where cid = " + class_ID
        cursor.execute(sql)
        sql = "select * from pro where pname = '" + class_pname + "'"
        cursor.execute(sql)
        data = cursor.fetchall()
        row = len(data)
        if row == 0:
            print("专业不存在！")
            return
        else:
            sql = "select pid, pname from pro where pname = '" + class_pname + "'"
            cursor.execute(sql)
            data1 = cursor.fetchall()
            sql = "select pid, pname from pro where pname = '" + self.class_pname_before + "'"
            cursor.execute(sql)
            data2 = cursor.fetchall()
            sql = "update class set class.pid = " + str(data1[0][0]) + " where class.pid = " + str(data2[0][0]) + " and class.cid = " + class_ID
            cursor.execute(sql)
        conn.commit()
        self.close()
        os.system("python call_stu_class.py")

    def rollback(self):
        self.close()
        os.system("python call_stu_class.py")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MyMainForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
