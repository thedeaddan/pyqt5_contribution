from PyQt5 import QtWidgets
from gui import first_window,second_window,third_window
import sys

Open = False
class Second(QtWidgets.QMainWindow):
    def __init__(self):
        super(Second, self).__init__()
        self.ui = second_window.Ui_MainWindow()
        self.ui.setupUi(self)

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
