# Title: FIFA World Cup Simulator

## Team Member(s): Hiral Rayani, Varun Kasbekar

# Monte Carlo Simulation Scenario & Purpose:
# Introduction:
FIFA World Cup Russia 2018 is just round the corner. This is the worlds largest soccer tournament in which 32 nations compete for the world cup. The teams are chosen on the basis of international friendlies which take place prior to the commencement of the world cup. The top 32 qualifying teams are categorized into 8 groups and compete against each other in their respective groupm stages.

The top 2 teams from every group enter the round of 16. This marks the knockout stage of the tournament. Quarter-finals, Semi-finals and the final are the rounds to follow. Each round eliminates teams and the winning teams go through to the next round. Ultimately two best teams battle for the World cup throne.

# Purpose- 
The purpose of this simulation model is to predict the FIFA world cup winner , along with the probility of each teams chance of winning the world cup. As we all know Paul OCTOPUS doesn't exist anymore, we have decided to continue the trend of predicting the FIFA world cup match winners.

# Scenario-
We will be using real world data from the Official FIFA world cup website which includes Team Rankings, Team's past performance in the world cups. We are grouping the qualified teams into 8 groups by performing random draws.
The groups will be as follows:

# GROUP STAGE:
____________________________________________
Group A: Team 1, Team 2, Team 3, Team 4
Group B: Team 5, Team 6, Team 7, Team 8
Group C: Team 9, Team 10, Team 11, Team 12
Group D: Team 13, Team 14, Team 15, Team 16
Group E: Team 17, Team 18, Team 19, Team 20
Group F: Team 21, Team 22, Team 23, Team 24
Group G: Team 25, Team 26, Team 27, Team 28
Group H: Team 29, Team 30, Team 31, Team 32

# ROUND OF 16:
___________________________________________________
QuarterFinalist1: QualifiedTeam1 vs QualifiedTeam2
QuarterFinalist2: QualifiedTeam3 vs QualifiedTeam4
QuarterFinalist3: QualifiedTeam5 vs QualifiedTeam6
QuarterFinalist4: QualifiedTeam7 vs QualifiedTeam8
QuarterFinalist5: QualifiedTeam9 vs QualifiedTeam10
QuarterFinalist6: QualifiedTeam11 vs QualifiedTeam12
QuarterFinalist7: QualifiedTeam13 vs QualifiedTeam14
QuarterFinalist8: QualifiedTeam15 vs QualifiedTeam16

# QUARTER FINALS:
___________________________________________________
SemiFinalist1: QualifiedTeam1 vs QualifiedTeam2
SemiFinalist2: QualifiedTeam3 vs QualifiedTeam4
SemiFinalist3: QualifiedTeam5 vs QualifiedTeam6
SemiFinalist4: QualifiedTeam7 vs QualifiedTeam8

# SEMI FINALS:
___________________________________________________

Finalist1: QualifiedTeam1 vs QualifiedTeam2
Finalist2: QualifiedTeam3 vs QualifiedTeam4

# FINAL:
_______________________
Finalist1 vs Finalist2

We will be randomizing the draws after each round. We first sort the teams based on their FIFA rankings and then randomly assign them 2 values - Attack, Defense based on their rankings. The winner of every group stage is decided from - the points obtained by the team, goals scored and goal difference. We have also considered giving an advantage to the team who wins a toss ( it will be completely randomised to avoid bias). For optimal accuracy our model uses an equation which does computation on those randomly generated ATTACK & DEFENCE values and gives us updated values. We are also trying to incorporate teams past performance in World Cups( Winning Ratio).

Our most important functions is Play_Match which computes the winner between two teams playing a match. We use this function in Group Stages and the Knockout phase. We use Poissons Distribution on average goals scored by Teams to generate the actual Score of the Match.

In the Group Stage, Winning team gets 3 points. In case of draws at group stage, both the teams get 1 point. However if we encounter a draw in the knockout stage, we treat it as an ET (Extra Time). So until the score is unequal, our model simulates the match end result. 


We predict the average goals scored by team 1 against team 2 by using the following equation:
averageGoalsTeam1 = Team1AttackPower / Team2DefensePower
