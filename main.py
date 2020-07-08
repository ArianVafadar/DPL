from DPLSystem.GUI import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

if __name__ == "__main__":
    from DPLSystem.DB.dbHandler import dbHandler
    x = dbHandler()
    x.add();



    # app = QtWidgets.QApplication(sys.argv)
    # Dialog = QtWidgets.QDialog()
    # ui = Ui_Dialog()
    # ui.setupUi(Dialog)
    # Dialog.show()
    # sys.exit(app.exec_())
