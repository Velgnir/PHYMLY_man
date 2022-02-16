# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI2.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStatusBar, QTextBrowser,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1178, 705)
        MainWindow.setStyleSheet(u"background-color: #4C566A;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 651, 261))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_8 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"color: #c9cdd4;")

        self.gridLayout.addWidget(self.lineEdit_8, 2, 4, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: #D8DEE9;")

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 5, 1, 1)

        self.lineEdit_7 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"color: #c9cdd4;")

        self.gridLayout.addWidget(self.lineEdit_7, 2, 1, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: #D8DEE9;")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"color: #c9cdd4;")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"color: #D8DEE9;")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_16)

        self.lineEdit_9 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setStyleSheet(u"color: #c9cdd4;")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_9)


        self.gridLayout.addLayout(self.formLayout, 1, 6, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 5, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.gridLayout.addLayout(self.horizontalLayout, 2, 2, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: #D8DEE9;")

        self.gridLayout.addWidget(self.label_8, 2, 3, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 5, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"color: #c9cdd4;")

        self.gridLayout.addWidget(self.lineEdit_4, 0, 7, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: #D8DEE9;")

        self.gridLayout.addWidget(self.label_2, 0, 6, 1, 1)

        self.checkBox = QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"color: #D8DEE9;")

        self.gridLayout.addWidget(self.checkBox, 3, 6, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"color: #D8DEE9;")

        self.gridLayout.addWidget(self.label_22, 2, 6, 1, 1)

        self.lineEdit_14 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setStyleSheet(u"color: #c9cdd4;")

        self.gridLayout.addWidget(self.lineEdit_14, 2, 7, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"color: #D8DEE9;")

        self.gridLayout.addWidget(self.label_23, 3, 0, 1, 1)

        self.lineEdit_15 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setStyleSheet(u"color: #c9cdd4;")

        self.gridLayout.addWidget(self.lineEdit_15, 3, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: #D8DEE9;")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"color: #c9cdd4;")

        self.gridLayout.addWidget(self.lineEdit_5, 0, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #D8DEE9;")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"color: #c9cdd4;")

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: #D8DEE9;")

        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)

        self.lineEdit_6 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"color: #c9cdd4;")

        self.gridLayout.addWidget(self.lineEdit_6, 0, 4, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: #D8DEE9;")

        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"color: #c9cdd4;")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 4, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 360, 621, 31))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: #D8DEE9;")

        self.gridLayout_2.addWidget(self.label_12, 0, 3, 1, 1)

        self.scrollArea_3 = QScrollArea(self.gridLayoutWidget_2)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 155, 27))
        self.textEdit_3 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(0, 0, 161, 31))
        self.textEdit_3.setStyleSheet(u"color: #c9cdd4;")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_2.addWidget(self.scrollArea_3, 0, 6, 1, 1)

        self.scrollArea_2 = QScrollArea(self.gridLayoutWidget_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 154, 27))
        self.textEdit_2 = QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(0, 0, 161, 31))
        self.textEdit_2.setStyleSheet(u"color: #c9cdd4;")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_2.addWidget(self.scrollArea_2, 0, 4, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: #D8DEE9;")

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(self.gridLayoutWidget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 155, 27))
        self.textEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 0, 161, 31))
        self.textEdit.setStyleSheet(u"color: #c9cdd4;")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 1, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: #D8DEE9;")

        self.gridLayout_2.addWidget(self.label_13, 0, 5, 1, 1)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 320, 325, 31))
        self.label_14.setStyleSheet(u"color: #D8DEE9;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(810, 520, 261, 51))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: #D8DEE9;")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(890, 70, 125, 20))
        self.label_17.setStyleSheet(u"color: #D8DEE9;")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(1040, 220, 125, 20))
        self.label_18.setStyleSheet(u"color: #D8DEE9;")
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(890, 380, 125, 16))
        self.label_19.setStyleSheet(u"color: #D8DEE9;")
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(730, 220, 275, 16))
        self.label_20.setStyleSheet(u"color: #D8DEE9;")
        self.lineEdit_10 = QLineEdit(self.centralwidget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(730, 250, 113, 20))
        self.lineEdit_10.setStyleSheet(u"color: #c9cdd4;")
        self.lineEdit_11 = QLineEdit(self.centralwidget)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(1040, 250, 113, 20))
        self.lineEdit_11.setStyleSheet(u"color: #c9cdd4;")
        self.lineEdit_12 = QLineEdit(self.centralwidget)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(890, 410, 113, 20))
        self.lineEdit_12.setStyleSheet(u"color: #c9cdd4;")
        self.lineEdit_13 = QLineEdit(self.centralwidget)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(890, 100, 111, 20))
        self.lineEdit_13.setStyleSheet(u"color: #c9cdd4;")
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(710, 30, 475, 31))
        self.label_21.setStyleSheet(u"color: #D8DEE9;")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(680, 0, 20, 511))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(900, 220, 91, 91))
        self.label_24.setPixmap(QPixmap(u"C:/Users/\u041c\u0438\u043b\u043e\u0440\u0434/Documents/Eren.png"))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(70, 520, 261, 51))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"background-color: #D8DEE9;")
        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(760, 500, 381, 16))
        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(760, 450, 381, 31))
        self.scrollArea_4 = QScrollArea(self.centralwidget)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setGeometry(QRect(10, 580, 1101, 81))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1099, 79))
        self.textBrowser = QTextBrowser(self.scrollAreaWidgetContents_4)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 0, 1101, 81))
        self.textBrowser.setStyleSheet(u"color:#BF616A;")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1178, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)

        self.label_7.setFont(font1)
        self.label_5.setFont(font1)
        self.label_16.setFont(font1)
        self.label_8.setFont(font1)
        self.label_2.setFont(font1)
        self.label_22.setFont(font1)
        self.label_23.setFont(font1)
        self.label_4.setFont(font1)
        self.label.setFont(font1)
        self.label_6.setFont(font1)
        self.label_3.setFont(font1)
        self.label_17.setFont(font1)
        self.label_18.setFont(font1)
        self.label_19.setFont(font1)
        self.label_20.setFont(font1)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"standard temperature[\u00b0 C]:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Temperature limit[\u00b0 C]:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"limit of steps in time:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"specific heat capacity[ kJ/(kg\u22c5C)]", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"step in time[S/2]:", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"rotate matrix on 90\u00b0", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"thermal conduction:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"density:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Step length, X axis [m]", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Number of steps, X axis[m]:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Step width, Y axis [m]:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Number of steps, Y axis[m]", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"y=", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"x=", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"temperature[\u00b0 C]=", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Create a temperature graphs by function here:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"upper border:  f1(x)=", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"right border:  f2(x)=", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"lower border:  f3(x)=", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"left border:  f4(x)=", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"You can make border values, which will be consant and heat matrix, here:", None))
        self.label_24.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Watch", None))
        self.label_25.setText("")
        self.label_26.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

