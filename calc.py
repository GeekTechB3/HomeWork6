import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.uic import loadUi

class Form(QMainWindow):
    def __init__(self):
        super(Form, self).__init__()

        loadUi('calc.ui', self)
        self.add.clicked.connect(self.add_num)
        self.sub.clicked.connect(self.sub_num)
        self.mult.clicked.connect(self.mult_num)
        self.dev.clicked.connect(self.dev_num)
    def add_num(self):
        try:
            num1 = int(self.input1.text())
            num2 = int(self.input2.text())
            self.output.setText(str(num1 + num2))
        except ValueError:
            self.output.setText("Ошибка")


    def sub_num(self):
        try:
            num1 = int(self.input1.text())
            num2 = int(self.input2.text())
            self.output.setText(str(num1 - num2))
        except ValueError:
            self.output.setText("Ошибка")
    
    def mult_num(self):
        try:
            num1 = int(self.input1.text())
            num2= int(self.input2.text())
            self.output.setText(str(num1 * num2))
        except  ValueError:
            self.output.setText("Ошибка")
    
    def dev_num(self):
        try:
            try:
                num1 = int(self.input1.text())
                num2 = int(self.input2.text())
                self.output.setText(str(num1 / num2))
            except ZeroDivisionError:
                self.output.setText("На ноль делить нельзя!")
        except ValueError:
            self.output.setText("Ошибка")


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
