import mysql.connector

username = input("Username: ")
password = input("Password: ")
hostname = input("Host: ")
databaseName = input("Database Name: ")
cnx = mysql.connector.connect(user=username, password=password, host=hostname, port = 3306, database=databaseName)
cursor = cnx.cursor(buffered=True)

print("Welcome to the Super Smash Bros. for Wii U Player Ranking System.")

pCursor = cnx.cursor(prepared=True)

admin = True
myInput = input("Is admin? (y/n): ")
if (myInput == 'n'):
    admin = False

def mainMenu():
    print()
    print("Please select an option from the menu below.")

    print("1). Player Rankings")
    print("2). Management Functions")
    print("3). Usage Rankings")
    print("4). Quit")

    option = getUserInput(4, 1)    
    if (option == 1):
        playerRankings()
    if (option == 2):
        if (admin == True):
            managementFunctions()
        else:
            print("Error: Admin-only function")
            mainMenu()
    if (option == 3):
        usageRankings()

def getUserInput(listMax, listMin):
    gotCorrectInput = False;

    while (gotCorrectInput == False):
        gotCorrectInput = True
        try: 
            option = int(input("Selection: "))
            if (option > listMax or option < listMin):
                gotCorrectInput = False
                print("Option out of range. Try again.")
        except ValueError:
            print("Error: Non-integer input.")
            gotCorrectInput = False
    return option
    
def playerRankings():
    print()
    print("~ Player Rankings Menu ~")
    print("Please select an option: ")

    print("1). Register Player")
    print("2). Update Player")
    print("3). Report Set")
    print("4). Show Player Rankings")
    print("5). Show Player's Set History")
    print("6). Show Player's Recently Attended Tournaments")
    print("7). Edit Set")
    print("8). Register Team")
    print("9). Update Team")
    print("10). Report Doubles Set")
    print("11). Show Team Rankings")
    print("12). Show Team's Set History")
    print("13). Show Team's Recently Attended Tournaments")
    print("14). Edit Doubles Set")
    print("15). Quit")

    option = getUserInput(15, 1)
    if (option == 1):
        if (admin == True):
            registerPlayer()
        else:
            print("Error: Admin-only function")
            mainMenu()
    if (option == 2):
        if (admin == True):
            updatePlayer()
        else:
            print("Error: Admin-only function")
            mainMenu()
    if (option == 3):
        if (admin == True):
            reportSet()
        else:
            print("Error: Admin-only function")
            mainMenu()
    if (option == 4):
        showPlayerRankings()
    if (option == 5):
        showPlayerSetHistory()
    if (option == 6):
        showTournamentHistory()
    if (option == 7):
        if (admin == True):
            editSet()
        else:
            print("Error: Admin-only function")
            mainMenu()
    if (option == 8):
        if (admin == True):
            registerTeam()
        else:
            print("Error: Admin-only function")
            mainMenu()
    if (option == 9):
        if (admin == True):
            updateTeam()
        else:
            print("Error: Admin-only function")
            mainMenu()
    if (option == 10):
        if (admin == True):
            reportDoublesSet()
        else:
            print("Error: Admin-only function")
            mainMenu()
    if (option == 11):
        showTeamRankings()
    if (option == 12):
        showTeamSetHistory()
    if (option == 13):
        showTeamTournamentHistory()
    if (option == 14):
        if (admin == True):
            editDoublesSet()
        else:
            print("Error: Admin-only function")
            mainMenu()
    if (option == 15):
        mainMenu()



def registerPlayer():
    print()
    print("- Player Registration")
    restart = False
    userOption = input("Please enter the tag of the player you wish to register (or type '!end!' to quit): ")
    if (tagExistsNoMsg(userOption)):
        print("Error: Player already exists in database.")
        userOption = '!end!'
    if (userOption != '!end!'):
        tag = userOption
        userOption = input("Please enter the player's city: ")
        if (userOption != '!end!'):
            city = userOption
            userOption = input("{} from {} will be initialized with zero wins, losses, and points (this can be edited later). Proceed? (y/n): ".format(tag, city))
            while (userOption != "y" and userOption != "n"):
                userOption = input("Error: Input must be y or n. Try again: ")
            if (userOption == 'y'):
                #need to generate new ID for player
                query = ("select * from player order by player_id asc")
                cursor.execute(query)
                uniqueID = 0
                for (player_id, player_tag, player_city, wins, losses, points) in cursor:
                    if (player_id == uniqueID):
                        uniqueID = uniqueID+1
                    if (tag == player_tag):
                        restart = True

                if (restart):
                    print("Error: Player already exists.")
                    registerPlayer()
                else:
                    registerPlayer = ("insert into player (player_id, tag, city, wins, losses, points) values(%s, %s, %s, %s, %s, %s)")
                    pCursor.execute(registerPlayer, (str(uniqueID), tag, city, 0, 0, 0))
                    query = ("select * from player where tag = '{}'".format(tag))
                    cursor.execute(query)
                    for (everything) in cursor:
                        print("{}".format(everything))
                    cursor.execute("commit")
    mainMenu()

