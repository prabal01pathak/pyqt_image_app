import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QToolTip, QMessageBox, QLabel)
from camera import CameraWindow
from viewimage2 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import glob

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Register')
        self.setWindowIcon(QtGui.QIcon('icon.png'))



class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "First Window"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.pushButton = QPushButton("Capture", self)
        self.pushButton.move(275, 200)
        self.pushButton.setToolTip("<h3>Capture the Image</h3>")

        self.pushButton.clicked.connect(self.camera_window)              # <===
        self.registerButton = QPushButton("View Image", self)
        self.registerButton.move(275, 250)
        self.registerButton.setToolTip("<h3>Register a new user</h3>")
        self.registerButton.clicked.connect(self.register_window)          # <===
        self.main_window()

    def main_window(self):
        self.label = QLabel("Manager", self)
        self.label.move(285, 175)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def camera_window(self):                                             # <===
        self.w = CameraWindow()
        self.w.show()

    def register_window(self):
        self.mainWindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
