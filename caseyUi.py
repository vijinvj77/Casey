# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caseyUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Casey(object):
    def setupUi(self, Casey):
        Casey.setObjectName("Casey")
        Casey.resize(1621, 872)
        self.centralwidget = QtWidgets.QWidget(Casey)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1621, 871))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("background.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1621, 871))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("foreground.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 800, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: #82EEFD;\n"
"border-radius: 4px;\n"
"border: 1px solid black;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1070, 800, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: #82EEFD;\n"
"border-radius: 4px;\n"
"border: 1px solid black;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1150, 90, 471, 81))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background: transparent;\n"
"border: none;\n"
"color: white;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(10, 70, 451, 101))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setStyleSheet("background: transparent;\n"
"border: none;\n"
"color: white;")
        self.textBrowser_4.setObjectName("textBrowser_4")
        Casey.setCentralWidget(self.centralwidget)

        self.retranslateUi(Casey)
        QtCore.QMetaObject.connectSlotsByName(Casey)

    def retranslateUi(self, Casey):
        _translate = QtCore.QCoreApplication.translate
        Casey.setWindowTitle(_translate("Casey", "MainWindow"))
        self.pushButton.setText(_translate("Casey", "RUN"))
        self.pushButton_2.setText(_translate("Casey", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Casey = QtWidgets.QMainWindow()
    ui = Ui_Casey()
    ui.setupUi(Casey)
    Casey.show()
    sys.exit(app.exec_())
