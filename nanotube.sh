#!/bin/bash
## function: roll a nanoribbon to a nanotube; input: POSCAR_ribbon;
## usage: bash nanotube.sh > POSCAR_tube
## refer to: https://mp.weixin.qq.com/s/6WO5A8Qa-XDyAEM0AbQVhQ


L=`awk '{if(NR==3)print $1}' POSCAR_ribbon`

C=`awk '{if(NR==4)print $2}' POSCAR_ribbon`

echo "Nanotube" 

echo "1.0"

echo  "$L 0.0 0.0" 

echo  "0.0 $L  0.0" 

echo  "0.0 0.0  $C" 

awk '{if(NR>5&&NR<9)print $0; if(NR>8)print 1/6.283185 * cos(6.283185*$1)+0.5, 1/6.283185 * sin(6.283185*$1) + 0.5, $2}' POSCAR_ribbon