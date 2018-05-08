# Title: FIFA World Cup Simulator

## Team Member(s): Hiral Rayani, Varun Kasbekar

# Monte Carlo Simulation Scenario & Purpose:

# Introduction:
FIFA World Cup Russia 2018 is just round the corner. This is the worlds largest soccer tournament in which 32 nations compete for the world cup. The teams are chosen on the basis of international friendlies which take place prior to the commencement of the world cup. The top 32 qualifying teams are categorized into 8 groups and compete against each other in their respective group stages.

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

## Simulation's variables of uncertainty
There are 6 random variables in our project. Attacking power attribute, Defense power attribute, Draws, Toss, Goal Scored by Team 1 in the match and Goal Scored by Team2 in the match.
 
# 1.Attacking Power Attribute 
This variable is used to demonstrate Attacking power of the team. It is randomly generated according to the ranking of the Team. It gives us a basic idea how strong is the Attack. This can be a major factor in deciding how many goals does the Team Score. We first find the Average Goals scored by a Team through this variable. Finally we compute Average Attack of the Team.
 
# 2.Defense Power Attribute 
This variable is used to demonstrate Defending power of the team. It is randomly generated according to the ranking of the Team. It gives us a basic idea how strong is the Defense. This can be a major factor in deciding how many goals does the Team Conceed. We first find the Average Goals Conceeded by a Team through this variable. Finally we compute Average Defense of the Team.
 
# 3.Draws
We randomize the draws for each round. So each round contain groups with different teams splitted randomly. This variable is randomly generated to avoid set parameters to decide which Team goes into which Group. All the worldCups have predefined set slots for teams. But our model includes this innovative feature that randomizes this and hence removes any sort of Bias. Its kind of a suspense which Teams will compete against each other in rounds to proceed. We took this idea from another well-known soccer tournament- UEFA Champions League
 
# 4.Toss
Toss is a crucial factor to be considered for a match played. We believe that TOSS could play a vital role in the outcome of a match. Our model randomizes Toss between two teams playing a match. The team winning the toss is given a slight advantage in terms of probability according to our model. We think that the Team that wins the toss gets a strategic advantage as it gets to decide between two options: Select Side & Kick-Off
We have analyzed the trend over years and observed that teams winning the toss have a better success rate.
 
# 5.Goals Scored By Team 1:
This variable is the actual representation of the goals scored in the match by Team 1. It is randomly generated using Poissons Distribution. We use Poissons Distribution on (Average Goals Scored By) to randomly generate a score for that match by Team1. We use this variable to distinguish between the winner and the loser of the match. Based on this variable we assign points, Goals Scored and Goal difference for the Group Stages.
 
avgscoredbyteam1 = AverageAttack(Team1)/ AverageDefense(Team2) * TossFactor
 
# 6.Goals Scored By Team 2:
This variable is the actual representation of the goals scored in the match by Team 2. It is randomly generated using Poissons Distribution. We use Poissons Distribution on (Average Goals Scored By) to randomly generate a score for that match by Team2. We use this variable to distinguish between the winner and the loser of the match. Based on this variable we assign points, Goals Scored and Goal difference for the Group Stages.
 
avgscoredbyteam2 = AverageAttack(Team2)/ AverageDefense(Team1) * TossFactor
 
## Hypothesis or hypotheses before running the simulation:
 
All Teams are independent of each other.

Any team can be assigned to any Group.

The performance of every team is independent of each other.

The Toss will be coin Toss that will be independent.

After the n simulations, the team who has highest probability of winning will be the predicted winner and positions can be decided according to other Teams winning probability.
 
## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)
 
We first simulated a Single Match based on the parameters above. Then we simulated the Group Stage. Ultimately we simulate the Knockout Phase to find out the Winner. During this Simulation, we thought that the accuracy of the model can be increased if we use the Win Ratio of Teams in past worldcups. So we incorporated that into our model. We are using Poissons distribution for two main reasons. Firstly Poissons Distribution works best when variables are independent of each other. So here assuming that the Average Goals Scored by Team is independent, we decided to use Poissons Distribution. Secondly Poissons Distribution works best when we know a single parameter(  Average Goals Scored by Team) in our case.
 
## Instructions on how to use the program:
Download the FifaRnakings.csv data file

Download the worldcup.py file and run it.

Import pandas, random and numpy

The code does not need an input to be given, It computes the probability of each team winning the worldcup by itself.

However the integer number that decides how many times to run the simulation can be changed.

## Conclusions
After several discussions, we came up with a more efficient way to assign attack and defense value to each team. Previously we assigned these values based on their team rankings. We then created bins of size 8 and segregated 32 teams into 4 such bins according to their rankings. We then randomly generated Attack and Defence values to the teams with respect to these bins. So now for the top notch teams i.e top 8 teams will have attack and defence values in one range and so on.This reduced any sort of bias and improved efficiency. Our model randomizes draws, score, toss every single time and thus we could not incorporate several Doctests. However we have included 1 doctest by setting the seed to get the same output every time. This can be just used an example on what input to give and how our output will be. We have also created a seperate TOSS function that can be used before every match. Also with due respect to the suggestions from our peers, we have incorporated Fixed draws and Random draws. Our model gives the flexibility to the user to choose whether he wants Fixed draws or Random draws. Fixed draws contain combinations of teams which FIFA 2018 WorldCup has predecided. Random draws will be our main approach that will randomise groups and teams. We have successfully predicted each teams probability of winning the Worldcup after simulating the tournament 10000 times. 
 
## All Sources Used:
http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0101-74382015000300577#B7

https://medium.com/@adamfreymiller/a-monte-carlo-simulation-of-the-2017-18-premier-league-season-3b7bbe8b8a13

https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/poisson-distribution
