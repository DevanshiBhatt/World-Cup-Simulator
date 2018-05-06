"""
Doctests:
>>> random.seed(0)
>>> np.random.seed(0)
>>> main(1,'fixed')
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
Result of 1 simulations
--------------------------------------------
This is GROUP STAGE
<BLANKLINE>
<BLANKLINE>
GROUP A RESULTS
<BLANKLINE>
<BLANKLINE>
russia 0 - 1 saudi arabia
russia 0 - 0 egypt
russia 1 - 0 uruguay
saudi arabia 1 - 0 egypt
saudi arabia 0 - 2 uruguay
egypt 0 - 0 uruguay
<BLANKLINE>
<BLANKLINE>
GROUP B RESULTS
<BLANKLINE>
<BLANKLINE>
portugal 4 - 0 spain
portugal 1 - 0 morrocco
portugal 0 - 1 iran
spain 1 - 0 morrocco
spain 1 - 0 iran
morrocco 1 - 0 iran
<BLANKLINE>
<BLANKLINE>
GROUP C RESULTS
<BLANKLINE>
<BLANKLINE>
france 2 - 0 australia
france 1 - 1 peru
france 0 - 0 denmark
australia 0 - 1 peru
australia 0 - 1 denmark
peru 0 - 0 denmark
<BLANKLINE>
<BLANKLINE>
GROUP D RESULTS
<BLANKLINE>
<BLANKLINE>
argentina 0 - 0 iceland
argentina 0 - 0 croatia
argentina 0 - 0 nigeria
iceland 0 - 0 croatia
iceland 0 - 0 nigeria
croatia 1 - 1 nigeria
<BLANKLINE>
<BLANKLINE>
GROUP E RESULTS
<BLANKLINE>
<BLANKLINE>
brazil 1 - 1 switzerland
brazil 0 - 0 costa rica
brazil 0 - 0 serbia
switzerland 0 - 0 costa rica
switzerland 0 - 0 serbia
costa rica 0 - 0 serbia
<BLANKLINE>
<BLANKLINE>
GROUP F RESULTS
<BLANKLINE>
<BLANKLINE>
germany 1 - 0 mexico
germany 0 - 0 sweden
germany 1 - 1 korea republic
mexico 1 - 0 sweden
mexico 1 - 0 korea republic
sweden 0 - 0 korea republic
<BLANKLINE>
<BLANKLINE>
GROUP G RESULTS
<BLANKLINE>
<BLANKLINE>
belgium 0 - 2 panama
belgium 0 - 1 tunisia
belgium 0 - 1 england
panama 0 - 1 tunisia
panama 1 - 1 england
tunisia 1 - 3 england
<BLANKLINE>
<BLANKLINE>
GROUP H RESULTS
<BLANKLINE>
<BLANKLINE>
polland 1 - 0 senegal
polland 0 - 1 colombia
polland 1 - 0 japan
senegal 0 - 0 colombia
senegal 1 - 0 japan
colombia 1 - 1 japan
Qualifies teams: polland
<BLANKLINE>
<BLANKLINE>
ROUND OF 16
<BLANKLINE>
<BLANKLINE>
saudi arabia 0 - 3 uruguay
portugal 0 - 1 spain
france 0 - 3 peru
nigeria 0 - 1 croatia
switzerland 1 - 0 brazil
mexico 2 - 0 germany
england 0 - 1 tunisia
polland 2 - 0 colombia
<BLANKLINE>
<BLANKLINE>
QUARTER - FINALS
<BLANKLINE>
<BLANKLINE>
uruguay 1 - 0 spain
peru 0 - 1 croatia
switzerland 0 - 2 mexico
tunisia 1 - 0 polland
<BLANKLINE>
<BLANKLINE>
SEMI - FINALS
<BLANKLINE>
<BLANKLINE>
uruguay 1 - 0 croatia
mexico 2 - 0 tunisia
<BLANKLINE>
<BLANKLINE>
WORLD-CUP FINAL
<BLANKLINE>
<BLANKLINE>
uruguay 0 - 1 mexico
<BLANKLINE>
<BLANKLINE>
mexico: 1.0
100.0% chance of winning the worldcup
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>
<BLANKLINE>

"""
import numpy as np
import operator as op
import pandas as pd
import random
from random import randint
from random import choice

#Assumptions
# The winner of the group stage is obtained from points, goal goaldifference, goal scored

