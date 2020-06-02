# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tool_gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(394, 292)
        self.pushButton_ok = QtWidgets.QPushButton(Dialog)
        self.pushButton_ok.setGeometry(QtCore.QRect(150, 210, 99, 27))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.lineEdit_name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_name.setGeometry(QtCore.QRect(150, 60, 113, 27))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_age = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_age.setGeometry(QtCore.QRect(150, 140, 113, 27))
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.label_name = QtWidgets.QLabel(Dialog)
        self.label_name.setGeometry(QtCore.QRect(70, 60, 67, 17))
        self.label_name.setObjectName("label_name")
        self.label_sexual = QtWidgets.QLabel(Dialog)
        self.label_sexual.setGeometry(QtCore.QRect(70, 100, 67, 17))
        self.label_sexual.setObjectName("label_sexual")
        self.label_age = QtWidgets.QLabel(Dialog)
        self.label_age.setGeometry(QtCore.QRect(70, 140, 67, 17))
        self.label_age.setObjectName("label_age")
        self.label_savepath = QtWidgets.QLabel(Dialog)
        self.label_savepath.setGeometry(QtCore.QRect(150, 250, 181, 21))
        self.label_savepath.setObjectName("label_savepath")
        self.pushButton_browse = QtWidgets.QPushButton(Dialog)
        self.pushButton_browse.setGeometry(QtCore.QRect(260, 210, 31, 31))
        self.pushButton_browse.setObjectName("pushButton_browse")
        self.comboBox_sexual = QtWidgets.QComboBox(Dialog)
        self.comboBox_sexual.setGeometry(QtCore.QRect(150, 100, 85, 27))
        self.comboBox_sexual.setObjectName("comboBox_sexual")
        self.comboBox_sexual.addItem("")
        self.comboBox_sexual.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_ok.setText(_translate("Dialog", "Ok"))
        self.label_name.setText(_translate("Dialog", "Name"))
        self.label_sexual.setText(_translate("Dialog", "Sexual"))
        self.label_age.setText(_translate("Dialog", "Age"))
        self.label_savepath.setText(_translate("Dialog", "Save Path"))
        self.pushButton_browse.setText(_translate("Dialog", "..."))
        self.comboBox_sexual.setItemText(0, _translate("Dialog", "male"))
        self.comboBox_sexual.setItemText(1, _translate("Dialog", "female"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
