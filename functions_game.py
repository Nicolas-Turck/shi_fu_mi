import random #import random method to prog choice

def gamePlay(name, user, prog):
    while user != 3 and prog != 3: #loop while  user or programm not 3 points display the choice
            print("               1:stone\n               2:leaf\n               3:scissors\n") #displays numbers and items
            userAnswers = input("{} enter number of your choice:\n".format(name)) #request to user enter a number of is choice

            while userAnswers != "1" and userAnswers != "2" and userAnswers != "3":# loop until  user enters a valid choice
                userAnswers = input("{} enter number of your choice:".format(name)) #request to user enter a number of his choice
                print("entry autorized number")

            prg = str(random.randint(1, 3)  )#prog choice a random number with the method random
            print("program choice : {}\n".format(prg)) #display program choice

            if userAnswers == prg or prg == userAnswers: #condition for answer user and program
                print("{} choice {} program choice {}".format(name, userAnswers, prg)) #return the choice with method format
                print(">>>>>>equality<<<<<<\n")
                user= user+0 #no add points to user and program score
                prog = prog+0

            elif prg == "1" and userAnswers == "2": #conditions for user and program answer
                print("{} choice {} program choice {}".format(name, userAnswers, prg)) #return the choice with method format
                print("~~~~~~~~~~~~~{} you win~~~~~~~~~~~~\n".format(name))
                user = user+1    #add pointsto user score

            elif prg == "2" and userAnswers == "3": #conditions for user and program answer
                print("{} choice {} program choice {}".format(name, userAnswers, prg)) #return the choice with method format
                print("~~~~~~~~~~~~~{} you win~~~~~~~~~~~~\n".format(name))
                user = user+1  #add points to user  score

            elif prg == "3" and userAnswers == "1": #conditions for user and program answer
                print("{} choice {} program choice {}".format(name, userAnswers, prg)) #return the choice with method format
                print("~~~~~~~~~~~~~{} you win~~~~~~~~~~~~\n".format(name))
                user = user+1 #add points to user score

            else:    #conditions for user and program answer
                print("{} choice {} program choice {}".format(name, userAnswers, prg)) #return the choice with method format
                print("~~~~~~~~~~~~~ you loose~~~~~~~~~~~~\n")
                prog = prog+1 #add points program score

            print("{} your score : {}".format(name, user))#display name and score of user with method format
            print("program score : {}\n".format(prog))#display score of program
            print("**************************************")

            calcScore(name, user, prog)
    return user


def nameUser(): #this function registered a name enter by player or assign a pseudo to player
    print("~(~)~(~)~(~)~(~)~(~)~(~)~(~)~(~)~")
    name = input("enter your name :") #request to user enter is name
    name = name.upper() #transformed user name in uppercase
    if name == "": #if user press enter and no entry name
        name = "TUX" #name choice TUX to username
    return name #the function return name player for continue game and reuse name in game

def calcScore(name, user, prog): #this function calculated the score of user and program
    score_all = {}
    scorUser = print("your score {} and program score {}".format(user, prog)) #display score
    if user == 3 : #if user score is equal 3 the function print win and add name and score in a dict 'score'
        score_all.update({name : +1})
        win = print("~~~~~~<<<<<<|**YOU WIN**|>>>~~~~~~~~~")
        #print(score)
        return win, scorUser, score_all #fonction return action print and dict score modify

    elif prog == 3: #if program score is equal 3 the function print loose and add name winner in dict 'score
        score_all.update({"prog" : +1})
        loose = print("~~~~~~~~<<<<|**PROG WIN**|>>>>~~~~~~~")
        #print(score)
        return loose, score_all#fonction return action print and dict score modify

def helpGame(): #this function display the rules of the game
    print("~~~~~~~~~~RULES OF THE GAME~~~~~~~~~~\n")#display help game
    print("     its game is very easy \n     you play versus the program \n     enter number of items you choice")
    print("     the stone wins scissors, the leaf wins the stones \n     and the scissor wins the leaf")
    print("     the winners is the first with 3 points")
