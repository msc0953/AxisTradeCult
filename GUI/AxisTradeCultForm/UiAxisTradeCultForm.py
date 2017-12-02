# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'axistradecultform.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AxisTradeCultForm(object):
    def setupUi(self, AxisTradeCultForm):
        AxisTradeCultForm.setObjectName("AxisTradeCultForm")
        AxisTradeCultForm.resize(930, 533)
        self.centralWidget = QtWidgets.QWidget(AxisTradeCultForm)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 911, 471))
        self.tabWidget.setObjectName("tabWidget")
        self.tabOverview = QtWidgets.QWidget()
        self.tabOverview.setObjectName("tabOverview")
        self.DisplayDate = QtWidgets.QDateEdit(self.tabOverview)
        self.DisplayDate.setGeometry(QtCore.QRect(70, 10, 110, 31))
        self.DisplayDate.setObjectName("DisplayDate")
        self.StockGroupsComboBox = QtWidgets.QComboBox(self.tabOverview)
        self.StockGroupsComboBox.setGeometry(QtCore.QRect(200, 10, 141, 31))
        self.StockGroupsComboBox.setObjectName("StockGroupsComboBox")
        self.UpdateButton = QtWidgets.QPushButton(self.tabOverview)
        self.UpdateButton.setGeometry(QtCore.QRect(800, 10, 91, 31))
        self.UpdateButton.setObjectName("UpdateButton")
        self.listView = QtWidgets.QListView(self.tabOverview)
        self.listView.setGeometry(QtCore.QRect(5, 50, 891, 381))
        self.listView.setObjectName("listView")
        self.UpdateProgressBar = QtWidgets.QProgressBar(self.tabOverview)
        self.UpdateProgressBar.setGeometry(QtCore.QRect(360, 10, 181, 31))
        self.UpdateProgressBar.setProperty("value", 0)
        self.UpdateProgressBar.setObjectName("UpdateProgressBar")
        self.SymbolLabel = QtWidgets.QLabel(self.tabOverview)
        self.SymbolLabel.setGeometry(QtCore.QRect(20, 50, 60, 31))
        self.SymbolLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SymbolLabel.setObjectName("SymbolLabel")
        self.OpenLabel = QtWidgets.QLabel(self.tabOverview)
        self.OpenLabel.setGeometry(QtCore.QRect(90, 50, 60, 31))
        self.OpenLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.OpenLabel.setObjectName("OpenLabel")
        self.HightLabel = QtWidgets.QLabel(self.tabOverview)
        self.HightLabel.setGeometry(QtCore.QRect(160, 50, 60, 31))
        self.HightLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.HightLabel.setObjectName("HightLabel")
        self.LowLabel = QtWidgets.QLabel(self.tabOverview)
        self.LowLabel.setGeometry(QtCore.QRect(230, 50, 60, 31))
        self.LowLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LowLabel.setObjectName("LowLabel")
        self.CloseLabel = QtWidgets.QLabel(self.tabOverview)
        self.CloseLabel.setGeometry(QtCore.QRect(300, 50, 60, 31))
        self.CloseLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CloseLabel.setObjectName("CloseLabel")
        self.VolumeLabel = QtWidgets.QLabel(self.tabOverview)
        self.VolumeLabel.setGeometry(QtCore.QRect(510, 50, 60, 31))
        self.VolumeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.VolumeLabel.setObjectName("VolumeLabel")
        self.ChangeCLabel = QtWidgets.QLabel(self.tabOverview)
        self.ChangeCLabel.setGeometry(QtCore.QRect(370, 50, 60, 31))
        self.ChangeCLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ChangeCLabel.setObjectName("ChangeCLabel")
        self.ChangeVLabel = QtWidgets.QLabel(self.tabOverview)
        self.ChangeVLabel.setGeometry(QtCore.QRect(580, 50, 60, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ChangeVLabel.setFont(font)
        self.ChangeVLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ChangeVLabel.setObjectName("ChangeVLabel")
        self.AvgC3MLabel = QtWidgets.QLabel(self.tabOverview)
        self.AvgC3MLabel.setGeometry(QtCore.QRect(440, 50, 60, 31))
        self.AvgC3MLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.AvgC3MLabel.setObjectName("AvgC3MLabel")
        self.AvgV3MLabel = QtWidgets.QLabel(self.tabOverview)
        self.AvgV3MLabel.setGeometry(QtCore.QRect(650, 50, 60, 31))
        self.AvgV3MLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.AvgV3MLabel.setObjectName("AvgV3MLabel")
        self.GraphSampleButton = QtWidgets.QPushButton(self.tabOverview)
        self.GraphSampleButton.setEnabled(True)
        self.GraphSampleButton.setGeometry(QtCore.QRect(830, 53, 51, 25))
        self.GraphSampleButton.setObjectName("GraphSampleButton")
        self.line = QtWidgets.QFrame(self.tabOverview)
        self.line.setGeometry(QtCore.QRect(30, 70, 791, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.StrikePrice1YLabel = QtWidgets.QLabel(self.tabOverview)
        self.StrikePrice1YLabel.setGeometry(QtCore.QRect(700, 50, 120, 31))
        self.StrikePrice1YLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.StrikePrice1YLabel.setObjectName("StrikePrice1YLabel")
        self.Stockline = QtWidgets.QLineEdit(self.tabOverview)
        self.Stockline.setGeometry(QtCore.QRect(560, 10, 71, 31))
        self.Stockline.setObjectName("Stockline")
        self.AddButton = QtWidgets.QPushButton(self.tabOverview)
        self.AddButton.setGeometry(QtCore.QRect(650, 10, 71, 31))
        self.AddButton.setObjectName("AddButton")
        self.StockCheckBox = QtWidgets.QCheckBox(self.tabOverview)
        self.StockCheckBox.setGeometry(QtCore.QRect(15, 50, 80, 31))
        self.StockCheckBox.setText("")
        self.StockCheckBox.setObjectName("StockCheckBox")
        self.DelButton = QtWidgets.QPushButton(self.tabOverview)
        self.DelButton.setGeometry(QtCore.QRect(10, 10, 41, 31))
        self.DelButton.setObjectName("DelButton")
        self.tabWidget.addTab(self.tabOverview, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        AxisTradeCultForm.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(AxisTradeCultForm)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 930, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuSetting = QtWidgets.QMenu(self.menuBar)
        self.menuSetting.setObjectName("menuSetting")
        AxisTradeCultForm.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(AxisTradeCultForm)
        self.statusBar.setObjectName("statusBar")
        AxisTradeCultForm.setStatusBar(self.statusBar)
        self.actionDataManager = QtWidgets.QAction(AxisTradeCultForm)
        self.actionDataManager.setObjectName("actionDataManager")
        self.menuSetting.addAction(self.actionDataManager)
        self.menuBar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(AxisTradeCultForm)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AxisTradeCultForm)

    def retranslateUi(self, AxisTradeCultForm):
        _translate = QtCore.QCoreApplication.translate
        AxisTradeCultForm.setWindowTitle(_translate("AxisTradeCultForm", "AxisTradeCultForm"))
        self.UpdateButton.setText(_translate("AxisTradeCultForm", "Update"))
        self.SymbolLabel.setText(_translate("AxisTradeCultForm", "Symbol"))
        self.OpenLabel.setText(_translate("AxisTradeCultForm", "Open"))
        self.HightLabel.setText(_translate("AxisTradeCultForm", "High"))
        self.LowLabel.setText(_translate("AxisTradeCultForm", "Low"))
        self.CloseLabel.setText(_translate("AxisTradeCultForm", "Close"))
        self.VolumeLabel.setText(_translate("AxisTradeCultForm", "Volume"))
        self.ChangeCLabel.setText(_translate("AxisTradeCultForm", "Change"))
        self.ChangeVLabel.setText(_translate("AxisTradeCultForm", "Change"))
        self.AvgC3MLabel.setText(_translate("AxisTradeCultForm", "Avg(3M)"))
        self.AvgV3MLabel.setText(_translate("AxisTradeCultForm", "Avg(3M)"))
        self.GraphSampleButton.setText(_translate("AxisTradeCultForm", "Graph"))
        self.StrikePrice1YLabel.setText(_translate("AxisTradeCultForm", "Strike Price(1Y)"))
        self.AddButton.setText(_translate("AxisTradeCultForm", "Add"))
        self.DelButton.setText(_translate("AxisTradeCultForm", "Del"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOverview), _translate("AxisTradeCultForm", "Overview"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("AxisTradeCultForm", "Tab 2"))
        self.menuSetting.setTitle(_translate("AxisTradeCultForm", "Setting"))
        self.actionDataManager.setText(_translate("AxisTradeCultForm", "DataManager"))

