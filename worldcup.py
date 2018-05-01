import numpy as np
import operator as op
import pandas as pd
import random
from random import randint
from random import choice

#Assumptions
# The winner of the group stage is obtained from points, goal goaldifference, goal scored

class WorldCupMatch:
    """
    >>>
    >>>


    """
    def __init__(self, team1, team2, groupcheck):

        self.winner = None
        self.team1score = 0
        self.team2score = 0
        self.team1 = team1
        self.team2 = team2
        self.groupcheck = groupcheck
        self.team1out=0
        self.team2out=0
        self.coin=0
        self.toss=0
        self.tossfactorteam1=0
        self.tossfactorteam2 = 0
        self.matchbetween()
        self.matchscore()



    def matchbetween(self):
        """
                This function is the most important in the program. It computes the result of a match between two teams. It makes use of tossfactor1 and tossfactor2 from the toss() function.
                This is the model which randomly generates score of the match using Poissons Distribution.

                :param datfr: The dataframe containing all the teams statistics
                :return: Prints the score of the match and the probability of both the teams winning. It also prints thre probability of a Tie between both the teams.
        """
        #TOSS

        self.coin = random.randint(1, 2)
        if self.coin == 1:
            # print("Team1 won the toss")
            self.team1out = 1
        elif self.coin == 2:
            # print("Team2 won the toss")
            self.team2out = 1

        self.toss = random.uniform(0.5, 1)
        if self.team1out == 1:
            self.tossfactorteam1 = (1 - self.toss)
            self.tossfactorteam2 = self.toss
        elif self.team2out == 1:
            self.tossfactorteam2 = (1 - self.toss)
            self.tossfactorteam1 = self.toss



        avgScoredByTeam1 = self.team1.attack / self.team2.defense * self.tossfactorteam1
        avgScoredByTeam2 = self.team2.attack / self.team1.defense * self.tossfactorteam2
        while True:
            self.team1score = np.random.poisson(avgScoredByTeam1)
            self.team2score = np.random.poisson(avgScoredByTeam2)
            if self.team1score > self.team2score:
                self.team1.points += 3
                self.team1.won += 1
                self.team2.lost += 1
                self.winner = self.team1
                break
            elif self.team1score < self.team2score:
                self.team2.points += 3
                self.team2.won += 1
                self.team1.lost += 1
                self.winner = self.team2
                break
            else:
                if self.groupcheck is True:
                    self.team1.points += 1
                    self.team2.points += 1
                    self.team1.tie += 1
                    self.team2.tie += 1
                    break
        self.team1.scored += self.team1score
        self.team2.scored += self.team2score
        self.team1.conceded += self.team2score
        self.team2.conceded += self.team1score
        self.team1.goaldifference += self.team1score-self.team2score
        self.team2.goaldifference += self.team2score-self.team1score

    def matchscore(self):
        print(self.team1.name + " " + str(self.team1score) + " - " + str(self.team2score) + " " + self.team2.name)

class WorldCupTeam:

    def __init__(self, name, table):
        self.points = 0
        self.won = 0
        self.lost = 0
        self.tie = 0
        self.scored = 0
        self.conceded = 0
        self.goaldifference = 0
        self.name = name.lower()

        for rec in table:
            if self.name in rec[0].lower():
                self.attack = rec[1]
                self.defense = rec[2]
                break


class TeamPool:

    def __init__(self, teams):
        self.first_qualified = None
        self.second_qualified = None
        self.teams = teams
        self.initialise()
        self.qualifiedteams()

    def initialise(self):
        for team in self.teams:
            team.points = 0
            team.won = 0
            team.lost = 0
            team.tie = 0
            team.scored = 0
            team.conceded = 0
            team.goaldifference = 0


    def qualifiedteams(self):
        for i in range(0, len(self.teams)):
            for j in range(i + 1, len(self.teams)):
                    WorldCupMatch(self.teams[i], self.teams[j], True)
        self.teams = sorted(self.teams, key=op.attrgetter('points', 'goaldifference', 'scored'))
        self.first_qualified = self.teams[len(self.teams)-1]
        self.second_qualified = self.teams[len(self.teams)-2]

