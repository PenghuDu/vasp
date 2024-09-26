#!/opt/python/2.7.13.1/bin/python

import os
f = open('KPOINTS','r')
f.readline()
nktot = int(f.readline())
nkscf = 0
f.readline()
line = f.readline().split()
while line != []:
	line = [float(i) for i in line]
	if line[3] != 0:
		nkscf += 1
	line = f.readline().split()
f.close()
nkpoint = nktot - nkscf

f = open('KPOINTS.bak','r')
f.readline()
nk = int(f.readline())
f.readline()
f.readline()
line = f.readline().split()
line = [float(i) for i in line]
kx0 = line[0]
ky0 = line[1]
kz0 = line[2]
f.close()

Ef = float(os.popen('grep E-fermi OUTCAR').read().split()[2])
flag = False
latt = []
n = 0
b1 = [0,0,0]
b2 = [0,0,0]
b3 = [0,0,0]
for line in open('OUTCAR','r'):
	if flag and n > 0:
		n -= 1		
		latt.append(line)
	if flag and n == 0:
		break
	if 'reciprocal lattice vectors' in line:
		flag = True
		n = 3
for i in range(len(latt)):
	latt[i] = latt[i].split()
	for j in range(len(latt[i])):
		latt[i][j] = float(latt[i][j])
for i in range(3):
	b1[i] = latt[0][i+3]
	b2[i] = latt[1][i+3]
	b3[i] = latt[2][i+3]

f = open('EIGENVAL','r')
for i in range(6):
	line = f.readline()
nband = int(line.split()[2])

for i in range(nkscf):
	for j in range(nband+2):
		f.readline()
	
distance = []
eigen = []
kx = []
ky = []
kz = []
r = [0.0,0.0,0.0]
dis = 0
CBM = 100
VBM = -100
for i in range(nkpoint):
	f.readline()
	line = f.readline().split()
	line = [float(k) for k in line]
        kx.append(line[0])
        ky.append(line[1])
        kz.append(line[2])
	x = kx[i] - kx0
	y = ky[i] - ky0
	z = kz[i] - kz0
	r2 = 0
	for k in range(len(r)):
		r[k] = x*b1[k] + y*b2[k] + z*b3[k]
		r2 += r[k]**2
	abs_r = r2**0.5
	dis += abs_r
	kx0 = kx[i]
	ky0 = ky[i]
	kz0 = kz[i]
	distance.append(dis)
	eigen.append([])
	for j in range(nband):
		line = f.readline()
		energy = float(line.split()[1]) - Ef
		eigen[i].append(energy)
		if energy > 0 and energy < CBM:
			CBM = energy
		if energy < 0 and energy > VBM:
			VBM = energy
Gap = CBM - VBM
f.close()

fw = open('kpoint.dat','w')
print >>fw,"the transtion k points are:"
for i in range(len(distance)):
	if (i % (nk-1) == 0):
		print >>fw,'%-12.8f' %kx[i],'%-12.8f' %ky[i],'%-12.8f' %kz[i],'%-10.8f' %distance[i]
fw.close()

fw = open('eigen.dat','w')
for j in range(nband):
	for i in range(nkpoint):
		print >>fw,'%-10.8f' %distance[i],'%-12.8f' %eigen[i][j]
	print >>fw,1
fw.write('CBM is located at %5.2f' %CBM+' eV\n')
fw.write('VBM is located at %5.2f' %VBM+' eV\n')
fw.write('Gap is %4.2f' %Gap+' eV')
fw.close()

fw = open('eigen-sort.dat','w')
for i in range(nkpoint):
	print >>fw,'%-12.8f' %kx[i],'%-12.8f' %ky[i],'%-12.8f' %kz[i],'%-10.8f' %distance[i],
	for j in range(nband):
		print >>fw,'%-12.8f' %eigen[i][j],
	print >>fw,''
fw.close()
