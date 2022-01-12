ATP = Tournament number (men)
WTA = Tournament number (women)
Location = Venue of tournament
Tournament = Name of tournament (including sponsor if relevant)
Data = Date of match (note: prior to 2003 the date shown for all matches played in a single tournament is the start date)
Series = Name of ATP tennis series (Grand Slam, Masters, International or International Gold)
Tier = Tier (tournament ranking) of WTA tennis series.
Court = Type of court (outdoors or indoors)
Surface = Type of surface (clay, hard, carpet or grass)
Round = Round of match
Best of = Maximum number of sets playable in match
Winner = Match winner
Loser = Match loser
WRank = ATP Entry ranking of the match winner as of the start of the tournament
LRank = ATP Entry ranking of the match loser as of the start of the tournament
L3 = Number of games won in 3rd set by match loser
W4 = Number of games won in 4th set by match winner
L4 = Number of games won in 4th set by match loser
W5 = Number of games won in 5th set by match winner
L5 = Number of games won in 5th set by match loser
Wsets = Number of sets won by match winner
Lsets = Number of sets won by match loser
Comment = Comment on the match (Completed, won through retirement of loser, or via Walkover)

setwd("~/Desktop/ATP")


tennis_data <- read.csv("merged.csv",stringsAsFactors = FALSE, header = TRUE)

# Review the first 5 observations
head(tennis_data)##   ATP Location                         Tournament   Date        Series
## 1   1 Adelaide Australian Hardcourt Championships 1/3/00 International
## 2   1 Adelaide Australian Hardcourt Championships 1/3/00 International
## 3   1 Adelaide Australian Hardcourt Championships 1/3/00 International
##     Court Surface     Round Best.of       Winner          Loser WRank
## 1 Outdoor    Hard 1st Round       3   Dosedel S.    Ljubicic I.    63
## 2 Outdoor    Hard 1st Round       3   Enqvist T.     Clement A.     5
## 3 Outdoor    Hard 1st Round       3    Escude N.  Baccanello P.    40
## 4 Outdoor    Hard 1st Round       3   Federer R. Knippschild J.    65
## 5 Outdoor    Hard 1st Round       3  Fromberg R.  Woodbridge T.    81
##   LRank W1 L1 W2 L2 W3 L3 W4 L4 W5 L5 Wsets Lsets   Comment X X.1 X.2 X.3
## 1    77  6  4  6  2 NA NA NA NA NA NA     2     0 Completed              
## 2    56  6  3  6  3 NA NA NA NA NA NA     2     0 Completed              
## 3   655  6  7  7  5  6  3 NA NA NA NA     2     1 Completed              
## 4    87  6  1  6  4 NA NA NA NA NA NA     2     0 Completed              
## 5   198  7  6  5  7  6  4 NA NA NA NA     2     1 Completed             
## 'data.frame':    52383 obs. of  83 variables:
##  $ ATP       : int  1 1 1 1 1 1 1 1 1 1 ...
##  $ Location  : chr  "Adelaide" "Adelaide" "Adelaide" "Adelaide" ...
##  $ Tournament: chr  "Australian Hardcourt Championships" "Australian Hardcourt Championships" "Australian Hardcourt Championships" "Australian Hardcourt Championships" ...
##  $ Date      : chr  "1/3/00" "1/3/00" "1/3/00" "1/3/00" ...
##  $ Series    : chr  "International" "International" "International" "International" ......
##  $ Winner    : chr  "Dosedel S." "Enqvist T." "Escude N." "Federer R." ...
##  $ Loser     : chr  "Ljubicic I." "Clement A." "Baccanello P." "Knippschild J." ...
##  $ WRank     : chr  "63" "5" "40" "65" ...
##  $ LRank     : chr  "77" "56" "655" "87" ...
##  $ W1        : chr  "6" "6" "6" "6" ...
##  $ L1        : chr  "4" "3" "7" "1" ...
##  $ W2        : int  6 6 7 6 5 7 6 7 2 6 ...
##  $ L2        : int  2 3 5 4 7 6 1 6 6 7 ...
##  $ W3        : int  NA NA 6 NA 6 6 NA NA 6 6 ...
##  $ L3        : int  NA NA 3 NA 4 4 NA NA 1 4 ...
##  $ Wsets     : int  2 2 2 2 2 2 2 2 2 2 ...
##  $ Lsets     : int  0 0 1 0 1 1 0 0 1 1 ...
##  $ Comment   : chr  "Completed" "Completed" "Completed" "Completed" ...
## 'data.frame':    2413 obs. of  26 variables:
##  $ ATP       : int  6 6 6 6 6 6 6 6 6 6 ...
##  $ Location  : chr  "Melbourne" "Melbourne" "Melbourne" "Melbourne" ...
##  $ Tournament: chr  "Australian Open" "Australian Open" "Australian Open" "Australian Open" ...
##  $ Date      : chr  "1/17/00" "1/17/00" "1/17/00" "1/17/00" ...
##  $ Series    : chr  "Grand Slam" "Grand Slam" "Grand Slam" "Grand Slam" ...
##  $ Court     : chr  "Outdoor" "Outdoor" "Outdoor" "Outdoor" ......
##  $ Best.of   : int  5 5 5 5 5 5 5 5 5 5 ...
##  $ Winner    : chr  "Agassi A." "Alami K." "Arazi H." "Behrend T." ...
##  $ Loser     : chr  "Puerta M." "Manta L." "Alonso J." "Meligeni F." ...
##  $ WRank     : chr  "1" "35" "41" "106" ...
##  $ LRank     : chr  "112" "107" "111" "28" ...
##  $ W1        : chr  "6" "6" "6" "6" ...
##  $ L1        : chr  "2" "4" "3" "2" ...
##  $ W2        : int  6 7 7 4 6 6 6 6 6 5 ...
##  $ L2        : int  2 6 6 6 4 1 1 4 4 7 ...
##  $ W3        : int  6 7 6 6 6 6 6 NA 6 6 ...
##  $ L3        : int  3 5 2 7 4 4 4 NA 4 3 ...
##  $ W4        : int  NA NA NA 6 0 NA 7 NA NA 7 ...
##  $ L4        : int  NA NA NA 3 6 NA 6 NA NA 5 ...
##  $ W5        : int  NA NA NA 6 6 NA NA NA NA NA ...
##  $ L5        : int  NA NA NA 0 4 NA NA NA NA NA ...
##  $ Wsets     : int  3 3 3 3 3 3 3 2 3 3 ...
##  $ Lsets     : int  0 0 0 2 2 0 1 0 0 1 ...
##  $ Comment   : chr  "Completed" "Completed" "Completed" "Completed" ...


