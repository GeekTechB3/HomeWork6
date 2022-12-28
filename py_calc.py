import sys 
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.uic import loadUi

class Form(QDialog):
    def __init__(self):
        super(Form, self).__init__()

        loadUi('calc.ui', self)
        self.add.clicked.connect(self.add_num)
        self.sub.clicked.connect(self.sub_num)
        self.mult.clicked.connect(self.mult_num)
        self.div.clicked.connect(self.div_num)

    def add_num(self):
        try:
          num1 = int(self.input1.text())
          num2 = int(self.input2.text())
          self.output.setText( "Ответ :" + str(num1 + num2))
        except ValueError:
            self.output.setText("Ощибка")  
    
    def sub_num(self):
        try:
            try:
                num1 = int(self.input1.text())
                num2 = int(self.input2.text())
                self.output.setText("Ответ: " + str(num1 - num2))
            except ZeroDivisionError:
                
                self.output.setText("Ошибка")
        except ValueError:
             self.output.setText("Ошибка")

    def div_num(self):
            try:
                try:
                    num1 = int(self.input1.text())
                    num2 = int(self.input2.text())
                    self.output.setText("Ответ: " +str(num1 / num2))

                except ZeroDivisionError:

                    self.output.setText("На ноль делить нельзя!")
            except ValueError:
                self.output.setText("Ощибка") 

    def mult_num(self):
            try:

                num1 = int(self.input1.text())
                num2 = int(self.input2.text())

                self.output.setText("Ответ: " +str(num1 * num2))
            except ValueError:
                self.output.setText("Ощибка")                    

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_() 