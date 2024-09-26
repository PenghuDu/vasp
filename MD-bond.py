#!/usr/bin/env python
#-*- coding:utf-8 -*-
# funtion: extract bond length between atoms No.(b1,b2) from AIMD; Input files: XDATCAR; Output files: bond.dat
# usage: python3 MD-bond.py
# edited by 丙丙de五线谱, Dupenghu 20210730

import numpy as np
b1=int(input("Input 1st atoms bwtween which you want to calculate the bond:\n"))
b2=int(input("Input 2nd atoms bwtween which you want to calculate the bond:\n"))
Mnum=int(input("Input the MD steps in your VASP AIMD calculation:\n"))

b1=b1-1
b2=b2-1
a=open("XDATCAR",'r+')

b=open("bond_{}-{}.dat".format(b1+1, b2+1),'w+')
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

#define function of bond-length
def bond(m,n):
 r=[n[i]-m[i] for i in range(3)]
 r2=[r[0]*X[i]+r[1]*Y[i]+r[2]*Z[i] for i in range(3)]
 r3=np.sqrt(r2[0]**2+r2[1]**2+r2[2]**2) 
 return r3

#get bond-length of each step
def bond_s():
 a.readline() #skip the line "Direct configuration="
 coord=[]
 for i in range(num):
   r=a.readline().strip().split() 
   r=[float(r[i]) for i in range(3)]
   coord.append(r)
 C_chose=[coord[b1],coord[b2]]
 return C_chose

for j in range(Mnum):
 m,n=bond_s()
 r=bond(m,n)
 b.write(str(r)+"\n")
 