def getPlayerStatus(prompt, currVal):
    gotCorrectInput = False
    while (gotCorrectInput == False):
        gotCorrectInput = True
        userOption = input("{} (Current Value: {}): ".format(prompt, currVal))
        try:
            userOption = int(userOption)
        except ValueError:
            if (userOption != "*" and userOption != "!exit!"):
                print("Error: Non-integer input.")
                gotCorrectInput = False
    if (userOption != "*"):
        return userOption
    else:
        return currVal

def updatePlayer():
    print()
    print("- Update Player")
    userOption = input("Enter the tag of the player you wish to update (!end! to exit): ")
    if (userOption != "!end!"):
        query = ("select * from player")
        cursor.execute(query)
        foundTag = False
        for (p_id, p_tag, city, wins, losses, points) in cursor:
            if (userOption == p_tag):
                foundTag = True
        if (foundTag):
            oldTag = userOption
            print("Fill in the information requested below (* to leave category unchanged): ")

            ### Getting tag
            userOption = input("Tag: ")
            if (userOption != "*"):
                newTag = userOption
            else:
                newTag = oldTag

            ### Getting city
            userOption = input("City: ")
            if (userOption != "*"):
                city = userOption
            else:
                query = ("select * from player")
                cursor.execute(query)
                for (p_id, p_tag, p_city, p_wins, p_losses, p_points) in cursor:
                    if (oldTag == p_tag):
                        city = p_city

            ### Getting number of wins
            query = ("select * from player")
            cursor.execute(query)
            currWins = 0
            for (p_id, p_tag, p_city, p_wins, p_losses, p_points) in cursor:
                if (oldTag == p_tag):
                    currWins = p_wins
            wins = getPlayerStatus("Wins", currWins)

            ### Getting number of losses
            query = ("select * from player")
            cursor.execute(query)
            currLosses = 0
            for (p_id, p_tag, p_city, p_wins, p_losses, p_points) in cursor:
                if (oldTag == p_tag):
                    currLosses = p_losses
            losses = getPlayerStatus("Losses", currLosses)

            ### Getting number of points
            query = ("select * from player")
            cursor.execute(query)
            currPoints = 0
            for (p_id, p_tag, p_city, p_wins, p_losses, p_points) in cursor:
                if (oldTag == p_tag):
                    currPoints = p_points
            points = getPlayerStatus("Points", currPoints)

            print("Updating player record...")
            query = ("update player SET tag = %s, city = %s, wins = %s, losses = %s, points = %s where tag = %s")
            cursor.execute(query, (newTag, city, wins, losses, points, oldTag))
            query = ("select * from player where tag = '{}'".format(newTag))
            cursor.execute(query)
            for (everything) in cursor:
                print("{}".format(everything))
            cursor.execute("commit")
    mainMenu()

def reportSet():
    print()
    print("- Report Set")
    print("Enter '!exit!' at any time to back out.")
    setID = input("Please enter the round and set number (e.g. 'WR1-2', 'LR3-4', 'GF'): ")
    if (setID != "!exit!"):
        tournamentID = input("Please enter the tournament abbreviation (e.g. 'PP-4', 'JRWI-6'): ")
        if (tournamentID != "!exit!"):
            query = ("select * from tournament")
            cursor.execute(query)
            foundTournament = False
            for (myId, myName, myVenue, myDate, myEntrants) in cursor:
                if (tournamentID == myId):
                    foundTournament = True
            if (foundTournament == False):
                print("Error: Tournament does not exist.")
            if (foundTournament):
                setUniqueID = "{}: {}".format(setID, tournamentID)
                query = ("select * from tournament_set")
                cursor.execute(query)
                isUnique = True
                for (thing1, thing2, thing3, thing4, thing5, thing6, thing7, thing8, thing9) in cursor:
                    if (setUniqueID == thing1):
                        isUnique = False
                        print("Error: Set ID already exists in database.")
                if (isUnique):
                    player1ID = input("Player 1 Tag: ")
                    if (player1ID != "!exit!"):
                        query = ("select * from player")
                        cursor.execute(query)
                        foundPlayer = False
                        for (p_id, p_tag, p_city, p_wins, p_losses, p_points) in cursor:
                            if (player1ID == p_tag):
                                foundPlayer = True
                        if (foundPlayer == False):
                            print("Error: Player 1 does not exist.")
                        else:
                            player2ID = input("Player 2 Tag: ")
                            if (player2ID != "!exit!"):
                                foundPlayer = False
                                cursor.execute(query)
                                for (p_id, p_tag, p_city, p_wins, p_losses, p_points) in cursor:
                                    if (player2ID == p_tag):
                                        foundPlayer = True
                                if (foundPlayer == False):
                                    print("Error: Player 2 does not exist.")
                                else:
                                    correctInput = False
                                    while (correctInput == False): 
                                        player1Score = input("Please enter Player 1's score: ")
                                        correctInput = True
                                        try:
                                            int(player1Score)    
                                        except ValueError:
                                            if (player1Score != "!exit!"):
                                                print("Error: Score must be an integer value.")
                                                correctInput = False
                                    if (player1Score != "!exit!"):
                                        correctInput = False
                                        while (correctInput == False):
                                            player2Score = input("Please enter Player 2's score: ")
                                            correctInput = True
                                            try:
                                                int(player2Score)
                                            except ValueError:
                                                if (player2Score != "!exit!"):
                                                    print("Error: Score must be an integer value.")
                                                    correctInput = False
                                        if (player2Score != "!exit!"):
                                            player1Char = input("Player 1's Character: ")
                                            if (player1Char != "!exit!"):
                                                query = ("select * from tournament_character")
                                                cursor.execute(query)
                                                foundChar = False
                                                for (charName, charRank) in cursor:
                                                    if (player1Char == charName):
                                                        foundChar = True
                                                if (foundChar == False):
                                                    print("Error: Character does not exist.")
                                                else:
                                                    player2Char = input("Player 2's Character: ")
                                                    if (player2Char != "!exit!"):
                                                        foundChar = False
                                                        cursor.execute(query)
                                                        for (charName, charRank) in cursor:
                                                            if (player2Char == charName):
                                                                foundChar = True
                                                        if (foundChar == False):
                                                            print("Error: Character does not exist.")
                                                        else:
                                                            theWinner = input("Enter the winner of the set: ")
                                                            if (theWinner != "!exit!"):
                                                                while (player1ID != theWinner and player2ID != theWinner):
                                                                    print("Error: That player did not play in this set.")
                                                                    theWinner = input("Enter the winner of the set: ")
                                                                query = ("insert into tournament_set values(%s, %s, %s, %s, %s, %s, %s, %s, %s)")
                                                                cursor.execute(query, (setUniqueID, tournamentID, player1ID, player2ID, player1Score, player2Score, player1Char, player2Char, theWinner))
                                                                query = ("select * from tournament_set where set_id = '{}'".format(setUniqueID))
                                                                cursor.execute(query)
                                                                theLoser = ""
                                                                
                                                                for (everything) in cursor:
                                                                    print("{}".format(everything))
                                                                if (theWinner == player1ID):
                                                                    theLoser = player2ID
                                                                else:
                                                                    theLoser = player1ID
                                                                updateStats(theWinner, theLoser)
                                                                cursor.execute("commit")
    mainMenu()
                                                                    
                                                                
