#导入程序运行必须模块
import sys
import os
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from select_department import Ui_Form

class Select_DeUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Select_DeUIForm, self).__init__(parent)
        self.setupUi(self)
        self.check_Button.clicked.connect(self.check)

    def check(self):
        Department_ID = self.lineEdit_1.text()
        Department_name = self.lineEdit_2.text()
        try:
            if Department_ID != "":
                Department_ID_int = int(Department_ID)
        except (ValueError or TypeError) as err_message:
            print(err_message)
            return 
        if Department_ID == "" and Department_name == "":
            print("请输入信息！")
        else:
            self.close()
            Department_ID = " Department.did=" + Department_ID
            Department_name = " Department.dname='" + Department_name + "'"
            os.system("python call_department.py" + Department_ID + Department_name)

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = Select_DeUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
