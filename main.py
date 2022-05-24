from PyQt5 import QtWidgets
from gui import first_window,second_window,third_window
import sys

global first_value,second_value, third_value
first_value = 0
second_value = 0
third_value = 0

class Third(QtWidgets.QMainWindow):
    def __init__(self):
        super(Third, self).__init__()
        self.ui = third_window.Ui_MainWindow()
        self.ui.setupUi(self)

class Second(QtWidgets.QMainWindow):
    def __init__(self):
        super(Second, self).__init__()
        self.ui = second_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.horizontalSlider.valueChanged[int].connect(self.changeValue)
        self.ui.horizontalSlider_2.valueChanged[int].connect(self.changeValue_2)
        self.ui.horizontalSlider_3.valueChanged[int].connect(self.changeValue_3)
        self.ui.lineEdit.textChanged.connect(self.changeValueLine)
        self.ui.lineEdit_2.textChanged.connect(self.changeValueLine_2)
        self.ui.lineEdit_3.textChanged.connect(self.changeValueLine_3)
        self.ui.pushButton.clicked.connect(self.change_output)

    def changeValueLine(self,value):
        global first_value
        try:
            first_value = int(value)
        except:
            self.ui.lineEdit.setText(value[:-1])
    def changeValueLine_2(self,value):
        global second_value
        try:
            second_value = int(value)
        except:
            self.ui.lineEdit_2.setText(value[:-1])
    def changeValueLine_3(self,value):
        global third_value
        try:
            third_value = int(value)
        except:
            self.ui.lineEdit_3.setText(value[:-1])

    def changeValue(self, value):
        global first_value
        self.ui.lineEdit.setText(str(value))
        first_value = value
    def changeValue_2(self, value):
        global second_value
        self.ui.lineEdit_2.setText(str(value))
        second_value = value
    def changeValue_3(self, value):
        global third_value
        self.ui.lineEdit_3.setText(str(value))
        third_value = value
        if first_value != 0 and second_value != 0:
            self.change_output()

    def change_output(self):

        self.ui.lineEdit_4.setText(str(value))
        self.ui.lineEdit_5.setText(str(value))
        self.ui.lineEdit_6.setText(str(value))

class First(QtWidgets.QMainWindow):
    def __init__(self):
        super(First, self).__init__()
        self.ui = first_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_second)

    def open_second(self):
        w1.setVisible(False)
        self.w2 = Second()
        self.w2.show()


app = QtWidgets.QApplication([])
w1 = First()
w1.show()
sys.exit(app.exec())
