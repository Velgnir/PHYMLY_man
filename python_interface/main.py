import sys
import os.path
import configparser
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
        self.ui.pushButton.clicked.connect(self.bp)
        self.ui.pushButton_2.clicked.connect(self.watch)
    def watch(self):
        global conf
        try:
            x_list = (self.ui.textEdit.toPlainText()).split("\n")
            y_list = (self.ui.textEdit_2.toPlainText()).split("\n")
            temperature_list = (self.ui.textEdit_3.toPlainText()).split("\n")
        except:
            pass
        if (len(x_list)!=len(y_list) or len(x_list)!= len(temperature_list)):
            self.ui.label_15.setStyleSheet("color: rgba(255,0,0,255);")
        else:
            self.ui.label_15.setStyleSheet("color: rgba(255,0,0,0);")
        try:
            self.ui.label_10.setStyleSheet("color: rgba(255,0,0,0);")
            self.ui.label_11.setStyleSheet("color: rgba(255,0,0,0);")

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
                self.ui.label_24.setGeometry(QRect(810, int(170+(181 -181*(coordinate_size_Y/coordinate_size_X))/2), 181, int(181*(coordinate_size_Y/coordinate_size_X))))
                resized_image = original_image.resize((181, int(181*(coordinate_size_Y/coordinate_size_X))))
            elif(coordinate_size_Y>181 and coordinate_size_Y>=coordinate_size_X):
                self.ui.label_24.setGeometry(QRect(int(810+(181 -181*(coordinate_size_X/coordinate_size_Y))/2), 170, int(181*(coordinate_size_X/coordinate_size_Y)), 181))
                resized_image = original_image.resize((int(181*(coordinate_size_X/coordinate_size_Y)), 181))
            elif(coordinate_size_Y<=181 and coordinate_size_X<=181):
                self.ui.label_24.setGeometry(QRect(810+int((181-coordinate_size_X)/2), 170+int((181-coordinate_size_Y)/2), coordinate_size_X, coordinate_size_Y))
                resized_image = original_image.resize((coordinate_size_X, coordinate_size_Y))
            resized_image.save('python_interface/WATCH2.png')
            self.ui.label_26.setPixmap(QPixmap("python_interface/WATCH1.png"))

            self.ui.label_24.setPixmap(QPixmap("python_interface/WATCH2.png"))
            if(MAX_TEMPERATURE>0):
                self.ui.label_25.setText("-273" + " "+" "*int(85*(273/(MAX_TEMPERATURE+273))) +"0"+" "+" "*int(85-85*(273/(MAX_TEMPERATURE+273)))+str(MAX_TEMPERATURE))
            else:
                self.ui.label_25.setText("-273"+" "*87+str(MAX_TEMPERATURE))
            self.ui.label_11.setStyleSheet("color: rgba(255,0,0,0);")
            self.ui.label_10.setStyleSheet("color: rgba(255,0,0,0);")
        except:
            if(self.ui.lineEdit.text()=="" or self.ui.lineEdit_2.text()=="" or self.ui.lineEdit_7.text()==""):
                self.ui.label_10.setStyleSheet("color: rgba(255,0,0,255);")
            else:
                self.ui.label_11.setStyleSheet("color: rgba(255,0,0,255);")
                self.ui.label_10.setStyleSheet("color: rgba(255,0,0,0);")


    def bp(self):
        global conf
        shutil.rmtree('images')
        os.mkdir("images")
        self.watch()
        try:
            x_list = (self.ui.textEdit.toPlainText()).split("\n")
            y_list = (self.ui.textEdit_2.toPlainText()).split("\n")
            temperature_list = (self.ui.textEdit_3.toPlainText()).split("\n")
        except:
            pass
        if (len(x_list)!=len(y_list) or len(x_list)!= len(temperature_list)):
            self.ui.label_15.setStyleSheet("color: rgba(255,0,0,255);")
        else:
            self.ui.label_15.setStyleSheet("color: rgba(255,0,0,0);")
        try:
            self.watch()
            self.ui.label_10.setStyleSheet("color: rgba(255,0,0,0);")
            self.ui.label_11.setStyleSheet("color: rgba(255,0,0,0);")

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

            try:
                try1 = int(self.ui.lineEdit_10.text())
                conf.set("field-properties", "left_func_arg", 1)
            except:
                conf.set("field-properties", "left_func_arg", 0)

            try:
                try2 = int(self.ui.lineEdit_13.text())
                conf.set("field-properties", "up_func_arg", 1)
            except:
                conf.set("field-properties", "up_func_arg", 0)

            try:
                try3 = int(self.ui.lineEdit_11.text())
                conf.set("field-properties", "right_func_arg", int(coordinate_size_X-1))
            except:
                conf.set("field-properties", "right_func_arg", int(coordinate_size_X))

            try:
                try4 = int(self.ui.lineEdit_12.text())
                conf.set("field-properties", "bottom_func_arg", int(coordinate_size_Y-1))
            except:
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
            
            os.system("bin/thermal_conductivity &")
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

            self.ui.label_11.setStyleSheet("color: rgba(255,0,0,0);")
            self.ui.label_10.setStyleSheet("color: rgba(255,0,0,0);")
        except:
            if(self.ui.lineEdit_15.text()=="" or self.ui.lineEdit_14.text()=="" or self.ui.lineEdit.text()=="" or self.ui.lineEdit_2.text()=="" or (self.ui.lineEdit_9.text()=="" and self.ui.lineEdit_3.text()=="") or self.ui.lineEdit_4.text()=="" or self.ui.lineEdit_5.text()=="" or self.ui.lineEdit_6.text()=="" or self.ui.lineEdit_7.text()=="" or self.ui.lineEdit_8.text()==""):
                self.ui.label_10.setStyleSheet("color: rgba(255,0,0,255);")
            else:
                self.ui.label_11.setStyleSheet("color: rgba(255,0,0,255);")
                self.ui.label_10.setStyleSheet("color: rgba(255,0,0,0);")
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    matrix_file.close()