library(dummies)

Round <- dummy(a$Round)
Best.of <- dummy(a$Best.of)
Winner <- dummy(a$Winner)
Loser <- dummy(a$Loser)

head(a) # check that the values are been converted to dummy variables
str(a)
# Impute missing values with "pmm" - predicted mean matching. m=5 imputed data sets is defaultimputed_Data <- mice(a.mis, m=5, maxit = 50, method = 'pmm', seed = 500)
summary(imputed_Data)

# inspect that missing data has been imputed
imputed_Data$imp$Lsets

# check imputed method
imputed_Data$meth# Plot the imputed data and inspect the distributionxyplot(imputed_Data,WRank ~ W1+L1+W2+L2+W3+L3+W4+L4+L5+W5+LRank,pch=18,cex=1)
player1 <- ggplot(a, aes(x=a$Year)) + geom_histogram() + ggtitle(" Histogram of Year")
p1

player2 <- ggplot(a, aes(x=a$WRank)) + geom_histogram()+ ggtitle(" Histogram of Winner's Ranking")
p2

player3 <- ggplot(a, aes(x=a$LRank)) + geom_histogram()+ ggtitle(" Histogram of Loser's Ranking")
p3

player4 <- ggplot(a, aes(x=a$W1)) + geom_histogram()+ ggtitle(" Histogram of Winner in the first set")
p4

player5 <- ggplot(a, aes(x=a$L1)) + geom_histogram()+ ggtitle(" Histogram of Loser in the first set")
p5

player6 <- ggplot(a, aes(x=a$W2)) + geom_histogram()+ ggtitle(" Histogram of Winner in the second set")
p6

player7 <- ggplot(a, aes(x=a$L2)) + geom_histogram()+ ggtitle(" Histogram of Loser in the second set")
p7

player8 <- ggplot(a, aes(x=a$W3)) + geom_histogram()+ ggtitle(" Histogram of Winner in the third set")
p8

player9 <- ggplot(a, aes(x=a$L3)) + geom_histogram()+ ggtitle(" Histogram of Loser in the third set")
p9


player10 <- plot(x= a$Winner,main = "Distribution of Winner", xlab = "Winner",
     ylab = "count")
