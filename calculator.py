# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(522, 590)
        MainWindow.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 441, 511))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.push6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.push6.sizePolicy().hasHeightForWidth())
        self.push6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push6.setFont(font)
        self.push6.setStyleSheet("QPushButton{\n"
"    font: 75 20pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(159, 135, 255);\n"
"    border radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(231, 172, 255);\n"
"    background-color: rgb(255, 217, 238);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 221, 245);\n"
"}")
        self.push6.setObjectName("push6")
        self.gridLayout.addWidget(self.push6, 5, 2, 1, 1)
        self.pushsubtract = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.pushsubtract.sizePolicy().hasHeightForWidth())
        self.pushsubtract.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushsubtract.setFont(font)
        self.pushsubtract.setStyleSheet("QPushButton{\n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(122, 105, 255);\n"
"    border radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    rgb(111, 255, 103)\n"
"    background-color: rgb(255, 217, 238);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 221, 245);\n"
"}")
        self.pushsubtract.setObjectName("pushsubtract")
        self.gridLayout.addWidget(self.pushsubtract, 3, 3, 1, 1)
        self.push2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.push2.sizePolicy().hasHeightForWidth())
        self.push2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push2.setFont(font)
        self.push2.setStyleSheet("QPushButton{\n"
"    font: 75 20pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(159, 135, 255);\n"
"    border radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(231, 172, 255);\n"
"    background-color: rgb(255, 217, 238);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 221, 245);\n"
"}")
        self.push2.setObjectName("push2")
        self.gridLayout.addWidget(self.push2, 3, 1, 1, 1)
        self.push4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.push4.sizePolicy().hasHeightForWidth())
        self.push4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push4.setFont(font)
        self.push4.setStyleSheet("QPushButton{\n"
"    font: 75 20pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(159, 135, 255);\n"
"    border radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(231, 172, 255);\n"
"    background-color: rgb(255, 217, 238);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 221, 245);\n"
"}")
        self.push4.setObjectName("push4")
        self.gridLayout.addWidget(self.push4, 5, 0, 1, 1)
        self.push5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.push5.sizePolicy().hasHeightForWidth())
        self.push5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push5.setFont(font)
        self.push5.setStyleSheet("QPushButton{\n"
"    font: 75 20pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(159, 135, 255);\n"
"    border radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(231, 172, 255);\n"
"    background-color: rgb(255, 217, 238);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 221, 245);\n"
"}")
        self.push5.setObjectName("push5")
        self.gridLayout.addWidget(self.push5, 5, 1, 1, 1)
        self.pushmultiply = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.pushmultiply.sizePolicy().hasHeightForWidth())
        self.pushmultiply.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushmultiply.setFont(font)
        self.pushmultiply.setStyleSheet("QPushButton{\n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(122, 105, 255);\n"
"    border radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    rgb(111, 255, 103)\n"
"    background-color: rgb(255, 217, 238);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 221, 245);\n"
"}")
        self.pushmultiply.setObjectName("pushmultiply")
        self.gridLayout.addWidget(self.pushmultiply, 5, 3, 1, 1)
        self.push3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.push3.sizePolicy().hasHeightForWidth())
        self.push3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push3.setFont(font)
        self.push3.setStyleSheet("QPushButton{\n"
"    font: 75 20pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(159, 135, 255);\n"
"    border radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(231, 172, 255);\n"
"    background-color: rgb(255, 217, 238);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 221, 245);\n"
"}")
        self.push3.setObjectName("push3")
        self.gridLayout.addWidget(self.push3, 3, 2, 1, 1)
        self.pushequal = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.pushequal.sizePolicy().hasHeightForWidth())
        self.pushequal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushequal.setFont(font)
        self.pushequal.setStyleSheet("QPushButton{\n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(122, 105, 255);\n"
"    border radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    rgb(111, 255, 103)\n"
"    background-color: rgb(255, 217, 238);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 221, 245);\n"
"}")
        self.pushequal.setObjectName("pushequal")
        self.gridLayout.addWidget(self.pushequal, 7, 3, 1, 1)
        self.pushdecimal = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.pushdecimal.sizePolicy().hasHeightForWidth())
        self.pushdecimal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushdecimal.setFont(font)
        self.pushdecimal.setStyleSheet("QPushButton{\n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(122, 105, 255);\n"
"    border radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    rgb(111, 255, 103)\n"
"    background-color: rgb(255, 217, 238);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 221, 245);\n"
"}")
        self.pushdecimal.setObjectName("pushdecimal")
        self.gridLayout.addWidget(self.pushdecimal, 7, 2, 1, 1)
        self.pushdelete = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.pushdelete.sizePolicy().hasHeightForWidth())
        self.pushdelete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushdelete.setFont(font)
        self.pushdelete.setStyleSheet("QPushButton{\n"
"    font: 75 20pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(159, 135, 255);\n"
"    border radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(231, 172, 255);\n"
"    background-color: rgb(255, 217, 238);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 221, 245);\n"
"}\n"
"   ")
        self.pushdelete.setObjectName("pushdelete")
        self.gridLayout.addWidget(self.pushdelete, 1, 2, 1, 1)
        self.push1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.push1.sizePolicy().hasHeightForWidth())
        self.push1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push1.setFont(font)
        self.push1.setStyleSheet("QPushButton{\n"
"    font: 75 20pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(159, 135, 255);\n"
"    border radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(231, 172, 255);\n"
"    background-color: rgb(255, 217, 238);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 221, 245);\n"
"}")
        self.push1.setObjectName("push1")
        self.gridLayout.addWidget(self.push1, 3, 0, 1, 1)
        self.pushadd = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.pushadd.sizePolicy().hasHeightForWidth())
        self.pushadd.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushadd.setFont(font)
        self.pushadd.setStyleSheet("QPushButton{\n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(122, 105, 255);\n"
"    border radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    rgb(111, 255, 103)\n"
"    background-color: rgb(255, 217, 238);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 221, 245);\n"
"}")
        self.pushadd.setObjectName("pushadd")
        self.gridLayout.addWidget(self.pushadd, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(13)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 75 28pt \"MS Shell Dlg 2\";")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    font: 75 20pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(159, 135, 255);\n"
