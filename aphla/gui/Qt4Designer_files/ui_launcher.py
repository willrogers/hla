# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_launcher.ui'
#
# Created: Tue Mar 25 11:27:46 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_5 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.layoutWidget = QtGui.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.stackedWidget_path = QtGui.QStackedWidget(self.layoutWidget)
        self.stackedWidget_path.setMaximumSize(QtCore.QSize(16777215, 49))
        self.stackedWidget_path.setObjectName(_fromUtf8("stackedWidget_path"))
        self.page_path_lineEdit = QtGui.QWidget()
        self.page_path_lineEdit.setObjectName(_fromUtf8("page_path_lineEdit"))
        self.gridLayout_3 = QtGui.QGridLayout(self.page_path_lineEdit)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lineEdit_path = QtGui.QLineEdit(self.page_path_lineEdit)
        self.lineEdit_path.setObjectName(_fromUtf8("lineEdit_path"))
        self.gridLayout_3.addWidget(self.lineEdit_path, 0, 0, 1, 1)
        self.stackedWidget_path.addWidget(self.page_path_lineEdit)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.page_4)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.pushButton_path_button_list_back = QtGui.QPushButton(self.page_4)
        self.pushButton_path_button_list_back.setObjectName(_fromUtf8("pushButton_path_button_list_back"))
        self.gridLayout_4.addWidget(self.pushButton_path_button_list_back, 0, 0, 1, 1)
        self.pushButton_path_button_list_1 = QtGui.QPushButton(self.page_4)
        self.pushButton_path_button_list_1.setObjectName(_fromUtf8("pushButton_path_button_list_1"))
        self.gridLayout_4.addWidget(self.pushButton_path_button_list_1, 0, 1, 1, 1)
        self.pushButton_path_button_list_forward = QtGui.QPushButton(self.page_4)
        self.pushButton_path_button_list_forward.setObjectName(_fromUtf8("pushButton_path_button_list_forward"))
        self.gridLayout_4.addWidget(self.pushButton_path_button_list_forward, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 3, 1, 1)
        self.stackedWidget_path.addWidget(self.page_4)
        self.horizontalLayout.addWidget(self.stackedWidget_path)
        self.lineEdit_search = QtGui.QLineEdit(self.splitter_2)
        self.lineEdit_search.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_search.setText(_fromUtf8(""))
        self.lineEdit_search.setObjectName(_fromUtf8("lineEdit_search"))
        self.verticalLayout.addWidget(self.splitter_2)
        self.splitterPanes = QtGui.QSplitter(self.centralwidget)
        self.splitterPanes.setOrientation(QtCore.Qt.Horizontal)
        self.splitterPanes.setObjectName(_fromUtf8("splitterPanes"))
        self.stackedWidgetMainPane = QtGui.QStackedWidget(self.splitterPanes)
        self.stackedWidgetMainPane.setObjectName(_fromUtf8("stackedWidgetMainPane"))
        self.pageListView = QtGui.QWidget()
        self.pageListView.setObjectName(_fromUtf8("pageListView"))
        self.gridLayout = QtGui.QGridLayout(self.pageListView)
        self.gridLayout.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.stackedWidgetMainPane.addWidget(self.pageListView)
        self.pageTreeView = QtGui.QWidget()
        self.pageTreeView.setObjectName(_fromUtf8("pageTreeView"))
        self.gridLayout_2 = QtGui.QGridLayout(self.pageTreeView)
        self.gridLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.stackedWidgetMainPane.addWidget(self.pageTreeView)
        self.verticalLayout.addWidget(self.splitterPanes)
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuGo = QtGui.QMenu(self.menubar)
        self.menuGo.setObjectName(_fromUtf8("menuGo"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuView.addSeparator()
        self.menuView.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuGo.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget_path.setCurrentIndex(0)
        self.stackedWidgetMainPane.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "APHLA Launcher", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Path:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_path_button_list_back.setText(QtGui.QApplication.translate("MainWindow", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_path_button_list_1.setText(QtGui.QApplication.translate("MainWindow", "Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_path_button_list_forward.setText(QtGui.QApplication.translate("MainWindow", "Forward", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_search.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Quick search", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuGo.setTitle(QtGui.QApplication.translate("MainWindow", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))