p10

player11 <- plot( x = a$Loser, main = "Distribution of Loser", xlab = "Loser",
      ylab = "Count")
p11

player12 <- plot( x = a$Best.of, main = "Distribution of Best.of", xlab = "Best Of",
      ylab = "Count")
p12

player13 <- plot( x = a$Round, main = "Distribution of Tennis Round", xlab = "Round",
      ylab = "Count")
p13
def getBigPointProb(server):
    if server==p1:
        return p1_big_point
    elif server==p2:
        return p2_big_point
    else:
        print("Error")
        
def isBigPoint(server_points, returner_points, tiebreak):
    #server_next_point = server_points+1
    server_next_point = server_points
    #print(server_next_point)
    if tiebreak==False:
        if server_next_point >= 3 and (server_next_point - returner_points) >= 1:
#in our write up, we detail how an objected oriented approach can clean up some of this logic
def getScore(pointsServer, pointsReturner, server_games, returner_games, completed_sets, tiebreaker):
    in_game = ['15', '30', '40']
    extra = ['D', 'A']
    
    display_server='0'
    display_returner='0'

        if pointsReturner==0:
            display_returner='0'
        elif pointsReturner>0 and pointsReturner<4:
            display_returner=in_game[pointsReturner-1]
            display_returner='D'


        if (display_server=='A' and display_returner=='A') or (display_server=='40' and display_returner=='40'):
            display_server = 'D'
            display_returner = 'D'
        if (display_server=='A' and display_returner=='40'):
            display_server = 'A'
            display_returner = 'D'
        if (display_server=='40' and display_returner=='A'):
            display_server = 'D'
            display_returner = 'A'
    else:
        display_server = str(pointsServer)
        display_returner = str(pointsReturner)
    
    if len(completed_sets)==0:
        print(display_server+"-"+display_returner+"|"+"["+str(server_games)+"-"+str(returner_games)+"]")
    else:
        completed = ""
        for sets in completed_sets:
winner and
#call out if server was broken
def player_serve(server, returner, server_prob, returner_prob, gamesMatch, S, server_points_match, returner_points_match, server_games, returner_games, server_pointsGame, returner_pointsGame, completed_sets):
    if isBigPoint(server_pointsGame, returner_pointsGame, False):
        server_prob = getBigPointProb(server)
    if random() < server_prob:
        print(server+" ", end = "")

        returner_pointsGame += 1
        returner_points_match += 1
    if max(server_pointsGame, returner_pointsGame) >= 4 and abs(server_pointsGame - returner_pointsGame) > 1:
        print("\t", server + ":", str(server_pointsGame) + ",", returner + ":", returner_pointsGame, end = "")
        if server_pointsGame > returner_pointsGame:
            server_games += 1

    return server_games, returner_games, gamesMatch, S, server_points_match, returner_points_match, server_pointsGame, returner_pointsGame

    while (max(gamesSet1, gamesSet2) < 6 or abs(gamesSet1 - gamesSet2) < 2) and gamesSet1 + gamesSet2 < 12: #Requirements to play another Game in this Set
        pointsGame1 = 0
        pointsGame2 = 0
        #player 1 serves
        while gamesMatch % 2 == 0:
            gamesSet1, gamesSet2, gamesMatch, S, pointsMatch1, pointsMatch2, pointsGame1, pointsGame2 = player_serve(p1, p2, a, b, gamesMatch, S, pointsMatch1, pointsMatch2, gamesSet1, gamesSet2, pointsGame1, pointsGame2, completed_sets)
        pointsGame1 = 0
        pointsGame2 = 0
        #player 2 serves, but we also incorporate in logic to end the set
        while gamesMatch % 2 == 1 and (max(gamesSet1, gamesSet2) < 6 or abs(gamesSet1 - gamesSet2) < 2) and gamesSet1 + gamesSet2 < 12:
            gamesSet2, gamesSet1, gamesMatch, S, pointsMatch2, pointsMatch1, pointsGame2, pointsGame1 = player_serve(p2, p1, b, a, gamesMatch, S, pointsMatch2, pointsMatch1, gamesSet2, gamesSet1, pointsGame2, pointsGame1, completed_sets)
    #at 6 games all we go to a tie breaker
    if gamesSet1 == 6 and gamesSet2 == 6:
        print("Set", S, "is 6-6 and going to a Tiebreaker.")
    
    return gamesSet1, gamesSet2, gamesMatch, S, pointsMatch1, pointsMatch2

