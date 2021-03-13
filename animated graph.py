# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 15:02:21 2021

@author: Bright Ogunjobi
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

freq = array([4.040, 3.760, 3.600, 3.030, 2.560, 1.000])
voltage = array([-158.594, -120.000, -100.000, -50.000, -25.000, 0])

fig = plt.figure()
ax = plt.axes(xlim=200, ylim=200)
line = ax.plot(freq, voltage,lw = 2)

def init():
    line.set_data(freq, voltage)
    return line


def animate(x,y):
    arrange = {"Frequency(GHz)": x, "Voltage(V)": y}
    data = pd.DataFrame(arrange)
    print(data)
    
    
    plt.grid()

    plt.xlabel('Frequency(GHz)', fontsize=10)
    plt.ylabel('Voltage(V)',fontsize=10)
    plt.title('Frequency(GHz) versus Voltage(V).',fontsize=15, color = "blue")
    plt.yticks(color='green')
    plt.xticks(color='red')
    
    
    data.plot(x = "Frequency(GHz)", y= "Voltage(V)", kind = "line")
    
anim = animation.FuncAnimation(fig, animate, init_func = init, frames = 200, interval = 20, blit=True)


plt.show()



    