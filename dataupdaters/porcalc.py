import random as r
import pandas as pd
import useful
import os

idlist = useful.load(r"C:\Users\Isaac\PycharmProjects\gcdiscordbot0\Bank\balance_data.csv")[1:]
for i in range(len(idlist)):
    idlist[i] = idlist[i][0]

portf = []
for i in range(len(idlist)):
    if len(useful.load(os.path.split(os.getcwd())[:-1][0] + rf"\portfolios\{idlist[i]}" + ".csv")[1:]) > 0:
        portf.append(useful.load(os.path.split(os.getcwd())[:-1][0] + rf"\portfolios\{idlist[i]}" + ".csv")[1:])

for i in range(len(portf)):
    portf[i].append(idlist[i])

for i in range(len(portf)):
    for j in range(len(portf[i]) - 1):
        m = round(r.uniform(-.9999, 1.00), 2)
        val = float(portf[i][j][2])
        portf[i][j][1] = f"{m * 100}%"
        portf[i][j][2] = (val* m) + val

for i in range(len(portf)):
    userid = portf[i][-1]
    odata = [['Name', 'Change', 'Price']]
    for j in range(len(portf[i]) - 1):
        odata.append(portf[i][j])
    useful.export(os.path.split(os.getcwd())[:-1][0] + rf"\portfolios\{userid}" + ".csv",odata)