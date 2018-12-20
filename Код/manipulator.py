import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

from scipy.interpolate import interp1d
from math import * 

def Array_parameters(x, y, psi, num=100):
    
    X   = np.linspace(x[0], x[1], num=num)
    Y   = np.linspace(y[0], y[1], num=num)
    PSI = np.linspace(psi[0], psi[1], num=num)
    
    return X, Y, PSI

def ozk(x,y,L1,L2,psi): 
    c2 = (x**2 + y**2 - L1**2- L2**2)/(2*L1*L2)
    s2 = np.sqrt(1 - c2**2)
    Qr2 = np.arctan2(s2,c2)
    Qr1 = np.arctan2(y,x) - np.arctan2(L2*s2,L1+L2*c2)
    Qr3 = psi - Qr1 - Qr2
    
    return Qr1, Qr2, Qr3

def pzk(L1,L2,Qr1, Qr2):
    x1 = L1 * np.cos(Qr1)
    y1 = L1 * np.sin(Qr1)

    x2 = x1 + L2 * np.cos(Qr1+Qr2)
    y2 = y1 + L2 * np.sin(Qr1+Qr2)

    return x1,y1,x2,y2

def interp(x,y,X):
    f = interp1d(x,y)
    Y_interp = f(X)
    return Y_interp

def diff_1_interp(Qr1, Qr2, Qr3, T):

    T_vector = np.linspace(0, T, len(Qr1))
    dt = np.ediff1d(T_vector)

    Qr_1 = np.ediff1d(Qr1)/dt
    Qr_2 = np.ediff1d(Qr2)/dt
    Qr_3 = np.ediff1d(Qr3)/dt
    return Qr_1,Qr_2,Qr_3

def diff_2_interp(Qr1, Qr2, Qr3, T):

    T_vector = np.linspace(0, T, len(Qr1))
    dt = np.ediff1d(T_vector)

    _Qr_1 = np.ediff1d((np.ediff1d(Qr1) / dt) / dt)
    _Qr_2 = np.ediff1d((np.ediff1d(Qr2) / dt) / dt)
    _Qr_3 = np.ediff1d((np.ediff1d(Qr3) / dt) / dt)                 
    return _Qr_1,_Qr_2,_Qr_3

def Plot_trajectory(x1, y1, x2, y2):

    fig = plt.figure()
    ax = fig.add_subplot(111, xlim=(0, 10), ylim=(-10, 0))
    ax.grid()

    line, = ax.plot([], [], 'o-', lw=2)
    line2, = ax.plot([], [], '-', lw=2)

    def init():
        line.set_data([], [])
        line2.set_data([], [])
        return line,line2

    def animate(i):
        thisx = [0, x1[i], x2[i]]
        thisy = [0, y1[i], y2[i]]

        line.set_data(thisx, thisy)
        line2.set_data(x2[:i],y2[:i])
        return line,line2

    ani = animation.FuncAnimation(fig, animate, frames= np.arange(1,len(x1)),
                                  interval=25, blit=True, init_func=init, repeat=False)
    plt.show()
    return ani  

def Plot(Qr1, Qr2, Qr3, T, legend=[], title=''):
    T = np.linspace(0, T, len(Qr1))

    fig = plt.figure()
    ax = fig.add_subplot(211, autoscale_on = True)
    ax.grid()
    
    f1, f2, f3 = ax.plot(T, Qr1,'-', T, Qr2, '--', T, Qr3, '-.', linewidth=2)
    
    ax.set_xlabel('Time(sec)')
    ax.set_ylabel('Radians')
    
    fig.legend((f1, f2, f3), (legend[0], legend[1], legend[2]), 'upper left')
    plt.title(title)
                         
    plt.show()

def Time(x, y, Speed, Axeleration):
    Distance = np.sqrt((x[1]-x[0])**2 + (y[1]-y[0])**2)
    T = Distance/Speed
    return T

