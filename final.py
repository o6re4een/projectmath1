# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Artem\PycharmProjects\mathgame\final.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form3(object):
    def setupUi(self, Form3):
        Form3.setObjectName("Form3")
        Form3.resize(472, 340)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Form3)
        QtCore.QMetaObject.connectSlotsByName(Form3)

    def retranslateUi(self, Form3):
        _translate = QtCore.QCoreApplication.translate
        Form3.setWindowTitle(_translate("Form3", "Form"))
        self.label.setText(_translate("Form3", "Ваша оценка:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form3 = QtWidgets.QWidget()
    ui = Ui_Form3()
    ui.setupUi(Form3)
    Form3.show()
    sys.exit(app.exec_())