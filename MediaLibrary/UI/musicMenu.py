import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtSql
from PyQt5.QtGui import QPalette, QColor


# create Menu for Adding Editing and Deleting music items
class musicMenu_Ui_Dialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def musicMenu_setupUi(self, dialog, username):
        """setup music UI"""

        self.username = username
        self.musicMenuDialog = dialog
        self.musicMenuDialog.setObjectName("Dialog")
        self.musicMenuDialog.resize(808, 880)
        self.musicMenuDialog.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.label = QtWidgets.QLabel(self.musicMenuDialog)
        self.label.setGeometry(QtCore.QRect(90, 270, 251, 251))
        self.label.setStyleSheet("background-image: url(:/newPrefix/User.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.musicMenuDialog)
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
        self.label_2.setStyleSheet("color: rgb(20, 85, 255);")
        self.label_2.setObjectName("label_2")
        self.label_1 = QtWidgets.QLabel(self.frame)
        self.label_1.setGeometry(QtCore.QRect(10, 130, 331, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("color: rgb(244, 35, 20);")
        self.label_1.setObjectName("label_1")
        self.table_view()
        self.addButton = QtWidgets.QPushButton(self.frame)
        self.addButton.setGeometry(QtCore.QRect(30, 250, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addButton.setFont(font)
        self.addButton.setStyleSheet("background-color: rgb(25, 25, 112);\n"
                                     "color: rgb(255, 255, 255);")
        self.addButton.setObjectName("pushButton")
        self.editButton = QtWidgets.QPushButton(self.frame)
        self.editButton.setGeometry(QtCore.QRect(30, 330, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.editButton.setFont(font)
        self.editButton.setStyleSheet("background-color: rgb(25, 25, 112);\n"
                                      "color: rgb(255, 255, 255);")
        self.editButton.setObjectName("pushButton")
        self.deleteButton = QtWidgets.QPushButton(self.frame)
        self.deleteButton.setGeometry(QtCore.QRect(30, 410, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet("background-color: rgb(25, 25, 112);\n"
                                        "color: rgb(255, 255, 255);")
        self.deleteButton.setObjectName("pushButton")

        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 580, 260, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(244, 35, 20);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton")
        self.backButton = QtWidgets.QPushButton(self.frame)
        self.backButton.setGeometry(QtCore.QRect(20, 580, 260, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("background-color: rgb(244, 35, 20);\n"
                                      "color: rgb(255, 255, 255);")
        self.backButton.setObjectName("backButton")
        self.retranslateUi(self.musicMenuDialog)
        QtCore.QMetaObject.connectSlotsByName(self.musicMenuDialog)
        return self.musicMenuDialog

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Select Category"))
        self.label_2.setText(_translate("Dialog", "music Menu"))
        self.label_1.setText(_translate("Dialog", "Welcome User"))
        self.addButton.setText(_translate("Dialog", "Add"))
        self.editButton.setText(_translate("Dialog", "Edit"))
        self.deleteButton.setText(_translate("Dialog", "Delete"))
        self.backButton.setText(_translate("Dialog", "Back"))
        self.pushButton_3.setText(_translate("Dialog", "Logout"))

    def table_view(self):
        """for viewing table in the layout """

        db_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(
            db_dir + r"\Database\mediaLibrary.sqlite")

        # try to open the database
        if not self.db.open():
            print("Could not open the database")

        self.model = QtSql.QSqlTableModel(self, self.db)
        self.model.setTable('music')
        self.filter_criteria = "user_id = ('%s')" % (self.username)

        self.model.setFilter(self.filter_criteria)
        self.model.select()
        self.tableLayout = QtWidgets.QHBoxLayout(self.frame)
        self.tableLayout.addStretch(2)

        self.tableWidget = QtWidgets.QTableWidget(self.frame)

        self.tableLayout.addWidget(self.tableWidget)
        self.tableWidget.setFixedSize(430, 380)
        self.tableWidget.setStyleSheet("background-color: rgb(215, 215, 215);")
        self.tview = QtWidgets.QTableView(self.tableWidget)

        self.tview.setModel(self.model)
        self.tview.hideColumn(0)
        self.tview.hideColumn(7)
        # self.tview.resizeColumnsToContents()
        # self.tview.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.layout = QtWidgets.QVBoxLayout(self.tableWidget)
        self.layout.addWidget(self.tview)

    def deleteContact(self):
        """Delete the selected music details from the database."""

        row = self.tview.currentIndex().row()
        if row < 0:
            return

        messageBox = QtWidgets.QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove the selected contact?",
            QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel,
        )

        if messageBox == QtWidgets.QMessageBox.Ok:
            try:
                self.model.removeRow(row)
                self.tview.setModel(self.model)
                # self.db.close()


            except Exception as e:
                print(e)

    def changeRecord(self):
        """ Edits music items in the table"""

        row = self.model.rowCount()
        # self.model.insertRow(row)

        index = self.model.index(row, 0)
        self.tview.setCurrentIndex(index)
        self.tview.edit(index)

