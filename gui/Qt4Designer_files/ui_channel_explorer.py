# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_channel_explorer.ui'
#
# Created: Tue Nov  6 21:05:45 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(926, 737)
        Dialog.setModal(True)
        self.gridLayout_3 = QtGui.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter_top_bottom = QtGui.QSplitter(Dialog)
        self.splitter_top_bottom.setOrientation(QtCore.Qt.Vertical)
        self.splitter_top_bottom.setObjectName("splitter_top_bottom")
        self.widget = QtGui.QWidget(self.splitter_top_bottom)
        self.widget.setObjectName("widget")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_filter = QtGui.QLabel(self.widget)
        self.label_filter.setMaximumSize(QtCore.QSize(16777215, 27))
        self.label_filter.setObjectName("label_filter")
        self.horizontalLayout_5.addWidget(self.label_filter)
        self.groupBox_filter_mode = QtGui.QGroupBox(self.widget)
        self.groupBox_filter_mode.setAutoFillBackground(False)
        self.groupBox_filter_mode.setStyleSheet("border: 2px solid black;\n"
"padding: 3px;")
        self.groupBox_filter_mode.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_filter_mode.setFlat(False)
        self.groupBox_filter_mode.setObjectName("groupBox_filter_mode")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_filter_mode)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_simple = QtGui.QRadioButton(self.groupBox_filter_mode)
        self.radioButton_simple.setStyleSheet("border: transparent;")
        self.radioButton_simple.setChecked(True)
        self.radioButton_simple.setObjectName("radioButton_simple")
        self.horizontalLayout.addWidget(self.radioButton_simple)
        self.radioButton_advanced = QtGui.QRadioButton(self.groupBox_filter_mode)
        self.radioButton_advanced.setStyleSheet("border: transparent;")
        self.radioButton_advanced.setObjectName("radioButton_advanced")
        self.horizontalLayout.addWidget(self.radioButton_advanced)
        self.horizontalLayout_5.addWidget(self.groupBox_filter_mode)
        self.checkBox_filter_case_sensitive = QtGui.QCheckBox(self.widget)
        self.checkBox_filter_case_sensitive.setMaximumSize(QtCore.QSize(16777215, 21))
        self.checkBox_filter_case_sensitive.setObjectName("checkBox_filter_case_sensitive")
        self.horizontalLayout_5.addWidget(self.checkBox_filter_case_sensitive)
        self.groupBox_elements_or_channels = QtGui.QGroupBox(self.widget)
        self.groupBox_elements_or_channels.setAutoFillBackground(False)
        self.groupBox_elements_or_channels.setStyleSheet("   border: 2px solid black;\n"
"   padding: 3px;\n"
"")
        self.groupBox_elements_or_channels.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.groupBox_elements_or_channels.setObjectName("groupBox_elements_or_channels")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_elements_or_channels)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_elements = QtGui.QRadioButton(self.groupBox_elements_or_channels)
        self.radioButton_elements.setStyleSheet("border: transparent;")
        self.radioButton_elements.setChecked(True)
        self.radioButton_elements.setObjectName("radioButton_elements")
        self.gridLayout.addWidget(self.radioButton_elements, 0, 0, 1, 1)
        self.radioButton_channels = QtGui.QRadioButton(self.groupBox_elements_or_channels)
        self.radioButton_channels.setStyleSheet("border: transparent;")
        self.radioButton_channels.setObjectName("radioButton_channels")
        self.gridLayout.addWidget(self.radioButton_channels, 0, 1, 1, 1)
        self.horizontalLayout_5.addWidget(self.groupBox_elements_or_channels)
        self.label_lattice = QtGui.QLabel(self.widget)
        self.label_lattice.setMaximumSize(QtCore.QSize(16777215, 27))
        self.label_lattice.setObjectName("label_lattice")
        self.horizontalLayout_5.addWidget(self.label_lattice)
        self.comboBox_lattice = QtGui.QComboBox(self.widget)
        self.comboBox_lattice.setObjectName("comboBox_lattice")
        self.horizontalLayout_5.addWidget(self.comboBox_lattice)
        spacerItem = QtGui.QSpacerItem(16777215, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pushButton_search = QtGui.QPushButton(self.widget)
        self.pushButton_search.setMaximumSize(QtCore.QSize(16777215, 27))
        self.pushButton_search.setObjectName("pushButton_search")
        self.horizontalLayout_5.addWidget(self.pushButton_search)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.stackedWidget = QtGui.QStackedWidget(self.widget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_advanced = QtGui.QWidget()
        self.page_advanced.setObjectName("page_advanced")
        self.verticalLayout = QtGui.QVBoxLayout(self.page_advanced)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_add_row = QtGui.QPushButton(self.page_advanced)
        self.pushButton_add_row.setMaximumSize(QtCore.QSize(16777215, 27))
        self.pushButton_add_row.setObjectName("pushButton_add_row")
        self.horizontalLayout_2.addWidget(self.pushButton_add_row)
        self.pushButton_remove_row = QtGui.QPushButton(self.page_advanced)
        self.pushButton_remove_row.setMaximumSize(QtCore.QSize(16777215, 27))
        self.pushButton_remove_row.setObjectName("pushButton_remove_row")
        self.horizontalLayout_2.addWidget(self.pushButton_remove_row)
        spacerItem1 = QtGui.QSpacerItem(16777215, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget_filter = QtGui.QTableWidget(self.page_advanced)
        self.tableWidget_filter.setObjectName("tableWidget_filter")
        self.tableWidget_filter.setColumnCount(11)
        self.tableWidget_filter.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_filter.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_filter.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_filter.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_filter.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_filter.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_filter.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_filter.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_filter.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_filter.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_filter.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_filter.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_filter.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_filter.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_filter.setItem(0, 1, item)
        self.tableWidget_filter.horizontalHeader().setMinimumSectionSize(16)
        self.tableWidget_filter.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget_filter)
        self.stackedWidget.addWidget(self.page_advanced)
        self.page_simple = QtGui.QWidget()
        self.page_simple.setObjectName("page_simple")
        self.gridLayout_2 = QtGui.QGridLayout(self.page_simple)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtGui.QLabel(self.page_simple)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 27))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.checkBox_simple_NOT = QtGui.QCheckBox(self.page_simple)
        self.checkBox_simple_NOT.setText("")
        self.checkBox_simple_NOT.setObjectName("checkBox_simple_NOT")
        self.verticalLayout_8.addWidget(self.checkBox_simple_NOT)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtGui.QLabel(self.page_simple)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 27))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.comboBox_simple_property = QtGui.QComboBox(self.page_simple)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_simple_property.sizePolicy().hasHeightForWidth())
        self.comboBox_simple_property.setSizePolicy(sizePolicy)
        self.comboBox_simple_property.setObjectName("comboBox_simple_property")
        self.verticalLayout_4.addWidget(self.comboBox_simple_property)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtGui.QLabel(self.page_simple)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 27))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.comboBox_simple_operator = QtGui.QComboBox(self.page_simple)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_simple_operator.sizePolicy().hasHeightForWidth())
        self.comboBox_simple_operator.setSizePolicy(sizePolicy)
        self.comboBox_simple_operator.setObjectName("comboBox_simple_operator")
        self.verticalLayout_5.addWidget(self.comboBox_simple_operator)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtGui.QLabel(self.page_simple)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 27))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.comboBox_simple_index = QtGui.QComboBox(self.page_simple)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_simple_index.sizePolicy().hasHeightForWidth())
        self.comboBox_simple_index.setSizePolicy(sizePolicy)
        self.comboBox_simple_index.setObjectName("comboBox_simple_index")
        self.verticalLayout_6.addWidget(self.comboBox_simple_index)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtGui.QLabel(self.page_simple)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 27))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.comboBox_simple_value = QtGui.QComboBox(self.page_simple)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_simple_value.sizePolicy().hasHeightForWidth())
        self.comboBox_simple_value.setSizePolicy(sizePolicy)
        self.comboBox_simple_value.setEditable(True)
        self.comboBox_simple_value.setObjectName("comboBox_simple_value")
        self.verticalLayout_7.addWidget(self.comboBox_simple_value)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        spacerItem2 = QtGui.QSpacerItem(16777215, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.verticalLayout_10, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_simple)
        self.verticalLayout_9.addWidget(self.stackedWidget)
        self.splitter_left_right = QtGui.QSplitter(self.splitter_top_bottom)
        self.splitter_left_right.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_left_right.setObjectName("splitter_left_right")
        self.layoutWidget = QtGui.QWidget(self.splitter_left_right)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_nMatched_nSelected = QtGui.QLabel(self.layoutWidget)
        self.label_nMatched_nSelected.setMaximumSize(QtCore.QSize(16777215, 16))
        self.label_nMatched_nSelected.setObjectName("label_nMatched_nSelected")
        self.verticalLayout_3.addWidget(self.label_nMatched_nSelected)
        self.tableWidget_matched = QtGui.QTableWidget(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_matched.sizePolicy().hasHeightForWidth())
        self.tableWidget_matched.setSizePolicy(sizePolicy)
        self.tableWidget_matched.setObjectName("tableWidget_matched")
        self.tableWidget_matched.setColumnCount(15)
        self.tableWidget_matched.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_matched.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_matched.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_matched.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_matched.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_matched.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_matched.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_matched.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_matched.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_matched.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_matched.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_matched.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_matched.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_matched.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_matched.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_matched.setHorizontalHeaderItem(14, item)
        self.verticalLayout_3.addWidget(self.tableWidget_matched)
        self.layoutWidget1 = QtGui.QWidget(self.splitter_left_right)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label__choice_list = QtGui.QLabel(self.layoutWidget1)
        self.label__choice_list.setMaximumSize(QtCore.QSize(16777215, 16))
        self.label__choice_list.setObjectName("label__choice_list")
        self.horizontalLayout_3.addWidget(self.label__choice_list)
        self.comboBox_choice_list = QtGui.QComboBox(self.layoutWidget1)
        self.comboBox_choice_list.setObjectName("comboBox_choice_list")
        self.horizontalLayout_3.addWidget(self.comboBox_choice_list)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.listView_choice_list = QtGui.QListView(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView_choice_list.sizePolicy().hasHeightForWidth())
        self.listView_choice_list.setSizePolicy(sizePolicy)
        self.listView_choice_list.setObjectName("listView_choice_list")
        self.verticalLayout_2.addWidget(self.listView_choice_list)
        self.gridLayout_3.addWidget(self.splitter_top_bottom, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Channel/Element Explorer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_filter.setText(QtGui.QApplication.translate("Dialog", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_filter_mode.setTitle(QtGui.QApplication.translate("Dialog", "Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_simple.setText(QtGui.QApplication.translate("Dialog", "Simple", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_advanced.setText(QtGui.QApplication.translate("Dialog", "Advanced", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_filter_case_sensitive.setText(QtGui.QApplication.translate("Dialog", "Case-sensitive", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_elements_or_channels.setTitle(QtGui.QApplication.translate("Dialog", "Object Type", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_elements.setText(QtGui.QApplication.translate("Dialog", "Elements", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_channels.setText(QtGui.QApplication.translate("Dialog", "Channels", None, QtGui.QApplication.UnicodeUTF8))
        self.label_lattice.setText(QtGui.QApplication.translate("Dialog", "Lattice", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_search.setText(QtGui.QApplication.translate("Dialog", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_add_row.setText(QtGui.QApplication.translate("Dialog", "Add Row", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_remove_row.setText(QtGui.QApplication.translate("Dialog", "Remove Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_filter.verticalHeaderItem(0).setText(QtGui.QApplication.translate("Dialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_filter.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Dialog", "Filter Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_filter.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Dialog", "Filter Set 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_filter.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("Dialog", "AND/OR", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_filter.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("Dialog", "Filter Set 2", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_filter.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("Dialog", "NOT", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_filter.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("Dialog", "Property", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_filter.horizontalHeaderItem(7).setText(QtGui.QApplication.translate("Dialog", "Operator", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_filter.horizontalHeaderItem(8).setText(QtGui.QApplication.translate("Dialog", "Index", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_filter.horizontalHeaderItem(9).setText(QtGui.QApplication.translate("Dialog", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_filter.horizontalHeaderItem(10).setText(QtGui.QApplication.translate("Dialog", "Expression", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.tableWidget_filter.isSortingEnabled()
        self.tableWidget_filter.setSortingEnabled(False)
        self.tableWidget_filter.setSortingEnabled(__sortingEnabled)
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "NOT", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Property", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Operator", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Index", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_nMatched_nSelected.setText(QtGui.QApplication.translate("Dialog", "Matched Objects (0 matched, 0 selected)", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_matched.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Dialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_matched.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Dialog", "Dev. Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_matched.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Dialog", "Cell", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_matched.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("Dialog", "Family", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_matched.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("Dialog", "Girder", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_matched.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("Dialog", "Group", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_matched.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("Dialog", "Lat. Index", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_matched.horizontalHeaderItem(7).setText(QtGui.QApplication.translate("Dialog", "Eff. Len.", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_matched.horizontalHeaderItem(8).setText(QtGui.QApplication.translate("Dialog", "Phys. Len.", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_matched.horizontalHeaderItem(9).setText(QtGui.QApplication.translate("Dialog", "PV", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_matched.horizontalHeaderItem(10).setText(QtGui.QApplication.translate("Dialog", "sb", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_matched.horizontalHeaderItem(11).setText(QtGui.QApplication.translate("Dialog", "se", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_matched.horizontalHeaderItem(12).setText(QtGui.QApplication.translate("Dialog", "Symmetry", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_matched.horizontalHeaderItem(13).setText(QtGui.QApplication.translate("Dialog", "Virtual", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_matched.horizontalHeaderItem(14).setText(QtGui.QApplication.translate("Dialog", "Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.label__choice_list.setText(QtGui.QApplication.translate("Dialog", "Choice List", None, QtGui.QApplication.UnicodeUTF8))

