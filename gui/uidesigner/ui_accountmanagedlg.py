# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uitemplate/accountmanagedlg.ui'
#
# Created: Fri Dec 12 18:18:29 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AccountDLG(object):
    def setupUi(self, AccountDLG):
        AccountDLG.setObjectName(_fromUtf8("AccountDLG"))
        AccountDLG.resize(566, 401)
        self.verticalLayout_6 = QtGui.QVBoxLayout(AccountDLG)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(AccountDLG)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tWAccounts = TaskTableWidget(self.groupBox)
        self.tWAccounts.setObjectName(_fromUtf8("tWAccounts"))
        self.tWAccounts.setColumnCount(4)
        self.tWAccounts.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tWAccounts.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tWAccounts.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tWAccounts.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tWAccounts.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.tWAccounts)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.gBTaskinfo = QtGui.QGroupBox(AccountDLG)
        self.gBTaskinfo.setObjectName(_fromUtf8("gBTaskinfo"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.gBTaskinfo)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.gBTaskinfo)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lEAccount = QtGui.QLineEdit(self.gBTaskinfo)
        self.lEAccount.setObjectName(_fromUtf8("lEAccount"))
        self.horizontalLayout.addWidget(self.lEAccount)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.gBTaskinfo)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lEPasswd = QtGui.QLineEdit(self.gBTaskinfo)
        self.lEPasswd.setEchoMode(QtGui.QLineEdit.Password)
        self.lEPasswd.setObjectName(_fromUtf8("lEPasswd"))
        self.horizontalLayout_2.addWidget(self.lEPasswd)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.gBTaskinfo)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lEGovId = QtGui.QLineEdit(self.gBTaskinfo)
        self.lEGovId.setObjectName(_fromUtf8("lEGovId"))
        self.horizontalLayout_4.addWidget(self.lEGovId)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_4 = QtGui.QLabel(self.gBTaskinfo)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lEPhoneNumber = QtGui.QLineEdit(self.gBTaskinfo)
        self.lEPhoneNumber.setObjectName(_fromUtf8("lEPhoneNumber"))
        self.horizontalLayout_5.addWidget(self.lEPhoneNumber)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_5.addWidget(self.gBTaskinfo)
        self.groupBox_2 = QtGui.QGroupBox(AccountDLG)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.pBAdd = QtGui.QPushButton(self.groupBox_2)
        self.pBAdd.setObjectName(_fromUtf8("pBAdd"))
        self.horizontalLayout_7.addWidget(self.pBAdd)
        self.pBImportfromfile = QtGui.QPushButton(self.groupBox_2)
        self.pBImportfromfile.setObjectName(_fromUtf8("pBImportfromfile"))
        self.horizontalLayout_7.addWidget(self.pBImportfromfile)
        self.pBClear = QtGui.QPushButton(self.groupBox_2)
        self.pBClear.setObjectName(_fromUtf8("pBClear"))
        self.horizontalLayout_7.addWidget(self.pBClear)
        self.pBOk = QtGui.QPushButton(self.groupBox_2)
        self.pBOk.setObjectName(_fromUtf8("pBOk"))
        self.horizontalLayout_7.addWidget(self.pBOk)
        self.pBCancel = QtGui.QPushButton(self.groupBox_2)
        self.pBCancel.setObjectName(_fromUtf8("pBCancel"))
        self.horizontalLayout_7.addWidget(self.pBCancel)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.retranslateUi(AccountDLG)
        QtCore.QObject.connect(self.pBAdd, QtCore.SIGNAL(_fromUtf8("clicked()")), AccountDLG.addAccount)
        QtCore.QObject.connect(self.pBClear, QtCore.SIGNAL(_fromUtf8("clicked()")), AccountDLG.clear)
        QtCore.QObject.connect(self.pBOk, QtCore.SIGNAL(_fromUtf8("clicked()")), AccountDLG.accept)
        QtCore.QObject.connect(self.pBCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), AccountDLG.reject)
        QtCore.QObject.connect(self.pBImportfromfile, QtCore.SIGNAL(_fromUtf8("clicked()")), AccountDLG.importFromFile)
        QtCore.QMetaObject.connectSlotsByName(AccountDLG)

    def retranslateUi(self, AccountDLG):
        AccountDLG.setWindowTitle(_translate("AccountDLG", "账户管理", None))
        self.groupBox.setTitle(_translate("AccountDLG", "账户", None))
        item = self.tWAccounts.horizontalHeaderItem(0)
        item.setText(_translate("AccountDLG", "AppleID", None))
        item = self.tWAccounts.horizontalHeaderItem(1)
        item.setText(_translate("AccountDLG", "密码", None))
        item = self.tWAccounts.horizontalHeaderItem(2)
        item.setText(_translate("AccountDLG", "身份证号码", None))
        item = self.tWAccounts.horizontalHeaderItem(3)
        item.setText(_translate("AccountDLG", "手机号码", None))
        self.gBTaskinfo.setTitle(_translate("AccountDLG", "添加账户", None))
        self.label.setText(_translate("AccountDLG", "账户ID:", None))
        self.label_2.setText(_translate("AccountDLG", "密码：", None))
        self.label_3.setText(_translate("AccountDLG", "身份证号：", None))
        self.label_4.setText(_translate("AccountDLG", "手机号：", None))
        self.pBAdd.setText(_translate("AccountDLG", "添加", None))
        self.pBImportfromfile.setText(_translate("AccountDLG", "从文件导入", None))
        self.pBClear.setText(_translate("AccountDLG", "清空", None))
        self.pBOk.setText(_translate("AccountDLG", "确定", None))
        self.pBCancel.setText(_translate("AccountDLG", "取消", None))

from tasktablewidget import TaskTableWidget