def showPlayerRankings():
    print()
    print("- Player Rankings: ")
    query = ("PREPARE getPlayersOrderByPoints from 'select tag, points from player order by points desc'")
    #query = ("select tag, points from player order by points desc")
    cursor.execute(query)
    query = ("EXECUTE getPlayersOrderByPoints")
    cursor.execute(query)
    i = 1
    for (tag, points) in cursor:
        print("{}). {}".format(str(i), tag))
        i = i+1
    query = ("DEALLOCATE PREPARE getPlayersOrderByPoints")
    cursor.execute(query)
    mainMenu()

def showPlayerSetHistory():
    print()
    print("- Player Set History: ")
    playerName = input("Please enter the player whose set history you would like to see: ")
    query = ("select * from player")
    cursor.execute(query)
    foundPlayer = False
    for (p_id, p_tag, p_city, p_wins, p_losses, p_points) in cursor:
        if (p_tag == playerName):
            foundPlayer = True
    if (foundPlayer):
        query = ("select * from tournament_set where p1_tag = '{}' or p2_tag = '{}'").format(playerName, playerName)
        cursor.execute(query)
        print()
        print("{}'s set history: ".format(playerName))
        opponentName = ""
        myScore = 0
        myChar = ""
        for (op1, op2, op3, op4, op5, op6, op7, op8, op9) in cursor:
            if (op3 == playerName):
                opponentName = op4
                myScore = op5
                opScore = op6
                myChar = op7
            else:
                opponentName = op3
                myScore = op6
                opScore = op5
                myChar = op8
            winStatus = "Defeat"
            if (op9 == playerName):
                winStatus = "Victory"
            
            print("Set ID: {} | Played Against: {} | Character Used: {} | Result: {} | Score: {}-{}".format(op1, opponentName, myChar, winStatus, myScore, opScore))
    else:
        print("Error: Player not found.")
    mainMenu()

def showTournamentHistory():
    print()
    print("- Player Tournament History: ")
    playerName = input("Please enter the player whose tournament history you would like to see: ")
    query = ("select * from player")
    cursor.execute(query)
    foundPlayer = False
    for (p_id, p_tag, p_city, p_wins, p_losses, p_points) in cursor:
        if (p_tag == playerName):
            foundPlayer = True
    if (foundPlayer):
        query = ("select * from tournament_history where (set_tournament_id = tournament_tournament_id and (p1_tag = '{}' or p2_tag = '{}'))").format(playerName, playerName);
        cursor.execute(query)
        print()
        print("{}'s tournament history: ".format(playerName))
        for (tid, tid2, tname, tdate, p1_tag, p2_tag) in cursor:
            print("{} ({})".format(tname, tdate))
    else:
        print("Error: Player not found.")
    mainMenu()


def tagExists(tag):
    cursor.execute("select getPlayerInfo('{}');".format(tag))
    result = cursor.fetchone()
    tagMatch = result[0]
    if (tagMatch == tag):
        return True
    if (tag != "*"):
        print("Error: Tag does not exist.")
    return False

def tagExistsNoMsg(tag):
    cursor.execute("select getPlayerInfo('{}');".format(tag))
    result = cursor.fetchone()
    tagMatch = result[0]
    if (tagMatch == tag):
        return True
    return False

def charExists(characterName):
    query = ("select * from tournament_character")
    #row = cursor.fetchone()
    #while row is not None:
        #row = cursor.fetchone()
    cursor.execute(query)
    for (cname, crank) in cursor:
        if (characterName == cname):
            return True
    if (characterName != "*"):
        print("Error: Character does not exist.")
    return False