first then optimizing is usually the dev process we prefer

#originally the player serving was being printed as well, but ultimately, it
#made the output results difficult to read so was commented out
def simulateTiebreaker(player1, player2, a, b, gamesMatch, pointsMatch1, pointsMatch2, completed_sets):
    pointsTie1, pointsTie2 = 0, 0           
    while max(pointsTie1, pointsTie2) < 7 or abs(pointsTie1 - pointsTie2) < 2:
        #player 1 will server first
        if gamesMatch % 2 == 0:
            while (pointsTie1 + pointsTie2) % 4 == 0 or (pointsTie1 + pointsTie2) % 4 == 3:
                server_prob = a
                if isBigPoint(pointsTie1, pointsTie2, True):
                    server_prob=getBigPointProb(player1)
                if random() < server_prob:
                    #print(player1+" ", end = "")
                    getScore(pointsTie1, pointsTie2, 6, 6, completed_sets, True)
                    pointsTie1 += 1
                    pointsMatch1 += 1
                else:
                    getScore(pointsTie1, pointsTie2, 6, 6, completed_sets, True)
                    pointsTie2 += 1
                    pointsMatch2 += 1
                if max(pointsTie1, pointsTie2) >= 7 and abs(pointsTie1 - pointsTie2) > 1:
                    print("\t", p1 + ":", str(pointsTie1) + ",", p2 + ":", pointsTie2)
                    gamesMatch += 1
                    break 
            while (max(pointsTie1, pointsTie2) < 7 or abs(pointsTie1 - pointsTie2) < 2) and ((pointsTie1 + pointsTie2) % 4 == 1 or (pointsTie1 + pointsTie2) % 4 == 2): # Conditions to continue Tiebreaker (race to 7, win by 2) and Player 2 serves (points 4N+1 and 4N+2)
                server_prob = b
                if isBigPoint(pointsTie2, pointsTie1, True):
                    server_prob=getBigPointProb(player2)
                if random() < server_prob:
                    #print(player2+" ", end = "")
                    getScore(pointsTie1, pointsTie2, 6, 6, completed_sets, True)
                    pointsTie2 += 1
                    pointsMatch2 += 1
                else:
                    getScore(pointsTie1, pointsTie2, 6, 6, completed_sets, True)
                    pointsTie1 += 1
                    pointsMatch1 += 1
                if max(pointsTie1, pointsTie2) >= 7 and abs(pointsTie1 - pointsTie2) > 1:
                    print("\t", p1 + ":", str(pointsTie1) + ",", p2 + ":", pointsTie2)
                    break
        
        #player 2 will server first
        if gamesMatch % 2 == 1:
            while (pointsTie1 + pointsTie2) % 4 == 1 or (pointsTie1 + pointsTie2) % 4 == 2:
                server_prob =  a
                if isBigPoint(pointsTie1, pointsTie2, True):
                    server_prob=getBigPointProb(player1)
                if random() < server_prob:
                    #print(player1+" ", end = "")
                    getScore(pointsTie1, pointsTie2, 6, 6, completed_sets, True)
                    pointsTie1 += 1
                    pointsMatch1 += 1
                else:
                    getScore(pointsTie1, pointsTie2, 6, 6, completed_sets, True)
                    pointsTie2 += 1
                    pointsMatch2 += 1
                if max(pointsTie1, pointsTie2) >= 7 and abs(pointsTie1 - pointsTie2) > 1:
                    print("\t", p1 + ":", str(pointsTie1) + ",", p2 + ":", pointsTie2)
                    break 
            while (max(pointsTie2, pointsTie1) < 7 or abs(pointsTie1 - pointsTie2) < 2) and ((pointsTie1 + pointsTie2) % 4 == 0 or (pointsTie1 + pointsTie2) % 4 == 3): # Conditions to continue Tiebreaker (race to 7, win by 2) and Player 2 serves (points 4N and 4N+3)
                server_prob =  b
                if isBigPoint(pointsTie2, pointsTie1, True):
                    server_prob=getBigPointProb(player2)
                if random() < server_prob:
                    #print(player2+" ", end = "")
                    getScore(pointsTie1, pointsTie2, 6, 6, completed_sets, True)
                    pointsTie2 += 1
                    pointsMatch2 += 1
                else:
                    getScore(pointsTie1, pointsTie2, 6, 6, completed_sets, True)
                    pointsTie1 += 1
                    pointsMatch1 += 1
                if max(pointsTie1, pointsTie2) >= 7 and abs(pointsTie1 - pointsTie2) > 1:
                    print("\t", p1 + ":", str(pointsTie1) + ",", p2 + ":", pointsTie2)
                    break                             
    gamesMatch += 1
    return pointsTie1, pointsTie2, gamesMatch, pointsMatch1, pointsMatch2
