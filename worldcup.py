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
    Match(df)

def toss():
    """
        This function generates a random toss between the two teams playing a match. A toss is computed before every match.
        :param :
        :return: tuple that contains two variables tossfactor1 and tossfactor2.
        """

    team1 = 0
    team2 = 0

    coin = random.randint(1, 2)
    if coin == 1:
        #print("Team1 won the toss")
        team1 = 1
    elif coin == 2:
        #print("Team2 won the toss")
        team2 = 1

    toss = random.uniform(0.5, 1)

    if team1 == 1:
        tossfactorteam1 = (1 - toss)
        tossfactorteam2 = toss
    elif team2 == 1:
        tossfactorteam2 = (1 - toss)
        tossfactorteam1 = toss
    return tossfactorteam1, tossfactorteam2


def Match(datfr):
    """
        This function is the most important in the program. It computes the result of a match between two teams. It makes use of tossfactor1 and tossfactor2 from the toss() function.
        This is the model which randomly generates score of the match using Poissons Distribution.

        :param datfr: The dataframe containing all the teams statistics
        :return: Prints the score of the match and the probability of both the teams winning. It also prints thre probability of a Tie between both the teams.
        """
    goal_scored_team1 = 0
    goal_scored_team2 = 0
    probab1=0
    probab2=0
    probab3=0
    k=100
    for i in range(0, k):
        tf1,tf2 = toss()
        avgScoredByTeam1 = datfr['Avg Attack'][1] / datfr['Avg Defense'][29] * tf1
        avgScoredByTeam2 = datfr['Avg Attack'][29] / datfr['Avg Defense'][1] * tf2
        # print("\n")
        goal_scored_team1 = np.random.poisson(avgScoredByTeam1)
        goal_scored_team2 = np.random.poisson(avgScoredByTeam2)
        if goal_scored_team1 > goal_scored_team2:
            probab1 += 1
        elif goal_scored_team2 > goal_scored_team1:
            probab2 += 1
        else:
            probab3 +=1

        print(datfr['Team'][1] + "\t" + str(goal_scored_team1) + " - " + str(goal_scored_team2) + "\t" + datfr['Team'][29])
    print("\n")
    print("Probability ", datfr['Team'][1], "wins:", round(((probab1 / k) * 100), 3), "%")
    print("Probability ", datfr['Team'][29], "wins:", round(((probab2 / k) * 100), 3), "%")
    print("Probability Match is Drawn:", round(((probab3 / k) * 100), 3), "%")


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
