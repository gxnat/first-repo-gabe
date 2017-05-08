#Rotation Curve 1 V as a function of R
import matplotlib.pyplot as plt
from numpy import *
galaxy = raw_input("Enter File Name:") 
print "Galaxy:", galaxy
data = open(galaxy, 'r')

list1 = [] 
list2 = []
list3 = []
with open(galaxy) as inf:
    for line in inf:
        parts = line.split() 
        if len(parts) > 1:   
            list1.append(float(parts[1])) #filling list1 with R
            list2.append(float(parts[5])) #filling list2 with V
            list3.append(float(parts[6])) #filling list3 with error in y

plt.plot(list1, list2,'k.' ) #plots x, y, pointstyle
plt.errorbar(list1, list2, yerr=list3, linestyle='None', marker='None', color='black')
plt.xlabel('Radius (kpc)')
plt.ylabel('Velocity (km/s)')
plt.title(galaxy + ' Rotation Curve')
plt.grid(True)
plt.savefig('RotCurve1.png') #file is saved
plt.show() #plot is displayed

