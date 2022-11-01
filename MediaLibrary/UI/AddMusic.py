from PyQt5 import QtCore, QtGui, QtWidgets


class addMusic_Ui_Dialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def addMusic_setupUi(self, Dialog):
        self.musicdialog = Dialog
        self.musicdialog.setObjectName("Dialog")
        self.musicdialog.resize(808, 880)
        self.musicdialog.setStyleSheet("background-color: rgb(85, 85, 127);")

        self.label = QtWidgets.QLabel(self.musicdialog)
        self.label.setGeometry(QtCore.QRect(90, 270, 251, 251))
        self.label.setStyleSheet("background-image: url(:/newPrefix/User.png);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.frame = QtWidgets.QFrame(self.musicdialog)
        self.frame.setGeometry(QtCore.QRect(100, 50, 611, 751))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(160, 40, 331, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(32)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_2.setObjectName("label_2")

        self.label_1 = QtWidgets.QLabel(self.frame)
        self.label_1.setGeometry(QtCore.QRect(170, 120, 331, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("color: rgb(244, 35, 20);")
        self.label_1.setObjectName("label_1")

        self.songName = QtWidgets.QLabel(self.frame)
        self.songName.setGeometry(QtCore.QRect(40, 190, 331, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.songName.setFont(font)
        self.songName.setStyleSheet("color: rgb(0, 0, 0);")
        self.songName.setObjectName("songName")

        self.songNameField = QtWidgets.QLineEdit(self.frame)
        self.songNameField.setGeometry(QtCore.QRect(260, 200, 331, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.songNameField.setFont(font)
        self.songNameField.setStyleSheet("color: rgb(244, 35, 20);")
        self.songNameField.setObjectName("songNameField")

        self.singerName = QtWidgets.QLabel(self.frame)
        self.singerName.setGeometry(QtCore.QRect(40, 250, 331, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.singerName.setFont(font)
        self.singerName.setStyleSheet("color: rgb(0, 0, 0);")
        self.singerName.setObjectName("singerName")

        self.artistNameField = QtWidgets.QLineEdit(self.frame)
        self.artistNameField.setGeometry(QtCore.QRect(260, 260, 331, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.artistNameField.setFont(font)
        self.artistNameField.setStyleSheet("color: rgb(244, 35, 20);")
        self.artistNameField.setObjectName("artistNameField")

        self.songYear = QtWidgets.QLabel(self.frame)
        self.songYear.setGeometry(QtCore.QRect(40, 310, 331, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.songYear.setFont(font)
        self.songYear.setStyleSheet("color: rgb(0, 0, 0);")
        self.songYear.setObjectName("singerName")

        self.yearField = QtWidgets.QLineEdit(self.frame)
        self.yearField.setGeometry(QtCore.QRect(260, 320, 331, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.yearField.setFont(font)
        self.yearField.setStyleSheet("color: rgb(244, 35, 20);")
        self.yearField.setObjectName("yearField")

        self.writerName = QtWidgets.QLabel(self.frame)
        self.writerName.setGeometry(QtCore.QRect(40, 370, 331, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.writerName.setFont(font)
        self.writerName.setStyleSheet("color: rgb(0, 0, 0);")
        self.writerName.setObjectName("writerName")

        self.writerField = QtWidgets.QLineEdit(self.frame)
        self.writerField.setGeometry(QtCore.QRect(260, 380, 331, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.writerField.setFont(font)
        self.writerField.setStyleSheet("color: rgb(244, 35, 20);")
        self.writerField.setObjectName("writerField")

        self.genreName = QtWidgets.QLabel(self.frame)
        self.genreName.setGeometry(QtCore.QRect(40, 430, 331, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.genreName.setFont(font)
        self.genreName.setStyleSheet("color: rgb(0, 0, 0);")
        self.genreName.setObjectName("genreName")

        self.genreField = QtWidgets.QLineEdit(self.frame)
        self.genreField.setGeometry(QtCore.QRect(260, 440, 331, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.genreField.setFont(font)
        self.genreField.setStyleSheet("color: rgb(244, 35, 20);")
        self.genreField.setObjectName("genreField")

        self.fileUploadField = QtWidgets.QLineEdit(self.frame)
        self.fileUploadField.setGeometry(QtCore.QRect(20, 500, 451, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.fileUploadField.setFont(font)
        self.fileUploadField.setStyleSheet("color: rgb(0, 0, 0);")
        self.fileUploadField.setObjectName("fileUploadField")

        self.searchFile = QtWidgets.QPushButton(self.frame)
        self.searchFile.setGeometry(QtCore.QRect(450, 500, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.searchFile.setFont(font)
        self.searchFile.setStyleSheet("background-color: rgb(25, 25, 112);\n"
                                        "color: rgb(255, 255, 255);")
        self.searchFile.clicked.connect(self.dialog)
        self.searchFile.setObjectName("searchFile")

        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 600, 260, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(244, 35, 20);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton")

        self.AddButton = QtWidgets.QPushButton(self.frame)
        self.AddButton.setGeometry(QtCore.QRect(20, 600, 260, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.AddButton.setFont(font)
        self.AddButton.setStyleSheet("background-color: rgb(244, 35, 20);\n"
                                        "color: rgb(255, 255, 255);")
        self.AddButton.setObjectName("AddButton")
        self.backButton = QtWidgets.QPushButton(self.frame)
        self.backButton.setGeometry(QtCore.QRect(180, 660, 260, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("background-color: rgb(244, 35, 20);\n"
                                      "color: rgb(255, 255, 255);")
        self.backButton.setObjectName("backButton")
        self.retranslateUi(self.musicdialog)
        QtCore.QMetaObject.connectSlotsByName(self.musicdialog)

        return self.musicdialog

    def dialog(self):
        file, check = QtWidgets.QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                                  "", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
        if check:
            self.fileUploadField.setText(file)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Select Category"))
        self.label_2.setText(_translate("Dialog", "Media Library"))
        self.label_1.setText(_translate("Dialog", "Add Music File"))
        self.songName.setText(_translate("Dialog", "Song Name"))
        self.singerName.setText(_translate("Dialog", "Singer Name"))
        self.songYear.setText(_translate("Dialog", "Song Year"))
        self.writerName.setText(_translate("Dialog", "Writer Name"))
        self.genreName.setText(_translate("Dialog", "Genre Name"))
        self.searchFile.setText(_translate("Dialog", "Search"))
        self.AddButton.setText(_translate("Dialog", "Upload"))
        self.pushButton_3.setText(_translate("Dialog", "Logout"))
        self.backButton.setText(_translate("Dialog", "Back"))


