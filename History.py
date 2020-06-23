# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'History.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MenuHistori(object):
    
    def setupUi(self, MenuHistori):
        MenuHistori.setObjectName("MenuHistori")
        MenuHistori.resize(498, 341)
        MenuHistori.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(209, 147, 57, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MenuHistori)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 40, 51, 21))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("001-search.png"))
        self.label.setObjectName("label")
        self.txtsearchmusic = QtWidgets.QLineEdit(self.centralwidget)
        self.txtsearchmusic.setGeometry(QtCore.QRect(130, 40, 291, 21))
        self.txtsearchmusic.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtsearchmusic.setText("")
        self.txtsearchmusic.setFrame(True)
        self.txtsearchmusic.setDragEnabled(False)
        self.txtsearchmusic.setReadOnly(False)
        self.txtsearchmusic.setPlaceholderText("")
        self.txtsearchmusic.setObjectName("txtsearchmusic")
        self.btnremove = QtWidgets.QPushButton(self.centralwidget)
        self.btnremove.setGeometry(QtCore.QRect(60, 40, 71, 21))
        self.btnremove.setObjectName("btnremove")
        self.btnplayhistory = QtWidgets.QPushButton(self.centralwidget)
        self.btnplayhistory.setGeometry(QtCore.QRect(0, 40, 61, 21))
        self.btnplayhistory.setObjectName("btnplayhistory")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 60, 501, 261))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(158)
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(0, 0, 41, 23))
        self.btnBack.setObjectName("btnBack")
        MenuHistori.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MenuHistori)
        self.statusbar.setObjectName("statusbar")
        MenuHistori.setStatusBar(self.statusbar)
        self.retranslateUi(MenuHistori)
        QtCore.QMetaObject.connectSlotsByName(MenuHistori)
    def retranslateUi(self, MenuHistori):
        _translate = QtCore.QCoreApplication.translate
        MenuHistori.setWindowTitle(_translate("MenuHistori", "History"))
        self.btnremove.setText(_translate("MenuHistori", "Remove"))
        self.btnplayhistory.setText(_translate("MenuHistori", "Play"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MenuHistori", "Music Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MenuHistori", "Duration"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MenuHistori", "Playback Date"))
        self.btnBack.setText(_translate("MenuHistori", "Back"))
    
    


    def showdataintable(self,data):
        for rows in range(0,len(data)): 
            self.tableWidget.setRowCount(rows + 1)
            for column in range(0,3):
                self.tableWidget.setItem(rows,column,QtWidgets.QTableWidgetItem(data[rows][column]))
            
    
    
    def showrecentmusics(self):
        sc=sqlite3.connect(r"D:\MyWork\python\projects\music player\musicplayer.db")
        cursor=sc.cursor()
        query="""select * from History"""
        cursor.execute(query)
        sc.commit()
        data=cursor.fetchall()
        cursor.close()
        sc.close()
        if len(data) !=0:
            self.showdataintable(data)
        

    def searchmusic(self):
        if self.txtsearchmusic.text()=="":
            self.showrecentmusics()
        else:
            sc=sqlite3.connect(r"D:\MyWork\python\projects\music player\musicplayer.db")
            cursor=sc.cursor()
            query="""select * from History where MusicName Like ?"""
            data_tuple=("%"+self.txtsearchmusic.text()+"%",)
            cursor.execute(query,data_tuple)
            sc.commit()
            data=cursor.fetchall()
            cursor.close()
            sc.close()
            if len(data) ==0:
                self.tableWidget.setRowCount(0)
            else:
                self.tableWidget.setRowCount(0)
                self.showdataintable(data)
    
    def removemusicfromhistory(self):
        row=self.tableWidget.currentRow()
        data=self.tableWidget.item(row,2).text()
        sc=sqlite3.connect(r"D:\MyWork\python\projects\music player\musicplayer.db")
        cursor=sc.cursor()
        query="""Delete from History where PlaybackDate= ?"""
        data_tuple=(data,)
        cursor.execute(query,data_tuple)
        sc.commit()
        data=cursor.fetchall()
        cursor.close()
        sc.close()
        self.tableWidget.setRowCount(0)
        self.searchmusic()
        
   

