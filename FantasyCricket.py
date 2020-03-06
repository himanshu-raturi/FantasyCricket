# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ok.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 568)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(252, 252, 252);\n"
"border-top-color: rgb(166, 166, 166);\n"
"border-top-color: rgb(172, 172, 172);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_3.addWidget(self.radioButton_4, 5, 4, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_3.addWidget(self.radioButton_3, 5, 3, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_3.addWidget(self.radioButton_2, 5, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(50, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 6, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 6, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(50, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 6, 8, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 4, 10, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 6, 7, 1, 1)
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1.setObjectName("radioButton_1")
        self.gridLayout_3.addWidget(self.radioButton_1, 5, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 4, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 5, 9, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 5, 10, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 4, 9, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 4, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 6, 11, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.gridLayout_2.addWidget(self.label_1, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 5, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 1, 6, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 7, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 0, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 3, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 1, 2, 10)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 7, 1, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_3.addWidget(self.listWidget, 6, 1, 1, 5)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_3.addWidget(self.listWidget_2, 6, 9, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 645, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("alternate-background-color: rgb(204, 204, 204);\n"
"selection-background-color: rgb(202, 202, 202);")
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addSeparator()
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menu)

        self.retranslateUi(MainWindow)

        self.radioButton_1.toggled.connect(self.ctg)
        self.radioButton_2.toggled.connect(self.ctg)
        self.radioButton_3.toggled.connect(self.ctg)
        self.radioButton_4.toggled.connect(self.ctg)

        self.listWidget.itemDoubleClicked.connect(self.removelist1)
        self.listWidget_2.itemDoubleClicked.connect(self.removelist2)

        

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "fantasy Cricket"))
        self.radioButton_4.setText(_translate("MainWindow", "WK"))
        self.radioButton_3.setText(_translate("MainWindow", "AR"))
        self.radioButton_2.setText(_translate("MainWindow", "BOW"))
        self.label_8.setText(_translate("MainWindow", "###"))
        self.label_17.setText(_translate("MainWindow", ">"))
        self.radioButton_1.setText(_translate("MainWindow", "BAT"))
        self.label_9.setText(_translate("MainWindow", "###"))
        self.label_15.setText(_translate("MainWindow", "Team Name"))
        self.label_16.setText(_translate("MainWindow", "Display Here"))
        self.label_25.setText(_translate("MainWindow", "Points Used"))
        self.label_24.setText(_translate("MainWindow", "Points Available"))
        self.label_4.setText(_translate("MainWindow", "##"))
        self.label_1.setText(_translate("MainWindow", "Batsman (BAT)"))
        self.label_11.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.label_6.setText(_translate("MainWindow", "##"))
        self.label_19.setText(_translate("MainWindow", "Wicket-keeper (WK)"))
        self.label_7.setText(_translate("MainWindow", "##"))
        self.label_21.setText(_translate("MainWindow", "Your Selection"))
        self.label_22.setText(_translate("MainWindow", "Bowler (BOW)"))
        self.label_5.setText(_translate("MainWindow", "##"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))

    def reset1 (self):
        self.label_4.setText("##")
        self.label_5.setText("##")
        self.label_6.setText("##")
        self.label_7.setText("##")
        self.label_8.setText("###")
        self.label_9.setText("###")
        self.label_16.setText("Display Here")
        self.listWidget.clear()
        self.listWidget_2.clear()

    def menu(self,action):
        txt=(action.text())
    
        if txt=='NEW Team':
            self.bat=0
            self.bow=0
            self.ar=0
            self.wk=0
            self.point_used=0
            self.point_ava=1000
            self.listWidget.clear()
            self.listWidget_2.clear()
            
            
            
            sql="select name from teams"
            cur=conn.execute(sql)
            row=cur.fetchone()
            text, ok=QtWidgets.QInputDialog.getText(MainWindow, "Team", "Enter name of team:")                       
            for row in cur:
                if text == row[0]:
                    self.showdlg("match found!!\ntry with another name")
                   
                    return
            
            
            self.label_16.setText(text)
            if self.label_16.text()=="":
                self.reset1()
                return
            self.show()


        if txt=='SAVE Team':
            if self.label_16.text()=='Display Here':
                self.showdlg("Create a team first\nManage Teams -> NEW Team")
                self.reset1()
                return
            count=self.listWidget_2.count()
            selected=""
            for i in range(count):
                selected+=self.listWidget_2.item(i).text()
                if i<count-1:
                    selected+=","

            self.saveteam(self.label_16.text(),selected,self.point_used)

        if txt=='OPEN Team':
            self.bat=0
            self.bow=0
            self.ar=0
            self.wk=0
            self.point_used=0
            self.point_ava=1000
            self.listWidget.clear()
            self.listWidget_2.clear()
            self.show()
            #print("rgr")
            self.openteam()


        if txt=='EVALUATE Team':            
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            #print("effieh")
            ret=Dialog.exec()
            
    def show(self):
        self.label_4.setText(str(self.bat))
        self.label_5.setText(str(self.bow))
        self.label_6.setText(str(self.ar))
        self.label_7.setText(str(self.wk))
        self.label_8.setText(str(self.point_used))
        self.label_9.setText(str(self.point_ava))
    
    def saveteam(self,nm,ply,val):
        #print("rvrv")
        
        if self.bat+self.bow+self.ar+self.wk!=11:
            self.showdlg("Insufficient players")
            return
        if self.ar ==0:
            self.showdlg("Insufficient Allrounders")
            return
        if self.wk ==0:
            self.showdlg("Insufficient Wicketkeepers")
            return

        sql="select name from teams"
        cur=conn.execute(sql)
        row=cur.fetchone()
        #print(row)
        text=self.label_16.text()
        count=self.listWidget_2.count()
        for row in cur:
            if text == row[0]:
                self.showdlg("match found!\nteam is already Saved")
                self.reset1()              
                return False
        sql1="INSERT INTO teams (name,players,value) VALUES ('"+nm+"','"+ply+"','"+str(val)+"');"
        #print("f3f4")
        try:
            #print("bjr")
            cur=conn.execute(sql1)
            #print("dehe")
            self.showdlg("Team Saved Succesfully")
            self.reset1()
            conn.commit()
        except:
            self.showdlg("Error in Operation")
            conn.rollback()   
          
    def openteam(self):
        #print("rvrjbv")
        
        sql="select name from teams;"
        #print("efef")
        cur=conn.execute(sql)
        #print("vebjb")
        teams=["Select Team"]

        for row in cur:
            teams.append(row[0])
        
        team, ok=QtWidgets.QInputDialog.getItem(MainWindow,"Fantasy Cricket","Choose A Team",teams,0,False)
        
        if ok and team:
            if team =="Select Team":
                self.showdlg("select a Team first")
                self.reset1()
                return

            self.label_16.setText(team)
        else:
            self.reset1()
            return
        sql1="SELECT players,value from teams where name='"+team+"';"
        cur=conn.execute(sql1)
        row=cur.fetchone()
        selected=row[0].split(',')
        self.listWidget_2.addItems(selected)
        self.point_used=row[1]
        
        self.point_ava=1000-row[1]
        count=self.listWidget_2.count()

        ##iterate to count no. of specific players

        for i in range(count):
            ply=self.listWidget_2.item(i).text()
            sql="select category from stats where player='"+ply+"';"
            
            cur=conn.execute(sql)
            row=cur.fetchone()
            
            ctgr=row[0]
            #print("ej")
            if ctgr=="BAT":self.bat+=1
            if ctgr=="BWL":self.bow+=1
            if ctgr=="AR":self.ar+=1
            if ctgr=="WK":self.wk+=1  

        self.show()

    def criteria(self,ctgr,item):
        msg=''
        
        
        if ctgr=="BAT" and self.bat>=5:msg="Batsmen not more than 5"
        if ctgr=="BWL" and self.bow>=5:msg="bowlers not more than 5"
        if ctgr=="AR" and self.ar>=3:msg="Allrounders not more than 3"
        if ctgr=="WK" and self.wk>=1:msg="Wicketkeepers not more than 1"
        if msg!='':
            self.showdlg(msg)
            return False

        sql="SELECT value from stats where player='"+item.text()+"'"
        cur=conn.execute(sql)
        row=cur.fetchone()
        self.point_ava-=int(row[0])
        self.point_used+=int(row[0])
                #msg="You Have Exhausted your Points"
        if self.point_ava<0:
            self.showdlg("You Have Exhausted your Points\n Choose some diffrent players")
            self.point_ava+=int(row[0])
            self.point_used-=int(row[0])
            return False

        if ctgr=="BAT":self.bat+=1
        if ctgr=="BWL":self.bow+=1
        if ctgr=="AR":self.ar+=1
        if ctgr=="WK":self.wk+=1

        return True

    def ctg(self):
        ctgr=''
        if self.radioButton_1.isChecked()==True:ctgr='BAT'
        if self.radioButton_2.isChecked()==True:ctgr='BWL'
        if self.radioButton_3.isChecked()==True:ctgr='AR'
        if self.radioButton_4.isChecked()==True:ctgr='WK'
        
        self.fillList(ctgr)
    # to show message 
    def showdlg(self,msg):
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowTitle("Fantasy Cricket")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        ret=Dialog.exec()

    #to fill the left list
    def fillList(self,ctgr):
        if self.label_16.text()=='Display Here':
            self.showdlg("Enter name of team")
            return
        
        self.listWidget.clear()
        sql="SELECT player from stats where category='"+ctgr+"';"
        cur=conn.execute(sql)
        for row in cur:
            selected=[]
            for i in range(self.listWidget_2.count()):
                selected.append(self.listWidget_2.item(i).text())
            if row[0] not in selected:self.listWidget.addItem(row[0])
    
    #remove item from list 1 and add it to list 2
    def removelist1(self,item):

        if self.bat+self.bow+self.ar+self.wk>=11:
            self.showdlg("players not more than 11")
            return
        ctgr=''
        if self.radioButton_1.isChecked()==True:ctgr='BAT'
        if self.radioButton_2.isChecked()==True:ctgr='BWL'
        if self.radioButton_3.isChecked()==True:ctgr='AR'
        if self.radioButton_4.isChecked()==True:ctgr='WK'
        ret=self.criteria(ctgr,item)
        
        if ret==True:
            self.listWidget.takeItem(self.listWidget.row(item))
            
            self.listWidget_2.addItem(item.text())
            self.show()
            

    #remove item from list 2 and add it to list 1
    def removelist2(self,item):
        self.listWidget_2.takeItem(self.listWidget_2.row(item))        
        cursor = conn.execute("SELECT player,value,category from stats where player='"+item.text()+"'")
        row=cursor.fetchone()
        self.point_ava=self.point_ava+int(row[1])
        self.point_used=self.point_used-int(row[1])
        ctgr=row[2]
        if ctgr=="BAT":
            self.bat-=1
            if self.radioButton_1.isChecked()==True:self.listWidget.addItem(item.text())
        if ctgr=="BWL":
            self.bow-=1
            if self.radioButton_2.isChecked()==True:self.listWidget.addItem(item.text())
        if ctgr=="AR":
            self.ar-=1
            if self.radioButton_3.isChecked()==True:self.listWidget.addItem(item.text())
        if ctgr=="WK":
            self.wk-=1
            if self.radioButton_4.isChecked()==True:self.listWidget.addItem(item.text())
        self.show()

