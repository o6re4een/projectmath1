# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Artem\PycharmProjects\mathgame\test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form2(object):
    def setupUi(self, form2):
        form2.setObjectName("form2")
        form2.resize(981, 588)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(form2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.stackedWidget = QtWidgets.QStackedWidget(form2)
        self.stackedWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(800, 250))
        self.stackedWidget.setBaseSize(QtCore.QSize(10, 50))
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.HLine)
        self.stackedWidget.setObjectName("stackedWidget")
        self.quest1 = QtWidgets.QWidget()
        self.quest1.setObjectName("quest1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.quest1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.qt1 = QtWidgets.QLabel(self.quest1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qt1.sizePolicy().hasHeightForWidth())
        self.qt1.setSizePolicy(sizePolicy)
        self.qt1.setStyleSheet("")
        self.qt1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qt1.setLineWidth(0)
        self.qt1.setText("")
        self.qt1.setPixmap(QtGui.QPixmap("z1.png"))
        self.qt1.setScaledContents(False)
        self.qt1.setAlignment(QtCore.Qt.AlignCenter)
        self.qt1.setWordWrap(False)
        self.qt1.setIndent(0)
        self.qt1.setOpenExternalLinks(False)
        self.qt1.setObjectName("qt1")
        self.verticalLayout_2.addWidget(self.qt1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.ans1 = QtWidgets.QLineEdit(self.quest1)
        self.ans1.setObjectName("ans1")
        self.verticalLayout_2.addWidget(self.ans1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.stackedWidget.addWidget(self.quest1)
        self.quest2 = QtWidgets.QWidget()
        self.quest2.setObjectName("quest2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.quest2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem3)
        self.qt2 = QtWidgets.QLabel(self.quest2)
        self.qt2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.qt2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qt2.setLineWidth(0)
        self.qt2.setMidLineWidth(0)
        self.qt2.setText("")
        self.qt2.setPixmap(QtGui.QPixmap("z2.png"))
        self.qt2.setAlignment(QtCore.Qt.AlignCenter)
        self.qt2.setObjectName("qt2")
        self.verticalLayout_5.addWidget(self.qt2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem4)
        self.ans2 = QtWidgets.QLineEdit(self.quest2)
        self.ans2.setObjectName("ans2")
        self.verticalLayout_5.addWidget(self.ans2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem5)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.stackedWidget.addWidget(self.quest2)
        self.quest3 = QtWidgets.QWidget()
        self.quest3.setObjectName("quest3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.quest3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem6 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem6)
        self.qt3 = QtWidgets.QLabel(self.quest3)
        self.qt3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qt3.setLineWidth(0)
        self.qt3.setText("")
        self.qt3.setPixmap(QtGui.QPixmap("z3.png"))
        self.qt3.setAlignment(QtCore.Qt.AlignCenter)
        self.qt3.setObjectName("qt3")
        self.verticalLayout_7.addWidget(self.qt3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem7)
        self.ans3 = QtWidgets.QLineEdit(self.quest3)
        self.ans3.setObjectName("ans3")
        self.verticalLayout_7.addWidget(self.ans3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem8)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.stackedWidget.addWidget(self.quest3)
        self.quest4 = QtWidgets.QWidget()
        self.quest4.setObjectName("quest4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.quest4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_9.addItem(spacerItem9)
        self.qt4 = QtWidgets.QLabel(self.quest4)
        self.qt4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qt4.setLineWidth(0)
        self.qt4.setText("")
        self.qt4.setPixmap(QtGui.QPixmap("z4.png"))
        self.qt4.setAlignment(QtCore.Qt.AlignCenter)
        self.qt4.setObjectName("qt4")
        self.verticalLayout_9.addWidget(self.qt4)
        spacerItem10 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_9.addItem(spacerItem10)
        self.ans4 = QtWidgets.QLineEdit(self.quest4)
        self.ans4.setObjectName("ans4")
        self.verticalLayout_9.addWidget(self.ans4)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_9.addItem(spacerItem11)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.stackedWidget.addWidget(self.quest4)
        self.quest5 = QtWidgets.QWidget()
        self.quest5.setObjectName("quest5")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.quest5)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        spacerItem12 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_18.addItem(spacerItem12)
        self.qt5 = QtWidgets.QLabel(self.quest5)
        self.qt5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qt5.setLineWidth(0)
        self.qt5.setText("")
        self.qt5.setPixmap(QtGui.QPixmap("z5.png"))
        self.qt5.setAlignment(QtCore.Qt.AlignCenter)
        self.qt5.setIndent(0)
        self.qt5.setObjectName("qt5")
        self.verticalLayout_18.addWidget(self.qt5)
        spacerItem13 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_18.addItem(spacerItem13)
        self.ans5 = QtWidgets.QLineEdit(self.quest5)
        self.ans5.setObjectName("ans5")
        self.verticalLayout_18.addWidget(self.ans5)
        spacerItem14 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_18.addItem(spacerItem14)
        self.verticalLayout_19.addLayout(self.verticalLayout_18)
        self.stackedWidget.addWidget(self.quest5)
        self.verticalLayout_11.addWidget(self.stackedWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 150, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.qb1 = QtWidgets.QPushButton(form2)
        self.qb1.setObjectName("qb1")
        self.horizontalLayout.addWidget(self.qb1)
        self.qb2 = QtWidgets.QPushButton(form2)
        self.qb2.setObjectName("qb2")
        self.horizontalLayout.addWidget(self.qb2)
        self.qb3 = QtWidgets.QPushButton(form2)
        self.qb3.setObjectName("qb3")
        self.horizontalLayout.addWidget(self.qb3)
        self.qb4 = QtWidgets.QPushButton(form2)
        self.qb4.setObjectName("qb4")
        self.horizontalLayout.addWidget(self.qb4)
        self.qb5 = QtWidgets.QPushButton(form2)
        self.qb5.setStyleSheet("borderElement {\n"
"  background-color: #EEDDFF;\n"
"  border: 6px solid #7922CC;\n"
"  border-radius: 25px;\n"
"}")
        self.qb5.setObjectName("qb5")
        self.horizontalLayout.addWidget(self.qb5)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem15)
        self.save_a = QtWidgets.QPushButton(form2)
        self.save_a.setObjectName("save_a")
        self.horizontalLayout.addWidget(self.save_a)
        self.fin = QtWidgets.QPushButton(form2)
        self.fin.setObjectName("fin")
        self.horizontalLayout.addWidget(self.fin)
        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self.retranslateUi(form2)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(form2)

    def retranslateUi(self, form2):
        _translate = QtCore.QCoreApplication.translate
        form2.setWindowTitle(_translate("form2", "Form"))
        self.qb1.setText(_translate("form2", "1"))
        self.qb2.setText(_translate("form2", "2"))
        self.qb3.setText(_translate("form2", "3"))
        self.qb4.setText(_translate("form2", "4"))
        self.qb5.setText(_translate("form2", "5"))
        self.save_a.setText(_translate("form2", "Сохранить ответы"))
        self.fin.setText(_translate("form2", "Завершить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form2 = QtWidgets.QWidget()
    ui = Ui_form2()
    ui.setupUi(form2)
    form2.show()
    sys.exit(app.exec_())
