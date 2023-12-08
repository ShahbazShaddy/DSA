# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainaFZuyM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1331, 670)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 65))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(200, 65))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Toggle.setFont(font)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_top.sizePolicy().hasHeightForWidth())
        self.frame_top.setSizePolicy(sizePolicy1)
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.dropdown_menu = QComboBox(self.frame_top)
        self.dropdown_menu.addItem("")
        self.dropdown_menu.addItem("")
        self.dropdown_menu.addItem("")
        self.dropdown_menu.addItem("")
        self.dropdown_menu.addItem("")
        self.dropdown_menu.addItem("")
        self.dropdown_menu.addItem("")
        self.dropdown_menu.addItem("")
        self.dropdown_menu.addItem("")
        self.dropdown_menu.setObjectName(u"dropdown_menu")
        self.dropdown_menu.setEnabled(True)
        self.dropdown_menu.setGeometry(QRect(20, 10, 191, 51))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dropdown_menu.sizePolicy().hasHeightForWidth())
        self.dropdown_menu.setSizePolicy(sizePolicy2)
        self.dropdown_menu.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(10)
        font1.setItalic(True)
        self.dropdown_menu.setFont(font1)
        self.dropdown_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.dropdown_menu.setAutoFillBackground(False)
        self.dropdown_menu.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:2px solid rbg(37,39,48);\n"
"	padding-left:10px;\n"
"}\n"
"\n"
"")
        self.dropdown_menu.setEditable(False)
        self.dropdown_menu.setDuplicatesEnabled(False)
        self.dropdown_menu.setFrame(True)
        self.btn_search = QLineEdit(self.frame_top)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setGeometry(QRect(880, 10, 221, 51))
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(12)
        self.btn_search.setFont(font2)
        self.btn_search.setStyleSheet(u"QLineEdit{\n"
"	border-color: rgb(255, 255, 255);\n"
"	border:2px solid rbg(37,39,48);\n"
"	border-radius:20px 14px;\n"
"	color: #FFF;\n"
"	padding-left:20px;\n"
"	padding-right:20px;\n"
"	backgroung-color: rgb(34,36,44);\n"
"}")
        self.btn_multiLvlSorting = QPushButton(self.frame_top)
        self.btn_multiLvlSorting.setObjectName(u"btn_multiLvlSorting")
        self.btn_multiLvlSorting.setGeometry(QRect(600, 10, 221, 51))
        font3 = QFont()
        font3.setFamily(u"Times New Roman")
        font3.setPointSize(10)
        self.btn_multiLvlSorting.setFont(font3)
        self.btn_multiLvlSorting.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_multiLvlSorting.setStyleSheet(u"QPushButton{	\n"
"\n"
"	border-radius:10px 11px;\n"
"	color: #FFF;\n"
"	padding-left:20px;\n"
"	padding-right:20px;\n"
"	backgroung-color: rgb(34,36,44);\n"
"	background-color: rgb(0, 126, 0);\n"
"}")
        self.btn_start = QPushButton(self.frame_top)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(250, 10, 131, 51))
        font4 = QFont()
        font4.setFamily(u"Times New Roman")
        font4.setPointSize(13)
        self.btn_start.setFont(font4)
        self.btn_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start.setStyleSheet(u"QPushButton{	\n"
"\n"
"	border-radius:22px;\n"
"	color: #FFF;\n"
"	padding-left:20px;\n"
"	padding-right:20px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_stop = QPushButton(self.frame_top)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setGeometry(QRect(420, 10, 131, 51))
        self.btn_stop.setFont(font4)
        self.btn_stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stop.setStyleSheet(u"QPushButton{	\n"
"\n"
"	border-radius:22px;\n"
"	color: #FFF;\n"
"	padding-left:20px;\n"
"	padding-right:20px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        self.search_count = QLabel(self.frame_top)
        self.search_count.setObjectName(u"search_count")
        self.search_count.setGeometry(QRect(1000, 20, 51, 31))
        self.search_count.setStyleSheet(u"color: #FFF;\n"
"backgroung-color: rgb(34,36,44);")
        self.search_count.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(200, 0))
        self.frame_left_menu.setMaximumSize(QSize(200, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setMinimumSize(QSize(200, 300))
        self.frame_top_menus.setMaximumSize(QSize(200, 300))
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 55))
        font5 = QFont()
        font5.setFamily(u"Times New Roman")
        font5.setPointSize(14)
        self.btn_page_1.setFont(font5)
        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_1)

        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 55))
        font6 = QFont()
        font6.setFamily(u"Times New Roman")
        font6.setPointSize(14)
        font6.setBold(False)
        font6.setWeight(50)
        self.btn_page_2.setFont(font6)
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 55))
        self.btn_page_3.setFont(font5)
        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_3)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tableWidget = QTableWidget(self.page_1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setStyleSheet(u"gridline-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 255);\n"
"gridline-color: rgb(85, 0, 0);\n"
"color: rgb(85, 0, 0);\n"
"")
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setColumnCount(0)

        self.verticalLayout_7.addWidget(self.tableWidget)

        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame)

        self.progressBar = QProgressBar(self.page_1)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: none;\n"
