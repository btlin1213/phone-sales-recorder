# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 654)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWindow = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWindow.setGeometry(QtCore.QRect(10, 10, 771, 601))
        self.tabWindow.setObjectName("tabWindow")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 310, 731, 241))
        self.groupBox_5.setObjectName("groupBox_5")
        self.phoneOut_assignPhoneToCustomer_pushButton = QtWidgets.QPushButton(self.groupBox_5)
        self.phoneOut_assignPhoneToCustomer_pushButton.setGeometry(QtCore.QRect(240, 140, 141, 31))
        self.phoneOut_assignPhoneToCustomer_pushButton.setObjectName("phoneOut_assignPhoneToCustomer_pushButton")
        self.phoneOut_addCustomer_pushButton = QtWidgets.QPushButton(self.groupBox_5)
        self.phoneOut_addCustomer_pushButton.setGeometry(QtCore.QRect(400, 20, 111, 23))
        self.phoneOut_addCustomer_pushButton.setObjectName("phoneOut_addCustomer_pushButton")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setGeometry(QtCore.QRect(30, 20, 61, 16))
        self.label.setObjectName("label")
        self.phoneOut_displayCustomer_tableWidget = QtWidgets.QTableWidget(self.groupBox_5)
        self.phoneOut_displayCustomer_tableWidget.setGeometry(QtCore.QRect(90, 60, 291, 71))
        self.phoneOut_displayCustomer_tableWidget.setObjectName("phoneOut_displayCustomer_tableWidget")
        self.phoneOut_displayCustomer_tableWidget.setColumnCount(2)
        self.phoneOut_displayCustomer_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.phoneOut_displayCustomer_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.phoneOut_displayCustomer_tableWidget.setHorizontalHeaderItem(1, item)
        self.phoneOut_findCustomer_comboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.phoneOut_findCustomer_comboBox.setGeometry(QtCore.QRect(90, 20, 291, 22))
        self.phoneOut_findCustomer_comboBox.setEditable(True)
        self.phoneOut_findCustomer_comboBox.setObjectName("phoneOut_findCustomer_comboBox")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 20, 731, 281))
        self.groupBox_6.setObjectName("groupBox_6")
        self.phoneOut_findIMEI_lineEdit = QtWidgets.QLineEdit(self.groupBox_6)
        self.phoneOut_findIMEI_lineEdit.setGeometry(QtCore.QRect(30, 40, 351, 20))
        self.phoneOut_findIMEI_lineEdit.setObjectName("phoneOut_findIMEI_lineEdit")
        self.phoneOut_checkBox_includeSold = QtWidgets.QCheckBox(self.groupBox_6)
        self.phoneOut_checkBox_includeSold.setGeometry(QtCore.QRect(30, 60, 191, 21))
        self.phoneOut_checkBox_includeSold.setObjectName("phoneOut_checkBox_includeSold")
        self.phoneOut_findIMEI_tableWidget = QtWidgets.QTableWidget(self.groupBox_6)
        self.phoneOut_findIMEI_tableWidget.setGeometry(QtCore.QRect(30, 111, 671, 151))
        self.phoneOut_findIMEI_tableWidget.setObjectName("phoneOut_findIMEI_tableWidget")
        self.phoneOut_findIMEI_tableWidget.setColumnCount(3)
        self.phoneOut_findIMEI_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.phoneOut_findIMEI_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.phoneOut_findIMEI_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.phoneOut_findIMEI_tableWidget.setHorizontalHeaderItem(2, item)
        self.label_2 = QtWidgets.QLabel(self.groupBox_6)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 47, 13))
        self.label_2.setObjectName("label_2")
        self.phoneOut_findIMEI_pushButton = QtWidgets.QPushButton(self.groupBox_6)
        self.phoneOut_findIMEI_pushButton.setGeometry(QtCore.QRect(390, 40, 81, 23))
        self.phoneOut_findIMEI_pushButton.setObjectName("phoneOut_findIMEI_pushButton")
        self.label_10 = QtWidgets.QLabel(self.groupBox_6)
        self.label_10.setGeometry(QtCore.QRect(30, 90, 161, 16))
        self.label_10.setObjectName("label_10")
        self.tabWindow.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 721, 171))
        self.groupBox.setObjectName("groupBox")
        self.addPhone_model_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.addPhone_model_comboBox.setGeometry(QtCore.QRect(30, 40, 191, 22))
        self.addPhone_model_comboBox.setEditable(True)
        self.addPhone_model_comboBox.setObjectName("addPhone_model_comboBox")
        self.addPhone_grade_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.addPhone_grade_comboBox.setGeometry(QtCore.QRect(340, 40, 81, 22))
        self.addPhone_grade_comboBox.setEditable(True)
        self.addPhone_grade_comboBox.setObjectName("addPhone_grade_comboBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(240, 20, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(440, 20, 47, 13))
        self.label_6.setObjectName("label_6")
        self.addPhone_color_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.addPhone_color_comboBox.setGeometry(QtCore.QRect(440, 40, 111, 22))
        self.addPhone_color_comboBox.setEditable(True)
        self.addPhone_color_comboBox.setObjectName("addPhone_color_comboBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(340, 20, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(570, 20, 121, 16))
        self.label_7.setObjectName("label_7")
        self.addPhone_storage_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.addPhone_storage_comboBox.setGeometry(QtCore.QRect(240, 40, 81, 22))
        self.addPhone_storage_comboBox.setEditable(True)
        self.addPhone_storage_comboBox.setObjectName("addPhone_storage_comboBox")
        self.addPhone_imei_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.addPhone_imei_lineEdit.setGeometry(QtCore.QRect(30, 90, 391, 20))
        self.addPhone_imei_lineEdit.setObjectName("addPhone_imei_lineEdit")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(30, 70, 47, 13))
        self.label_8.setObjectName("label_8")
        self.addPhone_productID_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.addPhone_productID_lineEdit.setGeometry(QtCore.QRect(570, 40, 121, 20))
        self.addPhone_productID_lineEdit.setObjectName("addPhone_productID_lineEdit")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(30, 120, 61, 16))
        self.label_9.setObjectName("label_9")
        self.addPhone_displayFullName_label = QtWidgets.QLabel(self.groupBox)
        self.addPhone_displayFullName_label.setGeometry(QtCore.QRect(110, 120, 361, 16))
        self.addPhone_displayFullName_label.setText("")
        self.addPhone_displayFullName_label.setObjectName("addPhone_displayFullName_label")
        self.addPhone_displayIMEI_label = QtWidgets.QLabel(self.groupBox)
        self.addPhone_displayIMEI_label.setGeometry(QtCore.QRect(110, 140, 47, 13))
        self.addPhone_displayIMEI_label.setText("")
        self.addPhone_displayIMEI_label.setObjectName("addPhone_displayIMEI_label")
        self.addPhone_addPhone_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.addPhone_addPhone_pushButton.setGeometry(QtCore.QRect(440, 90, 101, 23))
        self.addPhone_addPhone_pushButton.setObjectName("addPhone_addPhone_pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 200, 721, 351))
        self.groupBox_2.setObjectName("groupBox_2")
        self.addPhone_tableWidget_displayAddedPhones = QtWidgets.QTableWidget(self.groupBox_2)
        self.addPhone_tableWidget_displayAddedPhones.setGeometry(QtCore.QRect(10, 20, 701, 281))
        self.addPhone_tableWidget_displayAddedPhones.setObjectName("addPhone_tableWidget_displayAddedPhones")
        self.addPhone_tableWidget_displayAddedPhones.setColumnCount(4)
        self.addPhone_tableWidget_displayAddedPhones.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.addPhone_tableWidget_displayAddedPhones.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.addPhone_tableWidget_displayAddedPhones.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.addPhone_tableWidget_displayAddedPhones.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.addPhone_tableWidget_displayAddedPhones.setHorizontalHeaderItem(3, item)
        self.addPhone_pushButton_confirmChange = QtWidgets.QPushButton(self.groupBox_2)
        self.addPhone_pushButton_confirmChange.setGeometry(QtCore.QRect(250, 310, 171, 31))
        self.addPhone_pushButton_confirmChange.setObjectName("addPhone_pushButton_confirmChange")
        self.tabWindow.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.summaryPage_groupBox_addToWebsite = QtWidgets.QGroupBox(self.tab_4)
        self.summaryPage_groupBox_addToWebsite.setGeometry(QtCore.QRect(20, 20, 731, 531))
        self.summaryPage_groupBox_addToWebsite.setObjectName("summaryPage_groupBox_addToWebsite")
        self.addPhone_newQty_tableWidget = QtWidgets.QTableWidget(self.summaryPage_groupBox_addToWebsite)
        self.addPhone_newQty_tableWidget.setGeometry(QtCore.QRect(10, 30, 711, 461))
        self.addPhone_newQty_tableWidget.setObjectName("addPhone_newQty_tableWidget")
        self.addPhone_newQty_tableWidget.setColumnCount(5)
        self.addPhone_newQty_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.addPhone_newQty_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.addPhone_newQty_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.addPhone_newQty_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.addPhone_newQty_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.addPhone_newQty_tableWidget.setHorizontalHeaderItem(4, item)
        self.tabWindow.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 20, 321, 321))
        self.groupBox_3.setObjectName("groupBox_3")
        self.addCustomer_addCompany_lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.addCustomer_addCompany_lineEdit.setGeometry(QtCore.QRect(110, 39, 181, 31))
        self.addCustomer_addCompany_lineEdit.setObjectName("addCustomer_addCompany_lineEdit")
        self.addCustomer_addName_lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.addCustomer_addName_lineEdit.setGeometry(QtCore.QRect(110, 89, 181, 31))
        self.addCustomer_addName_lineEdit.setObjectName("addCustomer_addName_lineEdit")
        self.addCustomer_addPhone_lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.addCustomer_addPhone_lineEdit.setGeometry(QtCore.QRect(110, 139, 181, 31))
        self.addCustomer_addPhone_lineEdit.setObjectName("addCustomer_addPhone_lineEdit")
        self.addCustomer_addEmail_lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.addCustomer_addEmail_lineEdit.setGeometry(QtCore.QRect(110, 189, 181, 31))
        self.addCustomer_addEmail_lineEdit.setObjectName("addCustomer_addEmail_lineEdit")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(30, 50, 47, 13))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(30, 100, 47, 13))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(30, 150, 47, 13))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(30, 200, 47, 13))
        self.label_15.setObjectName("label_15")
        self.addCustomer_addCustomer_pushCustomer = QtWidgets.QPushButton(self.groupBox_3)
        self.addCustomer_addCustomer_pushCustomer.setGeometry(QtCore.QRect(100, 240, 91, 23))
        self.addCustomer_addCustomer_pushCustomer.setObjectName("addCustomer_addCustomer_pushCustomer")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_4.setGeometry(QtCore.QRect(380, 20, 351, 321))
        self.groupBox_4.setObjectName("groupBox_4")
        self.addCustomer_editCompany_lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.addCustomer_editCompany_lineEdit.setGeometry(QtCore.QRect(120, 39, 191, 31))
        self.addCustomer_editCompany_lineEdit.setObjectName("addCustomer_editCompany_lineEdit")
        self.addCustomer_editName_lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.addCustomer_editName_lineEdit.setGeometry(QtCore.QRect(120, 89, 191, 31))
        self.addCustomer_editName_lineEdit.setObjectName("addCustomer_editName_lineEdit")
        self.addCustomer_editPhone_lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.addCustomer_editPhone_lineEdit.setGeometry(QtCore.QRect(120, 139, 191, 31))
        self.addCustomer_editPhone_lineEdit.setObjectName("addCustomer_editPhone_lineEdit")
        self.addCustomer_editEmail_lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.addCustomer_editEmail_lineEdit.setGeometry(QtCore.QRect(120, 189, 191, 31))
        self.addCustomer_editEmail_lineEdit.setObjectName("addCustomer_editEmail_lineEdit")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(40, 50, 47, 13))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(40, 100, 47, 13))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setGeometry(QtCore.QRect(40, 150, 47, 13))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setGeometry(QtCore.QRect(40, 200, 47, 13))
        self.label_19.setObjectName("label_19")
        self.addCustomer_editSearch_pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.addCustomer_editSearch_pushButton.setGeometry(QtCore.QRect(120, 240, 81, 23))
        self.addCustomer_editSearch_pushButton.setObjectName("addCustomer_editSearch_pushButton")
        self.addCustomer_editConfirm_pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.addCustomer_editConfirm_pushButton.setGeometry(QtCore.QRect(230, 240, 81, 23))
        self.addCustomer_editConfirm_pushButton.setObjectName("addCustomer_editConfirm_pushButton")
        self.tabWindow.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuReport = QtWidgets.QMenu(self.menubar)
        self.menuReport.setObjectName("menuReport")
        self.menusdfs = QtWidgets.QMenu(self.menubar)
        self.menusdfs.setObjectName("menusdfs")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_import_action = QtWidgets.QAction(MainWindow)
        self.menu_import_action.setObjectName("menu_import_action")
        self.menu_export_action = QtWidgets.QAction(MainWindow)
        self.menu_export_action.setObjectName("menu_export_action")
        self.menu_customerHistory_action = QtWidgets.QAction(MainWindow)
        self.menu_customerHistory_action.setObjectName("menu_customerHistory_action")
        self.menu_stockTake_action = QtWidgets.QAction(MainWindow)
        self.menu_stockTake_action.setObjectName("menu_stockTake_action")
        self.menu_helpYourself_action = QtWidgets.QAction(MainWindow)
        self.menu_helpYourself_action.setObjectName("menu_helpYourself_action")
        self.menuFile.addAction(self.menu_import_action)
        self.menuFile.addAction(self.menu_export_action)
        self.menuReport.addAction(self.menu_customerHistory_action)
        self.menuReport.addSeparator()
        self.menuReport.addAction(self.menu_stockTake_action)
        self.menusdfs.addAction(self.menu_helpYourself_action)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuReport.menuAction())
        self.menubar.addAction(self.menusdfs.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWindow.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Assign To"))
        self.phoneOut_assignPhoneToCustomer_pushButton.setText(_translate("MainWindow", "Assign To Customer"))
        self.phoneOut_addCustomer_pushButton.setText(_translate("MainWindow", "Add New Customer"))
        self.label.setText(_translate("MainWindow", "Customer:"))
        item = self.phoneOut_displayCustomer_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Company"))
        item = self.phoneOut_displayCustomer_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Contact"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Select Phone"))
        self.phoneOut_checkBox_includeSold.setText(_translate("MainWindow", "Include Sold Devices"))
        item = self.phoneOut_findIMEI_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "IMEI"))
        item = self.phoneOut_findIMEI_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product"))
        self.label_2.setText(_translate("MainWindow", "IMEI:"))
        self.phoneOut_findIMEI_pushButton.setText(_translate("MainWindow", "Find"))
        self.label_10.setText(_translate("MainWindow", "Select Device:"))
        self.tabWindow.setTabText(self.tabWindow.indexOf(self.tab_2), _translate("MainWindow", "Phone Out"))
        self.groupBox.setTitle(_translate("MainWindow", "Add Device"))
        self.label_3.setText(_translate("MainWindow", "Model"))
        self.label_4.setText(_translate("MainWindow", "Storage"))
        self.label_6.setText(_translate("MainWindow", "Color"))
        self.label_5.setText(_translate("MainWindow", "Grade"))
        self.label_7.setText(_translate("MainWindow", "Product ID(optional)"))
        self.label_8.setText(_translate("MainWindow", "IMEI"))
        self.label_9.setText(_translate("MainWindow", "Last Added:"))
        self.addPhone_addPhone_pushButton.setText(_translate("MainWindow", "Add"))
        self.groupBox_2.setTitle(_translate("MainWindow", "New Phone"))
        item = self.addPhone_tableWidget_displayAddedPhones.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product ID"))
        item = self.addPhone_tableWidget_displayAddedPhones.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.addPhone_tableWidget_displayAddedPhones.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "IMEI"))
        item = self.addPhone_tableWidget_displayAddedPhones.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Delete"))
        self.addPhone_pushButton_confirmChange.setText(_translate("MainWindow", "Confirm"))
        self.tabWindow.setTabText(self.tabWindow.indexOf(self.tab), _translate("MainWindow", "Add Phone"))
        self.summaryPage_groupBox_addToWebsite.setTitle(_translate("MainWindow", "Add to website"))
        item = self.addPhone_newQty_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.addPhone_newQty_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product"))
        item = self.addPhone_newQty_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Just added"))
        item = self.addPhone_newQty_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total Qty"))
        item = self.addPhone_newQty_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Update Website"))
        self.tabWindow.setTabText(self.tabWindow.indexOf(self.tab_4), _translate("MainWindow", "Summary Page"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Add Customer"))
        self.label_12.setText(_translate("MainWindow", "Company"))
        self.label_13.setText(_translate("MainWindow", "Name"))
        self.label_14.setText(_translate("MainWindow", "Phone"))
        self.label_15.setText(_translate("MainWindow", "Email"))
        self.addCustomer_addCustomer_pushCustomer.setText(_translate("MainWindow", "Add Customer"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Edit Customer"))
        self.label_16.setText(_translate("MainWindow", "Company"))
        self.label_17.setText(_translate("MainWindow", "Name"))
        self.label_18.setText(_translate("MainWindow", "Phone"))
        self.label_19.setText(_translate("MainWindow", "Email"))
        self.addCustomer_editSearch_pushButton.setText(_translate("MainWindow", "Search"))
        self.addCustomer_editConfirm_pushButton.setText(_translate("MainWindow", "Confirm"))
        self.tabWindow.setTabText(self.tabWindow.indexOf(self.tab_3), _translate("MainWindow", "Add Customer"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuReport.setTitle(_translate("MainWindow", "Report"))
        self.menusdfs.setTitle(_translate("MainWindow", "Help"))
        self.menu_import_action.setText(_translate("MainWindow", "Import CSV"))
        self.menu_export_action.setText(_translate("MainWindow", "Export CSV"))
        self.menu_customerHistory_action.setText(_translate("MainWindow", "Customer Purchase History"))
        self.menu_stockTake_action.setText(_translate("MainWindow", "Stock Take Report"))
        self.menu_helpYourself_action.setText(_translate("MainWindow", "Yourself"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