#displays the running score in the way an umpire would announce the score at
#the end of a set
def printSetMatchSummary(p1, p2, gamesSet1, gamesSet2, S, pointsTie1, pointsTie2, setsMatch1, setsMatch2):
    if gamesSet1 > gamesSet2:
        setsMatch1 += 1
        print(p1.upper(), "wins Set", str(S) + ":", gamesSet1, "games to", str(gamesSet2) + ".")
    elif gamesSet2 > gamesSet1:
        setsMatch2 += 1
        print(p2.upper(), "wins Set", str(S) + ":", gamesSet2, "games to", str(gamesSet1) + ".")
    elif gamesSet1 == gamesSet2:
        if pointsTie1 > pointsTie2:
            setsMatch1 += 1
            print(p1.upper(), "wins Set", str(S) + ": 7 games to 6 (" + str(pointsTie1) + "-" + str(pointsTie2) + ").")
        else:
            setsMatch2 += 1
            print(p2.upper(), "wins Set", str(S) + ": 7 games to 6 (" + str(pointsTie2) + "-" + str(pointsTie1) + ").")
    print("After", S, "Sets:", p1, str(setsMatch1) + ",", p2, str(setsMatch2) + ".\n")   
    return setsMatch1, setsMatch2
#prints out final winner and number of sets won
def pointsMatchSummary(p1, p2, setsMatch1, setsMatch2, pointsMatch1, pointsMatch2):
        if setsMatch1 == 3:
            print(p1.upper(), "(" + str(a) + ")", "beat", p2, "(" + str(b) + ") by", setsMatch1, "Sets to", str(setsMatch2) + ".")
            winner.append(p1)
        else:
#this control flow a single simulation
winner = []
completed_sets = []
S = 0
gamesMatch = 0

#in all subscripted variables
#the subscript refers to the player
#for example, setsMatch1 is sets won by player1 and
#setsMatch2 is sets won by player2
pointsMatch1, pointsMatch2 = 0, 0
setsMatch1, setsMatch2 = 0, 0
pointsTie1, pointsTie2 = 0, 0
pointsGame1, pointsGame2 = 0, 0

#initialize player one and two
#a is ps1 and b is ps2
#p1_big_point and p2_big_point are the probability
#of p1 and p2 winning on a big point, respectively
p1 = "A"
p2 = "B"
a = 0.64
b = 0.62
p1_big_point = 0.70
p2_big_point = 0.68

while S < 5 and max(setsMatch1, setsMatch2) < 3:
    gamesSet1, gamesSet2, gamesMatch, S, pointsMatch1, pointsMatch2 = simulateSet(a, b, gamesMatch, S, 
                                                                                  pointsMatch1, pointsMatch2, 
                                                                                  completed_sets)
    print()
    if gamesSet1 == 6 and gamesSet2 == 6:
        pointsTie1, pointsTie2, gamesMatch, pointsMatch1, pointsMatch2 = simulateTiebreaker(p1, p2, a, b, 
                                                                                            gamesMatch, pointsMatch1, 
                                                                                            pointsMatch2, 
                                                                                            completed_sets)
    
    setsMatch1, setsMatch2 = printSetMatchSummary(p1, p2, gamesSet1, gamesSet2, 
                                                  S, pointsTie1, pointsTie2, 
                                                  setsMatch1, setsMatch2)
    
    if gamesSet1 == 6 and gamesSet2 == 6:
        if pointsTie1 > pointsTie2:
            completed_sets.append([gamesSet1+1, gamesSet2])
        else:
            completed_sets.append([gamesSet1, gamesSet2+1])
    else:
        completed_sets.append([gamesSet1, gamesSet2])

pointsMatchSummary(p1, p2, setsMatch1, setsMatch2, pointsMatch1, pointsMatch2)


#to pull a random number and determine
#that takes in a distribution and generates random numbers
#based on that
from random import random

