from urllib import request
import pandas as pd
import numpy as np

doc_url = f"https://drive.google.com/uc?export=download&id=1M5xRW3tnUn-vOjBZrv_AHupNqvjIiK3A"
doc_name = "Bliss Calc.csv"
with request.urlopen(doc_url) as f:
    df = pd.read_csv(f)

def xpToRaw(pr, xp):
    rawxp = 0
    i = 0
    while i < pr:
        rawxp += 200000000 * 2 ** i
        i += 1
    rawxp += xp * 2 ** pr
    return rawxp

def calcAmount(skill, oldPrestige=0, oldExp=0, newPrestige=None, newExp = 200000000):
    skill = skill.capitalize()
    if skill in df.columns:
        if newPrestige==None:
            newPrestige = oldPrestige
        rawExpDiff = (xpToRaw(newPrestige, newExp) - xpToRaw(oldPrestige, oldExp))/76
        newdf = df[[skill, skill+" XP"]].dropna()
        newdf["Amount Needed"] = (rawExpDiff / newdf[skill+" XP"]).apply(np.ceil).astype(int)
        return newdf[[skill, "Amount Needed"]]
    else:
        print("Skill not in calculator")