class WorldCupMatch:

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

    def toss_factor(self):
        """
        This function computes the toss at the beginning of every match. Our model assumes that the team winning the toss has a slight advantage over the opponent.
        The function randomly computes toss winner. Based on this result, we assign a randomly generated number between 0.5 and 1 to the losing team and 1-(that number) to the winning team. We do so because we will be multiplying that number(tossfactor1) in the denominator of an equation used in the match_between function.
        :return:

        """
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
        return self.tossfactorteam1, self.tossfactorteam2

    def matchbetween(self):
        """
                This function is the most important in the program. It computes the result of a match between two teams. It makes use of tossfactor1 and tossfactor2 from the toss() function.
                This is the model which randomly generates score of the match using Poissons Distribution.
                :param datfr: The dataframe containing all the teams statistics
                :return: Prints the score of the match and the probability of both the teams winning. It also prints the probability of a Tie between both the teams.
        """
        team1_toss_factor, team2_toss_factor = self.toss_factor()

        avgScoredByTeam1 = self.team1.attack / self.team2.defense * team1_toss_factor
        avgScoredByTeam2 = self.team2.attack / self.team1.defense * team2_toss_factor


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
        """
            This function prints the final match score for the match played between two teams.
            :return:

        """
        print(self.team1.name + " " + str(self.team1score) + " - " + str(self.team2score) + " " + self.team2.name)

class WorldCupTeam:
    """
    This class assigns attack and defence values to every team that can be used by the match between function to compute the result.
    :return:

     """


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
        """
            This function finds the top two qualified teams from each group. The top two teams from each group will be chosen according to their 'points', 'goaldifference', 'scored'
            :return:

        """
        for i in range(0, len(self.teams)):
            for j in range(i + 1, len(self.teams)):
                    WorldCupMatch(self.teams[i], self.teams[j], True)
        self.teams = sorted(self.teams, key=op.attrgetter('points', 'goaldifference', 'scored'))
        self.first_qualified = self.teams[len(self.teams)-1]
        self.second_qualified = self.teams[len(self.teams)-2]