#define what a big point is and
#have a separte function which can be called to get
#probability of a player winning a big point
def getBigPointProb(server):
    if server==p1:
        return p1_big_point
    elif server==p2:
        return p2_big_point
    else:
        print("Error")
        
def isBigPoint(server_points, returner_points, tiebreak):
    #server_next_point = server_points+1
    server_next_point = server_points
    #print(server_next_point)
    if tiebreak==False:
        if server_next_point >= 3 and (server_next_point - returner_points) >= 1:
#in our write up, we detail how an objected oriented approach can clean up some of this logic
def getScore(pointsServer, pointsReturner, server_games, returner_games, completed_sets, tiebreaker):
    in_game = ['15', '30', '40']
    extra = ['D', 'A']
    
    display_server='0'
    display_returner='0'
    
    if tiebreaker==False:
        if pointsServer==0:
            display_server='0'
        elif pointsServer>0 and pointsServer<4:
            display_server=in_game[pointsServer-1]
        elif pointsServer>=4:
            #clean_pointsServer = pointsServer-4
            display_server = 'D'

        if pointsReturner==0:
            display_returner='0'
        elif pointsReturner>0 and pointsReturner<4:
            display_returner=in_game[pointsReturner-1]
            display_returner='D'

        if display_server=='D' and display_server=='D':
            if pointsServer>pointsReturner:
                display_server='A'
            elif pointsReturner>pointsServer:
                display_returner='A'

        if (display_server=='A' and display_returner=='A') or (display_server=='40' and display_returner=='40'):
            display_server = 'D'
            display_returner = 'D'
        if (display_server=='A' and display_returner=='40'):
            display_server = 'A'
            display_returner = 'D'
        if (display_server=='40' and display_returner=='A'):
            display_server = 'D'
            display_returner = 'A'
    else:
        display_server = str(pointsServer)
        display_returner = str(pointsReturner)
    
    if len(completed_sets)==0:
        print(display_server+"-"+display_returner+"|"+"["+str(server_games)+"-"+str(returner_games)+"]")
    else:
        completed = ""
        for sets in completed_sets:
winner and
#call out if server was broken
def player_serve(server, returner, server_prob, returner_prob, gamesMatch, S, server_points_match, returner_points_match, server_games, returner_games, server_pointsGame, returner_pointsGame, completed_sets):
    if isBigPoint(server_pointsGame, returner_pointsGame, False):
        server_prob = getBigPointProb(server)
    if random() < server_prob:
        print(server+" ", end = "")

        returner_pointsGame += 1
        returner_points_match += 1
    if max(server_pointsGame, returner_pointsGame) >= 4 and abs(server_pointsGame - returner_pointsGame) > 1:
        print("\t", server + ":", str(server_pointsGame) + ",", returner + ":", returner_pointsGame, end = "")
        if server_pointsGame > returner_pointsGame:
            server_games += 1
            print()
        else:
            returner_games += 1
            print(" -- " + returner, "broke")
        gamesMatch += 1
        return server_games, returner_games, gamesMatch, S, server_points_match, returner_points_match, server_pointsGame, returner_pointsGame

    return server_games, returner_games, gamesMatch, S, server_points_match, returner_points_match, server_pointsGame, returner_pointsGame

    while (max(gamesSet1, gamesSet2) < 6 or abs(gamesSet1 - gamesSet2) < 2) and gamesSet1 + gamesSet2 < 12: #Requirements to play another Game in this Set
        pointsGame1 = 0
        pointsGame2 = 0
        #player 1 serves
        while gamesMatch % 2 == 0:
            gamesSet1, gamesSet2, gamesMatch, S, pointsMatch1, pointsMatch2, pointsGame1, pointsGame2 = player_serve(p1, p2, a, b, gamesMatch, S, pointsMatch1, pointsMatch2, gamesSet1, gamesSet2, pointsGame1, pointsGame2, completed_sets)
        pointsGame1 = 0
        pointsGame2 = 0
        #player 2 serves, but we also incorporate in logic to end the set
        while gamesMatch % 2 == 1 and (max(gamesSet1, gamesSet2) < 6 or abs(gamesSet1 - gamesSet2) < 2) and gamesSet1 + gamesSet2 < 12:
            gamesSet2, gamesSet1, gamesMatch, S, pointsMatch2, pointsMatch1, pointsGame2, pointsGame1 = player_serve(p2, p1, b, a, gamesMatch, S, pointsMatch2, pointsMatch1, gamesSet2, gamesSet1, pointsGame2, pointsGame1, completed_sets)
    #at 6 games all we go to a tie breaker
    if gamesSet1 == 6 and gamesSet2 == 6:
        print("Set", S, "is 6-6 and going to a Tiebreaker.")
    
    return gamesSet1, gamesSet2, gamesMatch, S, pointsMatch1, pointsMatch2

