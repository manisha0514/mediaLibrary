# -*- coding: utf-8 -*-

"""This module provides Media Library application."""

import sys
import os
from PyQt5 import QtWidgets
from MediaLibrary.Backend.database import createConnection
from MediaLibrary.UI.register import Ui_Dialog

def main():
    app = QtWidgets.QApplication(sys.argv)
    db_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if not createConnection(db_dir + r"\Database\mediaLibrary.sqlite"):
        sys.exit(1)

    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())