def setExists(setID):
    query = ("select * from tournament_set")
    cursor.execute(query)
    for (q1, q2, q3, q4, q5, q6, q7, q8, q9) in cursor:
        if (q1 == setID):
            return True
    print("Error: Tournament set ID does not exist.")
    return False

def editSet():
    print()
    print("- Edit Set: ")
    print("Input '!exit!' at any time to quit.")
    print()
    setID = input("Enter the unique ID of the set you want to modify (in the form of WR1-1: TT-6): ")
    if (setID != '!exit!' and setExists(setID)):
        query = ("select * from tournament_set")
        cursor.execute(query)
        foundSet = False
        oldP1Tag = ""
        oldP2Tag = ""
        oldP1Score = ""
        oldP2Score = ""
        oldP1Char = ""
        oldP2Char = ""
        oldWinner = ""
        for (q1, q2, q3, q4, q5, q6, q7, q8, q9) in cursor:
            if (q1 == setID):
                foundSet = True
                oldP1Tag = q3
                oldP2Tag = q4
                oldP1Score = q5
                oldP2Score = q6
                oldP1Char = q7
                oldP2Char = q8
                oldWinner = q9
        oldLoser = ""
        if (oldWinner == oldP1Tag):
            oldLoser = oldP2Tag
        else:
            oldLoser = oldP1Tag
        #Fixes win records such that the previously-reported wins and losses are overwitten
        revertStats(oldWinner, oldLoser)
        if (foundSet == False):
            print("Error: Set not found.")
        else:
            print("Input '*' in any of the following categories to leave unchanged.")
            print()
            #Get P1 Tag
            playerTag = input("Player 1's Tag (Currently {}): ".format(oldP1Tag))
            if (playerTag != "!exit!" and (playerTag == "*" or tagExists(playerTag))):    
                #Get P2 Tag
                player2Tag = input("Player 2's Tag (Currently {}): ".format(oldP2Tag))
                if (player2Tag != "!exit!" and (player2Tag == "*" or tagExists(player2Tag))):
                    #Get P1 Score
                    newP1Score = getPlayerStatus("Player 1's Score", oldP1Score)
                    if (newP1Score != '!exit!'):
                        #Get P2 Score
                        newP2Score = getPlayerStatus("Player 2's Score", oldP2Score)
                        if (newP2Score != '!exit!'):
                            #Get P1 Character
                            newP1Char = input("Player 1's Character (Currently {}): ".format(oldP1Char))
                            if (newP1Char != "!exit!" and (newP1Char == "*" or charExists(newP1Char))):
                                #Get P2 Character
                                newP2Char = input("Player 2's Character (Currently {}): ".format(oldP2Char))
                                if (newP2Char != "!exit!" and (newP2Char == "*" or charExists(newP2Char))):
                                    #Get Winner
                                    if (playerTag == "*"):
                                        playerTag = oldP1Tag
                                    if (player2Tag == "*"):
                                        player2Tag = oldP2Tag
                                    newWinner = input("Set Winner (Currently {}): ".format(oldWinner))
                                    while (newWinner == "*" and (oldWinner != playerTag and oldWinner != player2Tag)):
                                        print("Error: Player no longer in set.")
                                        newWinner = input("Set Winner (Currently {}): ".format(oldWinner))
                                    if (newWinner != "!exit!" and (newWinner == playerTag or newWinner == player2Tag or newWinner == "*")):
                                        if (newP1Char == "*"):
                                            newP1Char = oldP1Char
                                        if (newP2Char == "*"):
                                            newP2Char = oldP2Char
                                        if (newWinner == "*"):
                                            newWinner = oldWinner
                                        newLoser = ""
                                        if (newWinner == playerTag):
                                            newLoser = player2Tag
                                        else:
                                            newLoser = playerTag
                                        fetchedOne = cursor.fetchone()
                                        while (fetchedOne != None):
                                            fetchedOne = cursor.fetchone()
                                        query = ("UPDATE tournament_set SET p1_tag = %s, p2_tag = %s, p1_score = %s, p2_score = %s, p1_cname = %s, p2_cname = %s, winner = %s WHERE set_id = %s")
                                        cursor.execute(query, (playerTag, player2Tag, newP1Score, newP2Score, newP1Char, newP2Char, newWinner, setID))
                                        
                                        query = ("select * from tournament_set where set_id = '{}'").format(setID)
                                        cursor.execute(query)
                                        for (everything) in cursor:
                                            print(everything)
                                        updateStats(newWinner, newLoser)
                                        cursor.execute("commit")
    mainMenu()
                                        
                                        
def teamExists(tname):
    query = ("select * from team")
    cursor.execute(query)
    for (name, tag1, tag2, wins, losses, points) in cursor:
        if (tname == name):
            return True
    return False

def getIntegerInput(msg):
    correctVal = False
    while (correctVal == False):
        usrInput = input(msg)
        try:
            result = int(usrInput)
            correctVal = True
        except ValueError:
            if (usrInput != "!exit!"):
                print("Error: Input must be integer.")
            else:
                result = usrInput
                correctVal = True
    return result