first then optimizing is usually the dev process we prefer

#originally the player serving was being printed as well, but ultimately, it
#made the output results difficult to read so was commented out
def simulateTiebreaker(player1, player2, a, b, gamesMatch, pointsMatch1, pointsMatch2, completed_sets):
    pointsTie1, pointsTie2 = 0, 0           
    while max(pointsTie1, pointsTie2) < 7 or abs(pointsTie1 - pointsTie2) < 2:
        #player 1 will server first
        if gamesMatch % 2 == 0:
            while (pointsTie1 + pointsTie2) % 4 == 0 or (pointsTie1 + pointsTie2) % 4 == 3:
                server_prob = a
                if isBigPoint(pointsTie1, pointsTie2, True):
                    server_prob=getBigPointProb(player1)
                if random() < server_prob:
                    #print(player1+" ", end = "")
                    getScore(pointsTie1, pointsTie2, 6, 6, completed_sets, True)
                    pointsTie1 += 1
                    pointsMatch1 += 1
                else:
                    getScore(pointsTie1, pointsTie2, 6, 6, completed_sets, True)
                    pointsTie2 += 1
                    pointsMatch2 += 1
                if max(pointsTie1, pointsTie2) >= 7 and abs(pointsTie1 - pointsTie2) > 1:
                    print("\t", p1 + ":", str(pointsTie1) + ",", p2 + ":", pointsTie2)
                    gamesMatch += 1
                    break 
            while (max(pointsTie1, pointsTie2) < 7 or abs(pointsTie1 - pointsTie2) < 2) and ((pointsTie1 + pointsTie2) % 4 == 1 or (pointsTie1 + pointsTie2) % 4 == 2): # Conditions to continue Tiebreaker (race to 7, win by 2) and Player 2 serves (points 4N+1 and 4N+2)
                server_prob = b
                if isBigPoint(pointsTie2, pointsTie1, True):
                    server_prob=getBigPointProb(player2)
                if random() < server_prob:
                    #print(player2+" ", end = "")
                    getScore(pointsTie1, pointsTie2, 6, 6, completed_sets, True)
                    pointsTie2 += 1
                    pointsMatch2 += 1
                else:
                    getScore(pointsTie1, pointsTie2, 6, 6, completed_sets, True)
                    pointsTie1 += 1
                    pointsMatch1 += 1
                if max(pointsTie1, pointsTie2) >= 7 and abs(pointsTie1 - pointsTie2) > 1:
                    print("\t", p1 + ":", str(pointsTie1) + ",", p2 + ":", pointsTie2)
                    break
        
        #player 2 will server first
        if gamesMatch % 2 == 1:
            while (pointsTie1 + pointsTie2) % 4 == 1 or (pointsTie1 + pointsTie2) % 4 == 2:
                server_prob =  a
                if isBigPoint(pointsTie1, pointsTie2, True):
                    server_prob=getBigPointProb(player1)
                if random() < server_prob:
                    #print(player1+" ", end = "")
                    getScore(pointsTie1, pointsTie2, 6, 6, completed_sets, True)
                    pointsTie1 += 1
                    pointsMatch1 += 1
                else:
                    getScore(pointsTie1, pointsTie2, 6, 6, completed_sets, True)
                    pointsTie2 += 1
                    pointsMatch2 += 1
                if max(pointsTie1, pointsTie2) >= 7 and abs(pointsTie1 - pointsTie2) > 1:
                    print("\t", p1 + ":", str(pointsTie1) + ",", p2 + ":", pointsTie2)
                    break 
            while (max(pointsTie2, pointsTie1) < 7 or abs(pointsTie1 - pointsTie2) < 2) and ((pointsTie1 + pointsTie2) % 4 == 0 or (pointsTie1 + pointsTie2) % 4 == 3): # Conditions to continue Tiebreaker (race to 7, win by 2) and Player 2 serves (points 4N and 4N+3)
                server_prob =  b
                if isBigPoint(pointsTie2, pointsTie1, True):
                    server_prob=getBigPointProb(player2)
                if random() < server_prob:
                    #print(player2+" ", end = "")
                    getScore(pointsTie1, pointsTie2, 6, 6, completed_sets, True)
                    pointsTie2 += 1
                    pointsMatch2 += 1
                else:
                    getScore(pointsTie1, pointsTie2, 6, 6, completed_sets, True)
                    pointsTie1 += 1
                    pointsMatch1 += 1
                if max(pointsTie1, pointsTie2) >= 7 and abs(pointsTie1 - pointsTie2) > 1:
                    print("\t", p1 + ":", str(pointsTie1) + ",", p2 + ":", pointsTie2)
                    break                             
    gamesMatch += 1
    return pointsTie1, pointsTie2, gamesMatch, pointsMatch1, pointsMatch2
