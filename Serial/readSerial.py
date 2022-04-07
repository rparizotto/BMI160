#https://projects.raspberrypi.org/en/projects/nix-python-reading-serial-data

import serial
import numpy as np
import time
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.cos(x)

plt.ion()

#figure, ax = plt.subplots(figsize=(8,6))
#line1, = ax.plot(x, y)

fig = plt.figure(figsize=(12,6), facecolor='#DEDEDE')
ax0 = plt.subplot(121)
ax1 = plt.subplot(122)

plt.title("Dynamic Plot of sinx",fontsize=25)

plt.xlabel("X",fontsize=18)
plt.ylabel("sinX",fontsize=18)

plt.autoscale()

ser = serial.Serial('/dev/ttyUSB1', baudrate=115200)

xlist0 = []
ylist0 = []
xlist1 = []
ylist1 = []

plotStarted = False

def update_plot():
    ax0.set_facecolor('#DEDEDE')
    ax1.set_facecolor('#DEDEDE')
    ax0.cla()
    ax1.cla()
    ax0.plot(xlist0, ylist0)
    ax1.plot(xlist1, ylist1)
    #line1, = ax.plot(xlist, ylist)
    #line1.set_xdata(xlist)
    #line1.set_ydata(ylist)    
    plt.autoscale(True)
    fig.canvas.draw()    
    fig.canvas.flush_events()
    #time.sleep(0.1)

#started = False
xinit = 0
i = 0

def update_values(s):
    global xinit
    values = s.split(':')[1]
    values = values.replace('\n','').replace('\r', '')
    sx, sy = values.split(",")        
    x, y = float(sx), float(sy)
    if xinit == 0:
        xinit = x
    x = x - xinit
    if s.startswith('Data$0'):
        xlist = xlist0
        ylist = ylist0
    if s.startswith('Data$1'):
        xlist = xlist1
        ylist = ylist1        
    if len(xlist) >= 1000:
        xlist.pop(0)
        ylist.pop(0)
    xlist.append(x)
    ylist.append(y)

while True:
    s = ser.readline().decode()
    #if i < 10:
    #    print(s)
    if s.startswith('Data$'):
        update_values(s)
    i = i + 1
    #print(i)
    if i%10 == 0:
        update_plot()
        print(s)
        #print((x,y))
        #print(len(xlist))
        #print((xlist,ylist))