def getPlayerTag(msg, currVal):
    correctInput = False
    while (correctInput == False):
        usrInput = input("{} (Currently {}): ".format(msg, currVal))
        if (tagExists(usrInput)):
            correctInput = True
        else:
            if (usrInput != "*" and usrInput != "!exit!"):
                print("Error: Player does not exist.")
            elif (usrInput == "*"):
                usrInput = currVal
                correctInput = True
            else:
                  usrInput = "!exit!"
                  correctInput = True
    return usrInput

def registerTeam():
    print()
    print("- Team Registration")
    print("Input '!exit!' at any time to quit")
    print()
    teamName = input("Please input the name of the team you would like to register: ")
    if (teamExists(teamName)):
        print("Error: Team already exists.")
    else:
        tag1 = input("Enter the tag of the first player on the team: ")
        if (tagExistsNoMsg(tag1) == False):
            print("Error: Tag does not exist.")
        elif (tag1 != "!exit!"):
            tag2 = input("Enter the tag of the second player on the team: ")
            if (tagExistsNoMsg(tag2) == False):
                print("Error: Tag does not exist.")
            elif (tag2 != "!exit!"):
                wins = getIntegerInput("Enter this team's number of wins: ")
                if (wins != "!exit!"):
                    losses = getIntegerInput("Enter this team's number of losses: ")
                    if (losses != "!exit!"):
                        points = getIntegerInput("Enter this team's number of points: ")
                        if (points != "!exit!"):
                            query = ("insert into team values(%s, %s, %s, %s, %s, %s)")
                            cursor.execute(query, (teamName, tag1, tag2, wins, losses, points))
                            query = ("select * from team where tname = '{}'").format(teamName)
                            cursor.execute(query)
                            for (everything) in cursor:
                                print(everything)
                            cursor.execute("commit")
    mainMenu()

def updateTeam():
    print()
    print("- Update Team")
    print("Input '!exit!' at any time to quit")
    print()
    teamName = input("Please input the name of the team you would like to update: ")
    query = ("select * from team")
    cursor.execute(query)
    foundTeam = False
    for (tn, t1, t2, w, l, p) in cursor:
        if (teamName == tn):
            foundTeam = True
            oldTag1 = t1
            oldTag2 = t2
            oldWins = w
            oldLosses = l
            oldPoints = p
    if (foundTeam == False):
        print("Error: Team not found.")
    else:
        print("Updating team {}. Input '*' at any time to leave the following fields unchanged:".format(teamName))
        newT1 = getPlayerTag("Input the first team member's tag", oldTag1)
        if (newT1 != "!exit!"):
            newT2 = getPlayerTag("Input the second team member's tag", oldTag2)
            if (newT2 != "!exit!"):
                newW = getPlayerStatus("Input the number of wins for this team", oldWins)
                if (newW != "!exit!"):
                    newL = getPlayerStatus("Input the number of losses for this team", oldLosses)
                    if (newL != "!exit!"):
                        newP = getPlayerStatus("Input the number of points for this team", oldPoints)
                        if (newP != '!exit!'):
                            query = ("update team set p1_tag = %s, p2_tag = %s, wins = %s, losses = %s, points = %s where tname = %s")
                            cursor.execute(query, (newT1, newT2, newW, newL, newP, teamName))
                            query = ("select * from team where tname = '{}'").format(teamName)
                            cursor.execute(query)
                            for (everything) in cursor:
                                print(everything)
                            cursor.execute("commit")
    mainMenu()
    
def reportDoublesSet():
    print()
    print("- Report Doubles Set")
    print("Enter '!exit!' at any time to quit.")
    print()
    setID = input("Please enter the round and set number (e.g. 'WR1-2', 'LR3-4', 'GF'): ")
    if (setID != "!exit!"):
        tournamentID = input("Please enter the tournament abbreviation (e.g. 'PP-4', 'JRWI-6'): ")
        if (tournamentID != "!exit!"):
            query = ("select * from tournament")
            cursor.execute(query)
            foundTournament = False
            for (myId, myName, myVenue, myDate, myEntrants) in cursor:
                if (tournamentID == myId):
                    foundTournament = True
            if (foundTournament == False):
                print("Error: Tournament does not exist.")
            if (foundTournament):
                setUniqueID = "{}: {}".format(setID, tournamentID)
                query = ("select * from doubles_set")
                cursor.execute(query)
                isUnique = True
                for (thing1, thing2, thing3, thing4, thing5, thing6, thing7) in cursor:
                    if (setUniqueID == thing1):
                        isUnique = False
                        print("Error: Set ID already exists in database.")
                if (isUnique):
                    team1ID = input("Team 1 Name: ")
                    if (team1ID != "!exit!"):
                        query = ("select * from team")
                        cursor.execute(query)
                        foundTeam = False
                        for (t_name, p1_tag, p2_tag, t_wins, t_losses, t_points) in cursor:
                            if (team1ID == t_name):
                                foundTeam = True
                        if (foundTeam == False):
                            print("Error: Team 1 does not exist.")
                        else:
                            team2ID = input("Team 2 Name: ")
                            if (team2ID != "!exit!"):
                                foundTeam = False
                                cursor.execute(query)
                                for (t_name, p1_tag, p2_tag, t_wins, t_losses, t_points) in cursor:
                                    if (team2ID == t_name):
                                        foundTeam = True
                                if (foundTeam == False):
                                    print("Error: Team 2 does not exist.")
                                else:
                                    correctInput = False
                                    while (correctInput == False): 
                                        team1Score = input("Please enter Team 1's score: ")
                                        correctInput = True
                                        try:
                                            int(team1Score)    
                                        except ValueError:
                                            if (team1Score != "!exit!"):
                                                print("Error: Score must be an integer value.")
                                                correctInput = False
                                    if (team1Score != "!exit!"):
                                        correctInput = False
                                        while (correctInput == False):
                                            team2Score = input("Please enter Team 2's score: ")
                                            correctInput = True
                                            try:
                                                int(team2Score)
                                            except ValueError:
                                                if (team2Score != "!exit!"):
                                                    print("Error: Score must be an integer value.")
                                                    correctInput = False
                                        if (team2Score != "!exit!"):
                                            theWinner = input("Enter the winning team of the set: ")
                                            if (theWinner != "!exit!"):
                                                while (team1ID != theWinner and team2ID != theWinner):
                                                    print("Error: That team did not play in this set.")
                                                    theWinner = input("Enter the winner of the set: ")
                                                query = ("insert into doubles_set values(%s, %s, %s, %s, %s, %s, %s)")
                                                cursor.execute(query, (setUniqueID, tournamentID, team1ID, team2ID, team1Score, team2Score, theWinner))
                                                query = ("select * from doubles_set where dset_id = '{}'".format(setUniqueID))
                                                cursor.execute(query)
                                                for (everything) in cursor:
                                                    print("{}".format(everything))
                                                cursor.execute("commit")
    mainMenu()

