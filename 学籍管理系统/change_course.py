# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_course.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(615, 219)
        Form.setMinimumSize(QtCore.QSize(615, 219))
        Form.setMaximumSize(QtCore.QSize(615, 219))
        self.lineEdit_1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_1.setGeometry(QtCore.QRect(50, 60, 131, 31))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 60, 131, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 60, 131, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(440, 60, 131, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 130, 151, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 130, 151, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(180, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(310, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(440, 20, 91, 21))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "课程信息修改"))
        self.pushButton.setText(_translate("Form", "提交修改"))
        self.pushButton_2.setText(_translate("Form", "撤销修改"))
        self.label.setText(_translate("Form", "课程号"))
        self.label_2.setText(_translate("Form", "名称"))
        self.label_3.setText(_translate("Form", "学时"))
        self.label_4.setText(_translate("Form", "学分"))
