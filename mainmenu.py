# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musicplayer.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pygame import mixer
from library import Ui_librarymenu
from History import Ui_MenuHistori
import sqlite3
from mutagen.mp3 import MP3
import os


class Ui_MainMenu(QtWidgets.QDialog):
    playcondition="stop"
    previousmusic=""
    volume=1.0
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.setEnabled(True)
        MainMenu.resize(427, 268)
        MainMenu.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainMenu.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(209, 147, 57, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.btnnext = QtWidgets.QPushButton(self.centralwidget)
        self.btnnext.setGeometry(QtCore.QRect(260, 200, 41, 23))
        self.btnnext.setMinimumSize(QtCore.QSize(41, 23))
        self.btnnext.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"D:\MyWork\python\projects\music player\002-next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnnext.setIcon(icon)
        self.btnnext.setObjectName("btnnext")
        self.bntlibrary=QtWidgets.QPushButton(self.centralwidget)
        self.bntlibrary.setObjectName("btnlibrary")
        self.bntlibrary.setText("Library")
        self.btnHistory=QtWidgets.QPushButton(self.centralwidget)
        self.btnHistory.setObjectName("btnHistori")
        self.btnHistory.setText("History")
        self.btnHistory.move(70,0)

        self.btnsettings=QtWidgets.QPushButton(self.centralwidget)
        self.btnsettings.setObjectName("btnsettings")
        self.btnsettings.setText("Settings")
        self.btnsettings.move(140,0)
       

        self.btnplay = QtWidgets.QPushButton(self.centralwidget)
        self.btnplay.setGeometry(QtCore.QRect(220, 200, 41, 23))
        self.btnplay.setMinimumSize(QtCore.QSize(41, 23))
        self.btnplay.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(r"D:\MyWork\python\projects\music player\003-play-button-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnplay.setIcon(icon1)
        self.btnplay.setObjectName("btnplay")
        self.btnprevious = QtWidgets.QPushButton(self.centralwidget)
        self.btnprevious.setGeometry(QtCore.QRect(180, 200, 41, 23))
        self.btnprevious.setMinimumSize(QtCore.QSize(41, 23))
        self.btnprevious.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\MyWork\\python\\projects\\music player\\001-previous-4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnprevious.setIcon(icon2)
        self.btnprevious.setObjectName("btnprevious")
        self.btnvolumedown = QtWidgets.QPushButton(self.centralwidget)
        self.btnvolumedown.setGeometry(QtCore.QRect(350, 200, 20, 23))
        self.btnvolumedown.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(r"D:\MyWork\python\projects\music player\008-left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnvolumedown.setIcon(icon3)
        self.btnvolumedown.setObjectName("btnvolumedown")
        self.btnvolumeup = QtWidgets.QPushButton(self.centralwidget)
        self.btnvolumeup.setGeometry(QtCore.QRect(390, 200, 21, 23))
        self.btnvolumeup.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(r"D:\MyWork\python\projects\music player\001-right-arrow-4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnvolumeup.setIcon(icon4)
        self.btnvolumeup.setObjectName("btnvolumeup")
        self.slidermusic = QtWidgets.QSlider(self.centralwidget)
        self.slidermusic.setGeometry(QtCore.QRect(60, 180, 351, 22))
        self.slidermusic.setOrientation(QtCore.Qt.Horizontal)
        self.slidermusic.setObjectName("slidermusic")
        self.btnsound = QtWidgets.QPushButton(self.centralwidget)
        self.btnsound.setGeometry(QtCore.QRect(370, 200, 20, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnsound.setFont(font)
        self.btnsound.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(r"D:\MyWork\python\projects\music player\015-volume-adjustment.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnsound.setIcon(icon5)
        self.btnsound.setObjectName("btnsound")
        self.btnstop = QtWidgets.QPushButton(self.centralwidget)
        self.btnstop.setGeometry(QtCore.QRect(144, 200, 41, 23))
        self.btnstop.setMinimumSize(QtCore.QSize(41, 23))
        self.btnstop.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(r"D:\MyWork\python\projects\music player\stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnstop.setIcon(icon6)
        self.btnstop.setObjectName("btnstop")
        self.btnsearchmusic = QtWidgets.QPushButton(self.centralwidget)
        self.btnsearchmusic.setGeometry(QtCore.QRect(110, 200, 41, 23))
        self.btnsearchmusic.setMinimumSize(QtCore.QSize(41, 23))
        self.btnsearchmusic.setText("")
        self.btnrepeat = QtWidgets.QPushButton(self.centralwidget)
        self.btnrepeat.setGeometry(QtCore.QRect(84, 200, 31, 23))
        self.btnrepeat.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(r"D:\MyWork\python\projects\music player\004-music-player.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnrepeat.setIcon(icon8)
        self.btnrepeat.setObjectName("btnrepeat")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(r"D:\MyWork\python\projects\music player\002-eject.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnsearchmusic.setIcon(icon7)
        self.btnsearchmusic.setObjectName("btnsearchmusic")
        MainMenu.setCentralWidget(self.centralwidget)
    
        self.txtmusicname = QtWidgets.QLineEdit(self.centralwidget)
        self.txtmusicname.setGeometry(QtCore.QRect(60, 30, 341, 20))
        self.txtmusicname.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txtmusicname.setObjectName("txtmusicname")
        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)
        self.clickevent()

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Music Player"))

    def showLibraryMenu(self):
        self.librarymenu = QtWidgets.QMainWindow()
        self.ui = Ui_librarymenu()
        self.ui.setupUi(self.librarymenu)
        self.librarymenu.show()   

    def showHistoryMenu(self):
        self.historymenu=QtWidgets.QMainWindow()
        self.historyui=Ui_MenuHistori()
        self.historyui.setupUi(self.historymenu)
        self.historymenu.show()
        self.historyui.showrecentmusics()
        self.historyui.txtsearchmusic.textChanged.connect(self.historyui.searchmusic)
        self.historyui.btnBack.clicked.connect(self.historymenu.close)
        self.historyui.btnplayhistory.clicked.connect(self.playmusicfromhistory)
        self.historyui.btnremove.clicked.connect(self.historyui.removemusicfromhistory)

    def playmusicfromhistory(self):
        currentrow=self.historyui.tableWidget.currentRow()
        musicname=self.historyui.tableWidget.item(currentrow,0).text()
        if os.path.isfile(musicname):
            mixer.init()
            if mixer.music.get_busy():
                mixer.music.stop()
                self.txtmusicname.setText(musicname)
                self.playcondition="stop"
                self.playmusic()
                self.playcondition="play"
            else:
                self.txtmusicname.setText(musicname)
                self.playcondition="stop"
                self.playmusic()
                self.playcondition="play"
                



    def clickevent(self):
        self.btnsearchmusic.clicked.connect(self.browserclick)
        self.btnplay.clicked.connect(self.playmusic)
        self.btnstop.clicked.connect(self.stopmusic)  
        self.btnrepeat.clicked.connect(self.repeatmusic)
        self.btnvolumedown.clicked.connect(self.volumedown)
        self.btnvolumeup.clicked.connect(self.volumeup)
        self.bntlibrary.clicked.connect(self.showLibraryMenu)
        self.btnHistory.clicked.connect(self.showHistoryMenu) 


    def playmusic(self):
        import copy
        musicname=""
        mixer.init()
        musicname=self.txtmusicname.text()
        if mixer.music.get_busy():
            if self.playcondition=="play":
                icon11 = QtGui.QIcon()
                mixer.music.pause()
                icon11.addPixmap(QtGui.QPixmap(r"D:\MyWork\python\projects\music player\003-play-button-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.btnplay.setIcon(icon11)
                self.playcondition="pause"

            elif self.playcondition=="pause":
                mixer.music.unpause()
                icon12 = QtGui.QIcon()
                icon12.addPixmap(QtGui.QPixmap(r"D:\MyWork\python\projects\music player\010-pause-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.btnplay.setIcon(icon12)
                self.playcondition="play"
        
        else :
            if len(musicname) != 0:
                
                mixer.music.load(musicname)
                mixer.music.play()
                icon16 = QtGui.QIcon()
                icon16.addPixmap(QtGui.QPixmap(r"D:\MyWork\python\projects\music player\010-pause-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.btnplay.setIcon(icon16)
                self.playcondition="play"
                self.AddMusicToHistory()
                return




    def getlength(self):
        musicname=self.txtmusicname.text()
        music=MP3(musicname)
        length=int(music.info.length)
        min=int(length/60)
        sec=length-(min*60)
        return str(min)+":" + str(sec)

    

    def AddMusicToHistory(self):
        import time
        present=time.ctime()
        musicname=self.txtmusicname.text()
        length="unknown"
        musicformat=os.path.splitext(musicname)
        if musicformat[1]==".mp3":
            length=self.getlength()
        sc=sqlite3.connect(r"D:\MyWork\python\projects\music player\musicplayer.db")
        cursor=sc.cursor()
        query="""insert into History  values(?,?,?)"""
        data_tuple=(musicname,length,present,)
        cursor.execute(query,data_tuple)
        sc.commit()
        cursor.close()
        sc.close()


    def repeatmusic(self):
        musicname=self.txtmusicname.text()
        if len(musicname) != 0:
            mixer.init()
            mixer.music.stop()
            mixer.music.load(musicname)
            mixer.music.play()

    def stopmusic(self):
        mixer.init()
        if mixer.music.get_busy():
            icon13 = QtGui.QIcon()
            icon13.addPixmap(QtGui.QPixmap(r"D:\MyWork\python\projects\music player\003-play-button-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btnplay.setIcon(icon13)
            mixer.music.stop()
            self.playcondition="stop"

    
    def browserclick(self):
        musicname=QtWidgets.QFileDialog.getOpenFileName(self,"Select Music","C:\\","MP3 Files(*.mp3)")
        if musicname[0] != "" :
            mixer.init()
            mixer.music.load(musicname[0])
            mixer.music.play()
            icon15 = QtGui.QIcon()
            icon15.addPixmap(QtGui.QPixmap(r"D:\MyWork\python\projects\music player\010-pause-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.btnplay.setIcon(icon15)
            self.playcondition="play"
            self.txtmusicname.setText(musicname[0])
            self.AddMusicToHistory()
            
            
    def volumeup(self):
        mixer.init()
        sound=mixer.music.get_volume()
        if sound != 1.0:
            mixer.music.set_volume(sound + 0.1)
            self.volume=sound + 0.1

    def volumedown(self):
        sound=mixer.music.get_volume()
        if sound != 0.0:
            mixer.music.set_volume(sound - 0.1)
            self.volume=sound - 0.1
    


if __name__ == "__main__":
    import sys
    import os
    app = QtWidgets.QApplication(sys.argv)
    MainMenu = QtWidgets.QMainWindow()
    librarymenu=QtWidgets.QMainWindow()
    ui = Ui_MainMenu()
    ui.setupUi(MainMenu)
    MainMenu.show()
    sys.exit(app.exec_())