def showTeamRankings():
    print()
    print("- Team Rankings: ")
    query = ("select tname, points from team order by points desc")
    cursor.execute(query)
    i = 1
    for (tag, points) in cursor:
        print("{}). {}".format(str(i), tag))
        i = i+1
    mainMenu()

def showTeamSetHistory():
    print()
    print("- Team Set History: ")
    teamName = input("Please enter the team whose set history you would like to see: ")
    query = ("select * from team")
    cursor.execute(query)
    foundTeam = False
    for (t_name, p1_tag, p2_tag, t_wins, t_losses, t_points) in cursor:
        if (t_name == teamName):
            foundTeam = True
    if (foundTeam):
        query = ("select * from doubles_set where t1_name = '{}' or t2_name = '{}'").format(teamName, teamName)
        cursor.execute(query)
        print()
        print("{}'s set history: ".format(teamName))
        opponentName = ""
        myScore = 0
        for (op1, op2, op3, op4, op5, op6, op7) in cursor:
            if (op3 == teamName):
                opponentName = op4
                myScore = op5
                opScore = op6
            else:
                opponentName = op3
                myScore = op6
                opScore = op5
            winStatus = "Defeat"
            if (op7 == teamName):
                winStatus = "Victory"
            
            print("Set ID: {} | Played Against: {} | Result: {} | Score: {}-{}".format(op1, opponentName, winStatus, myScore, opScore))
    else:
        print("Error: Team not found.")
    mainMenu()

def showTeamTournamentHistory():
    print()
    print("- Team Tournament History: ")
    teamName = input("Please enter the team whose tournament history you would like to see: ")
    query = ("select * from team")
    cursor.execute(query)
    foundTeam = False
    for (t_name, p1_tag, p2_tag, t_wins, t_losses, t_points) in cursor:
        if (t_name == teamName):
            foundTeam = True
    if (foundTeam):
        query = ("SELECT doubles_set.tournament_id, tname, tdate FROM doubles_set, tournament WHERE doubles_set.tournament_id = tournament.tournament_id AND (t1_name = '{}' OR t2_name = '{}')").format(teamName, teamName);
        cursor.execute(query)
        print()
        print("{}'s tournament history: ".format(teamName))
        for (tid, tname, tdate) in cursor:
            print("{} ({})".format(tname, tdate))
    else:
        print("Error: Team not found.")
    mainMenu()
    

def editDoublesSet():
    print()
    print("- Edit Doubles Set: ")
    print("Input '!exit!' at any time to quit.")
    print()
    setID = input("Enter the unique ID of the set you want to modify (in the form of RR#-#: TT-#): ")
    if (setID != '!exit!'):
        query = ("select * from doubles_set")
        cursor.execute(query)
        foundSet = False
        for (q1, q2, q3, q4, q5, q6, q7) in cursor:
            if (q1 == setID):
                foundSet = True
                oldT1Name = q3
                oldT2Name = q4
                oldT1Score = q5
                oldT2Score = q6
                oldWinner = q7
        if (foundSet == False):
            print("Error: Set not found.")
        else:
            print("Input '*' in any of the following categories to leave unchanged.")
            print()
            #Get T1 Name
            t1Name = input("Team 1's Name (Currently {}): ".format(oldT1Name))
            if (t1Name != "!exit!" and (t1Name == "*" or teamExists(t1Name))):    
                #Get T2 Name
                t2Name = input("Team 2's Name (Currently {}): ".format(oldT2Name))
                if (t2Name != "!exit!" and (t2Name == "*" or teamExists(t2Name))):
                    #Get T1 Score
                    newT1Score = getPlayerStatus("Team 1's Score", oldT1Score)
                    if (newT1Score != '!exit!'):
                        #Get T2 Score
                        newT2Score = getPlayerStatus("Team 2's Score", oldT2Score)
                        if (newT2Score != '!exit!'):
                            #Get Winner
                            if (t1Name == "*"):
                                t1Name = oldT1Tag
                            if (t2Name == "*"):
                                t2Name = oldT2Tag
                            newWinner = input("Set Winner (Currently {}): ".format(oldWinner))
                            if (newWinner != "!exit!" and (newWinner == t1Name or newWinner == t2Name or newWinner == "*")):
                                if (newWinner == "*"):
                                    newWinner = oldWinner
                                query = ("UPDATE doubles_set SET t1_name = %s, t2_name = %s, t1_score = %s, t2_score = %s, winner = %s WHERE set_id = %s")
                                cursor.execute(query, (t1Name, t2Name, newT1Score, newT2Score, newWinner, setID))
                                query = ("select * from doubles_set where set_id = '{}'").format(setID)
                                cursor.execute(query)
                                for (everything) in cursor:
                                    print(everything)
                                cursor.execute("commit")
    mainMenu()

