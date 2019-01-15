# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 08:49:39 2018

@author: Anudeep
"""

import ctypes

for i in range(2015, 2019):
    filetoopen = str(i) + ".csv"
    try:
        fh = open(filetoopen, 'r')
    except FileNotFoundError:
        pass

allr, kan = {}, {}

################## Reading the CSV
for i in fh:
    temp = []
    i = i[:-1].split(',')
    try:
        assert len(i[-2]) < 6 and len(i[-1]) < 6
    except:
        ctypes.windll.user32.MessageBoxW(0, i[1], "Error", 0)
    if "Kanpur" in i[1]:
        kan[i[1]] = [int(i[-2]), int(i[-1])]
    else:
        allr[i[1]] = [int(i[-2]), int(i[-1])]

################## Heart of Algo
totcomp = {}
for i in kan:
    opr, clr = kan[i][-2], kan[i][-1]
    sumc = 0
    for j in allr:
        tempor, tempcr = allr[j][-2], allr[j][-1]
        if ((tempor <= clr) and (tempor >= opr)) or ((tempcr >= opr) \
            and (tempor <= clr)):
            comp = ((min(clr, tempcr) - max(opr, tempor))/(clr-opr))
            comp *= ((tempor/tempcr)/(tempcr-tempor))
            sumc += comp
    totcomp[i] = sumc

################### Comparing outputs
# =============================================================================
# outcsv = open("allthecomps.csv", 'r')
# template = {}
# check = []
# for i in outcsv:
#     newline = i[:-1].split(',')
#     template[newline[0]] = float(newline[1])
#     check.append(round(totcomp[newline[0]], 12) == round(template[newline[0]], 12))
# 
# print(all(check))
# 
# outcsv.close()
# =============================================================================
    
################### Writing to CSV
outcsv = open("allthecomps.csv", 'w+')
outcsv.write("Branch" + ',' + "Comp" + ',' + "OR" + ',' + "CR" + ',' +\
             "Pref" + '\n')
for i in totcomp:
    opr = kan[i][-2]
    clr = kan[i][-1]
    pref = (opr/clr)/(clr - opr)
    outcsv.write(' '.join(i.split(' ')[5:]) + ',' + str(totcomp[i]) + ',' + str(kan[i][-2]) + ','\
                 + str(kan[i][-1]) + ',' + str(pref) + '\n')


outcsv.close()
fh.close()