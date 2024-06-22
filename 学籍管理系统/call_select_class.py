#导入程序运行必须模块
import sys
from datetime import datetime
import os
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from select_class import Ui_Form

class Select_classUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Select_classUIForm, self).__init__(parent)
        self.setupUi(self)
        self.check_Button.clicked.connect(self.check)
        self.back_Button.clicked.connect(self.back)

    def check(self):
        class_ID = self.lineEdit_1.text()
        class_name = self.lineEdit_2.text()
        class_num = self.lineEdit_3.text()
        class_proname = self.lineEdit_4.text()
        try:
            if class_ID != "":
                class_ID_int = int(class_ID)
            if class_num != "":
                class_num_int = int(class_num)
        except (ValueError or TypeError) as err_message:
            print(err_message)
            return 
        if class_ID == "" and class_name == "" and class_num == "" and class_proname == "":
            print("请输入信息！")
        else:
            self.close()
            class_ID = " class.cid=" + class_ID
            class_name = " class.cname='" + class_name + "'"
            class_num = " class.num=" + class_num
            class_proname = " pro.pname='" + class_proname + "'"
            os.system("python call_stu_class.py" + class_ID + class_name +  class_num + class_proname)

    def back(self):
        self.close()
        os.system("python call_stu_class.py")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = Select_classUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