"    border radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(231, 172, 255);\n"
"    background-color: rgb(255, 217, 238);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 221, 245);\n"
"}\n"
" \n"
" ")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 2)
        self.push0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.push0.sizePolicy().hasHeightForWidth())
        self.push0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push0.setFont(font)
        self.push0.setStyleSheet("QPushButton{\n"
"    font: 75 20pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(159, 135, 255);\n"
"    border radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(231, 172, 255);\n"
"    background-color: rgb(255, 217, 238);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 221, 245);\n"
"}")
        self.push0.setObjectName("push0")
        self.gridLayout.addWidget(self.push0, 7, 0, 1, 2)
        self.push7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.push7.sizePolicy().hasHeightForWidth())
        self.push7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push7.setFont(font)
        self.push7.setStyleSheet("QPushButton{\n"
"    font: 75 20pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(159, 135, 255);\n"
"    border radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(231, 172, 255);\n"
"    background-color: rgb(255, 217, 238);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 221, 245);\n"
"}")
        self.push7.setObjectName("push7")
        self.gridLayout.addWidget(self.push7, 6, 0, 1, 1)
        self.push8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.push8.sizePolicy().hasHeightForWidth())
        self.push8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push8.setFont(font)
        self.push8.setStyleSheet("QPushButton{\n"
"    font: 75 20pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(159, 135, 255);\n"
"    border radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(231, 172, 255);\n"
"    background-color: rgb(255, 217, 238);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 221, 245);\n"
"}")
        self.push8.setObjectName("push8")
        self.gridLayout.addWidget(self.push8, 6, 1, 1, 1)
        self.push9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.push9.sizePolicy().hasHeightForWidth())
        self.push9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push9.setFont(font)
        self.push9.setStyleSheet("QPushButton{\n"
"    font: 75 20pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(159, 135, 255);\n"
"    border radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(231, 172, 255);\n"
"    background-color: rgb(255, 217, 238);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 221, 245);\n"
"}")
        self.push9.setObjectName("push9")
        self.gridLayout.addWidget(self.push9, 6, 2, 1, 1)
        self.pushdivide = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(12)
        sizePolicy.setHeightForWidth(self.pushdivide.sizePolicy().hasHeightForWidth())
        self.pushdivide.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushdivide.setFont(font)
        self.pushdivide.setStyleSheet("QPushButton{\n"
"    font: 75 36pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(122, 105, 255);\n"
"    border radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    rgb(111, 255, 103)\n"
"    background-color: rgb(255, 217, 238);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 221, 245);\n"
"}")
        self.pushdivide.setObjectName("pushdivide")
        self.gridLayout.addWidget(self.pushdivide, 6, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.push_1.clicked.connect(self.method_1)
        self.push_2.clicked.connect(self.method_2)
        self.push_3.clicked.connect(self.method_3)
        self.push_4.clicked.connect(self.method_4)
        self.push_5.clicked.connect(self.method_5)
        self.push_6.clicked.connect(self.method_6)
        self.push_7.clicked.connect(self.method_7)
        self.push_8.clicked.connect(self.method_8)
        self.push_9.clicked.connect(self.method_9)
        self.push_0.clicked.connect(self.method_0)
        self.push_decimal.clicked.connect(self.method_decimal)
        self.push_add.clicked.connect(self.method_add)
        self.push_subtract.clicked.connect(self.method_subtract)
        self.push_multiply.clicked.connect(self.method_multiply)
        self.push_divide.clicked.connect(self.method_divide)
        self.push_equal.clicked.connect(self.method_equal)
        self.push_Button.clicked.connect(self.method_Button)
        self.push_delete.clicked.connect(self.method_delete)

    def method_1(self):
        text=self.label.text()
        self.label.setText(text+"1")
        
    def method_2(self):
        text=self.label.text()
        self.label.setText(text+"2")
        
    def method_3(self):
        text=self.label.text()
        self.label.setText(text+"3")
        
    def method_4(self): 
        text=self.label.text()
        self.label.setText(text+"4")
        
    def method_5(self):
        text=self.label.text()
        self.label.setText(text+"5")
        
    def method_6(self):
        text=self.label.text()
        self.label.setText(text+"6")
        
    def method_7(self):
        text=self.label.text()
        self.label.setText(text+"7")
        
    def method_8(self):
        text=self.label.text()
        self.label.setText(text+"8")
        
    def method_9(self):
        text=self.label.text()
        self.label.setText(text+"9")
        
    def method_0(self):
        text=self.label.text()
        self.label.setText(text+"0")
        
    def method_decimal(self):
        text=self.label.text()
        self.label.setText(text+"decimal")
        
    def method_add(self):
        text=self.label.text()
        self.label.setText(text+"+")
        
    def method_subtract(self):
        text=self.label.text()
        self.label.setText(text+"-")
        
    def method_multiply(self):
        text=self.label.text()
        self.label.setText(text+"*")
        
    def method_divide(self):
        text=self.label.text()
        self.label.setText(text+"/")
        
    def method_equal(self):
        text=self.label.text()
        try:
            ans=eval(text)
            self.label.setText(str(ans))
        except:
            self.label.setText("Wrong Input")
            
    def method_Button(self):
        self.label.setText("")
        
    def method_delete(self):
        text=self.label.text()
        self.label.setText(text[:len(text)-1]) 
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.push6.setText(_translate("MainWindow", "6"))
        self.pushsubtract.setText(_translate("MainWindow", "-"))
        self.push2.setText(_translate("MainWindow", "2"))
        self.push4.setText(_translate("MainWindow", "4"))
        self.push5.setText(_translate("MainWindow", "5"))
        self.pushmultiply.setText(_translate("MainWindow", "*"))
        self.push3.setText(_translate("MainWindow", "3"))
        self.pushequal.setText(_translate("MainWindow", "="))
        self.pushdecimal.setText(_translate("MainWindow", "."))
        self.pushdelete.setText(_translate("MainWindow", "del"))
        self.push1.setText(_translate("MainWindow", "1"))
        self.pushadd.setText(_translate("MainWindow", "+"))
        self.pushButton.setText(_translate("MainWindow", "clear"))
        self.push0.setText(_translate("MainWindow", "0"))
        self.push7.setText(_translate("MainWindow", "7"))
        self.push8.setText(_translate("MainWindow", "8"))
        self.push9.setText(_translate("MainWindow", "9"))
        self.pushdivide.setText(_translate("MainWindow", "/"))


    if __name__ == "__main__":
     import sys
     app = QtWidgets.QApplication(sys.argv)
     MainWindow = QtWidgets.QMainWindow()
     ui = Ui_MainWindow()
     ui.setupUi(MainWindow)
     MainWindow.show()
     sys.exit(app.exec_())
