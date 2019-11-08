import sys
print("~~~~~~~~~~WELCOMME SHI FU MI~~~~~~~~~~\n")


def userChoice():#create function menu
    print("\n~~~~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~~~~\n\n                1:Play \n                2:Score \n                3:Help \n                4:Exit")
    
    userEntry = input("\nEnter number corresponding of your choice:\n")#request answer to user
    if userEntry == None:#if user no entry answer
        userChoice()#return to fonction userChoice
    if userEntry != "1" and userEntry != "2" and userEntry != "3" and userEntry != "4":#if user is no valide
        print("enter a number")#request enter a number 
        userChoice()#return to fonction userChoice
    if userEntry == "1":#if user answer is 1
        from functions_game import game#go to functions_game
        
    if userEntry == "2":#if user answer is 2
        print("\n~~~~~~~~~~~~~~~~SCORE~~~~~~~~~~~~~~~~")#display all score
        return userChoice()#return to function userChoice
    if userEntry == "3":#if user answer is 3
        print("~~~~~~~~~~RULES OF THE GAME~~~~~~~~~~\n")#display help game
        print("     its game is very easy \n     you play versus the program \n     enter number of items you choice")
        print("     the stone wins scissors, the leaf wins the stones \n     and the scissor wins the leaf")
        print("     the winners is the first with 3 points")
        return userChoice()#return to function_game
    if userEntry == "4":#if user answer is 4 display good bye and quit the game
        print("\n~~~~~~~~~~~~~~GOOD BYE~~~~~~~~~~~~~")
        sys.exit()
    
userChoice()