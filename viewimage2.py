from PyQt5 import QtCore, QtGui, QtWidgets
import glob
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 682)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 441))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Pictures/2photo.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=self.previous_image)
        self.pushButton.setGeometry(QtCore.QRect(0, 470, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked=self.next_image)
        self.pushButton_2.setGeometry(QtCore.QRect(412, 470, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked=self.delete_image)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 540, 191, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.image_number = 0
        self.images = glob.glob("image/*.jpg")

    def next_image(self, image_path):
        if self.image_number < len(self.images):
            self.label.setPixmap(QtGui.QPixmap(self.images[self.image_number]))
            self.image_number += 1

    def previous_image(self,image_path):
        if self.image_number > 0:
            self.label.setPixmap(QtGui.QPixmap(self.images[self.image_number - 1]))
            self.image_number -= 1

    def delete_image(self, image_path):
        if self.image_number >= 0 and self.image_number < len(self.images):
            os.remove(self.images[self.image_number])
            self.images.remove(self.images[self.image_number])

            if len(self.images) > 1:
                self.label.setPixmap(QtGui.QPixmap(self.images[0]))
            else:
                self.label.setPixmap(QtGui.QPixmap("../../Pictures/2photo.jpg"))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Previous"))
        self.pushButton_2.setText(_translate("MainWindow", "Next"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
