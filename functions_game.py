import random#import random method to prog choice
def game():#create function game
    print("~(~)~(~)~(~)~(~)~(~)~(~)~(~)~(~)~")
    name = input("enter your name :")#request to user enter is name
    name = name.upper()#transformed user name in uppercase
    if name == "":#if user no entru name
        name = "TUX"#name choice TUX to username

    score = {}#create dictionnary
    user= 0#create variable score user = 0
    prog= 0#create  variable score program  = 0

    while user != 3 and prog != 3:#while user or programm not 3 points display the choice
        print("               1:stone\n               2:leaf\n               3:scissors\n")#displays numbers and items
        userAnswers = input("{} enter number of your choice:\n".format(name))#request to user enter a number of is choice



        while userAnswers != "1" and userAnswers != "2" and userAnswers != "3":#loop until  user enters a valid choice
            userAnswers = input("{} enter number of your choice:".format(name))
            print("entry autorized number")

        prg = random.randint(1, 3)#prog choice a number
        print("program choice : {}\n".format(prg))#display program choice


        if userAnswers == "1" and prg == 2:
            print("your choice STONE and program choice LEAF ")
            print("~~~~~~~~~~~~~{} you loose~~~~~~~~~~~~\n".format(name))
            #condition of win or loose
            prog =  prog+1#add point




        if userAnswers == "2" and prg == 3:
            print("your choice LEAF and program choice SCISSORS")
            print("~~~~~~~~~~~~~{} you loose~~~~~~~~~~~~\n".format(name))
            prog =  prog+1#add point
            #condition of win or loose



        if userAnswers == "3" and prg == 1:
            print("your choice SCISSORS and program choice STONE")
            print("~~~~~~~~~~~~~{} you loose~~~~~~~~~~~~\n".format(name))
            prog =  prog+1#add point
            #condition of win or loose


        if prg == 1 and userAnswers == "2":
            print("your choice LEAF and program choice STONE")
            print("~~~~~~~~~~~~~{} you win~~~~~~~~~~~~\n".format(name))
            user = prog+1#add point
            #condition of win or loose


        if prg == 2 and userAnswers == "3":
            print("your choice SCISSORS and program choice LEAF")
            print("~~~~~~~~~~~~~{} you win~~~~~~~~~~~~\n".format(name))
            user = user+1#add point
            #condition of win or loose


        if prg == 3 and userAnswers == "1":
            print("your choice STONE and program choice SCISSORS")
            print("~~~~~~~~~~~~~{} you win~~~~~~~~~~~~\n".format(name))
            #condition of win or loose
            user = user+1#add point

        if userAnswers == prg:
            print(">>>>>>equality<<<<<<\n")

    print("{} your score : {}".format(name, user))#display score of user
    print("program score : {}\n".format(prog))#display score of program
    print("**************************************")
    if user == 3 :#condition if user win
        print("            |***********|")
        print("~~~~~~<<<<<<|**YOU WIN**|>>>~~~~~~~~~")
        print("            |***********|")
        print("your score {} and program score {}".format(user, prog))
        score.update({name : 1})#add score to dict score
        print(score)#print dict


    if prog == 3:#condition if program win
        print("            |************|")
        print("~~~~~~~~<<<<|**PROG WIN**|>>>>~~~~~~~")
        print("            |************|")
        print("your score {} and program score {}".format(user, prog))
        score.update({"bots" : 1})#add score to dict score
        print(score)#display score