def managementFunctions():
    print()
    print("~ Management Functions Menu ~")
    print()
    print("Please select an option: ")
    print("1). Create tournament")
    print("2). Register venue")
    print("3). Update character rank")
    print("4). I wrote a function so that my grade wouldn't get docked for not having triggers in my database.")
    print("5). Quit")

    option = getUserInput(5, 1)
    if (option == 1):
        createTournament()
    elif (option == 2):
        registerVenue()
    elif (option == 3):
        updateCharacterRank()
    elif (option == 4):
        rebrandingAsAMarketingStrategy()
    elif (option == 5):
        mainMenu()

#This is a horrible function, don't use it
def rebrandingAsAMarketingStrategy():
    print("- This is about to get really dumb.")
    print()
    print("Basically what's happening here is I'm changing the name of this tournament and that makes a trigger increment the total number of entrants of that tournament by one. The result is not committed because this is not desirable behavior.")
    print()
    print("For reference, here's what the current tournament table looks like: ")
    query = ("select * from tournament")
    print()
    cursor.execute(query)
    for (everything) in cursor:
        print(everything)
    print()
    newName = input("No backing out now. Tell me what you want to rename Friday Night Smash 15 to: ")
    print("Ok got it.")
    query = ("update tournament set tname = '{}' where tname = 'Friday Night Smash 15' ".format(newName))
    cursor.execute(query)
    print("Now the table looks like this:")
    query = ("select * from tournament")
    cursor.execute(query)
    for (everything) in cursor:
        print(everything)
    mainMenu()

def tournamentIDExists(t_id):
    query = ("select * from tournament")
    cursor.execute(query)
    for (tournament_id, tname, vname, tdate, entrants) in cursor:
        if (t_id == tournament_id):
            return True
    return False

def tournamentExists(tourName):
    query = ("select * from tournament")
    cursor.execute(query)
    for (tournament_id, tname, vname, tdate, entrants) in cursor:
        if (tourName == tname):
            return True
    return False

def venueExists(venName):
    query = ("select * from venue")
    cursor.execute(query)
    for (vname, city) in cursor:
        if (venName == vname):
            return True
    return False

def createTournament():
    print()
    print("- Tournament Creation")
    print("Input '!exit!' at any time to quit")
    print()
    tournamentID = input("Please enter the ID of the tournament you would like to create: ")
    if (tournamentID != "!exit!"):
        if (tournamentIDExists(tournamentID)):
            print("Error: Tournament ID already exists.")
        else:
            tournamentName = input("Please enter the name of the tournament: ")
            if (tournamentExists(tournamentName)):
                print("Error: Tournament already exists.")
            elif (tournamentName != "!exit!"):
                venueName = input("Please enter the name of the venue where the tournament will take place: ")
                if (venueExists(venueName) == False):
                    print("Error: Venue does not exist.")
                elif (venueName != "!exit!"):
                    tourDate = input("Please enter the date that the tournament will take place (YYYY-MM-DD): ")
                    if (tourDate != "!exit"):
                        entrants = input("Please enter the amount of entrants in the tournament: ")
                        if (entrants != "!exit!"):
                            query = ("insert into tournament values(%s, %s, %s, %s, %s)")
                            cursor.execute(query, (tournamentID, tournamentName, venueName, tourDate, entrants))
                            print()
                            print("- Tournament successfully added")
                            query = ("select * from tournament where tournament_id = '{}'").format(tournamentID)
                            cursor.execute(query)
                            for (everything) in cursor:
                                print(everything)
                            cursor.execute("commit")
    mainMenu()

def registerVenue():
    print()
    print("- Register Venue")
    print("Input '!exit!' at any time to quit")
    print()
    venueName = input("Please enter the name of the venue: ")
    if (venueExists(venueName)):
        print("Error: Venue already exists")
    elif (venueName != "!exit!"):
        city = input("Please enter the city where the venue is located: ")
        if (city != "!exit"):
            query = ("insert into venue values(%s, %s)")
            cursor.execute(query, (venueName, city))
            print()
            print("- Venue successfully registered")
            query = ("select * from venue where vname = '{}'").format(venueName)
            cursor.execute(query)
            for (everything) in cursor:
                print(everything)
            cursor.execute("commit")
    mainMenu()

