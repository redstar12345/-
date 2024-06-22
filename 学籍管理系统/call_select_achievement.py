#导入程序运行必须模块
import sys
from datetime import datetime
import os
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from select_achievement import Ui_Form

class Select_achievementUIForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(Select_achievementUIForm, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.check)
        self.pushButton_2.clicked.connect(self.back)

    def check(self):
        achievement_stu_ID = self.lineEdit_1.text()
        achievement_stu_name = self.lineEdit_2.text()
        achievement_course_ID = self.lineEdit_3.text()
        achievement_course_name = self.lineEdit_4.text()
        achievement_score = self.lineEdit_5.text()
        try:
            if achievement_stu_ID != "":
                achievement_stu_ID_int = int(achievement_stu_ID)
            if achievement_course_ID != "":
                achievement_course_ID_int = int(achievement_course_ID)
            if achievement_score != "":
                achievement_score_int = int(achievement_score)
        except (ValueError or TypeError) as err_message:
            print(err_message)
            return 
        if achievement_stu_ID == "" and achievement_stu_name == "" and achievement_course_ID == "" and achievement_course_ID == "" and achievement_course_name == "" and achievement_score == "":
            print("请输入信息！")
        else:
            self.close()
            achievement_stu_ID = " achievement.sid=" + achievement_stu_ID
            achievement_stu_name = " student.sname='" + achievement_stu_name + "'"
            achievement_course_ID = " achievement.csid=" + achievement_course_ID
            achievement_course_name = " course.csname='" + achievement_course_name + "'"
            achievement_score = " achievement.score=" + achievement_score
            os.system("python call_stu_achievement.py" + achievement_stu_ID + achievement_stu_name +  achievement_course_ID + achievement_course_name + achievement_score)

    def back(self):
        self.close()
        os.system("python call_stu_achievement.py")

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = Select_achievementUIForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())