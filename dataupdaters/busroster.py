from wonderwords import RandomWord
import random as r
from useful import export
import os

title = ["inc.", "corp.", "LLC", "international","labs","industries", "co.", "communications", "solutions", "technologies",
             "group","transportations", "consulting", "foods", "services", "firm", "farms", "insurance", "supermarket", "construction",
             "bank", "communities", "management", "investments", "entertainment", "clothing", "pharmaceuticals"]

R = RandomWord()
odata = [["Company Name", "Company Price"]]
for i in range(100):
    a = R.word(include_parts_of_speech=["nouns"])
    b = R.word(include_parts_of_speech=["adjectives"])
    compna = b + ' ' + a + " " + r.choice(title)
    price = round(r.uniform(0.01, 5000),2)
    odata.append([compna, price])
export(os.path.split(os.getcwd())[:-1][0] + r"\market\market.csv", odata)
