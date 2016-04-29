from __future__ import division
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:31:13 2016

@author: vinay
"""

#import sys for exceptions
import sys
import math
import csv
import time 
import datetime

import numpy as np
import matplotlib.pyplot as plt

class Create_list:
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def get_coord(self):
		return self.x,self.y
		
	def set_x(self,x):
		self.x=x
	
	def set_y(self,y):
		self.y=y	
		
		
	def get_x(self):
		return self.x
	
	def get_y(self):
		return self.y
		
	def set_cluster(self, clusterNumber):
		self.clusterNumber = clusterNumber
    
	def get_cluster(self):
		return self.clusterNumber	
		

def calc_distance(valueX,valueY,centroidX,centroidY):
    return math.sqrt(math.pow((centroidX - valueX), 2) + math.pow((centroidY - valueY), 2))




value_set=[]
centroids=[]
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
        a=time2
        b=change
        value_set.append(Create_list(a,b))
    toggle += 1


no_of_pairs=len(value_set)
print (no_of_pairs)
no_of_cluster =int(input(" Enter no. of clusters to create : "))
print( " Choosing arbitary intial centroid values..")

for j in range(no_of_cluster):
	centroids.append(Create_list(value_set[j].get_x(),value_set[j].get_y()))
	
	

for k in range(no_of_cluster):
	print( " Centroid  ",(k+1)," : ",centroids[k].get_coord())

isShuffling=True;
passes=0
no_of_pass=1

while isShuffling:
#calculating distance of each pair from centroids and putting in clusters
	isShuffling=False
	for num in range(no_of_pairs):		
		if(no_of_pass==1):
			min_dist= calc_distance(value_set[num].get_x(),value_set[num].get_y(),centroids[0].get_x(),centroids[0].get_y())
			value_set[num].set_cluster((1))
			#print("first pass")
		else:
			#print("second pass")
			current_cluster=(value_set[num].get_cluster()-1)
			min_dist= calc_distance(value_set[num].get_x(),value_set[num].get_y(),centroids[current_cluster].get_x(),centroids[current_cluster].get_y())
			#print( "min_dist of : ",value_set[num].get_coord(),"with: ",centroids[current_cluster].get_coord()," is : ",min_dist

		
		for cluster in range(no_of_cluster):
			dist=calc_distance(value_set[num].get_x(),value_set[num].get_y(),centroids[cluster].get_x(),centroids[cluster].get_y())
			#print( "dist of : ",value_set[num].get_coord(),"with: ",centroids[cluster].get_coord()," is : ",dist
			if(dist<min_dist):
				#setting cluster number even if it's comparing dist with itself
				#print( "value of cluster set : ",cluster
				value_set[num].set_cluster((cluster+1))
				if(centroids[cluster].get_coord()!= value_set[num].get_coord()):
					#print( "min dist :",min_dist
					#print( "dist of : ",value_set[num].get_coord(),"with: ",centroids[cluster].get_coord()," is : ",dist
					#print( "I'm in"
					isShuffling=True
	no_of_pass=no_of_pass+1
				
			
		
	
#print( "",value_set[num].get_cluster()		

#print(ing clusters:

	
	for cluster in range(no_of_cluster):
		centroids[cluster].set_y(0)
		centroids[cluster].set_x(0)
		#print( " print(ing cluster ",(cluster+1)," : ")
		num_of_elements=0;
		for num in range(no_of_pairs):
			if((cluster+1)==value_set[num].get_cluster()):
				
				#print( "  ",value_set[num].get_coord())
				#if(centroids[cluster].get_coord() != value_set[num].get_coord()):
				num_of_elements=num_of_elements+1
				#print( "num_of_elements :",num_of_elements)
				centroids[cluster].set_x(float(centroids[cluster].get_x()+value_set[num].get_x()))
				centroids[cluster].set_y(float(centroids[cluster].get_y()+value_set[num].get_y()))
				#print( "mean x: ",((centroids[cluster].get_x()+value_set[num].get_x())/num_of_elements)
				#print( "cluster x now :", centroids[cluster].get_x()
				#print( "cluster y now: ", centroids[cluster].get_y()
		#print( " centeroidX: ",centroids[cluster].get_x())
		#print( "centroidY:",centroids[cluster].get_y())
		
		centroids[cluster].set_x((centroids[cluster].get_x()/num_of_elements))
		centroids[cluster].set_y((centroids[cluster].get_y()/num_of_elements))
		#print( "Mean of cluster ",(cluster+1)," : ",centroids[cluster].get_coord())
	passes=passes+1
	#if(passes>3):
		#isShuffling=False
		
#print( "Done."	)



# Generate scatter plot of dataset
for num in range(no_of_pairs):
    if(value_set[num].get_cluster()==1):    
        s = np.pi * (1 * 2)**2
        plt.scatter(value_set[num].get_x(), value_set[num].get_y(), s=s, c='yellow', alpha=0.5)        
    elif(value_set[num].get_cluster()==2):
        s = np.pi * (1 * 2)**2
        plt.scatter(value_set[num].get_x(), value_set[num].get_y(), s=s, c='blue', alpha=0.5)    
    else:
        s = np.pi * (1 * 2)**2
        plt.scatter(value_set[num].get_x(), value_set[num].get_y(), s=s, c='red', alpha=0.5)
        
plt.show()        
        
        