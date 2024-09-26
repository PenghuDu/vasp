#!/usr/bin/env python
#-*- coding:utf-8 -*-
#funtion: plot bond between two atoms vs. time curve. 
#usage: python plot_bond.py
#edition: Dupenghu 2022.1.19

xlab="Time steps"
ylab="Bond-length  "+r'$\AA$'
fs=15
fz=[8,4]
fn="bond.dat"
savefn="bond.png"
import matplotlib.pyplot as plt
plt.rcParams['font.family']=['Times New Roman']
file=open(fn,'r+')
lines=file.readlines()
x=[i for i in range(1,10001)]
y1=[float(lines[i].strip().split()[0])for i in range(len(lines))]
fig=plt.figure(figsize=fz)
ax=plt.subplot(111)
ax.plot(x,y1,label=ylab,color='red')
#ax.legend()
plt.ylabel(ylab, fontsize = fs)
plt.xlabel(xlab, fontsize = fs)
plt.savefig(savefn,format='png',bbox_inches='tight',  dpi=300)‘
plt.show()
