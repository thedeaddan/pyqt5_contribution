# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 0, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 130, 201, 31))
        self.lineEdit.setFrame(False)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 260, 201, 31))
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 230, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 260, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 130, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(60, 170, 201, 22))
        self.horizontalSlider.setMinimum(1000)
        self.horizontalSlider.setMaximum(10000000)
        self.horizontalSlider.setSingleStep(1000)
        self.horizontalSlider.setProperty("value", 1000)
        self.horizontalSlider.setSliderPosition(1000)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(60, 300, 201, 22))
        self.horizontalSlider_2.setMinimum(31)
        self.horizontalSlider_2.setMaximum(1825)
        self.horizontalSlider_2.setSingleStep(1)
        self.horizontalSlider_2.setPageStep(1)
        self.horizontalSlider_2.setProperty("value", 1)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 390, 201, 31))
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setDragEnabled(False)
        self.lineEdit_3.setClearButtonEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(60, 430, 201, 22))
        self.horizontalSlider_3.setMinimum(1000)
        self.horizontalSlider_3.setMaximum(5000000)
        self.horizontalSlider_3.setSingleStep(1000)
        self.horizontalSlider_3.setProperty("value", 1000)
        self.horizontalSlider_3.setSliderPosition(1000)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 360, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 390, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(99, 300, 3, 19))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(142, 440, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(260, 430, 3, 19))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(60, 430, 3, 19))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 440, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(250, 440, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(60, 300, 3, 19))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(250, 310, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(138, 302, 3, 19))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(260, 300, 3, 19))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(127, 310, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 310, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(90, 310, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(145, 180, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(70, 180, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(157, 172, 3, 19))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(260, 170, 3, 19))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(82, 170, 3, 19))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(30, 180, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(60, 170, 3, 19))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(260, 180, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(159, 430, 3, 19))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(490, 100, 281, 411))
        self.textBrowser.setObjectName("textBrowser")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(530, 110, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(530, 150, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(530, 180, 201, 27))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setFrame(True)
        self.lineEdit_4.setDragEnabled(False)
        self.lineEdit_4.setClearButtonEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(530, 250, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(530, 210, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(530, 360, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(530, 320, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(693, 182, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(527, 280, 201, 27))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setFrame(True)
        self.lineEdit_5.setDragEnabled(False)
        self.lineEdit_5.setClearButtonEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(690, 282, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(527, 388, 201, 27))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setFrame(True)
        self.lineEdit_6.setDragEnabled(False)
        self.lineEdit_6.setClearButtonEnabled(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(690, 390, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 440, 192, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background: rgb(0,85,255);\n"
"color: rgb(255,255,255);\n"
"")
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "??????????????????????"))
        self.label.setText(_translate("MainWindow", "???????????????????? ??????????"))
        self.label_2.setText(_translate("MainWindow", "??????????"))
        self.label_3.setText(_translate("MainWindow", "????????"))
        self.label_4.setText(_translate("MainWindow", "????????"))
        self.label_5.setText(_translate("MainWindow", "??????."))
        self.label_7.setText(_translate("MainWindow", "?????????????????????? ????????????????????"))
        self.label_6.setText(_translate("MainWindow", "??????."))
        self.label_8.setText(_translate("MainWindow", "2,5 ??????"))
        self.label_9.setText(_translate("MainWindow", "0 ??????."))
        self.label_10.setText(_translate("MainWindow", "5 ??????"))
        self.label_11.setText(_translate("MainWindow", "5 ??????"))
        self.label_12.setText(_translate("MainWindow", "2 ????????"))
        self.label_13.setText(_translate("MainWindow", "1 ??????."))
        self.label_14.setText(_translate("MainWindow", "1 ??????"))
        self.label_15.setText(_translate("MainWindow", "5 ??????"))
        self.label_16.setText(_translate("MainWindow", "1 ??????"))
        self.label_17.setText(_translate("MainWindow", "1 ??????."))
        self.label_18.setText(_translate("MainWindow", "10 ??????"))
        self.label_19.setText(_translate("MainWindow", "????????????????????"))
        self.label_20.setText(_translate("MainWindow", "?????????? ???? ????????????:"))
        self.label_21.setText(_translate("MainWindow", "?????????? ???? ????????????:"))
        self.label_22.setText(_translate("MainWindow", "??????????????????????"))
        self.label_23.setText(_translate("MainWindow", "?????????? ???? ????????????:"))
        self.label_24.setText(_translate("MainWindow", "????????????????"))
        self.label_25.setText(_translate("MainWindow", "??????."))
        self.label_26.setText(_translate("MainWindow", "??????."))
        self.label_27.setText(_translate("MainWindow", "??????."))
        self.pushButton.setText(_translate("MainWindow", "???????????????? ??????????????????"))
