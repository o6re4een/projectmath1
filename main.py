
import sys
from w3 import Ui_Form
from mw import Ui_MainWindow
from test import Ui_form2
from PyQt5 import QtCore, QtGui, QtWidgets
from povtor import Ui_povtor
import webbrowser
from PyQt5.QtGui import QPixmap, QImage
from final import Ui_Form3
import requests


#Открытие

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()







def openpovt(): #
    global povtor
    povtor = QtWidgets.QWidget()
    ui = Ui_povtor()
    ui.setupUi(povtor)
    povtor.show()
    MainWindow.close()
    ui.trig.clicked.connect(linkt)
    ui.logar.clicked.connect(linkl)
    ui.Nerav.clicked.connect(linkt)
    def menub():
        povtor.close()
        MainWindow.show()
    ui.menub.clicked.connect(menub)
ui.Ready.clicked.connect(openpovt)
def linkt():
    webbrowser.open_new("https://ru.wikipedia.org/wiki/Тригонометрические_функции")

def linkl():
    webbrowser.open_new("https://ik-study.ru/ege_math/logharifmy")
def linkn():
    webbrowser.open_new("https://ik-study.ru/ege_math/logharifmy")



def openWindow(): #
    global Form
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    MainWindow.close()
    Form.show()
    def menubtn(self): #
        Form.close()
        MainWindow.show()
    ui.munubut.clicked.connect(menubtn)
    def opentest(): #открытие окна теста
        global form2
        form2 = QtWidgets.QWidget()
        ui = Ui_form2()
        ui.setupUi(form2)
        form2.show()
        Form.close()



        url_image = "https://ege.sdamgia.ru/formula/svg/01/01af9d628fcf4a61f4ba0d32453a7896.svg"
        image = QImage()
        image.loadFromData(requests.get(url_image).content)
        ui.qt1.setPixmap(QPixmap(image))



        # Переключение виджета по кнопкам
        def qst1():
            ui.stackedWidget.setCurrentWidget(ui.quest1)
        def qst2():
            ui.stackedWidget.setCurrentWidget(ui.quest2)
        def qst3():
            ui.stackedWidget.setCurrentWidget(ui.quest3)
        def qst4():
            ui.stackedWidget.setCurrentWidget(ui.quest4)
        def qst5():
            ui.stackedWidget.setCurrentWidget(ui.quest5)

        ##Привязка к кнопкам
        ui.qb1.clicked.connect(qst1)
        ui.qb2.clicked.connect(qst2)
        ui.qb3.clicked.connect(qst3)
        ui.qb4.clicked.connect(qst4)
        ui.qb5.clicked.connect(qst5)
        #Создание теста
    
        
        def saveotv1():
            global ot1
            ot1=ui.ans1.text()           
            return ot1
        def saveotv2():
            global ot2
            ot2=ui.ans2.text()           
            return ot2
        def saveotv3():
            global ot3
            ot3=ui.ans3.text()           
            return ot3
        def saveotv4():
            global ot4
            ot4=ui.ans4.text()           
            return ot4
        def saveotv5():
            global ot5 
            ot5=ui.ans5.text()                      
            return ot5
            
            
        
        
        ui.ans1.textChanged[str].connect(saveotv1)
        ui.ans2.textChanged[str].connect(saveotv2)
        ui.ans3.textChanged[str].connect(saveotv3)
        ui.ans4.textChanged[str].connect(saveotv4)
        ui.ans5.textChanged[str].connect(saveotv5)

        

    


        


            
            
            

        
        def openfin():

            
            



            k=0
            if ot1 == "-1/2":
                k+=1
            else:
                k+=0
            if ot2=="1/4":
                k+=1
            else:
                k+=0
            if ot3 == "1":
                k+=1
            else:
                k+=0
            if ot4 == "-ctga":
                k+=1
            else:
                k+=0
            if ot5 == "8cos^4a":
                k+=1
            else:
                k+=0
            
            k= "Ваша оценка: " + str(k) 
          
            
            

            
            global Form3
            Form3 = QtWidgets.QWidget()
            ui = Ui_Form3()
            ui.setupUi(Form3)
            ui.label.setText(k)
            Form3.show()

            form2.close()
       
        ui.fin.clicked.connect(openfin)

        
        





     




    

    ui.trigan.clicked.connect(opentest)

ui.test.clicked.connect(openWindow)





sys.exit(app.exec_())