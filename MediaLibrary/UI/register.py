import os,sys
from PyQt5 import QtCore, QtGui, QtWidgets
import re
from MediaLibrary.Backend.database import createConnection
from MediaLibrary.Backend.insertData import insertuserIntoTable, insertMoviesIntoTable, insertMusicIntoTable, insertGameIntoTable
from MediaLibrary.UI.login import Ui_Dialog_login
from MediaLibrary.UI.selectCategory import selectCategory_Ui_Dialog
from MediaLibrary.UI.AddMovies import addMovies_Ui_Dialog
from MediaLibrary.UI.AddMusic import addMusic_Ui_Dialog
from MediaLibrary.UI.AddGames import addGame_Ui_Dialog
from MediaLibrary.Backend.loginAuthentication import login_check
from MediaLibrary.UI.movieMenu import movieMenu_Ui_Dialog
from MediaLibrary.UI.musicMenu import musicMenu_Ui_Dialog
from MediaLibrary.UI.gameMenu import gameMenu_Ui_Dialog
class Ui_Dialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, Dialog):
        self.Dialog = Dialog
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
        self.label_2.setGeometry(QtCore.QRect(130, 40, 331, 41))
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
        self.userName.setObjectName("userName")

        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(90, 250, 421, 51))
        self.password.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")



        self.re_password = QtWidgets.QLineEdit(self.frame)
        self.re_password.setGeometry(QtCore.QRect(90, 350, 421, 51))
        self.re_password.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.re_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.re_password.setObjectName("re_password")

        self.email = QtWidgets.QLineEdit(self.frame)
        self.email.setGeometry(QtCore.QRect(90, 440, 421, 51))
        self.email.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.email.setObjectName("email")

        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(100, 530, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(70, 630, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(244, 35, 20);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")

        self.loginButton = QtWidgets.QPushButton(self.frame)
        self.loginButton.setGeometry(QtCore.QRect(320, 630, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("background-color: rgb(244, 35, 20);\n"
                                      "color: rgb(255, 255, 255);")
        self.loginButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        return Dialog

    def regEx(self):
        regexEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if ( self.userName.text() =="" ) or (self.email.text() == "") or (self.password == ""):
            resEmpty = False
        else:
            resEmpty = True
        if(re.fullmatch(regexEmail, self.email.text())):
            resEmail = True
        else:
            resEmail = False

        if self.password.text() != self.re_password.text():
            resPass =  False
        else:
            resPass = True
        return  resEmpty, resEmail, resPass



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Register"))
        self.label_2.setText(_translate("Dialog", "Create an account"))
        self.userName.setPlaceholderText(_translate("Dialog", "User Name"))
        self.password.setPlaceholderText(_translate("Dialog", "Password"))
        self.re_password.setPlaceholderText(_translate("Dialog", "Retype Password"))
        self.email.setPlaceholderText(_translate("Dialog", "Email"))
        self.radioButton.setText(_translate("Dialog", "I Agree with Terms and Conditions"))
        self.pushButton.setText(_translate("Dialog", "Sign Up"))
        self.loginButton.setText(_translate("Dialog", "Login"))
        self.pushButton.clicked.connect(self.insertData)
        self.loginButton.clicked.connect(lambda : self.login_UI(self.Dialog))

    def insertData(self):
        resEmpty, resEmail, resPass = self.regEx()
        if resEmpty and resPass and resEmail:
            self.userId = self.userName.text()
            self.Iemail = self.email.text()
            self.Ipassword = self.password.text()
            insert_res = insertuserIntoTable(self.userId, self.Iemail, self.Ipassword)
            if insert_res:
                self.login_UI(self.Dialog)
            else:
                message = "AUser Already exists"
                self.dataEmptyMessageBox(message, self.Dialog)

        elif not resEmpty:
            message = "All Fields are empty"
            self.dataEmptyMessageBox(message, self.Dialog)


        elif not resPass:
            message = "Passwords are not matching"
            self.dataEmptyMessageBox(message, self.Dialog)

        elif not resEmail:
            message = "Email not in right format"
            self.dataEmptyMessageBox(message, self.Dialog)


    def login_UI(self, hide_dialog):
        self.Ui_Dialog_login_obj = Ui_Dialog_login()
        hide_dialog.hide()
        self.loginDialog = self.Ui_Dialog_login_obj.setupUi_login(self.Dialog)
        self.loginDialog.show()
        self.Ui_Dialog_login_obj.pushButton.clicked.connect(lambda : self.selectcategory_UI(self.loginDialog))
        self.Ui_Dialog_login_obj.backButton.clicked.connect(self.login_backUI)

    def login_backUI(self):
        self.loginDialog.hide()
        self.reg_dialog = self.setupUi(self.Dialog)
        self.reg_dialog.show()

    def selectcategory_UI(self, hide_dialog):
        self.userName = self.Ui_Dialog_login_obj.userName.text()
        self.password = self.Ui_Dialog_login_obj.password.text()
        login_result = login_check(self.userName, self.password)
        if login_result:
            self.selectCategory_Ui_Dialog_obj = selectCategory_Ui_Dialog()
            hide_dialog.hide()
            self.selectCat_dialog = self.selectCategory_Ui_Dialog_obj.selectCategory_setupUi(self.loginDialog)
            self.selectCat_dialog.show()
            self.selectCategory_Ui_Dialog_obj.movieButton.clicked.connect(lambda :self.menu_UI_movie(self.selectCat_dialog))
            self.selectCategory_Ui_Dialog_obj.musicButton.clicked.connect(lambda :self.menu_UI_music(self.selectCat_dialog))
            self.selectCategory_Ui_Dialog_obj.gameButton.clicked.connect(lambda :self.menu_UI_game(self.selectCat_dialog))
            self.selectCategory_Ui_Dialog_obj.pushButton_3.clicked.connect(lambda :self.logout_UI(self.selectCat_dialog))
        else:
            message = "UserName or Password is Invalid"
            self.dataEmptyMessageBox(message, self.loginDialog)

    def menu_UI_movie(self, hide_dilog):
        self.movieMenu_Ui_Dialog_obj = movieMenu_Ui_Dialog()
        hide_dilog.hide()
        self.movieMenuDialog = self.movieMenu_Ui_Dialog_obj.movieMenu_setupUi(self.selectCat_dialog, self.userName)
        self.movieMenuDialog.show()
        self.movieMenu_Ui_Dialog_obj.addButton.clicked.connect(self.AddMoviesUI)
        self.movieMenu_Ui_Dialog_obj.deleteButton.clicked.connect(self.movieMenu_Ui_Dialog_obj.deleteContact)
        self.movieMenu_Ui_Dialog_obj.editButton.clicked.connect(self.movieMenu_Ui_Dialog_obj.changeRecord)

        self.movieMenu_Ui_Dialog_obj.backButton.clicked.connect(lambda: self.selectcategory_UI(self.movieMenuDialog))
        #self.movieMenu_Ui_Dialog_obj.viewButton.clicked.connect(movieMenu_Ui_Dialog.table_view)
        self.movieMenu_Ui_Dialog_obj.pushButton_3.clicked.connect(lambda : self.login_UI(self.movieMenuDialog))

    def menu_UI_music(self, hide_dialog):
        self.musicMenu_Ui_Dialog_obj = musicMenu_Ui_Dialog()
        hide_dialog.hide()
        self.musicMenuDialog = self.musicMenu_Ui_Dialog_obj.musicMenu_setupUi(self.selectCat_dialog, self.userName)
        self.musicMenuDialog.show()
        self.musicMenu_Ui_Dialog_obj.addButton.clicked.connect(self.AddMusicUI)
        self.musicMenu_Ui_Dialog_obj.deleteButton.clicked.connect(self.musicMenu_Ui_Dialog_obj.deleteContact)
        self.musicMenu_Ui_Dialog_obj.editButton.clicked.connect(self.musicMenu_Ui_Dialog_obj.changeRecord)

        self.musicMenu_Ui_Dialog_obj.backButton.clicked.connect(lambda: self.selectcategory_UI(self.musicMenuDialog))
        self.musicMenu_Ui_Dialog_obj.pushButton_3.clicked.connect(lambda : self.logout_UI(self.musicMenuDialog))

    def menu_UI_game(self, hide_dialog):
        self.gameMenu_Ui_Dialog_obj = gameMenu_Ui_Dialog()
        hide_dialog.hide()
        self.gameMenuDialog = self.gameMenu_Ui_Dialog_obj.gameMenu_setupUi(self.selectCat_dialog, self.userName)
        self.gameMenuDialog.show()
        self.gameMenu_Ui_Dialog_obj.addButton.clicked.connect(self.AddGameUI)
        self.gameMenu_Ui_Dialog_obj.deleteButton.clicked.connect(self.gameMenu_Ui_Dialog_obj.deleteContact)
        self.gameMenu_Ui_Dialog_obj.editButton.clicked.connect(self.gameMenu_Ui_Dialog_obj.changeRecord)
        self.gameMenu_Ui_Dialog_obj.backButton.clicked.connect(lambda: self.selectcategory_UI(self.gameMenuDialog))
        self.gameMenu_Ui_Dialog_obj.pushButton_3.clicked.connect(lambda : self.login_UI(self.gameMenuDialog))

    def logout_UI(self, hide_dialog):
        self.Ui_Dialog_login_obj = Ui_Dialog_login()
        #self.selectCat_dialog.hide()
        hide_dialog.hide()
        self.loginDialog = self.Ui_Dialog_login_obj.setupUi_login(self.selectCat_dialog)
        self.loginDialog.show()
        self.Ui_Dialog_login_obj.pushButton.clicked.connect(lambda: self.selectcategory_UI(self.loginDialog))
        self.Ui_Dialog_login_obj.backButton.clicked.connect(self.login_backUI)


    def AddMoviesUI(self):
        self.addMovies_Ui_Dialog_obj = addMovies_Ui_Dialog()
        self.movieMenuDialog.hide()
        self.addMovies_dialog = self.addMovies_Ui_Dialog_obj.addMovies_setupUi(self.movieMenuDialog)
        self.addMovies_dialog.show()

        self.addMovies_Ui_Dialog_obj.AddButton.clicked.connect(self.insertMovieData)
        self.addMovies_Ui_Dialog_obj.backButton.clicked.connect(lambda : self.menu_UI_movie(self.addMovies_dialog))
        self.addMovies_Ui_Dialog_obj.pushButton_3.clicked.connect(lambda : self.logout_UI(self.addMovies_dialog))

    def insertMovieData(self):
        movieName = self.addMovies_Ui_Dialog_obj.movieNameField.text()
        movieYear = self.addMovies_Ui_Dialog_obj.yearField.text()
        actorName = self.addMovies_Ui_Dialog_obj.artistNameField.text()
        directorName = self.addMovies_Ui_Dialog_obj.directorField.text()
        genreName = self.addMovies_Ui_Dialog_obj.genreField.text()
        userName = self.Ui_Dialog_login_obj.userName.text()
        movieData = self.addMovies_Ui_Dialog_obj.fileUploadField.text()
        if movieName != "" and movieYear != "" and actorName != "" and directorName != "" and genreName != "" and userName != "" and movieData != "":
            insert_movie_res = insertMoviesIntoTable(movieName, movieYear, actorName, directorName, genreName, movieData,userName)
            if insert_movie_res:
                self.addMovies_dialog.hide()
                self.addMovies_dialog.show()
            else:
                message = "Insert Movie Data Failed..."
                self.dataEmptyMessageBox(message, self.addMovies_dialog)
        else:
            message = "Data Fields can't be Empty..."
            self.dataEmptyMessageBox(message, self.addMovies_dialog)


    def dataEmptyMessageBox(self, message, dialog):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(message)
        msgBox.setWindowTitle("Error Message")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msgBox.buttonClicked.connect(dialog.show)
        msgBox.exec()

    def AddMusicUI(self):
        self.addMusic_Ui_Dialog_obj = addMusic_Ui_Dialog()
        self.musicMenuDialog.hide()
        self.addMusic_dialog = self.addMusic_Ui_Dialog_obj.addMusic_setupUi(self.musicMenuDialog)
        self.addMusic_dialog.show()
        self.addMusic_Ui_Dialog_obj.AddButton.clicked.connect(self.insertMusicData)
        self.addMusic_Ui_Dialog_obj.backButton.clicked.connect(lambda : self.menu_UI_music(self.addMusic_dialog))
        self.addMusic_Ui_Dialog_obj.pushButton_3.clicked.connect(lambda : self.logout_UI(self.addMusic_dialog))

    def insertMusicData(self):
        songNameField = self.addMusic_Ui_Dialog_obj.songNameField.text()
        artistNameField = self.addMusic_Ui_Dialog_obj.artistNameField.text()
        yearField = self.addMusic_Ui_Dialog_obj.yearField.text()
        writerField = self.addMusic_Ui_Dialog_obj.writerField.text()
        genreField = self.addMusic_Ui_Dialog_obj.genreField.text()
        userName = self.Ui_Dialog_login_obj.userName.text()
        musicData = self.addMusic_Ui_Dialog_obj.fileUploadField.text()
        if songNameField != "" and artistNameField != "" and yearField != "" and writerField != "" and genreField != "" and userName != "" and musicData != "":

            insert_music_res = insertMusicIntoTable(songNameField, artistNameField, yearField, writerField, genreField, musicData, userName)

            if insert_music_res:
                self.addMusic_dialog.hide()
                self.addMusic_dialog.show()
            else:
                message = "Insert Music Data Failed..."
                self.dataEmptyMessageBox(message, self.addMusic_dialog)
        else:
            message = "Data Fields can't be Empty..."
            self.dataEmptyMessageBox(message, self.addMusic_dialog)


    def AddGameUI(self):
        self.addGame_Ui_Dialog_obj = addGame_Ui_Dialog()
        self.gameMenuDialog.hide()
        self.addGame_dialog = self.addGame_Ui_Dialog_obj.addGame_setupUi(self.gameMenuDialog)
        self.addGame_dialog.show()
        self.addGame_Ui_Dialog_obj.AddButton.clicked.connect(self.insertGameData)
        self.addGame_Ui_Dialog_obj.backButton.clicked.connect(lambda : self.menu_UI_game(self.addGame_dialog))
        self.addGame_Ui_Dialog_obj.pushButton_3.clicked.connect(lambda : self.logout_UI(self.addGame_dialog))

    def insertGameData(self):
        gameNameField = self.addGame_Ui_Dialog_obj.gameNameField.text()
        artistNameField = self.addGame_Ui_Dialog_obj.artistNameField.text()
        yearField = self.addGame_Ui_Dialog_obj.yearField.text()
        writerField = self.addGame_Ui_Dialog_obj.writerField.text()
        genreField = self.addGame_Ui_Dialog_obj.genreField.text()
        userName = self.Ui_Dialog_login_obj.userName.text()
        gameData = self.addGame_Ui_Dialog_obj.fileUploadField.text()
        if gameNameField != "" and artistNameField != "" and yearField != "" and writerField != "" and genreField != "" and userName != "" and gameData != "":

            insert_music_res = insertGameIntoTable(gameNameField, artistNameField, yearField, writerField, genreField, gameData, userName)
            if insert_music_res:
                self.addGame_dialog.hide()
                self.addGame_dialog.show()
            else:
                message = "Insert Game Data Failed..."
                self.dataEmptyMessageBox(message, self.addGame_dialog)
        else:
            message = "Data Fields can't be Empty..."
            self.dataEmptyMessageBox(message, self.addGame_dialog)

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    db_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(db_dir + r"\Database\mediaLibrary.sqlite")
    if not createConnection(db_dir + r"\Database\mediaLibrary.sqlite"):
        sys.exit(1)


    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

