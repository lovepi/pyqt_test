# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 's2_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(937, 625)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(937, 625))
        MainWindow.setMaximumSize(QtCore.QSize(937, 625))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 54, 12))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 10, 681, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 54, 12))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 40, 681, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 54, 12))
        self.label_3.setObjectName("label_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(220, 120, 89, 16))
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(290, 120, 89, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(360, 120, 89, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup.addButton(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(430, 120, 89, 16))
        self.radioButton_4.setObjectName("radioButton_4")
        self.buttonGroup.addButton(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(500, 120, 89, 16))
        self.radioButton_5.setObjectName("radioButton_5")
        self.buttonGroup.addButton(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(570, 120, 89, 16))
        self.radioButton_6.setObjectName("radioButton_6")
        self.buttonGroup.addButton(self.radioButton_6)
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setGeometry(QtCore.QRect(640, 120, 89, 16))
        self.radioButton_7.setObjectName("radioButton_7")
        self.buttonGroup.addButton(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_8.setGeometry(QtCore.QRect(710, 120, 89, 16))
        self.radioButton_8.setObjectName("radioButton_8")
        self.buttonGroup.addButton(self.radioButton_8)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 150, 881, 441))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 10, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 851, 371))
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 54, 12))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 10, 611, 20))
        self.lineEdit_3.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(710, 10, 41, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(760, 10, 41, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(810, 10, 41, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 40, 851, 371))
        self.textEdit_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 54, 12))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 10, 341, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(420, 20, 54, 12))
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(470, 10, 71, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_7.setGeometry(QtCore.QRect(550, 10, 81, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_8.setGeometry(QtCore.QRect(640, 10, 81, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_9.setGeometry(QtCore.QRect(420, 40, 51, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_19.setGeometry(QtCore.QRect(480, 40, 51, 23))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_20.setGeometry(QtCore.QRect(540, 40, 51, 23))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_21.setGeometry(QtCore.QRect(600, 40, 51, 23))
        self.pushButton_21.setObjectName("pushButton_21")
        self.textEdit_5 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_5.setGeometry(QtCore.QRect(10, 70, 851, 171))
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(10, 250, 54, 12))
        self.label_10.setObjectName("label_10")
        self.textEdit_6 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_6.setGeometry(QtCore.QRect(10, 270, 851, 141))
        self.textEdit_6.setObjectName("textEdit_6")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.pushButton_22 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_22.setGeometry(QtCore.QRect(244, 10, 91, 23))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_23.setGeometry(QtCore.QRect(740, 10, 111, 23))
        self.pushButton_23.setObjectName("pushButton_23")
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(20, 40, 54, 12))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(650, 40, 211, 16))
        self.label_14.setObjectName("label_14")
        self.textEdit_7 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_7.setGeometry(QtCore.QRect(10, 60, 851, 351))
        self.textEdit_7.setObjectName("textEdit_7")
        self.layoutWidget = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 201, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_4.addWidget(self.lineEdit_9)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget1.setGeometry(QtCore.QRect(490, 10, 213, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout.addWidget(self.lineEdit_10)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pushButton_24 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_24.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton_24.setObjectName("pushButton_24")
        self.textEdit_8 = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit_8.setGeometry(QtCore.QRect(10, 40, 851, 371))
        self.textEdit_8.setObjectName("textEdit_8")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.pushButton_25 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_25.setGeometry(QtCore.QRect(10, 10, 111, 23))
        self.pushButton_25.setObjectName("pushButton_25")
        self.listView = QtWidgets.QListView(self.tab_6)
        self.listView.setGeometry(QtCore.QRect(10, 40, 256, 371))
        self.listView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listView.setObjectName("listView")
        self.pushButton_26 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_26.setGeometry(QtCore.QRect(280, 10, 151, 23))
        self.pushButton_26.setObjectName("pushButton_26")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidget.setGeometry(QtCore.QRect(280, 40, 581, 371))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_27 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_27.setGeometry(QtCore.QRect(800, 10, 61, 23))
        self.pushButton_27.setObjectName("pushButton_27")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_6)
        self.layoutWidget2.setGeometry(QtCore.QRect(600, 10, 189, 22))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_3.addWidget(self.label_15)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_3.addWidget(self.lineEdit_11)
        self.tabWidget.addTab(self.tab_6, "")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(20, 80, 54, 12))
        self.label_16.setObjectName("label_16")
        self.radioButton_9 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_9.setGeometry(QtCore.QRect(150, 120, 89, 16))
        self.radioButton_9.setObjectName("radioButton_9")
        self.buttonGroup.addButton(self.radioButton_9)
        self.radioButton_10 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_10.setGeometry(QtCore.QRect(80, 120, 89, 16))
        self.radioButton_10.setObjectName("radioButton_10")
        self.buttonGroup.addButton(self.radioButton_10)
        self.radioButton_11 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_11.setGeometry(QtCore.QRect(80, 100, 89, 16))
        self.radioButton_11.setObjectName("radioButton_11")
        self.buttonGroup.addButton(self.radioButton_11)
        self.radioButton_12 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_12.setGeometry(QtCore.QRect(150, 100, 89, 16))
        self.radioButton_12.setObjectName("radioButton_12")
        self.buttonGroup.addButton(self.radioButton_12)
        self.radioButton_13 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_13.setGeometry(QtCore.QRect(780, 120, 89, 16))
        self.radioButton_13.setObjectName("radioButton_13")
        self.buttonGroup.addButton(self.radioButton_13)
        self.radioButton_14 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_14.setGeometry(QtCore.QRect(850, 120, 89, 16))
        self.radioButton_14.setObjectName("radioButton_14")
        self.buttonGroup.addButton(self.radioButton_14)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(80, 70, 681, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(780, 10, 106, 22))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_26 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_5.addWidget(self.label_26)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_3)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(780, 40, 118, 22))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_27 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_6.addWidget(self.label_27)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget4)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 937, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Strust2 漏洞利用工具"))
        self.label.setText(_translate("MainWindow", "目标："))
        self.label_2.setText(_translate("MainWindow", "Cookie："))
        self.label_3.setText(_translate("MainWindow", "漏洞："))
        self.radioButton.setText(_translate("MainWindow", "S2-037"))
        self.radioButton_2.setText(_translate("MainWindow", "S2-032"))
        self.radioButton_3.setText(_translate("MainWindow", "devMode"))
        self.radioButton_4.setText(_translate("MainWindow", "S2-019"))
        self.radioButton_5.setText(_translate("MainWindow", "S2-016"))
        self.radioButton_6.setText(_translate("MainWindow", "S2-013"))
        self.radioButton_7.setText(_translate("MainWindow", "S2-009"))
        self.radioButton_8.setText(_translate("MainWindow", "S2-005"))
        self.pushButton.setText(_translate("MainWindow", "获取信息"))
        self.pushButton_2.setText(_translate("MainWindow", "保存信息"))
        self.pushButton_3.setText(_translate("MainWindow", "清空"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "目标信息"))
        self.label_4.setText(_translate("MainWindow", "命令："))
        self.pushButton_4.setText(_translate("MainWindow", "执行"))
        self.pushButton_5.setText(_translate("MainWindow", "保存"))
        self.pushButton_6.setText(_translate("MainWindow", "清空"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "执行命令"))
        self.label_5.setText(_translate("MainWindow", "文件路径："))
        self.label_6.setText(_translate("MainWindow", "文件名："))
        self.pushButton_7.setText(_translate("MainWindow", "上传指定目录"))
        self.pushButton_8.setText(_translate("MainWindow", "上传当前目录"))
        self.pushButton_9.setText(_translate("MainWindow", "Test"))
        self.pushButton_19.setText(_translate("MainWindow", "JSP小马"))
        self.pushButton_20.setText(_translate("MainWindow", "K8cmd马"))
        self.pushButton_21.setText(_translate("MainWindow", "菜刀马"))
        self.textEdit_5.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "上传回显："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "文件上传"))
        self.pushButton_22.setText(_translate("MainWindow", "清空"))
        self.pushButton_23.setText(_translate("MainWindow", "上传大马"))
        self.label_13.setText(_translate("MainWindow", "大马内容："))
        self.label_14.setText(_translate("MainWindow", "上传后路径：为当前站点S2框架根目录"))
        self.label_11.setText(_translate("MainWindow", "小马地址："))
        self.label_12.setText(_translate("MainWindow", "输出文件名："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "连接小马"))
        self.pushButton_24.setText(_translate("MainWindow", "列根目录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "文件管理"))
        self.pushButton_25.setText(_translate("MainWindow", "读取目标网站列表"))
        self.pushButton_26.setText(_translate("MainWindow", "开始批量扫描"))
        self.pushButton_27.setText(_translate("MainWindow", "保存结果"))
        self.label_15.setText(_translate("MainWindow", "进程数："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "批量扫描"))
        self.label_16.setText(_translate("MainWindow", "UserAget："))
        self.radioButton_9.setText(_translate("MainWindow", "S2-045"))
        self.radioButton_10.setText(_translate("MainWindow", "S2-048"))
        self.radioButton_11.setText(_translate("MainWindow", "S2-053"))
        self.radioButton_12.setText(_translate("MainWindow", "S2-052"))
        self.radioButton_13.setText(_translate("MainWindow", "S2-003"))
        self.radioButton_14.setText(_translate("MainWindow", "S2-001"))
        self.comboBox.setItemText(0, _translate("MainWindow", "User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko"))
        self.comboBox.setItemText(1, _translate("MainWindow", "User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"))
        self.comboBox.setItemText(2, _translate("MainWindow", "User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"))
        self.comboBox.setItemText(3, _translate("MainWindow", "User-Agent: MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"))
        self.label_26.setText(_translate("MainWindow", "编码："))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "UTF-8"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "GB2312"))
        self.label_27.setText(_translate("MainWindow", "HTTP方法："))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "POST"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "GET"))
