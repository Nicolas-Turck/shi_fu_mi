from functions_game import *
import random
print("~~~~~~~~~~WELCOMME SHI FU MI~~~~~~~~~~\n")
# i create many variable to reuse after
user_score= 0
program_score= 0
# i declae name equal the return of the function nameUser
name = nameUser() 
# loop for the choice of user
while 1: 
    # i drisplay the menu of the game
    print("\n~~~~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~~~~\n\n                1:Play \n                2:Score \n                3:Help \n                4:Exit")
    user_entry = input("\n{} Enter number corresponding of your choice:\n".format(name)) 
    #condition if user enter is no valid
    if user_entry != "1" and user_entry != "2" and user_entry != "3" and user_entry != "4":
        print("{} enter a number".format(name))
    if user_entry == "1":
        print(">>>>>>>>>>>>START GAME<<<<<<<<<<<<<")
        #ask the function with parameters
        gamePlay(name, user_score, program_score)
    if user_entry == "2": 
        print("sorry no score")
    if user_entry == "3":
        #ask the function  
        helpGame()
    if user_entry == "4":
        print("~~~~~~~~~~~~~~~~{}~~~~~~~~~~~~~~~~~~".format(name))
        print("\n~~~~~~~~~~~~~~GOOD BYE~~~~~~~~~~~~~")
        exit() 
