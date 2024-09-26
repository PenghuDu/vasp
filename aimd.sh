#!/usr/bin/sh
## Function: post-processing of AIMD, extract Pair correlation function (PCF), Energy, Temperature, 
## Usage: bash aimd.sh
## edition: PenghuDu, 2022.1.19

## extract Energy and Temperature from OSZICAR file or OUTCAR file
grep T= OSZICAR|awk '{print $1"\t", $3"\t", $7"\t", $9"\t", $11}' > temp_energy.dat
#grep "free energy" OUTCAR | awk '{print $5}' > energy.dat

## extract PCF from PCDAT file
awk < PCDAT > PCF.dat ' NR==8 {pcskal=$1} NR==9 {pcfein=$1} NR>=13 {line=line+1; print (line-0.5)*pcfein/pcskal,$1} '


