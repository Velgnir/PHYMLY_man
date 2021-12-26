import sys
import os.path
import configparser
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtWidgets
from python_ui_interface import Ui_MainWindow
import os
import compiles
import webbrowser



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.bp)

    def bp(self):
        global conf
        x_list = (self.ui.textEdit.toPlainText()).split("\n")
        y_list = (self.ui.textEdit_2.toPlainText()).split("\n")
        temperature_list = (self.ui.textEdit_3.toPlainText()).split("\n")
        if (len(x_list)!=len(y_list) or len(x_list)!= len(temperature_list)):
            self.ui.label_15.setStyleSheet("color: rgba(255,0,0,255);")
        else:
            self.ui.label_15.setStyleSheet("color: rgba(255,0,0,0);")
        try:
            self.ui.label_10.setStyleSheet("color: rgba(255,0,0,0);")
            self.ui.label_11.setStyleSheet("color: rgba(255,0,0,0);")

            coordinate_size_X = float(self.ui.lineEdit.text())
            coordinate_size_Y = float(self.ui.lineEdit_2.text())
            
            step_in_time = float(self.ui.lineEdit_4.text())
            step_in_X = float(self.ui.lineEdit_5.text())
            step_in_Y = float(self.ui.lineEdit_6.text())
            standart_temperature = float(self.ui.lineEdit_7.text())
            heat_capacity = float(self.ui.lineEdit_8.text())
            

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


            with open("config.conf", "w") as config:
                conf.write(config)

            coordinate_size_Y+=1
            matrix = []
            for i in range(0,int(coordinate_size_Y)):
                matrix.append([])
            for i in range(0,int(coordinate_size_Y)):
                for j in range(0,int(coordinate_size_X)):
                    matrix[i].append(standart_temperature)

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
            
            try:
                border_function = self.ui.lineEdit_10.text()
                for i in range(int(coordinate_size_Y)):
                    try:
                        result =border_function.replace("x",str(i))
                        print(result) 
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
                    matrix[int(coordinate_size_X)][i] = int(eval(result))
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
            self.ui.label_11.setStyleSheet("color: rgba(255,0,0,0);")
            self.ui.label_10.setStyleSheet("color: rgba(255,0,0,0);")

            compiles.compiles()
 
        except:
            if(self.ui.lineEdit.text()=="" or self.ui.lineEdit_2.text()=="" or self.ui.lineEdit_3.text()=="" or self.ui.lineEdit_4.text()=="" or self.ui.lineEdit_5.text()=="" or self.ui.lineEdit_6.text()=="" or self.ui.lineEdit_7.text()=="" or self.ui.lineEdit_8.text()==""):
                self.ui.label_10.setStyleSheet("color: rgba(255,0,0,255);")
            else:
                self.ui.label_11.setStyleSheet("color: rgba(255,0,0,255);")
                self.ui.label_10.setStyleSheet("color: rgba(255,0,0,0);")


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    webbrowser.open("python_interface/how_to_use.txt")
    sys.exit(app.exec_())
    matrix_file.close()