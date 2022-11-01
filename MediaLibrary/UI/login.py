from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def setupUi_login(self, dialog):

        self.loginDialog = dialog
        self.loginDialog .setObjectName("Dialog")
        self.loginDialog .resize(808, 880)
        self.loginDialog .setStyleSheet("background-color: rgb(85, 85, 127);")
        self.label = QtWidgets.QLabel(self.loginDialog )
        self.label.setGeometry(QtCore.QRect(90, 270, 251, 251))
        self.label.setStyleSheet("background-image: url(:/newPrefix/User.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.loginDialog)
        self.frame.setGeometry(QtCore.QRect(100, 50, 611, 751))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(180, 40, 331, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_2.setObjectName("label_2")
        self.userName = QtWidgets.QLineEdit(self.frame)
        self.userName.setGeometry(QtCore.QRect(90, 160, 421, 51))
        self.userName.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.userName.setInputMask("")
        self.userName.setText("")
        self.userName.setReadOnly(False)
        self.userName.setObjectName("lineEdit")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(90, 250, 421, 51))
        self.password.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(90, 380, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(244, 35, 20);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.backButton = QtWidgets.QPushButton(self.frame)
        self.backButton.setGeometry(QtCore.QRect(90, 440, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("background-color: rgb(244, 35, 20);\n"
                                      "color: rgb(255, 255, 255);")
        self.backButton.setObjectName("backButton")

        self.retranslateUi(self.loginDialog)
        QtCore.QMetaObject.connectSlotsByName(self.loginDialog)

        return self.loginDialog

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.label_2.setText(_translate("Dialog", "Media Library"))
        self.userName.setPlaceholderText(_translate("Dialog", "User Name"))
        self.password.setPlaceholderText(_translate("Dialog", "Password"))
        self.pushButton.setText(_translate("Dialog", "Login"))
        self.backButton.setText(_translate("Dialog", "Back"))



