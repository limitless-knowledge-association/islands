# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 655)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons/island128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(622, 0))
        self.tabWidget.setObjectName("tabWidget")
        self.tabIslandManagement = QtWidgets.QWidget()
        self.tabIslandManagement.setObjectName("tabIslandManagement")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabIslandManagement)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.tabIslandManagement)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/icons/island256.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setContentsMargins(-1, 2, -1, 24)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.islandStatusLabel = QtWidgets.QLabel(self.tabIslandManagement)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.islandStatusLabel.sizePolicy().hasHeightForWidth())
        self.islandStatusLabel.setSizePolicy(sizePolicy)
        self.islandStatusLabel.setMaximumSize(QtCore.QSize(1965, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.islandStatusLabel.setFont(font)
        self.islandStatusLabel.setStyleSheet("")
        self.islandStatusLabel.setScaledContents(False)
        self.islandStatusLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.islandStatusLabel.setObjectName("islandStatusLabel")
        self.horizontalLayout_2.addWidget(self.islandStatusLabel)
        self.islandStatus = QtWidgets.QLabel(self.tabIslandManagement)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.islandStatus.sizePolicy().hasHeightForWidth())
        self.islandStatus.setSizePolicy(sizePolicy)
        self.islandStatus.setMaximumSize(QtCore.QSize(1965, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(173, 173, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 173, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.islandStatus.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.islandStatus.setFont(font)
        self.islandStatus.setStyleSheet("")
        self.islandStatus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.islandStatus.setObjectName("islandStatus")
        self.horizontalLayout_2.addWidget(self.islandStatus)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 14, -1, 0)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.island_access_label = QtWidgets.QLabel(self.tabIslandManagement)
        self.island_access_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.island_access_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.island_access_label.setObjectName("island_access_label")
        self.horizontalLayout_6.addWidget(self.island_access_label)
        self.island_access_address = QtWidgets.QLabel(self.tabIslandManagement)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.island_access_address.setFont(font)
        self.island_access_address.setStyleSheet("")
        self.island_access_address.setText("")
        self.island_access_address.setOpenExternalLinks(True)
        self.island_access_address.setObjectName("island_access_address")
        self.horizontalLayout_6.addWidget(self.island_access_address)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.island_admin_access_address = QtWidgets.QLabel(self.tabIslandManagement)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.island_admin_access_address.setFont(font)
        self.island_admin_access_address.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.island_admin_access_address.setStyleSheet("")
        self.island_admin_access_address.setText("")
        self.island_admin_access_address.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.island_admin_access_address.setOpenExternalLinks(True)
        self.island_admin_access_address.setObjectName("island_admin_access_address")
        self.horizontalLayout_8.addWidget(self.island_admin_access_address)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.groupBox = QtWidgets.QGroupBox(self.tabIslandManagement)
        self.groupBox.setEnabled(False)
        self.groupBox.setVisible(False)
        self.groupBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.setup_required_reason = QtWidgets.QLabel(self.groupBox)
        self.setup_required_reason.setObjectName("setup_required_reason")
        self.horizontalLayout_5.addWidget(self.setup_required_reason)
        self.setup_required_icon = QtWidgets.QLabel(self.groupBox)
        self.setup_required_icon.setMaximumSize(QtCore.QSize(16, 16))
        self.setup_required_icon.setText("")
        self.setup_required_icon.setPixmap(QtGui.QPixmap(":/images/info"))
        self.setup_required_icon.setScaledContents(True)
        self.setup_required_icon.setObjectName("setup_required_icon")
        self.horizontalLayout_5.addWidget(self.setup_required_icon)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.button_launch_setup = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_launch_setup.sizePolicy().hasHeightForWidth())
        self.button_launch_setup.setSizePolicy(sizePolicy)
        self.button_launch_setup.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.button_launch_setup.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/gear"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_launch_setup.setIcon(icon1)
        self.button_launch_setup.setObjectName("button_launch_setup")
        self.verticalLayout.addWidget(self.button_launch_setup)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.launchIslandButton = QtWidgets.QPushButton(self.tabIslandManagement)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.launchIslandButton.sizePolicy().hasHeightForWidth())
        self.launchIslandButton.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/play"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.launchIslandButton.setIcon(icon2)
        self.launchIslandButton.setIconSize(QtCore.QSize(48, 48))
        self.launchIslandButton.setAutoDefault(False)
        self.launchIslandButton.setObjectName("launchIslandButton")
        self.verticalLayout_2.addWidget(self.launchIslandButton)
        self.launchMode = QtWidgets.QComboBox(self.tabIslandManagement)
        self.launchMode.setObjectName("launchMode")
        self.launchMode.addItem("")
        self.launchMode.addItem("")
        self.verticalLayout_2.addWidget(self.launchMode)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.shutdownIslandButton = QtWidgets.QPushButton(self.tabIslandManagement)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shutdownIslandButton.sizePolicy().hasHeightForWidth())
        self.shutdownIslandButton.setSizePolicy(sizePolicy)
        self.shutdownIslandButton.setStyleSheet("padding: 15px")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/stop"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shutdownIslandButton.setIcon(icon3)
        self.shutdownIslandButton.setIconSize(QtCore.QSize(48, 48))
        self.shutdownIslandButton.setObjectName("shutdownIslandButton")
        self.verticalLayout_4.addWidget(self.shutdownIslandButton)
        self.stopMode = QtWidgets.QComboBox(self.tabIslandManagement)
        self.stopMode.setObjectName("stopMode")
        self.stopMode.addItem("")
        self.stopMode.addItem("")
        self.verticalLayout_4.addWidget(self.stopMode)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.restartIslandButton = QtWidgets.QPushButton(self.tabIslandManagement)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restartIslandButton.sizePolicy().hasHeightForWidth())
        self.restartIslandButton.setSizePolicy(sizePolicy)
        self.restartIslandButton.setStyleSheet("padding: 20px;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/reload"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restartIslandButton.setIcon(icon4)
        self.restartIslandButton.setIconSize(QtCore.QSize(48, 48))
        self.restartIslandButton.setObjectName("restartIslandButton")
        self.horizontalLayout_4.addWidget(self.restartIslandButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tabIslandManagement, "")
        self.tabIslandSettings = QtWidgets.QWidget()
        self.tabIslandSettings.setObjectName("tabIslandSettings")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tabIslandSettings)
        self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.vMnameLabel = QtWidgets.QLabel(self.tabIslandSettings)
        self.vMnameLabel.setMinimumSize(QtCore.QSize(125, 0))
        self.vMnameLabel.setObjectName("vMnameLabel")
        self.horizontalLayout_10.addWidget(self.vMnameLabel)
        self.vmnameLineEdit = QtWidgets.QLineEdit(self.tabIslandSettings)
        self.vmnameLineEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.vmnameLineEdit.setObjectName("vmnameLineEdit")
        self.horizontalLayout_10.addWidget(self.vmnameLineEdit)
        self.vmnameSave = QtWidgets.QPushButton(self.tabIslandSettings)
        self.vmnameSave.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/yes"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vmnameSave.setIcon(icon5)
        self.vmnameSave.setObjectName("vmnameSave")
        self.horizontalLayout_10.addWidget(self.vmnameSave)
        self.vmnameDefault = QtWidgets.QPushButton(self.tabIslandSettings)
        self.vmnameDefault.setIcon(icon4)
        self.vmnameDefault.setObjectName("vmnameDefault")
        self.horizontalLayout_10.addWidget(self.vmnameDefault)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.vboxmanagePathLabel = QtWidgets.QLabel(self.tabIslandSettings)
        self.vboxmanagePathLabel.setMinimumSize(QtCore.QSize(125, 0))
        self.vboxmanagePathLabel.setObjectName("vboxmanagePathLabel")
        self.horizontalLayout_11.addWidget(self.vboxmanagePathLabel)
        self.vboxmanagePathLineEdit = QtWidgets.QLineEdit(self.tabIslandSettings)
        self.vboxmanagePathLineEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.vboxmanagePathLineEdit.setObjectName("vboxmanagePathLineEdit")
        self.horizontalLayout_11.addWidget(self.vboxmanagePathLineEdit)
        self.vboxmanageSelectPath = QtWidgets.QPushButton(self.tabIslandSettings)
        self.vboxmanageSelectPath.setObjectName("vboxmanageSelectPath")
        self.horizontalLayout_11.addWidget(self.vboxmanageSelectPath)
        self.vboxmanageSave = QtWidgets.QPushButton(self.tabIslandSettings)
        self.vboxmanageSave.setEnabled(False)
        self.vboxmanageSave.setIcon(icon5)
        self.vboxmanageSave.setObjectName("vboxmanageSave")
        self.horizontalLayout_11.addWidget(self.vboxmanageSave)
        self.vboxmanageDefault = QtWidgets.QPushButton(self.tabIslandSettings)
        self.vboxmanageDefault.setIcon(icon4)
        self.vboxmanageDefault.setObjectName("vboxmanageDefault")
        self.horizontalLayout_11.addWidget(self.vboxmanageDefault)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_2 = QtWidgets.QLabel(self.tabIslandSettings)
        self.label_2.setMinimumSize(QtCore.QSize(125, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_12.addWidget(self.label_2)
        self.dfLineEdit = QtWidgets.QLineEdit(self.tabIslandSettings)
        self.dfLineEdit.setObjectName("dfLineEdit")
        self.horizontalLayout_12.addWidget(self.dfLineEdit)
        self.dfSelectPath = QtWidgets.QPushButton(self.tabIslandSettings)
        self.dfSelectPath.setObjectName("dfSelectPath")
        self.horizontalLayout_12.addWidget(self.dfSelectPath)
        self.dfSave = QtWidgets.QPushButton(self.tabIslandSettings)
        self.dfSave.setEnabled(False)
        self.dfSave.setIcon(icon5)
        self.dfSave.setObjectName("dfSave")
        self.horizontalLayout_12.addWidget(self.dfSave)
        self.dfDefault = QtWidgets.QPushButton(self.tabIslandSettings)
        self.dfDefault.setIcon(icon4)
        self.dfDefault.setObjectName("dfDefault")
        self.horizontalLayout_12.addWidget(self.dfDefault)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem3)
        self.tabWidget.addTab(self.tabIslandSettings, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 774, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuOptions = QtWidgets.QMenu(self.menuBar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setIconVisibleInMenu(True)
        self.actionExit.setObjectName("actionExit")
        self.actionMinimize = QtWidgets.QAction(MainWindow)
        self.actionMinimize.setIconVisibleInMenu(True)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName("actionAbout")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.actionMinimize_2 = QtWidgets.QAction(MainWindow)
        self.actionMinimize_2.setObjectName("actionMinimize_2")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuOptions.addAction(self.actionInfo)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionMinimize_2)
        self.menuOptions.addAction(self.actionClose)
        self.menuBar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Island Manager"))
        self.islandStatusLabel.setText(_translate("MainWindow", "Island status: "))
        self.islandStatus.setText(_translate("MainWindow", "unknown"))
        self.island_access_label.setText(_translate("MainWindow", "Access:"))
        self.setup_required_reason.setText(_translate("MainWindow", "Island VM not found"))
        self.button_launch_setup.setText(_translate("MainWindow", "Run setup"))
        self.launchIslandButton.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Launch island. </p></body></html>"))
        self.launchIslandButton.setText(_translate("MainWindow", "Launch Island"))
        self.launchMode.setItemText(0, _translate("MainWindow", "Quiet"))
        self.launchMode.setItemText(1, _translate("MainWindow", "Normal"))
        self.shutdownIslandButton.setText(_translate("MainWindow", "Shutdown Island"))
        self.stopMode.setItemText(0, _translate("MainWindow", "Soft"))
        self.stopMode.setItemText(1, _translate("MainWindow", "Force"))
        self.restartIslandButton.setText(_translate("MainWindow", "Restart Island"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabIslandManagement), _translate("MainWindow", "Manage"))
        self.vMnameLabel.setText(_translate("MainWindow", "Island VM name:"))
        self.vmnameSave.setText(_translate("MainWindow", "Save"))
        self.vmnameDefault.setText(_translate("MainWindow", "Restore default"))
        self.vboxmanagePathLabel.setText(_translate("MainWindow", "Path to vboxmanage:"))
        self.vboxmanageSelectPath.setText(_translate("MainWindow", "Browse..."))
        self.vboxmanageSave.setText(_translate("MainWindow", "Save"))
        self.vboxmanageDefault.setText(_translate("MainWindow", "Restore default"))
        self.label_2.setText(_translate("MainWindow", "Data folder path:"))
        self.dfSelectPath.setText(_translate("MainWindow", "Browse..."))
        self.dfSave.setText(_translate("MainWindow", "Save"))
        self.dfDefault.setText(_translate("MainWindow", "Restore default"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabIslandSettings), _translate("MainWindow", "Settings"))
        self.menuOptions.setTitle(_translate("MainWindow", "Menu"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionMinimize.setText(_translate("MainWindow", "Minimize"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionMinimize_2.setText(_translate("MainWindow", "Minimize"))
        self.actionClose.setText(_translate("MainWindow", "Close"))

import forms.resources_rc
