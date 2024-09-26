#!/usr/bin/python
import os
import math

'''Read POSCAR file'''
f = open('POSCAR')
elements = f.readlines()[5].split()
f.close()

''' The path of POTCAR files'''
potdir="/gpfs/share/home/2001111761/vasp/potential/pbe/"

if os.path.isfile("./POTCAR"):
        os.system('rm POTCAR')

cmd="zcat "
for i in range(len(elements)):
        cmd=cmd+potdir+elements[i]+"/POTCAR "
cmd=cmd+">POTCAR"
os.system(cmd)

os.system("grep VR POTCAR > VR")
os.system("cat VR")