"	text-align: center;\n"
"	border: 21px;\n"
"}\n"
"QProgressBar::chunk{	\n"
"	\n"
"}\n"
"")
        self.progressBar.setValue(0)

        self.verticalLayout_7.addWidget(self.progressBar)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-30, -60, 16777215, 16777215))
        self.label_2.setMinimumSize(QSize(16777214, 16777214))
        font7 = QFont()
        font7.setPointSize(40)
        self.label_2.setFont(font7)
        self.label_2.setStyleSheet(u"")
        self.widget = QWidget(self.page_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(220, -11, 471, 611))
        self.widget.setStyleSheet(u"QPushButton#pushButton{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushButton:pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{	\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color:rgba(85, 98, 112, 255);\n"
"}\n"
"QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{	\n"
"	color:rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;"
                        "\n"
"	color:rgba(115, 128, 142, 255);\n"
"}")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 30, 300, 420))
        self.label_6.setStyleSheet(u"border-image: url(:/images/background.png);\n"
"border-radius:20px;")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 30, 381, 541))
        self.label_7.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
"border-radius:20px;")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 40, 361, 521))
        self.label_8.setStyleSheet(u"background-color:rgba(0, 0, 0, 100);\n"
"border-radius:15px;\n"
"background-image: url(:/images/images/background.png);")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(180, 120, 161, 51))
        font8 = QFont()
        font8.setPointSize(20)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_9.setFont(font8)
        self.label_9.setStyleSheet(u"color:rgba(255, 255, 255);\n"
"background-color: rgb(36, 85, 99);")
        self.admin_name = QLineEdit(self.widget)
        self.admin_name.setObjectName(u"admin_name")
        self.admin_name.setGeometry(QRect(130, 210, 200, 40))
        font9 = QFont()
        font9.setPointSize(10)
        self.admin_name.setFont(font9)
        self.admin_name.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.admin_password = QLineEdit(self.widget)
        self.admin_password.setObjectName(u"admin_password")
        self.admin_password.setGeometry(QRect(130, 280, 200, 40))
        self.admin_password.setFont(font9)
        self.admin_password.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.admin_password.setEchoMode(QLineEdit.Password)
        self.Login_btn = QPushButton(self.widget)
        self.Login_btn.setObjectName(u"Login_btn")
        self.Login_btn.setGeometry(QRect(130, 360, 200, 40))
        font10 = QFont()
        font10.setPointSize(12)
        font10.setBold(True)
        font10.setWeight(75)
        self.Login_btn.setFont(font10)
        self.Login_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Login_btn.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.733, y1:0.705, x2:1, y2:1, stop:0 rgba(0, 0, 118, 255), stop:1 rgba(255, 255, 255));\n"
"border-radius:20px")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 9, 1043, 569))
        self.label.setFont(font7)
        self.label.setStyleSheet(u"color: #FFF;")
        self.label.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self.page_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(19, 49, 201, 101))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.tableWidget_admin = QTableWidget(self.page_3)
        self.tableWidget_admin.setObjectName(u"tableWidget_admin")
        self.tableWidget_admin.setEnabled(True)
        self.tableWidget_admin.setGeometry(QRect(0, 0, 1111, 541))
        sizePolicy.setHeightForWidth(self.tableWidget_admin.sizePolicy().hasHeightForWidth())
        self.tableWidget_admin.setSizePolicy(sizePolicy)
        self.tableWidget_admin.setMinimumSize(QSize(0, 0))
        self.tableWidget_admin.setStyleSheet(u"gridline-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 255);\n"
"gridline-color: rgb(85, 0, 0);\n"
"color: rgb(85, 0, 0);\n"
"")
        self.tableWidget_admin.setFrameShadow(QFrame.Sunken)
        self.tableWidget_admin.setShowGrid(True)
        self.tableWidget_admin.setGridStyle(Qt.SolidLine)
        self.tableWidget_admin.setWordWrap(True)
        self.tableWidget_admin.setColumnCount(0)
        self.progressBar_admin = QProgressBar(self.page_3)
        self.progressBar_admin.setObjectName(u"progressBar_admin")
        self.progressBar_admin.setGeometry(QRect(0, 550, 1093, 21))
        self.progressBar_admin.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: none;\n"
"	text-align: center;\n"
"	border: 21px;\n"
"}\n"
"QProgressBar::chunk{	\n"
"	\n"
"}\n"
"")
        self.progressBar_admin.setValue(0)
        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Nofil Analytics App", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"Main Menu", None))
        self.dropdown_menu.setItemText(0, QCoreApplication.translate("MainWindow", u"Merge Sort", None))
        self.dropdown_menu.setItemText(1, QCoreApplication.translate("MainWindow", u"Hybrid Merge Sort", None))
        self.dropdown_menu.setItemText(2, QCoreApplication.translate("MainWindow", u"Bubble Sort", None))
        self.dropdown_menu.setItemText(3, QCoreApplication.translate("MainWindow", u"Insertion Sort", None))
        self.dropdown_menu.setItemText(4, QCoreApplication.translate("MainWindow", u"Selection Sort", None))
        self.dropdown_menu.setItemText(5, QCoreApplication.translate("MainWindow", u"Quick Sort", None))
        self.dropdown_menu.setItemText(6, QCoreApplication.translate("MainWindow", u"Counting Sort", None))
        self.dropdown_menu.setItemText(7, QCoreApplication.translate("MainWindow", u"Radix Sort", None))
        self.dropdown_menu.setItemText(8, QCoreApplication.translate("MainWindow", u"Bucket Sort", None))

        self.btn_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.btn_multiLvlSorting.setText(QCoreApplication.translate("MainWindow", u"Multi-Level Sorting", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.search_count.setText("")
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"Sort and Search", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"Admin Login", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_2.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.admin_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  User Name", None))
        self.admin_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Password", None))
        self.Login_btn.setText(QCoreApplication.translate("MainWindow", u"L o g  I n", None))
        self.label.setText("")
    # retranslateUi

