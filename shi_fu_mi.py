from functions_game import *
import random
print("~~~~~~~~~~WELCOMME SHI FU MI~~~~~~~~~~\n")
# i create many variable to reuse after
user= (0)
prog= (0)

name = nameUser() # i declae name equal the return of the function nameUser

while 1: #loop for the choice of user
    # i drisplay the menu of the game
    print("\n~~~~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~~~~\n\n                1:Play \n                2:Score \n                3:Help \n                4:Exit")
    userEntry = input("\n{} Enter number corresponding of your choice:\n".format(name)) #request answer to user

    if userEntry != "1" and userEntry != "2" and userEntry != "3" and userEntry != "4": #condition if user enter is no valid
        print("{} enter a number".format(name))#request enter a number

    if userEntry == "1":#loop if user answer  entry is 1
        print(">>>>>>>>>>>>START GAME<<<<<<<<<<<<<")
        gamePlay(name, user, prog)
         #function to calculate score of user and program and return score

    if userEntry == "2": #condition to display score dict
        print("sorry no score")



    if userEntry == "3": #conditions if  user answer is 3 display the rules of the game
        helpGame()

    if userEntry == "4":#if user answer is 4 display good bye and quit the game
        print("~~~~~~~~~~~~~~~~{}~~~~~~~~~~~~~~~~~~".format(name))
        print("\n~~~~~~~~~~~~~~GOOD BYE~~~~~~~~~~~~~")
        exit() #quit the program
