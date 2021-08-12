import csv
import useful
import pandas as pd
import os

def inv(userid):
    userid = int(userid)
    filepath = rf"portfolios\{userid}" + ".csv"
    try:
        data = useful.load(filepath)
        for i in range(len(data)):
            data[i].append(i - 1)
        return data
    except:
        with open(filepath, "w", newline='') as file:
            writer = csv.writer(file)
            row = ["Name", "Change", "Price"]
            writer.writerow(row)
            data = useful.load(filepath)
            return data

def buy(index,userid):
    #set index and userid
    index = int(index)
    userid = int(userid)

    # check if index is indexed correctly
    if index < 0:
        return "Cannot have index less than 0"

    #Load list of businesses balance of all users and users portfolio
    smark = pd.read_csv(r"market\market.csv")

    bald = pd.read_csv(r"Bank\balance_data.csv")
    bald = bald.set_index('userid')

    upor = useful.load(rf"portfolios\{userid}" + ".csv")

    #store the users balance
    userbal = float(bald.loc[userid,'balance'])

    #select the selected company
    comp = smark.iloc[[index]]
    comppri = float(comp['Company Price'])
    compna = str(comp.loc[index,'Company Name'])

    #check if user can actually buy the company
    if comppri > userbal:
        return "Not enough money"

    #update users portfolio
    upor.append([compna, '0%',comppri])

    #update users balance
    bald.loc[userid, 'balance'] = userbal - comppri

    #update market
    smark = smark.drop([index])

    #update all csvs
    smark.to_csv(r"market\market.csv",index=False)
    bald.to_csv(r"Bank\balance_data.csv")
    useful.export(rf"portfolios\{userid}" + ".csv",upor)

    return(f"<@!{userid}> just bought {compna} for ${comppri}")

def sell(index, userid):
    index = int(index)
    userid = int(userid)
    if index < 0:
        return "Cannot have index less than 0"

    bald = pd.read_csv(r"Bank\balance_data.csv")
    bald = bald.set_index('userid')

    upor = pd.read_csv(rf"portfolios\{userid}" + ".csv")
    userbal = float(bald.loc[userid, 'balance'])

    comppri = float(upor.loc[index,'Price'])
    compna = str(upor.loc[index, 'Name'])

    bald.loc[userid, 'balance'] = userbal + comppri
    upor = upor.drop([index])

    bald.to_csv(r"Bank\balance_data.csv")
    upor.to_csv(rf"portfolios\{userid}" + ".csv",index=False)

    return (f"<@!{userid}> just sold {compna} for ${comppri}")