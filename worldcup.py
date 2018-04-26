import pandas as pd
import random
from random import choice
from random import randint
import numpy as np

def main():
    """
    This is the main function. We create a dataframe that has all the team statistics.
    """

    df = pd.read_csv('FifaRankings.csv', index_col="Ranking")
    a_set = set()
    while True:
        a_set.add(randint(42, 85))
        if len(a_set) == 32:
            break
    lst1 = sorted(list(a_set), reverse=True)

    a_set = set()
    while True:
        a_set.add(randint(38, 83))
        if len(a_set) == 32:
            break
    lst2 = sorted(list(a_set), reverse=True)
    print("\n")
    df['Attack'] = lst1
    df['Defence'] = lst2
    a = list(df["Team"])

    avgScored = 0
    avgConceded = 0
    avgScored = df['Attack'].sum()
    avgConceded = df['Defence'].sum()

    avgScored = avgScored / len(df)
    avgConceded = avgConceded / len(df)
    print("\n")
    avgattack = []
    avgdefense = []

    for i in range(1, 33):
        if df['Matches Played'][i] != 0:
            win_rate = (df['WorldCup Wins'][i] / df['Matches Played'][i])
        else:
            win_rate = 0
        avgattack.append((df['Attack'][i] / avgScored) + win_rate)
        avgdefense.append((df['Defence'][i] / avgConceded) + win_rate)

    df['Avg Attack'] = avgattack
    df['Avg Defense'] = avgdefense
    print("\n")
    print(df)
    print("\n")
    print("The draws for the GROUP STAGE are:\n", GroupDraws(a))

def GroupDraws(l : list):
    """
    This function computes Groupwise  random draws.
    :param l: list containing all the team names obtained from the data frame
    :return: dataframe that contains the randomized match draws
    """
    GroupA = []
    GroupB = []
    GroupC = []
    GroupD = []
    GroupE = []
    GroupF = []
    GroupG = []
    GroupH = []
    Groups = [GroupA, GroupB, GroupC, GroupD, GroupE, GroupF, GroupG, GroupH]
    for i in Groups:
        for j in range(4):
            teamname = choice(l)
            i.append(teamname)
            l.remove(teamname)

    print("\n")
    draws = pd.DataFrame(
        {'GROUP A': Groups[0],
         'GROUP B': Groups[1],
         'GROUP C': Groups[2],
         'GROUP D': Groups[3],
         'GROUP E': Groups[4],
         'GROUP F': Groups[5],
         'GROUP G': Groups[6],
         'GROUP H': Groups[7]
         })

    return draws

if __name__ == '__main__':
    main()
