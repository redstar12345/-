# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_pro.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(496, 219)
        Form.setMinimumSize(QtCore.QSize(496, 219))
        Form.setMaximumSize(QtCore.QSize(496, 219))
        self.pid_lineEdit = QtWidgets.QLineEdit(Form)
        self.pid_lineEdit.setGeometry(QtCore.QRect(50, 60, 131, 31))
        self.pid_lineEdit.setObjectName("pid_lineEdit")
        self.pname_lineEdit = QtWidgets.QLineEdit(Form)
        self.pname_lineEdit.setGeometry(QtCore.QRect(180, 60, 131, 31))
        self.pname_lineEdit.setObjectName("pname_lineEdit")
        self.commitButton = QtWidgets.QPushButton(Form)
        self.commitButton.setGeometry(QtCore.QRect(60, 130, 151, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.commitButton.setFont(font)
        self.commitButton.setObjectName("commitButton")
        self.rollbackButton = QtWidgets.QPushButton(Form)
        self.rollbackButton.setGeometry(QtCore.QRect(310, 130, 151, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.rollbackButton.setFont(font)
        self.rollbackButton.setObjectName("rollbackButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(180, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(310, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.dname_textBrowser = QtWidgets.QTextBrowser(Form)
        self.dname_textBrowser.setGeometry(QtCore.QRect(310, 60, 161, 31))
        self.dname_textBrowser.setObjectName("dname_textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "专业信息修改"))
        self.commitButton.setText(_translate("Form", "提交修改"))
        self.rollbackButton.setText(_translate("Form", "撤销修改"))
        self.label.setText(_translate("Form", "专业编号"))
        self.label_2.setText(_translate("Form", "专业名称"))
        self.label_3.setText(_translate("Form", "院系名称"))
