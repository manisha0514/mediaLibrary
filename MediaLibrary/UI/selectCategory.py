from PyQt5 import QtCore, QtGui, QtWidgets


class selectCategory_Ui_Dialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def selectCategory_setupUi(self, dialog):
        self.Dialog = dialog
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(808, 880)
        self.Dialog.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(90, 270, 251, 251))
        self.label.setStyleSheet("background-image: url(:/newPrefix/User.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.Dialog)
        self.frame.setGeometry(QtCore.QRect(100, 50, 611, 751))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(180, 40, 331, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(32)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_2.setObjectName("label_2")
        self.label_1 = QtWidgets.QLabel(self.frame)
        self.label_1.setGeometry(QtCore.QRect(80, 160, 331, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("color: rgb(244, 35, 20);")
        self.label_1.setObjectName("label_1")
        self.movieButton = QtWidgets.QPushButton(self.frame)
        self.movieButton.setGeometry(QtCore.QRect(90, 250, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.movieButton.setFont(font)
        self.movieButton.setStyleSheet("background-color: rgb(25, 25, 112);\n"
                                      "color: rgb(255, 255, 255);")
        self.movieButton.setObjectName("pushButton")
        self.musicButton = QtWidgets.QPushButton(self.frame)
        self.musicButton.setGeometry(QtCore.QRect(90, 330, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.musicButton.setFont(font)
        self.musicButton.setStyleSheet("background-color: rgb(25, 25, 112);\n"
                                      "color: rgb(255, 255, 255);")
        self.musicButton.setObjectName("pushButton")
        self.gameButton = QtWidgets.QPushButton(self.frame)
        self.gameButton.setGeometry(QtCore.QRect(90, 410, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.gameButton.setFont(font)
        self.gameButton.setStyleSheet("background-color: rgb(25, 25, 112);\n"
                                        "color: rgb(255, 255, 255);")
        self.gameButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 540, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(244, 35, 20);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton")
        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)
        return self.Dialog

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Select Category"))
        self.label_2.setText(_translate("Dialog", "Media Library"))
        self.label_1.setText(_translate("Dialog", "Welcome User"))
        self.movieButton.setText(_translate("Dialog", "Movies"))
        self.musicButton.setText(_translate("Dialog", "Music"))
        self.gameButton.setText(_translate("Dialog", "Games"))
        self.pushButton_3.setText(_translate("Dialog", "Logout"))



# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = selectCategory_Ui_Dialog()
#     ui.selectCategory_setupUi(Dialog)
#     # Dialog.show()
#     sys.exit(app.exec_())