import sys
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QWidget,
                             QPushButton,
                             QGridLayout,
                             QLabel,
                             QLineEdit,
                             QMessageBox,
                             QComboBox,
                             QRadioButton,
                             QDialog,
                             QFormLayout
                            )
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import requests
from camera import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.buttons()

    def initUI(self):
        self.setWindowTitle("Camear App")
        self.setGeometry(300, 300, 300, 300)

    def buttons(self):
        self.layout = QGridLayout()
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.register_button = QPushButton("Register")
        self.capture_button = QPushButton("Capture")
        self.register_button.clicked.connect(open_camera)
        self.capture_button.clicked.connect(self.capture)
        self.layout.addWidget(self.register_button)
        self.layout.addWidget(self.capture_button)
        self.centralWidget.setLayout(self.layout)

    def register(self):
        self.dialog = QDialog()
        self.dialog.setWindowTitle("Register")
        self.dialog.setGeometry(300, 300, 300, 300)
        self.dialog.setLayout(self.layout)
        self.dialog.show()
        self.dialog.exec_()

    def capture(self):
        self.dialog = QDialog()
        self.dialog.setWindowTitle("Capture")
        self.dialog.setGeometry(300, 300, 300, 300)
        self.dialog.setLayout(self.layout)
        self.dialog.show()
        self.dialog.exec_()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
