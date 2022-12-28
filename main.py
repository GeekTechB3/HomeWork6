from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def add_buttton_label():
    print("Hello World")


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Window")
    window.setGeometry(300, 250, 500, 500)

    main_text = QtWidgets.QLabel(window)
    main_text.setText("Hello World")
    main_text.move(100,100)
    main_text.adjustSize()

    button = QtWidgets.QPushButton(window)
    button.setText("Нажми на меня")
    button.move(100,70)
    button.clicked.connect(add_buttton_label)

    window.show()
    sys.exit(app.exec_())

application()
