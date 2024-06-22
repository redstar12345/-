#导入程序运行必须模块
import sys
import os
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from select_pro import Ui_Form

class Select_proUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Select_proUIForm, self).__init__(parent)
        self.setupUi(self)
        self.check_Button.clicked.connect(self.check)
        self.back_Button.clicked.connect(self.back)

    def check(self):
        pro_ID = self.lineEdit_1.text()
        pro_name = self.lineEdit_2.text()
        pro_department_name = self.lineEdit_3.text()
        try:
            if pro_ID != "":
                pro_ID_int = int(pro_ID)
        except (ValueError or TypeError) as err_message:
            print(err_message)
            return 
        if pro_ID == "" and pro_name == "" and pro_department_name == "":
            print("请输入信息！")
        else:
            self.close()
            pro_ID = " pro.pid=" + pro_ID
            pro_name = " pro.pname='" + pro_name + "'"
            pro_department_name = " Department.dname='" + pro_department_name + "'"
            os.system("python call_promessage.py" + pro_ID + pro_name +  pro_department_name)

    def back(self):
        self.close()
        os.system("python call_promessage.py")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = Select_proUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
