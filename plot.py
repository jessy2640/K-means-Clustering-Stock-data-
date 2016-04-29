# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 09:13:41 2016

@author: vinay
"""
import csv
import time 
import datetime

import numpy as np
import matplotlib.pyplot as plt


x = []
y = []

cr = csv.reader(open("GOOGL.csv","rt"))
toggle = 0
for row in cr:
    if toggle != 0:                
        change = ((float(row[4]) - float(row[1]))/float(row[1]))*100        
        #time.mktime returns a floating point value by accepting a time tuple
        #class datetime.datetime :A combination of a date and a time. Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.                  
        time2 = time.mktime(datetime.datetime.strptime(row[0], "%m/%d/%Y").timetuple())                        
        x.append(time2)
        y.append(change)        
    toggle += 1


# Generate scatter plot of dataset
s = np.pi * (1 * 2)**2
plt.scatter(x, y, s=s, c=x, alpha=0.5)
plt.show()