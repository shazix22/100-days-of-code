from random import randrange 
import random

def selector():
    print("Welcome to Games of Luck!!!Everything is completely by chance here!!")
    print("Which game would you like to play?")
    print("Game Options: Heads Or Tails (HT), Russian Roulette (RR), Dice (D), and Raffle (R)!")
    userInput = input()
    if userInput == "HT":
        print("Good Choice!")
        HT()
    elif userInput == "RR":
        print("Good Choice!")
        RR()
    elif userInput == "D":
        print("Good Choice!")
        D()
    elif userInput == "R":
        R()
    else:
        print("Sorry, that isn't option.Try again.")
        selector()

def HT():
    print("Welcome to Heads & Tails.")
    print("Place your bets! (H,T)")
    userInput = input()
    generator = randrange(2)
    if userInput == "H" or userInput == "Heads" or  userInput == "heads" or  userInput == "h":
        if generator == 0:
            print("It's Heads!!You won!!")
        elif generator == 1:
            print("oops, it's tails! you lost :(((")
    elif userInput == "T" or  userInput == "Tails" or  userInput == "tails" or userInput == "t":
        if generator == 0:
            print("oops, it's heads! you lost :(((")
        elif generator == 1:
            print("yayyy, its tails!! You won!!")
    else:
        print("Sorry, that's not an option :((. Try again!")
        HT()

def RR():
    # badNumber = generate a number from 0-5
    # generate = 0-5
    # if userInput == badNumber then lose
    print("Welcome to Russian Roulette.")
    print("Place your bets! (1-6)")
    userInput = int(input())
    badNumber = randrange(7)
    if userInput == badNumber: 
        print("The deadly number was ",badNumber)
        print("Your number was ",userInput)
        print("sorry, you died :(((")
        RR()
    elif userInput != badNumber:
        print("The deadly number was ",badNumber)
        print("Your number was ",userInput)
        print("yayyyy, you survived!")
        RR()
    elif userInput == 0 or userInput > 6:
        print("Sorry, that is not an option. Try Again!")
        RR()
    else:
        print("Sorry, that is not an option. Try Again!")
        RR()

def D():
    print("Welcome to Dice! Which dice would you like to pick?")
    print("Dice Options: 6 dice, 9 dice, 12 dice [6, 9, 12]")
    userInput = int(input())
    if userInput == 6:
        maxRange = 6
    elif userInput == 9:
        maxRange = 9
    elif userInput == 12:
        maxRange = 12
    else:
        print("That's not an option, Try again")
        D()
    
    print("Please select a number between 0 and", maxRange)
    goodNumber = randrange(maxRange)
    userInput = int(input())
    if userInput == goodNumber:
        print("The correct number was ", goodNumber)
        print("Your number was ", userInput)
        print("Congrats, you did it!")
        D()
    elif userInput != goodNumber:
        print("The correct number was ", goodNumber)
        print("Your number was ", userInput)
        print("Sorry, you lost")
        D()
    elif userInput == 0 or userInput > maxRange:
        print("Your number was ", userInput)
        print("That's not an option, please try again")
        D()
    else:
        print("Sorry, that is not an option. Try Again!")
        RR()

names = []

def addPlayers():
    print("Do you want to add another player? (Y/n)")
    yesOrNo = input()
    if yesOrNo == "y" or yesOrNo  == "Y":
        print("Please enter the Player's name")
        newPlayer = input()
        names.append(newPlayer)
        addPlayers()
    if yesOrNo == "n" or yesOrNo  == "N":
        print("Cool, Let the game begin...")
        print("Total Player Count: ", len(names) )
        print("List of all players:")
        for x in names:
            print("- ", x)
    

def R():
    print("Welcome to the raffle!")
    print("Please enter the Player's name")
    playerOne = input()
    names.append(playerOne)
    print("Please enter the Player's name")
    playerTwo = input()
    names.append(playerTwo)
    addPlayers()
    winner = random.choice(names)
    print("Which player do you guess will win?")
    userInput = input()
    print("Your guess was ", userInput)
    print("The winner was", winner)
    if userInput == winner:
        print("You win, congrats, play again?")
        addPlayers()
    else: 
        print("Sorry, you lost")
        addPlayers()   
    

    


selector()