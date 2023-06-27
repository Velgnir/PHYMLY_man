import sys
import os.path
import pip


import configparser
from configparser import ConfigParser
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap
from PySide6 import QtWidgets
from python_ui_interface import Ui_MainWindow
from PySide6.QtCore import QRect
import os
import compiles
from PIL import Image
import shutil


def C_to_rgb(Temperature, Temperature_limit):
    if(Temperature <= 0):
        r = 0
        g = int((255.0/273.0) * (Temperature+273))
        b = 255
    elif(Temperature <= Temperature_limit/3):
        r = 0
        g = 255
        b = int((255.0 / (Temperature_limit / 3)) * ((Temperature_limit / 3.0) - Temperature))
    elif(Temperature <= ((2*Temperature_limit)/3)):
        r = int((255.0/((Temperature_limit)/3.0)) * (Temperature - Temperature_limit/3.0))
        g = 255
        b = 0
    else:
        r = 255
        g = int((255.0 / (Temperature_limit / 3.0)) * (Temperature_limit - Temperature))
        b = 0
    return [r, g, b]

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.spinBox.setValue(1)
        self.ui.pushButton.clicked.connect(self.bp)
        self.ui.pushButton_2.clicked.connect(self.check)
        self.ui.pushButton_3.clicked.connect(self.save)
        self.ui.pushButton_4.clicked.connect(self.restore)


    def check(self, warerror):
        self.ui.lineEdit.setStyleSheet("background-color: #A3BE8C;")
        self.ui.lineEdit_2.setStyleSheet("background-color: #A3BE8C;")
        self.ui.lineEdit_3.setStyleSheet("background-color: #A3BE8C;")
        self.ui.lineEdit_7.setStyleSheet("background-color: #A3BE8C;")
        self.ui.lineEdit_9.setStyleSheet("background-color: #A3BE8C;")
        self.ui.lineEdit_4.setStyleSheet("background-color: #A3BE8C;")
        self.ui.lineEdit_5.setStyleSheet("background-color: #A3BE8C;")
        self.ui.lineEdit_6.setStyleSheet("background-color: #A3BE8C;")
        self.ui.lineEdit_8.setStyleSheet("background-color: #A3BE8C;")
        self.ui.lineEdit_10.setStyleSheet("background-color: #A3BE8C;")
        self.ui.lineEdit_11.setStyleSheet("background-color: #A3BE8C;")
        self.ui.lineEdit_12.setStyleSheet("background-color: #A3BE8C;")
        self.ui.lineEdit_13.setStyleSheet("background-color: #A3BE8C;")
        self.ui.lineEdit_14.setStyleSheet("background-color: #A3BE8C;")
        self.ui.lineEdit_15.setStyleSheet("background-color: #A3BE8C;")

        self.ui.textEdit.setStyleSheet("background-color: #A3BE8C;")
        self.ui.textEdit_2.setStyleSheet("background-color: #A3BE8C;")
        self.ui.textEdit_3.setStyleSheet("background-color: #A3BE8C;")
        self.ui.spinBox.setStyleSheet("background-color: #A3BE8C;")

        errors = 0
        text_browser = ""
        col = "#BF616A;"
        if (warerror==False):
            warerror = "WARNING"
            col = "#EBCB8B;"
        if(self.ui.spinBox.value()==0):
            text_browser=text_browser+warerror+": 'number of calculating threads' - impossible number \n"
            self.ui.spinBox.setStyleSheet("background-color: "+col)
            errors +=1
        if(self.ui.lineEdit.text() == ""):
            text_browser=text_browser+"ERROR: 'coordinate size X' - empty \n"
            self.ui.lineEdit.setStyleSheet("background-color: #BF616A;")
        else:
            try:
                check = float(self.ui.lineEdit.text())
                if(check>0 and check < 2147483647):
                    pass
                else:
                    text_browser=text_browser+"ERROR: 'coordinate size X' - unreal value \n"
                    self.ui.lineEdit.setStyleSheet("background-color: #BF616A;")
            except:
                text_browser=text_browser+"ERROR: 'coordinate size X' - unreal value \n"
                self.ui.lineEdit.setStyleSheet("background-color: #BF616A;")

        if(self.ui.lineEdit_2.text() == ""):
            text_browser=text_browser+"ERROR: 'coordinate size Y' - empty \n"
            self.ui.lineEdit_2.setStyleSheet("background-color: #BF616A;")
        else:
            try:
                check = float(self.ui.lineEdit_2.text())
                if(check>0):
                    pass
                else:
                    text_browser=text_browser+"ERROR: 'coordinate size Y' - unreal value \n"
                    self.ui.lineEdit_2.setStyleSheet("background-color: #BF616A;")
            except:
                text_browser=text_browser+"ERROR: 'coordinate size Y' - unreal value \n"
                self.ui.lineEdit_2.setStyleSheet("background-color: #BF616A;")

        if(self.ui.lineEdit_4.text() == ""):
            text_browser=text_browser+warerror+": 'step in time' - empty \n"
            self.ui.lineEdit_4.setStyleSheet("background-color: "+col)
        else:
            try:
                check = float(self.ui.lineEdit_4.text())
                if(check>0 and check < 2147483647):
                    pass
                else:
                    text_browser=text_browser+warerror+": 'step in time' - unreal value \n"
                    self.ui.lineEdit_4.setStyleSheet("background-color: "+col)
            except:
                text_browser=text_browser+warerror+": 'step in time' - unreal value \n"
                self.ui.lineEdit_4.setStyleSheet("background-color: "+col)

        if(self.ui.lineEdit_5.text() == ""):
            text_browser=text_browser+warerror+": 'step in X' - empty \n"
            self.ui.lineEdit_5.setStyleSheet("background-color: "+col)
        else:
            try:
                check = float(self.ui.lineEdit_5.text())
                if(check>0 and check < 2147483647):
                    pass
                else:
                    text_browser=text_browser+warerror+": 'step in X' - unreal value \n"
                    self.ui.lineEdit_5.setStyleSheet("background-color: "+col)
            except:
                text_browser=text_browser+warerror+": 'step in X' - unreal value \n"
                self.ui.lineEdit_5.setStyleSheet("background-color: "+col)

        if(self.ui.lineEdit_6.text() == ""):
            text_browser=text_browser+warerror+": 'step in Y' - empty \n"
            self.ui.lineEdit_6.setStyleSheet("background-color: "+col)
        else:
            try:
                check = float(self.ui.lineEdit_6.text())
                if(check>0 and check < 2147483647):
                    pass
                else:
                    text_browser=text_browser+warerror+": 'step in Y' - unreal value \n"
                    self.ui.lineEdit_6.setStyleSheet("background-color: "+col)
            except:
                text_browser=text_browser+warerror+": 'step in Y' - unreal value \n"
                self.ui.lineEdit_6.setStyleSheet("background-color: "+col)

        if(self.ui.lineEdit_7.text() == ""):
            text_browser=text_browser+"ERROR: 'standart temperature' - empty \n"
            self.ui.lineEdit_7.setStyleSheet("background-color: #BF616A;")
        else:
            try:
                check = float(self.ui.lineEdit_7.text())
                if(check>-273.16 and check < 2147483647):
                    pass
                else:
                    text_browser=text_browser+"ERROR: 'standart temperature' - unreal value \n"
                    self.ui.lineEdit_7.setStyleSheet("background-color: #BF616A;")
            except:
                text_browser=text_browser+"ERROR: 'standart temperature' - unreal value \n"
                self.ui.lineEdit_7.setStyleSheet("background-color: #BF616A;")

        if(self.ui.lineEdit_8.text() == ""):
            text_browser=text_browser+warerror+": 'specific heat capacity' - empty \n"
            self.ui.lineEdit_8.setStyleSheet("background-color: "+col)
        else:
            try:
                check = float(self.ui.lineEdit_8.text())
                if(check>0 and check < 2147483647):
                    pass
                else:
                    text_browser=text_browser+warerror+": 'specific heat capacity' - unreal value \n"
                    self.ui.lineEdit_8.setStyleSheet("background-color: "+col)
            except:
                text_browser=text_browser+warerror+": 'specific heat capacity' - unreal value \n"
                self.ui.lineEdit_8.setStyleSheet("background-color: "+col)

        if(self.ui.lineEdit_14.text() == ""):
            text_browser=text_browser+warerror+": 'thermal conduction' - empty \n"
            self.ui.lineEdit_14.setStyleSheet("background-color: "+col)
        else:
            try:
                check = float(self.ui.lineEdit_14.text())
                if(check>0 and check < 2147483647):
                    pass
                else:
                    text_browser=text_browser+warerror+": 'thermal conduction' - unreal value \n"
                    self.ui.lineEdit_14.setStyleSheet("background-color: "+col)
            except:
                text_browser=text_browser+warerror+": 'thermal conduction' - unreal value \n"
                self.ui.lineEdit_14.setStyleSheet("background-color: "+col)

        if(self.ui.lineEdit_15.text() == ""):
            text_browser=text_browser+warerror+": 'density' - empty \n"
            self.ui.lineEdit_15.setStyleSheet("background-color: "+col)
        else:
            try:
                check = float(self.ui.lineEdit_15.text())
                if(check>0 and check < 2147483647):
                    pass
                else:
                    text_browser=text_browser+warerror+": 'density' - unreal value \n"
                    self.ui.lineEdit_15.setStyleSheet("background-color: "+col)
            except:
                text_browser=text_browser+warerror+": 'density' - unreal value \n"
                self.ui.lineEdit_15.setStyleSheet("background-color: "+col)

        if(self.ui.lineEdit_3.text() == "" and self.ui.lineEdit_9.text()==""):
            text_browser=text_browser+warerror+": 'Temperature limit' and 'limit of steps in time' - empty \n"
            self.ui.lineEdit_3.setStyleSheet("background-color: "+col)
            self.ui.lineEdit_9.setStyleSheet("background-color: "+col)
        else:
            try:
                check = float(self.ui.lineEdit_3.text())
                if(check>0 and check < 2147483647):
                    pass
                else:
                    text_browser=text_browser+warerror+": 'Temperature limit' - unreal value \n"
                    self.ui.lineEdit_3.setStyleSheet("background-color: "+col)
            except:
                if(self.ui.lineEdit_3.text()==""):
                    pass
                else:
                    text_browser=text_browser+warerror+": 'Temperature limit' - unreal value \n"
                    self.ui.lineEdit_3.setStyleSheet("background-color: "+col)
            try:
                check = float(self.ui.lineEdit_9.text())
                if(check>0 and check < 2147483647):
                    pass
                else:
                    text_browser=text_browser+warerror+": 'limit of steps in time' - unreal value \n"
                    self.ui.lineEdit_9.setStyleSheet("background-color: "+col)
            except:
                if(self.ui.lineEdit_9.text()==""):
                    pass
                else:
                    text_browser=text_browser+warerror+": 'limit of steps in time' - unreal value \n"
                    self.ui.lineEdit_9.setStyleSheet("background-color: "+col)

        if(self.ui.lineEdit_10.text()==""):
            pass
        else:
            try:
                check = self.ui.lineEdit_10.text().replace("x","1")
            except:
                check = self.ui.lineEdit_10.text()
            try:
                check = eval(check)
            except:
                text_browser = text_browser+"ERROR: 'left border: f4(x)' - unreal value \n"
                self.ui.lineEdit_10.setStyleSheet("background-color: #BF616A;")

        if(self.ui.lineEdit_13.text()==""):
            pass
        else:
            try:
                check = self.ui.lineEdit_13.text().replace("x","1")
            except:
                check = self.ui.lineEdit_13.text()
            try:
                check = eval(check)
            except:
                text_browser = text_browser+"ERROR: 'upper border: f1(x)' - unreal value \n"
                self.ui.lineEdit_13.setStyleSheet("background-color: #BF616A;")

        if(self.ui.lineEdit_11.text()==""):
            pass
        else:
            try:
                check = self.ui.lineEdit_11.text().replace("x","1")
            except:
                check = self.ui.lineEdit_11.text()
            try:
                check = eval(check)
            except:
                text_browser = text_browser+"ERROR: 'right border: f2(x)' - unreal value \n"
                self.ui.lineEdit_11.setStyleSheet("background-color: #BF616A;")

        if(self.ui.lineEdit_12.text()==""):
            pass
        else:
            try:
                check = self.ui.lineEdit_12.text().replace("x","1")
            except:
                check = self.ui.lineEdit_12.text()
            try:
                check = eval(check)
            except:
                text_browser = text_browser+"ERROR: 'lower border: f3(x)' - unreal value \n"
                self.ui.lineEdit_12.setStyleSheet("background-color: #BF616A;")


        try:
            x_list = (self.ui.textEdit.toPlainText()).split("\n")
            y_list = (self.ui.textEdit_2.toPlainText()).split("\n")
            temperature_list = (self.ui.textEdit_3.toPlainText()).split("\n")
        except:
            pass
        if (len(x_list)!=len(y_list) or len(x_list)!= len(temperature_list) or (x_list[0]=="" and (temperature_list[0]!="" or y_list[0]!="")) or (y_list[0]=="" and (temperature_list[0]!="" or x_list[0]!="")) or (temperature_list[0]=="" and (x_list[0]!="" or y_list[0]!="")) ):
            text_browser=text_browser+"ERROR: numbers of line of functions are different \n"
            self.ui.textEdit.setStyleSheet("background-color: #BF616A;")
            self.ui.textEdit_2.setStyleSheet("background-color: #BF616A;")
            self.ui.textEdit_3.setStyleSheet("background-color: #BF616A;")
        elif(x_list[0] =="" and y_list[0]=="" and temperature_list[0]==""):
            pass
        else:
            for i in range(len(x_list)):
                try:
                    check = x_list[i].replace("x","1")
                except:
                    check = x_list[i]
                try:
                    check = eval(check)
                except:
                    text_browser = text_browser+"ERROR: line number "+str(i+1)+" in 'X' - has unreal value \n"
                    self.ui.textEdit.setStyleSheet("background-color: #BF616A;")

                if(y_list[i][0]=="<" or y_list[i][0]==">"):
                    y_list[i]=y_list[i][1::]
                try:
                    check = y_list[i].replace("x","1")
                except:
                    check = y_list[i]
                try:
                    check = eval(check)
                except:
                    text_browser = text_browser+"ERROR: line number "+str(i+1)+" in 'Y' - has unreal value \n"
                    self.ui.textEdit_2.setStyleSheet("background-color: #BF616A;")

                try:
                    check = temperature_list[i].replace("x","1")
                except:
                    check = temperature_list[i]
                try:
                    check = eval(check)
                except:
                    text_browser = text_browser+"ERROR: line number "+str(i+1)+" in 'temperature' - has unreal value \n"
                    self.ui.textEdit_3.setStyleSheet("background-color: #BF616A;")
        

        self.ui.textBrowser.setText(text_browser)
        
        global conf
        try:
            x_list = (self.ui.textEdit.toPlainText()).split("\n")
            y_list = (self.ui.textEdit_2.toPlainText()).split("\n")
            temperature_list = (self.ui.textEdit_3.toPlainText()).split("\n")
        except:
            pass

        try:
            coordinate_size_X = float(self.ui.lineEdit.text())
            coordinate_size_Y = float(self.ui.lineEdit_2.text())

            standart_temperature = float(self.ui.lineEdit_7.text())

            coordinate_size_Y+=1
            matrix = []
            for i in range(0,int(coordinate_size_Y)):
                matrix.append([])
            for i in range(0,int(coordinate_size_Y)):
                for j in range(0,int(coordinate_size_X)):
                    matrix[i].append(standart_temperature)

            try:
                for i in range(0,len(x_list)):
                    if(y_list[i][0]==">"):

                        for x in range(0,int(coordinate_size_X)):
                            try:
                                x_string = x_list[i].replace("x",str(x))
                            except:
                                x_string = x_list[i]
                            try:
                                temperature = temperature_list[i].replace("x",eval(str(x_string)))
                            except:
                                temperature = temperature_list[i]

                            for y in range(0,int(coordinate_size_Y)):
                                if(eval(y_list[i][1::].replace("x",str(eval(x_string)))) <= y-1):
                                    matrix[y][x] = eval(temperature)
                    elif(y_list[i][0]=="<"):
                        for x in range(0,int(coordinate_size_X)):
                            try:
                                x_string = x_list[i].replace("x",str(x))
                            except:
                                x_string = x_list[i]
                            try:
                                temperature = temperature_list[i].replace("x",eval(str(x_string)))
                            except:
                                temperature = temperature_list[i]
                            for y in range(0,int(coordinate_size_Y)):
                                if(eval(y_list[i][1::].replace("x",str(eval(x_string)))) >= y-1):
                                    matrix[y][x] = eval(temperature)
                    else:
                        for x in range(0,int(coordinate_size_X)):
                            try:
                                x_string = x_list[i].replace("x",str(x))
                            except:
                                x_string = x_list[i]
                            try:
                                temperature = temperature_list[i].replace("x",eval(str(x_string)))
                            except:
                                temperature = temperature_list[i]
                            for y in range(0,int(coordinate_size_Y)):
                                if(eval(y_list[i][1::].replace("x",str(eval(x_string)))) == y):
                                    matrix[y][x] = eval(temperature)
            except:
                pass
            try:
                border_function = self.ui.lineEdit_10.text()
                for i in range(int(coordinate_size_Y)):
                    try:
                        result =border_function.replace("x",str(i))
                    except:
                        result = border_function
                    matrix[i][0] = int(eval(result))
            except:
                pass
            

            try:
                border_function = self.ui.lineEdit_11.text()
                for i in range(int(coordinate_size_Y)):
                    try:
                        result =border_function.replace("x",str(i))
                    except:
                        result = border_function
                    matrix[i][int(coordinate_size_X-1)] = int(eval(result))
            except:
                pass

            try:
                border_function = self.ui.lineEdit_13.text()
                for i in range(int(coordinate_size_X)):
                    try:
                        result =border_function.replace("x",str(i))
                    except:
                        result = border_function
                    matrix[int(coordinate_size_Y-1)][i] = int(eval(result))
            except:
                pass

            try:
                border_function = self.ui.lineEdit_12.text()
                for i in range(int(coordinate_size_X)):
                    try:
                        result =border_function.replace("x",str(i))
                    except:
                        result = border_function
                    matrix[1][i] = int(eval(result))
            except:
                pass
            for x in range(len(matrix)):
                for y in range(len(matrix[x])):
                    if(matrix[x][y]<-273.15 or matrix[x][y]>2147483647):
                        errors += 1
                        text_browser = text_browser + "ERROR: as a result of using plots in X: " +str(y)+" and Y: "+str(x)+" - unreal value \n"


            MAX_TEMPERATURE = -273.15
            for row in matrix:
                for el in row:
                    if (el>MAX_TEMPERATURE):
                        MAX_TEMPERATURE = el
            pixels = list()
            rbg=[]
            j=-273.0   
            set1=True
            while(True):
                if(j==-273.0):
                    for z in range(3):
                        pixels.append((0,0,0,255))
                elif(j>-0.1 and set1==True):
                    for z in range(3):
                        pixels.append((0,0,0,255))
                    set1 = False
                elif(j>MAX_TEMPERATURE):
                    for z in range(3):
                        pixels.append((0,0,0,255))
                    break;
            
                j=j+((MAX_TEMPERATURE+273)/337)
                rbg = C_to_rgb(j,MAX_TEMPERATURE)
                pixels.append((rbg[0],rbg[1],rbg[2],255))
        


            image_out = Image.new("RGBA",(len(pixels),30))
            image_out.putdata(pixels*30)
            image_out.save('python_interface/WATCH1.png')


            image_out2 = Image.new("RGBA",(int(coordinate_size_X),int(coordinate_size_Y)))
            pixels = []

            if(self.ui.checkBox.isChecked()):
                for j in range(0,int(coordinate_size_X)):
                    for i in range(1,int(coordinate_size_Y)):
                        rbg = C_to_rgb(matrix[i][j], MAX_TEMPERATURE)
                        pixels.append((rbg[0],rbg[1],rbg[2],255))
            else:
                for i in range(int(coordinate_size_Y-1),-1,-1):
                    for j in range(0,int(coordinate_size_X)):
                        rbg = C_to_rgb(matrix[i][j], MAX_TEMPERATURE)
                        pixels.append((rbg[0],rbg[1],rbg[2],255))
            image_out2.putdata(pixels)
            image_out2.save('python_interface/WATCH2.png')

            original_image = Image.open('python_interface/WATCH2.png')

            if(coordinate_size_X>181 and coordinate_size_X>=coordinate_size_Y):
                self.ui.label_24.setGeometry(QRect(850, int(170+(181 -181*(coordinate_size_Y/coordinate_size_X))/2), 181, int(181*(coordinate_size_Y/coordinate_size_X))))
                resized_image = original_image.resize((181, int(181*(coordinate_size_Y/coordinate_size_X))))
            elif(coordinate_size_Y>181 and coordinate_size_Y>=coordinate_size_X):
                self.ui.label_24.setGeometry(QRect(int(850+(181 -181*(coordinate_size_X/coordinate_size_Y))/2), 170, int(181*(coordinate_size_X/coordinate_size_Y)), 181))
                resized_image = original_image.resize((int(181*(coordinate_size_X/coordinate_size_Y)), 181))
            elif(coordinate_size_Y<=181 and coordinate_size_X<=181):
                self.ui.label_24.setGeometry(QRect(850+int((181-coordinate_size_X)/2), 170+int((181-coordinate_size_Y)/2), coordinate_size_X, coordinate_size_Y))
                resized_image = original_image.resize((coordinate_size_X, coordinate_size_Y))
            resized_image.save('python_interface/WATCH2.png')
            self.ui.label_26.setPixmap(QPixmap("python_interface/WATCH1.png"))

            self.ui.label_24.setPixmap(QPixmap("python_interface/WATCH2.png"))
            if(MAX_TEMPERATURE>0):
                self.ui.label_25.setText("-273" + " "+" "*int(85*(273/(MAX_TEMPERATURE+273))) +"0"+" "+" "*int(85-85*(273/(MAX_TEMPERATURE+273)))+str(MAX_TEMPERATURE))
            else:
                self.ui.label_25.setText("-273"+" "*87+str(MAX_TEMPERATURE))
            pass
        except:
            pass
        self.ui.textBrowser.setText(text_browser)
        if(errors>0):
            return 1

    def save(self):
        global conf
        if(self.check("WARNING") == 1):
            return 0
        try:
            x_list = (self.ui.textEdit.toPlainText()).split("\n")
            y_list = (self.ui.textEdit_2.toPlainText()).split("\n")
            temperature_list = (self.ui.textEdit_3.toPlainText()).split("\n")
        except:
            print("ERROR 1")
        coordinate_size_X = float(self.ui.lineEdit.text())

        coordinate_size_Y = float(self.ui.lineEdit_2.text())
            
        step_in_time = float(self.ui.lineEdit_4.text())
        step_in_X = float(self.ui.lineEdit_5.text())
        step_in_Y = float(self.ui.lineEdit_6.text())
        standart_temperature = float(self.ui.lineEdit_7.text())
        heat_capacity = float(self.ui.lineEdit_8.text())
        density = float(self.ui.lineEdit_15.text())
        thermal_conduction = float(self.ui.lineEdit_14.text())
            

        conf = configparser.RawConfigParser()
        conf.read("config.conf")

        if(len(self.ui.lineEdit_10.text())>0):
            try1 = self.ui.lineEdit_10.text()
            try:
                result =try1.replace("x",'1')
                result = eval(result)
            except:
                result = eval(try1)

            conf.set("field-properties", "left_func_arg", 1)
        else:
            conf.set("field-properties", "left_func_arg", 0)

        if(len(self.ui.lineEdit_13.text())>0):
            try1 = self.ui.lineEdit_13.text()
            try:
                result =try1.replace("x",'1')
                result = eval(result)
            except:
                result = eval(try1)

            conf.set("field-properties", "up_func_arg", 1)
        else:
            conf.set("field-properties", "up_func_arg", 0)

        if(len(self.ui.lineEdit_11.text())>0):
            try1 = self.ui.lineEdit_11.text()
            try:
                result =try1.replace("x",'1')
                result = eval(result)
            except:
                result = eval(try1)

            conf.set("field-properties", "right_func_arg", int(coordinate_size_X-1))
        else:
            conf.set("field-properties", "right_func_arg", int(coordinate_size_X))

        if(len(self.ui.lineEdit_12.text())>0):
            try1 = self.ui.lineEdit_12.text()
            try:
                result =try1.replace("x",'1')
                result = eval(result)
            except:
                result = eval(try1)

            conf.set("field-properties", "bottom_func_arg", int(coordinate_size_Y-1))
        else:
            conf.set("field-properties", "bottom_func_arg", int(coordinate_size_Y))

        try:
            cycle_limit = int(self.ui.lineEdit_9.text())
            conf.set("main", "max_number_of_cycles", cycle_limit)
        except:
            conf.set("main", "max_number_of_cycles", -1)
            temperature_limit = float(self.ui.lineEdit_3.text())
            conf.set("main", "temperature_limit", temperature_limit)
        try:
            temperature_limit = float(self.ui.lineEdit_3.text())
            conf.set("main", "temperature_limit", temperature_limit)
        except:
            conf.set("main", "temperature_limit", -275)

        conf.set("field-properties", "width", int(coordinate_size_X))
        conf.set("field-properties", "height", int(coordinate_size_Y))

        conf.set("main", "delta_x", step_in_X)
        conf.set("main", "delta_t", step_in_time)
        conf.set("main", "delta_y", step_in_Y)
        conf.set("main", "specific_heat_capacity", heat_capacity)
        conf.set("main", "density", density)
        conf.set("main", "thermal_conduction", thermal_conduction)
        with open("config.conf", "w") as config:
            conf.write(config)

        conf = configparser.RawConfigParser()
        conf.read("interface_additional.conf")
        left_function = self.ui.lineEdit_10.text()
        top_function = self.ui.lineEdit_13.text()
        right_function = self.ui.lineEdit_11.text()
        bottom_function = self.ui.lineEdit_12.text()
        x_list = self.ui.textEdit.toPlainText()
        y_list = self.ui.textEdit_2.toPlainText()
        temperature_list = self.ui.textEdit_3.toPlainText()
        standart_temperature_to_SAVE = self.ui.lineEdit_7.text()

        conf.set("main", "standart", standart_temperature_to_SAVE)
        conf.set("main", "x", x_list)
        conf.set("main", "y", y_list)
        conf.set("main", "temperature", temperature_list)
        conf.set("main", "left", left_function)
        conf.set("main", "top", top_function)
        conf.set("main", "right", right_function)
        conf.set("main", "bottom", bottom_function)

        with open("interface_additional.conf", "w") as config:
            conf.write(config)

    def restore(self):
        config_object = ConfigParser()
        config_object.read("config.conf")
        userinfo = config_object["main"]
        self.ui.lineEdit_5.setText(userinfo["delta_x"])
        self.ui.lineEdit_6.setText(userinfo["delta_y"])
        self.ui.lineEdit_4.setText(userinfo["delta_t"])
        self.ui.lineEdit_15.setText(userinfo["density"])
        self.ui.lineEdit_3.setText(userinfo["temperature_limit"])
        self.ui.lineEdit_14.setText(userinfo["thermal_conduction"])
        self.ui.lineEdit_9.setText(userinfo["max_number_of_cycles"])
        self.ui.lineEdit_8.setText(userinfo["specific_heat_capacity"])
        userinfo = config_object["field-properties"]
        self.ui.lineEdit.setText(userinfo["width"])
        self.ui.lineEdit_2.setText(userinfo["height"])
        config_object = ConfigParser()
        config_object.read("interface_additional.conf")
        userinfo = config_object["main"]
        self.ui.lineEdit_7.setText(userinfo["standart"])
        self.ui.textEdit.setText(userinfo["x"])
        self.ui.textEdit_2.setText(userinfo["y"])
        self.ui.lineEdit_10.setText(userinfo["left"])
        self.ui.textEdit_3.setText(userinfo["temperature"])
        self.ui.lineEdit_13.setText(userinfo["top"])
        self.ui.lineEdit_11.setText(userinfo["right"])
        self.ui.lineEdit_12.setText(userinfo["bottom"])
        
    def bp(self):
        global conf
        shutil.rmtree('images')
        os.mkdir("images")
        if(self.check("ERROR") == 1):
            return 0
        try:
            x_list = (self.ui.textEdit.toPlainText()).split("\n")
            y_list = (self.ui.textEdit_2.toPlainText()).split("\n")
            temperature_list = (self.ui.textEdit_3.toPlainText()).split("\n")
        except:
            pass
        try:
            coordinate_size_X = float(self.ui.lineEdit.text())
            coordinate_size_Y = float(self.ui.lineEdit_2.text())
            
            step_in_time = float(self.ui.lineEdit_4.text())
            step_in_X = float(self.ui.lineEdit_5.text())
            step_in_Y = float(self.ui.lineEdit_6.text())
            standart_temperature = float(self.ui.lineEdit_7.text())
            heat_capacity = float(self.ui.lineEdit_8.text())
            density = float(self.ui.lineEdit_15.text())
            thermal_conduction = float(self.ui.lineEdit_14.text())
            

            conf = configparser.RawConfigParser()
            conf.read("config.conf")

            if(len(self.ui.lineEdit_10.text())>0):
                try1 = self.ui.lineEdit_10.text()
                try:
                    result =try1.replace("x",'1')
                    result = eval(result)
                except:
                    result = eval(try1)

                conf.set("field-properties", "left_func_arg", 1)
            else:
                conf.set("field-properties", "left_func_arg", 0)

            if(len(self.ui.lineEdit_13.text())>0):
                try1 = self.ui.lineEdit_13.text()
                try:
                    result =try1.replace("x",'1')
                    result = eval(result)
                except:
                    result = eval(try1)

                conf.set("field-properties", "up_func_arg", 1)
            else:
                conf.set("field-properties", "up_func_arg", 0)

            if(len(self.ui.lineEdit_11.text())>0):
                try1 = self.ui.lineEdit_11.text()
                try:
                    result =try1.replace("x",'1')
                    result = eval(result)
                except:
                    result = eval(try1)

                conf.set("field-properties", "right_func_arg", int(coordinate_size_X-1))
            else:
                conf.set("field-properties", "right_func_arg", int(coordinate_size_X))

            if(len(self.ui.lineEdit_12.text())>0):
                try1 = self.ui.lineEdit_12.text()
                try:
                    result =try1.replace("x",'1')
                    result = eval(result)
                except:
                    result = eval(try1)

                conf.set("field-properties", "bottom_func_arg", int(coordinate_size_Y-1))
            else:
                conf.set("field-properties", "bottom_func_arg", int(coordinate_size_Y))






            try:
                cycle_limit = int(self.ui.lineEdit_9.text())
                conf.set("main", "max_number_of_cycles", cycle_limit)
            except:
                conf.set("main", "max_number_of_cycles", -1)
                temperature_limit = float(self.ui.lineEdit_3.text())
                conf.set("main", "temperature_limit", temperature_limit)
            try:
                temperature_limit = float(self.ui.lineEdit_3.text())
                conf.set("main", "temperature_limit", temperature_limit)
            except:
                conf.set("main", "temperature_limit", -275)

            conf.set("field-properties", "width", int(coordinate_size_X))
            conf.set("field-properties", "height", int(coordinate_size_Y))

            conf.set("main", "delta_x", step_in_X)
            conf.set("main", "delta_t", step_in_time)
            conf.set("main", "delta_y", step_in_Y)
            conf.set("main", "specific_heat_capacity", heat_capacity)
            conf.set("main", "density", density)
            conf.set("main", "thermal_conduction", thermal_conduction)


            with open("config.conf", "w") as config:
                conf.write(config)

            coordinate_size_Y+=1
            matrix = []
            for i in range(0,int(coordinate_size_Y)):
                matrix.append([])
            for i in range(0,int(coordinate_size_Y)):
                for j in range(0,int(coordinate_size_X)):
                    matrix[i].append(standart_temperature)

            try:
                for i in range(0,len(x_list)):
                    if(y_list[i][0]==">"):

                        for x in range(0,int(coordinate_size_X)):
                            try:
                                x_string = x_list[i].replace("x",str(x))
                            except:
                                x_string = x_list[i]
                            try:
                                temperature = temperature_list[i].replace("x",eval(str(x_string)))
                            except:
                                temperature = temperature_list[i]

                            for y in range(0,int(coordinate_size_Y)):
                                if(eval(y_list[i][1::].replace("x",str(eval(x_string)))) <= y-1):
                                    matrix[y][x] = eval(temperature)
                    elif(y_list[i][0]=="<"):
                        for x in range(0,int(coordinate_size_X)):
                            try:
                                x_string = x_list[i].replace("x",str(x))
                            except:
                                x_string = x_list[i]
                            try:
                                temperature = temperature_list[i].replace("x",eval(str(x_string)))
                            except:
                                temperature = temperature_list[i]
                            for y in range(0,int(coordinate_size_Y)):
                                if(eval(y_list[i][1::].replace("x",str(eval(x_string)))) >= y-1):
                                    matrix[y][x] = eval(temperature)
                    else:
                        for x in range(0,int(coordinate_size_X)):
                            try:
                                x_string = x_list[i].replace("x",str(x))
                            except:
                                x_string = x_list[i]
                            try:
                                temperature = temperature_list[i].replace("x",eval(str(x_string)))
                            except:
                                temperature = temperature_list[i]
                            for y in range(0,int(coordinate_size_Y)):
                                if(eval(y_list[i][1::].replace("x",str(eval(x_string)))) == y):
                                    matrix[y][x] = eval(temperature)
            except:
                pass
            try:
                border_function = self.ui.lineEdit_10.text()
                for i in range(int(coordinate_size_Y)):
                    try:
                        result =border_function.replace("x",str(i))
                    except:
                        result = border_function
                    matrix[i][0] = int(eval(result))
            except:
                pass
            

            try:
                border_function = self.ui.lineEdit_11.text()
                for i in range(int(coordinate_size_Y)):
                    try:
                        result =border_function.replace("x",str(i))
                    except:
                        result = border_function
                    matrix[i][int(coordinate_size_X-1)] = int(eval(result))
            except:
                pass

            try:
                border_function = self.ui.lineEdit_13.text()
                for i in range(int(coordinate_size_X)):
                    try:
                        result =border_function.replace("x",str(i))
                    except:
                        result = border_function
                    matrix[int(coordinate_size_Y-1)][i] = int(eval(result))
            except:
                pass

            try:
                border_function = self.ui.lineEdit_12.text()
                for i in range(int(coordinate_size_X)):
                    try:
                        result =border_function.replace("x",str(i))
                    except:
                        result = border_function
                    matrix[1][i] = int(eval(result))
            except:
                pass

            matrix_file = open("input.txt", "w")

            if(self.ui.checkBox.isChecked()):
                for j in range(0,int(coordinate_size_X)):
                    for i in range(1,int(coordinate_size_Y)):
                        matrix_file.write(str(float(matrix[i][j]))+" ")
                    matrix_file.write("\n")
            else:
                for i in range(int(coordinate_size_Y-1),0,-1):
                    for j in range(0,int(coordinate_size_X)):
                        matrix_file.write(str(float(matrix[i][j]))+" ")
                    matrix_file.write("\n")
            matrix_file.close()
            

            if(self.ui.spinBox.value()>1):
                os.system("mpirun -np "+str(self.ui.spinBox.value())+" ./bin/thermal_conductivity")
            elif(self.ui.spinBox.value()==1):
                os.system("./bin/thermal_conductivity_1_thread")
            im_number=0
            while(os.path.exists("images/zEND.png") != True):
                if(os.path.exists(str("images/im"+str(im_number)+".png"))):
                    self.ui.label_24.setPixmap(QPixmap(str("images/im"+str(im_number)+".png")))  
                    im_number = im_number+1
                
            self.ui.label_24.setPixmap(QPixmap(str("images/"+str('zEND')+".png")))
            onlyfiles = next(os.walk("images"))[2] #dir is your directory path as string
            len_of = len(onlyfiles)-1
            frames = []
            for i in range(100):
                path ="images/im"+str(int(i*(len_of/100)))+".png"
                frames.append(Image.open(path))
            frames.append(Image.open("images/zEND.png"))
            frames[0].save('result.gif', format='GIF',
                append_images=frames[1:],
                save_all=True,
                duration=30, loop=0)
        except:
            if(self.ui.spinBox.value()>1):
                os.system("mpirun -np "+str(self.ui.spinBox.value())+" ./bin/thermal_conductivity")
            elif(self.ui.spinBox.value()==1):
                os.system("./bin/thermal_conductivity_1_thread")
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    matrix_file.close()