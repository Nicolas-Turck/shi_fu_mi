import random#import random method to prog choice
def game():#create function game
    print("~(~)~(~)~(~)~(~)~(~)~(~)~(~)~(~)~")
name = input("enter your name :")#request to user enter is name
name = name.upper()#transformed user name in uppercase
if name == "":#if user no entru name
    name = "TUX"#name choice TUX to username
score = {}#create dictionnary
user= int(0)#create variable user = 0
prog= (0)#create prog variable  = 0
while user != 3 and prog != 3:#while user or programm not 3 points display the choice
    print("               1:stone\n               2:leaf\n               3:scissors\n")
    userAnswers = input("{} enter number of your choice:\n".format(name))#request to user enter a number of is choice
    