#class containing Evaluate Team dailog box
class Ui_Dialog(Ui_MainWindow):
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 3)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 1, 1, 6)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox)
        sql="select name from teams"
        cur=conn.execute(sql)
        teams=[]
        for row in cur:
            self.comboBox.addItem(row[0])        
        
        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 4, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate)
        self.gridLayout.addWidget(self.pushButton, 8, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 9, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 7, 7, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 7, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setMaxVisibleItems(20)
        self.comboBox_2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 3, 4, 1, 2)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("selection-color: rgb(85, 170, 255);\n"
"color: rgb(85, 170, 255);")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 5, 1, 1)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 7, 1, 1, 2)
        self.listWidget_2 = QtWidgets.QListWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.listWidget_2.setFont(font)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout.addWidget(self.listWidget_2, 7, 4, 1, 2)

        self.retranslateUi(Dialog)
        self.comboBox_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    #function used to calculate points scored by the team
    def calculate(self):
        if self.comboBox.currentText() =='Select Team':
            self.listWidget.clear()
            self.listWidget_2.clear()
            self.label_5.setText("###")
            t = Ui_MainWindow()
            t.showdlg('Select Team')
            return
        if self.comboBox_2.currentText() =="Select Match":
            self.listWidget.clear()
            self.listWidget_2.clear()
            self.label_5.setText("###")
            t = Ui_MainWindow()
            t.showdlg('Select Match')
            return
        
        team=self.comboBox.currentText()
        self.listWidget.clear()
        sql1="select players, value from teams where name='"+team+"'"
        cur=conn.execute(sql1)
        row=cur.fetchone()
        selected=row[0].split(',')
        self.listWidget.addItems(selected)
        teamttl=0
        self.listWidget_2.clear()
        match=self.comboBox_2.currentText()
        for i in range(self.listWidget.count()):
            ttl, batscore, bowlscore, fieldscore=0,0,0,0
            nm=self.listWidget.item(i).text()
            cursor=conn.execute("select * from "+match+" where player='"+nm+"'")
            row=cursor.fetchone()
            batscore=int(row[1]//2)
            if batscore>=50: batscore+=5
            if batscore>=100: batscore+=10
            if row[2]>0:
                sr=(row[1]/row[2])*100
                if sr>=80: batscore+=2
                if sr>=100:batscore+=4
            batscore+=row[3]
            batscore+=2*row[4]
            bowlscore=row[8]*10
            if row[8]>=3: bowlscore=bowlscore+5
            if row[8]>=5: bowlscore=bowlscore+10
            if row[5]>0:
                er=row[7]/row[5]
                if er<=2: bowlscore=bowlscore+10
                elif er>2 and er<=3.5: bowlscore=bowlscore+7
                elif er>3.5 and er<=4.5: bowlscore=bowlscore+4
            fieldscore=(row[9]+row[10]+row[11])*10            
            ttl=batscore+bowlscore+fieldscore
            self.listWidget_2.addItem(str(ttl))
            teamttl=teamttl+ttl
        self.label_5.setText(str(teamttl))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Fantasy Cricket"))
        self.label.setText(_translate("Dialog", "Evaluate the Performance of your Fantasy Team"))
        self.label_3.setText(_translate("Dialog", "Players"))
        self.comboBox.setItemText(0, _translate("Dialog", "Select Team"))
        self.label_4.setText(_translate("Dialog", "Points"))
        self.pushButton.setText(_translate("Dialog", "Calculate Score"))
        self.comboBox_2.setCurrentText(_translate("Dialog", "Select Match"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Select Match"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "match1"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "match2"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "match3"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "match4"))
        self.comboBox_2.setItemText(5, _translate("Dialog", "match5"))
        self.label_5.setText(_translate("Dialog", "###"))
        self.listWidget_2.setWhatsThis(_translate("Dialog", "<html><head/><body><p>help</p></body></html>"))



if __name__ == "__main__":
    import sys
    import sqlite3
    conn = sqlite3.connect('FantasyCricket.db')
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