def main(simulations, userschoice):
    # The teams data are obtained from FIFA statistics
    # Team Name, Attack, Defence
    """
    This is the main function of the program. Users are given a choice for simulating either for fixed draws or for random draws for the entire tournament.
    We have taken team statistics such as rankings from FIFA website. We have also taken team WorldCup wins and matches played statistics data from the official website.
    :return:

    """
    quarters = ['quarter1', 'quarter2', 'quarter3', 'quarter4', 'quarter5', 'quarter6', 'quarter7', 'quarter8']
    semifinalists = ['semifinalist1', 'semifinalist2', 'semifinalist3', 'semifinalist4']
    finalists = ['finalist1', 'finalist2']

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


    #INPUT USERS CHOICE FOR FIXED CHOICE
    choices= ["random", "Random", "RANDOM"]
    choicess = ["fixed", "Fixed", "FIXED"]
    if userschoice in choices:
        countries = [germany, brazil, belgium, portugal, argentina, france, switzerland, spain, russia, japan, polland,
                     korea_republic, england, denmark, peru, tunisia, mexico, colombia, uruguay, croatia, australia,
                     iceland, sweden, costa_rica, senegal, serbia, morrocco, egypt, nigeria, saudi_arabia, panama, iran]
        finalresults = {}

        GroupA, GroupB, GroupC, GroupD, GroupE, GroupF, GroupG, GroupH = ([] for i in range(8))

        Groups = [GroupA, GroupB, GroupC, GroupD, GroupE, GroupF, GroupG, GroupH]
        for i in Groups:
            for j in range(4):
                teamname = choice(countries)
                i.append(teamname)
                countries.remove(teamname)

        print("DRAWS for the WorldCup 2018 are:")
        print("\n")
        for i in range(simulations):
            # Play first stage
            print("Result of", i + 1, "simulations")
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
            r16 = [groupA.first_qualified, groupA.second_qualified, groupB.first_qualified, groupB.second_qualified,
                   groupC.first_qualified, groupC.second_qualified, groupD.first_qualified, groupD.second_qualified,
                   groupE.first_qualified, groupE.second_qualified, groupF.first_qualified, groupF.second_qualified,
                   groupG.first_qualified, groupG.second_qualified, groupH.first_qualified, groupH.second_qualified]


            GroupP, GroupQ, GroupR, GroupS, GroupT, GroupU, GroupV, GroupW =([] for i in range(8))

            round16groups = [GroupP, GroupQ, GroupR, GroupS, GroupT, GroupU, GroupV, GroupW]

            for k in round16groups:
                for j in range(2):
                    teamname = choice(r16)
                    k.append(teamname)
                    r16.remove(teamname)

            for i in range(8):
                quarters[i]=WorldCupMatch(round16groups[i][0], round16groups[i][1], False).winner

            # Quarters
            print("\n")
            print("QUARTER - FINALS")
            print("\n")
            quarterfinal = [quarters[0], quarters[1], quarters[2], quarters[3], quarters[4], quarters[5], quarters[6],
                            quarters[7]]
            GroupA1, GroupB1, GroupC1, GroupD1 = ([] for i in range(4))

            quarterfinalgroups = [GroupA1, GroupB1, GroupC1, GroupD1]

            i = 0
            for i in quarterfinalgroups:
                for j in range(2):
                    teamname = choice(quarterfinal)
                    i.append(teamname)
                    quarterfinal.remove(teamname)

            for i in range(4):
                semifinalists[i] = WorldCupMatch(quarterfinalgroups[i][0], quarterfinalgroups[i][1], False).winner

                # Semifinals
            print("\n")
            print("SEMI - FINALS")
            print("\n")

            semifinal = [semifinalists[0], semifinalists[1], semifinalists[2], semifinalists[3]]
            GroupP1, GroupQ1 = ([] for i in range(2))
            semifinalgroups = [GroupP1, GroupQ1]

            i = 0
            for i in semifinalgroups:
                for j in range(2):
                    teamname = choice(semifinal)
                    i.append(teamname)
                    semifinal.remove(teamname)

            for i in range(2):
                finalists[i] = WorldCupMatch(semifinalgroups[i][0], semifinalgroups[i][1], False).winner
                # Finals
            print("\n")
            print("WORLD-CUP FINAL")
            print("\n")
            winner = WorldCupMatch(finalists[0], finalists[1], False).winner
            print("\n")

            if winner.name in finalresults:
                finalresults[winner.name] += 1
            else:
                finalresults[winner.name] = 1

            for key in sorted(finalresults, key=finalresults.get, reverse=True):
                print(key + ": " + str(finalresults[key] / simulations))
                ro=(finalresults[key] / simulations) * 100
                print(str(ro) + "% chance of winning the worldcup")
                print("\n")
            print("\n")


    elif userschoice in choicess:

        print("\n")
        finalresults = {}
        groupA1 = [russia , saudi_arabia,egypt, uruguay]
        groupB1 = [portugal, spain, morrocco, iran]
        groupC1 = [france, australia, peru, denmark]
        groupD1 = [argentina, iceland, croatia, nigeria]
        groupE1 = [brazil, switzerland, costa_rica, serbia]
        groupF1 = [germany, mexico, sweden, korea_republic]
        groupG1 = [belgium, panama, tunisia, england]
        groupH1 = [polland, senegal, colombia, japan]
        print("\n")
        for i in range(simulations):
            # Play first stage
            print("Result of", i+1 ,"simulations")
            print("--------------------------------------------")
            print("This is GROUP STAGE")
            print("\n")
            print("GROUP A RESULTS")
            print("\n")
            groupA = TeamPool(groupA1)
            print("\n")
            print("GROUP B RESULTS")
            print("\n")
            groupB = TeamPool(groupB1)
            print("\n")
            print("GROUP C RESULTS")
            print("\n")
            groupC = TeamPool(groupC1)
            print("\n")
            print("GROUP D RESULTS")
            print("\n")
            groupD = TeamPool(groupD1)
            print("\n")
            print("GROUP E RESULTS")
            print("\n")
            groupE = TeamPool(groupE1)
            print("\n")
            print("GROUP F RESULTS")
            print("\n")
            groupF = TeamPool(groupF1)
            print("\n")
            print("GROUP G RESULTS")
            print("\n")
            groupG = TeamPool(groupG1)
            print("\n")
            print("GROUP H RESULTS")
            print("\n")
            groupH = TeamPool(groupH1)
            print("Qualifies teams:", groupH.first_qualified.name)

            # Play second stage
            print("\n")
            print("ROUND OF 16")
            print("\n")

            quarter1 = WorldCupMatch(groupA.first_qualified, groupA.second_qualified, False).winner
            quarter2 = WorldCupMatch(groupB.first_qualified, groupB.second_qualified, False).winner
            quarter3 = WorldCupMatch(groupC.first_qualified, groupC.second_qualified, False).winner
            quarter4 = WorldCupMatch(groupD.first_qualified, groupD.second_qualified, False).winner
            quarter5 = WorldCupMatch(groupE.first_qualified, groupE.second_qualified, False).winner
            quarter6 = WorldCupMatch(groupF.first_qualified, groupF.second_qualified, False).winner
            quarter7 = WorldCupMatch(groupG.first_qualified, groupG.second_qualified, False).winner
            quarter8 = WorldCupMatch(groupH.first_qualified, groupH.second_qualified, False).winner

            # Quarters
            print("\n")
            print("QUARTER - FINALS")
            print("\n")

            semifinalist1 = WorldCupMatch(quarter1, quarter2, False).winner
            semifinalist2 = WorldCupMatch(quarter3, quarter4, False).winner
            semifinalist3 = WorldCupMatch(quarter5, quarter6, False).winner
            semifinalist4 = WorldCupMatch( quarter7, quarter8, False).winner

            # Semifinals
            print("\n")
            print("SEMI - FINALS")
            print("\n")
            finalist1 = WorldCupMatch(semifinalist1, semifinalist2, False).winner
            finalist2 = WorldCupMatch(semifinalist3, semifinalist4, False).winner

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
                rou = (finalresults[key] / simulations) * 100
                print(str(rou) + "% chance of winning the worldcup")
                print("\n")
            print("\n")
    else:
        print("Please enter correct input and try again")
        pass

if __name__ == '__main__':

    userschoice = input(" Do you want to simulate for fixed or random draws? \n Enter fixed or random\n")

    main(1000,userschoice)