import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.CaptureImage = QtWidgets.QPushButton(self.centralwidget)
        self.CaptureImage.setGeometry(QtCore.QRect(30, 10, 241, 161))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.CaptureImage.setFont(font)
        self.CaptureImage.setObjectName("CaptureImage")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 220, 241, 141))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "MainWindow"))
        self.CaptureImage.setText(_translate("MainWindow2", "Capture Image"))
        self.pushButton.setText(_translate("MainWindow2", "Register"))

if __name__=="__main__":
    app = QApplication([])
    MainWindow2 = QMainWindow()
    window = Ui_MainWindow2()
    window.setupUi(MainWindow2)
    MainWindow2.show()
    sys.exit(app.exec_())
