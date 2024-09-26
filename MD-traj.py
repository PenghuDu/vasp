#!/usr/bin/env python
#-*- coding:utf-8 -*-
# funtion: extract move trajectory of No.* atom from AIMD; Input files: XDATCAR; Output files: traj_*.dat
# usage: python3 MD-traj.py
# edited by Dupenghu 20210730

import numpy as np
n=int(input("Input atom No. which you want to extract its trajectory:\n"))
Mnum=int(input("Input the MD steps in your VASP AIMD calculation:\n"))

a=open("XDATCAR",'r+')
b=open("traj_{}.dat".format(n),'w+')
#skip line1-2
for i in range(2): 
 a.readline() 

#get vectors
X=a.readline().strip().split()
Y=a.readline().strip().split()
Z=a.readline().strip().split()
X=[float(X[i]) for i in range(3)]
Y=[float(Y[i]) for i in range(3)]
Z=[float(Z[i]) for i in range(3)]
#skip line-6
a.readline()

#get total atom number
num=a.readline().strip().split()
num=[int(num[i]) for i in range(len(num))]
num=sum(num)


#get atomic direct coordinates of one step
def traj(n):
 a.readline() #skip the line "Direct configuration="
 coord=[]
 for i in range(num):
   r=a.readline().strip().split() 
   r=[float(r[i]) for i in range(3)]
   coord.append(r)
 coord_direct=coord[n]
 return coord_direct

for j in range(Mnum):
 coord_direct=traj(n-1) #get atomic direct coordinates of each step 
 coord_cart=[coord_direct[0]*X[i]+coord_direct[1]*Y[i]+coord_direct[2]*Z[i]  for i in range(3)] #get atomic Cartesian coordinates of each step 
 b.write(str(coord_cart[0])+"\t"+str(coord_cart[1])+"\t"+str(coord_cart[2])+"\n")
 