def main():
    # The teams data are obtained from FIFA statistics
    # Team Name, Attack, Defence

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
    print(df)


    teamstats=[]
    for i in range(1,len(df)+1):
        teaminfo=[]
        teaminfo = (df["Team"][i], df['Avg Attack'][i], df['Avg Defense'][i])
        teaminfo=list(teaminfo)
        teamstats.append(teaminfo)

    germany = WorldCupTeam("GERMANY", teamstats)
    brazil = WorldCupTeam("BRAZIL", teamstats)
    belgium = WorldCupTeam("BELGIUM", teamstats)
    portugal = WorldCupTeam("PORTUGAL", teamstats)
    argentina = WorldCupTeam("ARGENTINA", teamstats)
    france = WorldCupTeam("FRANCE", teamstats)
    switzerland = WorldCupTeam("SWITZERLAND", teamstats)
    spain = WorldCupTeam("SPAIN", teamstats)
    russia = WorldCupTeam("RUSSIA", teamstats)
    japan = WorldCupTeam("JAPAN", teamstats)
    polland=WorldCupTeam("POLLAND", teamstats)
    korea_republic = WorldCupTeam("KOREA REPUBLIC", teamstats)
    england = WorldCupTeam("ENGLAND", teamstats)
    denmark= WorldCupTeam("DENMARK", teamstats)
    peru= WorldCupTeam("PERU", teamstats)
    tunisia=WorldCupTeam("TUNISIA", teamstats)
    mexico = WorldCupTeam("MEXICO", teamstats)
    colombia = WorldCupTeam("COLOMBIA", teamstats)
    uruguay = WorldCupTeam("URUGUAY", teamstats)
    croatia = WorldCupTeam("CROATIA", teamstats)
    australia = WorldCupTeam("AUSTRALIA", teamstats)
    iceland=WorldCupTeam("ICELAND", teamstats)
    sweden=WorldCupTeam("SWEDEN", teamstats)
    costa_rica = WorldCupTeam("COSTA RICA", teamstats)
    senegal=WorldCupTeam("SENEGAL", teamstats)
    serbia=WorldCupTeam("SERBIA", teamstats)
    morrocco=WorldCupTeam("MORROCCO", teamstats)
    egypt=WorldCupTeam("EGYPT", teamstats)
    nigeria = WorldCupTeam("NIGERIA", teamstats)
    saudi_arabia=WorldCupTeam("SAUDI ARABIA", teamstats)
    panama=WorldCupTeam("PANAMA", teamstats)
    iran = WorldCupTeam("IRAN", teamstats)

    countries=[germany,brazil,belgium,portugal,argentina,france,switzerland,spain,russia,japan,polland,korea_republic,england,denmark,peru,tunisia,mexico,colombia,uruguay,croatia,australia,iceland,sweden,costa_rica,senegal,serbia,morrocco,egypt,nigeria,saudi_arabia,panama,iran]
    finalresults = {}

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
            teamname = choice(countries)
            i.append(teamname)
            countries.remove(teamname)

    print("DRAWS for the WorldCup 2018 are:")
    print("\n")

    print("\n")
    simulations=10
    for i in range(simulations):
        # Play first stage
        print("Result of", i+1 ,"simulations")
        print("--------------------------------------------")
        print("This is GROUP STAGE")
        print("\n")
        print("GROUP A RESULTS")
        print("\n")
        groupA = TeamPool(Groups[0])
        print("\n")
        print("GROUP B RESULTS")
        print("\n")
        groupB = TeamPool(Groups[1])
        print("\n")
        print("GROUP C RESULTS")
        print("\n")
        groupC = TeamPool(Groups[2])
        print("\n")
        print("GROUP D RESULTS")
        print("\n")
        groupD = TeamPool(Groups[3])
        print("\n")
        print("GROUP E RESULTS")
        print("\n")
        groupE = TeamPool(Groups[4])
        print("\n")
        print("GROUP F RESULTS")
        print("\n")
        groupF = TeamPool(Groups[5])
        print("\n")
        print("GROUP G RESULTS")
        print("\n")
        groupG = TeamPool(Groups[6])
        print("\n")
        print("GROUP H RESULTS")
        print("\n")
        groupH = TeamPool(Groups[7])

        # Play second stage
        print("\n")
        print("ROUND OF 16")
        print("\n")
        r16 = [groupA.first_qualified, groupA.second_qualified,groupB.first_qualified, groupB.second_qualified,groupC.first_qualified, groupC.second_qualified,groupD.first_qualified, groupD.second_qualified,groupE.first_qualified, groupE.second_qualified,groupF.first_qualified, groupF.second_qualified,groupG.first_qualified, groupG.second_qualified, groupH.first_qualified, groupH.second_qualified ]
        GroupP = []
        GroupQ = []
        GroupR = []
        GroupS = []
        GroupT = []
        GroupU = []
        GroupV = []
        GroupW = []
        round16groups = [GroupP, GroupQ, GroupR, GroupS, GroupT, GroupU, GroupV, GroupW]
        i = 0
        for i in round16groups:
            for j in range(2):
                teamname = choice(r16)
                i.append(teamname)
                r16.remove(teamname)


        quarter1 = WorldCupMatch(round16groups[0][0],round16groups[0][1], False).winner
        quarter2 = WorldCupMatch(round16groups[1][0],round16groups[1][1], False).winner
        quarter3 = WorldCupMatch(round16groups[2][0],round16groups[2][1], False).winner
        quarter4 = WorldCupMatch(round16groups[3][0],round16groups[3][1], False).winner
        quarter5 = WorldCupMatch(round16groups[4][0],round16groups[4][1], False).winner
        quarter6 = WorldCupMatch(round16groups[5][0],round16groups[5][1], False).winner
        quarter7 = WorldCupMatch(round16groups[6][0],round16groups[6][1], False).winner
        quarter8 = WorldCupMatch(round16groups[7][0],round16groups[7][1], False).winner

        # Quarters
        print("\n")
        print("QUARTER - FINALS")
        print("\n")
        quarterfinal =[quarter1, quarter2, quarter3, quarter4, quarter5, quarter6, quarter7, quarter8]
        GroupA1 = []
        GroupB1 = []
        GroupC1 = []
        GroupD1 = []
        quarterfinalgroups =[GroupA1, GroupB1, GroupC1, GroupD1]
        i = 0
        for i in quarterfinalgroups:
            for j in range(2):
                teamname = choice(quarterfinal)
                i.append(teamname)
                quarterfinal.remove(teamname)
        semifinalist1 = WorldCupMatch(quarterfinalgroups[0][0], quarterfinalgroups[0][1], False).winner
        semifinalist2 = WorldCupMatch(quarterfinalgroups[1][0], quarterfinalgroups[1][1], False).winner
        semifinalist3 = WorldCupMatch(quarterfinalgroups[2][0], quarterfinalgroups[2][1], False).winner
        semifinalist4 = WorldCupMatch(quarterfinalgroups[3][0], quarterfinalgroups[3][1], False).winner

        # Semifinals
        print("\n")
        print("SEMI - FINALS")
        print("\n")

        semifinal=[semifinalist1, semifinalist2, semifinalist3, semifinalist4]
        GroupP1 =[]
        GroupQ1 =[]
        semifinalgroups=[GroupP1, GroupQ1]
        i = 0
        for i in semifinalgroups:
            for j in range(2):
                teamname = choice(semifinal)
                i.append(teamname)
                semifinal.remove(teamname)

        finalist1 = WorldCupMatch(semifinalgroups[0][0], semifinalgroups[0][1], False).winner
        finalist2 = WorldCupMatch(semifinalgroups[1][0], semifinalgroups[1][1], False).winner

        # Final
        print("\n")
        print("WORLD-CUP FINAL")
        print("\n")
        winner = WorldCupMatch(finalist1, finalist2, False).winner
        print("\n")

        if winner.name in finalresults:
            finalresults[winner.name] += 1
        else:
            finalresults[winner.name] = 1

        for key in sorted(finalresults, key=finalresults.get, reverse=True):
            print(key + ": " + str(finalresults[key] / simulations))


        print("\n")

if __name__ == '__main__':
    main()