def updateCharacterRank():
    print()
    print("- Updating Character Rank")
    print("Input '!exit!' at any time to quit")
    print()
    name = input("Please enter the name of the character being updated: ")
    exists = charExists(name)
    while exists != True:
        name = input("Please try again: ")
        exists = charExists(name)
    if (name != "!exit!"):
        rank = input("Enter the new rank of the character: ")
        correctInput = False
        while (correctInput == False):
            try:
                rank = int(rank)
                correctInput = True
            except ValueError:
                if (rank != "!exit!"):
                    print("Error: Rank must be an integer value.")
                else:
                    correctInput = True                
        if (rank != "!exit!"):
            currRank = 0
            cursor.fetchall()
            query = ("update tournament_character set ranking = '{}' where cname = '{}'".format(rank, name))
            cursor.execute(query)
            query = ("select * from tournament_character where cname = '{}'".format(name))
            cursor.execute(query)
            for (everything) in cursor:
                print(everything)
    mainMenu()

def usageRankings():
    print("\n"
          "~ Usage Rankings Menu ~\n"
          "\n"
          "Please select an option:\n"
          "1). Rank character usage\n"
          "2). Rank tournament attendance\n"
          "3). Rank cities by player density\n"
          "4). Rank cities by player ranking\n"
          "5). Rank cities by tournament density\n"
          "6). Quit")

    option = getUserInput(6, 1)
    if (option == 1):
        rankCharacterUsage()
    elif (option == 2):
        rankTourAttendance()
    elif (option == 3):
        rankCitiesByPlayerDens()
    elif (option == 4):
        rankCitiesByPlayerRank()
    elif (option == 5):
        rankCitiesByTourDens()
    elif (option == 6):
        mainMenu()

def rankCharacterUsage():
    print("\n"
          "- Rank Character Usage\n"
          "\n")
    cursor.callproc('rankCharUsage', args=())
    i = 1
    for result in cursor.stored_results():
        for (cname, rank) in result:
            print("{}). {}".format(i, cname))
            i = i+1
    mainMenu()
        

def rankTourAttendance():
    print("\n"
          "- Rank Tournament Attendance\n")

    query = ("select tname, entrants from tournament group by entrants desc")
    cursor.execute(query)
    i = 1
    for (tname, entrants) in cursor:
        print("{}). {}: {} entrants".format(i, tname, entrants))
        i += 1
    mainMenu()

def rankCitiesByPlayerDens():
    print("\n"
          "- Rank Cities by Player Density\n")

    query = ("select city, count(city) as amount from player group by city desc")
    cursor.execute(query)
    i = 1
    for (city, amount) in cursor:
        print("{}). {}: {} players".format(i, city, amount))
        i += 1
    mainMenu()

def rankCitiesByPlayerRank():
    print("\n"
          "- Rank Cities by Player Ranking\n")

    query = ("select city, avg(points) from player group by city order by avg(points) desc")
    cursor.execute(query)
    i = 1
    for (city, avgPoints) in cursor:
        print("{}). {}: {} average points from players".format(i, city,avgPoints))
        i += 1
    mainMenu()

def rankCitiesByTourDens():
    print("\n"
          "- Rank Cities by Tournament Density\n")

    query = ("select city, count(city) as amount from tournament natural join venue group by city order by count(city) desc")
    cursor.execute(query)
    i = 1
    for (city, amount) in cursor:
        if (amount == 1):
            print("{}). {}: {} tournament".format(i, city, amount))
        else:
            print("{}). {}: {} tournaments".format(i, city, amount))
        i += 1
    mainMenu()

#-----------------------------------------------------------------------------------------------------------------------

#Example of transaction
def updateStats(winner, loser):
    #Start of transaction
    cursor.execute("start transaction")
    query = ("select * from player where tag = '{}'".format(winner))
    cursor.execute(query)
    for (player_id, tag, city, wins, losses, points) in cursor:
        currWins = wins
        currWins += 1
        query = ("update player set wins = '{}' where tag = '{}'".format(currWins, winner))
        cursor.execute(query)
    query = ("select * from player where tag  = '{}'".format(loser))
    cursor.execute(query)
    for (player_id, tag, city, wins, losses, points) in cursor:
        currLosses = losses
        currLosses += 1
        query = ("update player set losses = '{}' where tag = '{}'".format(currLosses, loser))
        cursor.execute(query)
    #End of transaction
    cursor.execute("commit")

#This function should only ever be called when editing a set
def revertStats(oldWinner, oldLoser):
    cursor.execute("start transaction")
    query = ("select * from player where tag = '{}'".format(oldWinner))
    cursor.execute(query)
    for (player_id, tag, city, wins, losses, points) in cursor:
        currWins = wins
        currWins -= 1
        query = ("update player set wins = '{}' where tag = '{}'".format(currWins, oldWinner))
        cursor.execute(query)
    query = ("select * from player where tag  = '{}'".format(oldLoser))
    cursor.execute(query)
    for (player_id, tag, city, wins, losses, points) in cursor:
        currLosses = losses
        currLosses -= 1
        query = ("update player set losses = '{}' where tag = '{}'".format(currLosses, oldLoser))
        cursor.execute(query)
    #End of transaction
    cursor.execute("commit")

mainMenu()

cnx.close()
