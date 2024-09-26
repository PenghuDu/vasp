#!/usr/bin/env python
#-*- coding:utf-8 -*-
# funtion: extract bond angle between atoms No.(b1,b2,b3) from AIMD; Input files: XDATCAR; Output files: angle.dat
# usage: python3 MD-angle.py
# usage: python3 MD-angle.py
# edited by 丙丙de五线谱, Dupenghu 20210730

import math
b1=int(input("Input 1st atoms number bwtween which you want to calculate the bond:\n"))
b2=int(input("Input 2nd atoms number bwtween which you want to calculate the bond:\n"))
b3=int(input("Input 3rd atoms number bwtween which you want to calculate the bond:\n"))
Mnum=int(input("Input the MD steps in your VASP AIMD calculation:\n"))

b1=b1-1
b2=b2-1
b3=b3-1
a=open("XDATCAR",'r+')

b=open("angle_{}-{}-{}.dat".format(b1+1, b2+1, b3+1),'w+')
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

#define function of bond-angle
def angle(m,n,t):
 r=[m[i]-n[i] for i in range(3)]
 r2=[r[0]*X[i]+r[1]*Y[i]+r[2]*Z[i] for i in range(3)]
 r3=math.sqrt(r2[0]**2+r2[1]**2+r2[2]**2)
 
 rb=[t[i]-n[i] for i in range(3)]
 r2b=[rb[0]*X[i]+rb[1]*Y[i]+rb[2]*Z[i] for i in range(3)]
 r3b=math.sqrt(r2b[0]**2+r2b[1]**2+r2b[2]**2) 
 
 cos = (r2[0]*r2b[0] + r2[1]*r2b[1] + r2[2]*r2b[2])/(r3*r3b)
 angle = math.acos(cos)
 return angle/math.pi

#get bond-angle of each step
def bond_s(b1,b2,b3):
 a.readline() #skip the line "Direct configuration="
 coord=[]
 for i in range(num):
   r=a.readline().strip().split() 
   r=[float(r[i]) for i in range(3)]
   coord.append(r)
 C_chose=[coord[b1],coord[b2],coord[b3]]
 return C_chose

for j in range(Mnum):
 m,n,t =bond_s(b1,b2,b3)
 angles=angle(m,n,t)
 b.write(str(angles)+"\n")

 
