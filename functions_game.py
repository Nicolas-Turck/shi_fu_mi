#import random method to prog choice
import random 

def gamePlay(name, user_score, program_score):
    """function to ask play answer and calculate 
    score of user and program and return score"""
    
    #loop while  user or programm not 3 points display the choice
    while user_score != 3 and program_score != 3: 
            print("               1:stone\n               2:leaf\n               3:scissors\n") 
            userAnswers = input("{} enter number of your choice:\n".format(name))
            # loop until  user enters a valid choice
            while userAnswers != "1" and userAnswers != "2" and userAnswers != "3":
                userAnswers = input("{} enter number of your choice:".format(name)) 
                print("entry autorized number")
            #prog choice a random number with the method random
            prg = str(random.randint(1, 3))
            print("program choice : {}\n".format(prg)) 
            #condition for answer user and program
            if userAnswers == prg or prg == userAnswers: 
                print("{} choice {} program choice {}".format(name, userAnswers, prg)) 
                print(">>>>>>equality<<<<<<\n")
                #no add points to user and program score
                user_score= user_score+0 
                program_score = program_score+0
            elif prg == "1" and userAnswers == "2": 
                print("{} choice {} program choice {}".format(name, userAnswers, prg)) 
                print("~~~~~~~~~~~~~{} you win~~~~~~~~~~~~\n".format(name))
                user_score = user_score+1    
            elif prg == "2" and userAnswers == "3":
                print("{} choice {} program choice {}".format(name, userAnswers, prg)) 
                print("~~~~~~~~~~~~~{} you win~~~~~~~~~~~~\n".format(name))
                user_score = user_score+1 
            elif prg == "3" and userAnswers == "1": 
                print("{} choice {} program choice {}".format(name, userAnswers, prg)) 
                print("~~~~~~~~~~~~~{} you win~~~~~~~~~~~~\n".format(name))
                user_score = user_score+1 
            else:  
                print("{} choice {} program choice {}".format(name, userAnswers, prg)) 
                print("~~~~~~~~~~~~~ you loose~~~~~~~~~~~~\n")
                program_score = program_score+1 
            #display name and score of user with method format
            print("{} your score : {}".format(name, user_score))
            print("program score : {}\n".format(program_score))
            print("**************************************")

            calcScore(name, user_score, program_score)
    return user_score


def nameUser(): 
    """this function registered a name enter by player or assign a pseudo to player"""
    print("~(~)~(~)~(~)~(~)~(~)~(~)~(~)~(~)~")
    name = input("enter your name :") 
    #transformed user name in uppercas
    name = name.upper() 
    if name == "": 
        name = "TUX"
    return name 

def calcScore(name, user_score, program_score): 
    """this function calculated the score of user and program"""
    score_all = {}
    scor_User = print("your score {} and program score {}".format(user_score, program_score)) 
    if user_score == 3 : 
        score_all.update({name : +1})
        win = print("~~~~~~<<<<<<|**YOU WIN**|>>>~~~~~~~~~")
        
        return win, scor_User, score_all 

    elif program_score == 3:
        score_all.update({"prog" : +1})
        loose = print("~~~~~~~~<<<<|**PROG WIN**|>>>>~~~~~~~")
        #print(score)
        return loose, score_all

def helpGame(): 
    """this function display the rules of the game"""
    print("~~~~~~~~~~RULES OF THE GAME~~~~~~~~~~\n")
    print("     its game is very easy \n     you play versus the program \n     enter number of items you choice")
    print("     the stone wins scissors, the leaf wins the stones \n     and the scissor wins the leaf")
    print("     the winners is the first with 3 points")
