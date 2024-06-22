import sys
import pymysql
from datetime import datetime
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from add_class import Ui_Form
import os
 
class Add_classUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Add_classUIForm, self).__init__(parent)
        self.setupUi(self)
        self.textBrowser.setText("0")
        #添加登录按钮信号
        self.commit_Button.clicked.connect(self.Insert)
        self.back_Button.clicked.connect(self.back)

    def Insert(self):
        class_ID = self.lineEdit_1.text()
        class_name = self.lineEdit_2.text()
        class_proname = self.lineEdit_4.text()
        try:
            if class_ID != "":
                class_ID_int = int(class_ID)
        except (ValueError or TypeError) as err_message:
            print(err_message)
            return
        if class_ID == "" or class_name == "" or class_proname == "":
            print("请输入完整信息！")
        else:
            conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
            cursor = conn.cursor()
            sql = "use student_sys_db"
            cursor.execute(sql)
            sql = "select * from class where cid = " + class_ID
            cursor.execute(sql)
            data = cursor.fetchall()
            row = len(data)
            if row != 0:
                print("信息重复！请重新输入或退出！")
                return
            sql = "select * from pro where pname = '" + class_proname + "'"
            cursor.execute(sql)
            data = cursor.fetchall()
            row = len(data)
            if row == 0:
                print("专业不存在！请检查输入！")
                return
            else:
                pro_ID = str(data[0][0])
            sql = "insert into class(cid, cname, num, pid) values(" + class_ID + ", '" + class_name + "', 0, " + pro_ID + ")"
            cursor.execute(sql)
            conn.commit()
            self.close()
            os.system("python call_stu_class.py")

    def back(self):
        self.close()
        os.system("python call_stu_class.py")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = Add_classUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
