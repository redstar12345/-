#导入程序运行必须模块
import sys
from datetime import datetime
import os
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from select_rp import Ui_Form

class Select_rpUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Select_rpUIForm, self).__init__(parent)
        self.setupUi(self)
        self.check_Button.clicked.connect(self.check)
        self.back_Button.clicked.connect(self.back)

    def check(self):
        rp_ID = self.lineEdit_1.text()
        rp_student_ID = self.lineEdit_2.text()
        rp_name = self.lineEdit_3.text()
        rp_period = self.lineEdit_4.text()
        try:
            if rp_ID != "":
                rp_ID_int = int(rp_ID)
            if rp_student_ID != "":
                rp_student_ID_int = int(rp_student_ID)
        except (ValueError or TypeError) as err_message:
            print(err_message)
            return 
        if rp_ID == "" and rp_student_ID == "" and rp_name == "" and rp_period == "":
            print("请输入信息！")
        else:
            self.close()
            rp_ID = " rewards_punishment.rpid=" + rp_ID
            rp_student_ID = " rewards_punishment.sid=" + rp_student_ID
            rp_name = " rewards_punishment.rpname='" + rp_name + "'"
            rp_period = " rewards_punishment.rpperiod='" + rp_period + "'"
            os.system("python call_stu_rp.py" + rp_ID + rp_student_ID +  rp_name + rp_period)

    def back(self):
        self.close()
        os.system("python call_stu_rp.py")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = Select_rpUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
