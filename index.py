from PyQt5 import QtWidgets, uic
import pickle
import numpy as np
import sys
from PyQt5.QtWidgets import QMessageBox

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.btn.clicked.connect(lambda: self.button_click())
        self.show()

    def button_click(self):
        age=float(self.text1.text())
        
        Gender= self.text2.text()
        
        if Gender == "male" :
            Gender = 1
        elif Gender == "female"  :
            Gender = 0
        
        Total_Bilirubin = float(self.text3.text())
        Direct_Bilirubin = float(self.text4.text())
        Alkaline_Phosphotase = float(self.text5.text())
        Alamine_Aminotransferase = float(self.text6.text())
        Aspartate_Aminotransferase = float(self.text7.text())
        Total_Protiens = float(self.text8.text())
        Albumin = float(self.text9.text())
        Albumin_and_Globulin_Ratio = float(self.text10.text())

        clf = pickle.load(open(r"F:\python ml\projects\Liver Disease\liversavemo.pkl","rb"))
        test = np.array([[age,   Gender ,Total_Bilirubin,    Direct_Bilirubin ,   Alkaline_Phosphotase ,   Alamine_Aminotransferase,    Aspartate_Aminotransferase,   Total_Protiens, Albumin,Albumin_and_Globulin_Ratio ]])
        predicition = clf.predict(test)

        if predicition == 1:
            QMessageBox.about(self, "Title", "you are diganosed with liver deise")
           
        elif predicition==2:
            QMessageBox.about(self, "Title", "you are fine")
            
            




        














app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

 

