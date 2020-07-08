from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        self.EnteredPasscode = []
    def changeCnt(cnt):
        EnteredPasscode.append(x);
        print(EnteredPasscode)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(663, 451)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)

        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 100, 451, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 3, 1, 1, 1)

        self.pushButton_BackSpace = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_BackSpace.setObjectName("pushButton_BackSpace")
        self.gridLayout.addWidget(self.pushButton_BackSpace, 3, 0, 1, 1)

        self.pushButton_Cancel = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.gridLayout.addWidget(self.pushButton_Cancel, 3, 2, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.WelcomeLabel = QtWidgets.QLabel(Dialog)
        self.WelcomeLabel.setGeometry(QtCore.QRect(160, 20, 431, 20))
        self.WelcomeLabel.setObjectName("WelcomeLabel")

        self.push_ScanQR = QtWidgets.QPushButton(Dialog)
        self.push_ScanQR.setGeometry(QtCore.QRect(220, 40, 231, 61))
        self.push_ScanQR.setObjectName("push_ScanQR")

        self.push_Enter = QtWidgets.QPushButton(Dialog)
        self.push_Enter.setGeometry(QtCore.QRect(110, 400, 451, 41))
        self.push_Enter.setObjectName("push_Enter")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        self.pushButton_0.setText(_translate("Dialog", "0"))
        self.pushButton_0.clicked.connect(lambda: self.EnteredPasscode.append(0))

        self.pushButton_1.setText(_translate("Dialog", "1"))
        self.pushButton_1.clicked.connect(lambda: self.EnteredPasscode.append(1))

        self.pushButton_2.setText(_translate("Dialog", "2"))
        self.pushButton_2.clicked.connect(lambda: self.EnteredPasscode.append(2))

        self.pushButton_3.setText(_translate("Dialog", "3"))
        self.pushButton_3.clicked.connect(lambda: self.EnteredPasscode.append(3))

        self.pushButton_4.setText(_translate("Dialog", "4"))
        self.pushButton_4.clicked.connect(lambda: self.EnteredPasscode.append(4))

        self.pushButton_5.setText(_translate("Dialog", "5"))
        self.pushButton_5.clicked.connect(lambda: self.EnteredPasscode.append(5))

        self.pushButton_6.setText(_translate("Dialog", "6"))
        self.pushButton_6.clicked.connect(lambda: self.EnteredPasscode.append(6))

        self.pushButton_7.setText(_translate("Dialog", "7"))
        self.pushButton_7.clicked.connect(lambda: self.EnteredPasscode.append(7))

        self.pushButton_8.setText(_translate("Dialog", "8"))
        self.pushButton_8.clicked.connect(lambda: self.EnteredPasscode.append(8))

        self.pushButton_9.setText(_translate("Dialog", "9"))
        self.pushButton_9.clicked.connect(lambda: self.EnteredPasscode.append(9))


        self.pushButton_BackSpace.setText(_translate("Dialog", "Backspace"))
        self.pushButton_BackSpace.clicked.connect(lambda: print(self.EnteredPasscode))

        self.pushButton_Cancel.setText(_translate("Dialog", "Cancel"))
        self.pushButton_Cancel.clicked.connect(lambda: self.EnteredPasscode.clear() )

        self.push_Enter.setText(_translate("Dialog", "Enter"))
        self.push_Enter.clicked.connect(lambda: print(self.EnteredPasscode))


        self.WelcomeLabel.setText(_translate("Dialog", "Please Enter your Passcode Or Scan your Package/QrCode"))
        self.push_ScanQR.setText(_translate("Dialog", "Scan Qr Code/Tracking Number"))
