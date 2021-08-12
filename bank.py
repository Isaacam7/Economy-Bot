import pandas as pd
import useful
import os
roster = r"Bank\balance_data.csv"

def balance(userid):
    userid = int(userid)
    users = useful.load(roster)
    nusers = []

    for i in range(len(users)):
        nusers.append((users[i][0]))

    if str(userid) in nusers:
        pass
    elif str(userid) not in nusers:
        users.append([userid, 1000])
        useful.export(roster, users)

    Bdata = pd.read_csv(roster)
    userbal = Bdata.loc[Bdata['userid'] == userid]

    return round(float(userbal['balance']),2)

def checkbalance(userid):
    userid = int(userid)
    users = useful.load(roster)
    nusers = []
    for i in range(len(users)):
        nusers.append((users[i][0]))

    if str(userid) in nusers:
        Bdata = pd.read_csv(roster)
        userbal = Bdata.loc[Bdata['userid'] == userid]
        return round(float(userbal['balance']),2)
    elif str(userid) not in nusers:
        return f"<@!{userid}> HAS NOT REGISTERED YET"

def check(userid):
    users = useful.load(roster)
    nusers = []
    for i in range(len(users)):
        nusers.append((users[i][0]))

    if str(userid) in nusers:
        pass
    elif userid not in nusers:
        users.append([userid, 1000])
        useful.export(roster, users)