#displays the running score in the way an umpire would announce the score at
#the end of a set
def printSetMatchSummary(p1, p2, gamesSet1, gamesSet2, S, pointsTie1, pointsTie2, setsMatch1, setsMatch2):
    if gamesSet1 > gamesSet2:
        setsMatch1 += 1
        print(p1.upper(), "wins Set", str(S) + ":", gamesSet1, "games to", str(gamesSet2) + ".")
    elif gamesSet2 > gamesSet1:
        setsMatch2 += 1
        print(p2.upper(), "wins Set", str(S) + ":", gamesSet2, "games to", str(gamesSet1) + ".")
    elif gamesSet1 == gamesSet2:
        if pointsTie1 > pointsTie2:
            setsMatch1 += 1
            print(p1.upper(), "wins Set", str(S) + ": 7 games to 6 (" + str(pointsTie1) + "-" + str(pointsTie2) + ").")
        else:
            setsMatch2 += 1
            print(p2.upper(), "wins Set", str(S) + ": 7 games to 6 (" + str(pointsTie2) + "-" + str(pointsTie1) + ").")
    print("After", S, "Sets:", p1, str(setsMatch1) + ",", p2, str(setsMatch2) + ".\n")   
    return setsMatch1, setsMatch2
#prints out final winner and number of sets won
def pointsMatchSummary(p1, p2, setsMatch1, setsMatch2, pointsMatch1, pointsMatch2):
        if setsMatch1 == 3:
            print(p1.upper(), "(" + str(a) + ")", "beat", p2, "(" + str(b) + ") by", setsMatch1, "Sets to", str(setsMatch2) + ".")
            winner.append(p1)
        else:
#this control flow a single simulation
winner = []
completed_sets = []
S = 0
gamesMatch = 0

#in all subscripted variables
#the subscript refers to the player
#for example, setsMatch1 is sets won by player1 and
#setsMatch2 is sets won by player2
pointsMatch1, pointsMatch2 = 0, 0
setsMatch1, setsMatch2 = 0, 0
pointsTie1, pointsTie2 = 0, 0
pointsGame1, pointsGame2 = 0, 0

#initialize player one and two
#a is ps1 and b is ps2
#p1_big_point and p2_big_point are the probability
#of p1 and p2 winning on a big point, respectively
p1 = "A"
p2 = "B"
a = 0.64
b = 0.62
p1_big_point = 0.70
p2_big_point = 0.68

while S < 5 and max(setsMatch1, setsMatch2) < 3:
    gamesSet1, gamesSet2, gamesMatch, S, pointsMatch1, pointsMatch2 = simulateSet(a, b, gamesMatch, S, 
                                                                                  pointsMatch1, pointsMatch2, 
                                                                                  completed_sets)
    print()
    if gamesSet1 == 6 and gamesSet2 == 6:
        pointsTie1, pointsTie2, gamesMatch, pointsMatch1, pointsMatch2 = simulateTiebreaker(p1, p2, a, b, 
                                                                                            gamesMatch, pointsMatch1, 
                                                                                            pointsMatch2, 
                                                                                            completed_sets)
    
    setsMatch1, setsMatch2 = printSetMatchSummary(p1, p2, gamesSet1, gamesSet2, 
                                                  S, pointsTie1, pointsTie2, 
                                                  setsMatch1, setsMatch2)
    
    if gamesSet1 == 6 and gamesSet2 == 6:
        if pointsTie1 > pointsTie2:
            completed_sets.append([gamesSet1+1, gamesSet2])
        else:
            completed_sets.append([gamesSet1, gamesSet2+1])
    else:
        completed_sets.append([gamesSet1, gamesSet2])

pointsMatchSummary(p1, p2, setsMatch1, setsMatch2, pointsMatch1, pointsMatch2)
