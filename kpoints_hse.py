#!/opt/python/2.7.13.1/bin/python

import os
import copy

f0 = open('IBZKPT')
f1 = open('KPOINTS')
f2 = open('kpoints','w')
f3 = open('points','w')
f0.readline()
nk = int(f0.readline().strip())
f0.readline()
for i in range(nk):
	line = f0.readline().strip()
	print >>f3,line

f1.readline()
num = int(f1.readline().strip())
if num == 0:
	print 'Error in reading KPOINTS!\n'

weight = 0

f1.readline()
f1.readline()
p1 = f1.readline().split()
p2 = f1.readline().split()
if p1 != [] and p2 != []:
	p1 = [float(i) for i in p1]
	p2 = [float(i) for i in p2]
	step = [0.0,0.0,0.0]
	for i in range(len(step)):
		step[i] = (p2[i] - p1[i]) / (num - 1)
	for i in range(num):
		print >>f3,'%-10.6f %-10.6f %-10.6f %d' %(p1[0],p1[1],p1[2],weight)
		nk += 1
		for j in range(len(p1)):
			p1[j] += step[j]
	f1.readline()
	p1 = f1.readline().split()
	p2 = f1.readline().split()
while p1 != [] and p2 != []:
	p1 = [float(i) for i in p1]
	p2 = [float(i) for i in p2]
	step = [0.0,0.0,0.0]
	for i in range(len(step)):
		step[i] = (p2[i] - p1[i]) / (num - 1)
	for i in range(1,num):
		for j in range(len(p1)):
			p1[j] += step[j]
		print >>f3,'%-10.6f %-10.6f %-10.6f %d' %(p1[0],p1[1],p1[2],weight)
		nk += 1
	f1.readline()
	p1 = f1.readline().split()
	p2 = f1.readline().split()
print >>f2,'kpoints'
print >>f2,nk
print >>f2,'Reciprocal'

f0.close()
f1.close()
f2.close()
f3.close()
os.system('mv KPOINTS KPOINTS.bak')
os.system('cat < points >> kpoints')
os.system('mv kpoints KPOINTS')
os.system('rm -f points')
