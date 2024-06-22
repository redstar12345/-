import sys
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from delete_hint import Ui_Form
import os
 
class Delete_hintUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Delete_hintUIForm, self).__init__(parent)
        self.setupUi(self)
        #添加登录按钮信号
        self.pushButton.clicked.connect(self.back)

    def back(self):# 根据传入参数确定返回哪一个UI
        if len(sys.argv) == 1:
            self.close()
            os.system("python call_stu_basic.py")
        cmd = "python " + sys.argv[1] + ".py"
        self.close()
        os.system(cmd)

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = Delete_hintUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
