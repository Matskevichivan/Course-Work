import sys
import numpy as np
import manipulator as mn
import Manipulator_app as M_app
from PyQt5 import QtWidgets, QtGui, QtCore

def Solution():

    x = np.array([5, 4.3])
    y = np.array([-5.6, -1.2])
    psi = np.radians(np.array([0,90]))
    V = 0.7
    A = 6.5
    T = mn.Time(x, y, V, A)

    L1 = 6
    L2 = 4

    X, Y, PSI = mn.Array_parameters(x, y, psi)
    Qr1, Qr2, Qr3 = mn.ozk(X, Y, L1, L2, PSI)
    x1, y1, x2, y2 = mn.pzk(L1, L2, Qr1, Qr2)

    return x, y, X, Y, PSI, T, Qr1, Qr2, Qr3, x1, y1, x2, y2, L1, L2

class MainWindow(QtWidgets.QMainWindow, M_app.Ui_MainWindow):
    
    def __init__(self, callback):
        super().__init__()
        
        x, y, X, Y, PSI, T, Qr1, Qr2, Qr3, x1, y1, x2, y2, L1, L2 = callback()

        self.T = T
        self.X = X
        self.Y = Y
        self.L1 = L1
        self.L2 = L2
        self.Qr1 = Qr1
        self.Qr2 = Qr2
        self.Qr3 = Qr3
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.PSI = PSI
        self.x = x
        self.y = y
        self.home() 
    
    def home(self):
        self.setupUi(self)
        self.Velosity_plot_btn.clicked.connect(self.Velosity_plot)
        self.Axeleration_plot_btn.clicked.connect(self.Axeleration_plot)
        self.Moving_plot_btn.clicked.connect(self.Moving_plot)
        self.Trajectory_plot_btn.clicked.connect(self.Manipulator_plot)
        self.Close_btn.clicked.connect(sys.exit)
        self.show()       

    def Velosity_plot(self):
        
        Qr1_, Qr_2, Qr_3 = mn.diff_1_interp(self.Qr1, self.Qr2, self.Qr3, self.T)     
        
        return mn.Plot(Qr1_, Qr_2, Qr_3, self.T, 
                         legend=['Q1\'(t)', 'Q2\'(t)', 'Q3\'(t)'], 
                         title='График угловой скорости')

    def Axeleration_plot(self):
        
        _Qr_1,_Qr_2,_Qr_3 = mn.diff_2_interp(self.Qr1, self.Qr2, self.Qr3, self.T)     
        
        return mn.Plot(_Qr_1,_Qr_2,_Qr_3, self.T, 
                         legend=['Q1\"(t)', 'Q2\"(t)', 'Q3\"(t)'], 
                         title='График углового ускорения')

    def Moving_plot(self):     
        return mn.Plot(self.Qr1, self.Qr2, self.Qr3, self.T, 
                         legend=['Q1(t)', 'Q2(t)', 'Q3(t)'], 
                         title='График углового перемещения')

    def Manipulator_plot(self):     
        return mn.Plot_trajectory(self.x1, self.y1, 
                                    self.x2, self.y2)
  
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(Solution)
    window.show()
    app.exec_()
    
if __name__ == '__main__':
    main()
