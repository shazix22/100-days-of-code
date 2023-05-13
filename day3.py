def intro():
    print("Welcome to Treasure Island!")
    print("Your mission is to find the treasure")
    print("You're at a crossroads. Which path will you take, left or right? [left, right]")
    selector()

def death(reason):
    print("You died ", reason)
    retry()

def retry():
    print("Would you like to restart? [Yes, No]")
    userInput = input()
    if userInput == "Yes":
        intro()
    elif userInput == "No":
        print("okie bye ;333333")    
    else: 
        print("sorry i didnt understand")
        retry()

def fisherRide():
    print("After a day of waiting, a friendly fisher comes by and offers you a ride. Do you accept or decline? [accept, decline]")
    userInput = input()
    if userInput == "accept":
        print("""The friendly fisher turned out not to be so friendly. 
        He had ran out of fish food recently, and decided you were a cheaper alternative""")
        death("being fed to the fishies, it's a crazy world.")
    elif userInput == "decline":
        print("""The fisher donates some fish for your journey, also slipping in his business card with it, 
        and says he hopes that you'll cross paths once more before leaving. 
        Will you start a fire to cook the fish, or will you be mistrustful of his gift and go gather fruits? [fish, fruit]""")

        
    else: 
        print("sorry i didnt understand. Let me explain once more.")
        fisherRide()

def spooky():
    print("""You find shelter in the house for the night, but are plagued with mysterious voices in your dreams.
    Will you listen to the voices and attempt to aid them, or seek a new shelter the next morning? [listen, leave]""")
    userInput = input()
    if userInput == "leave":
        print("""You leave the safety the house afforded you, and get lost in the endlessness of the forest.
        You are eventually found again...by a pack of hungry wolves""")
        death("eaten by the wolves of the forest.Yummy!`")
    elif userInput == "listen":
        print("""The voices whisper clues to the location of the treasure,
        but also tell the story of the great sacrifice that comes with obtaining it.
        Will you follow their clues, or ignore them out of suspicion? [follow, ignore]""")
    else: 
        print("sorry i didnt understand. Let me explain once more.")
        spooky()  
    

def forest():
    print("you found it yayyyyy")




def selector():
    userInput = input()
    if userInput == "left":
        print("You come to a lake in the middle of the island. Do you swim or wait for a boat? [swim, wait]")
        userInput = input()
        if userInput == "swim":
            death("trying to swim to the island")
        elif userInput == "wait":
            fisherRide()
        else:
            print("sorry, i didn't understand. I'll give you a second chance; Do you wish to go left, or right?")
            selector()
    elif userInput == "right":
        print("You come to a spooky house in the middle of a dark forest. Do you enter the house before it gets dark, or wander the forest? [enter, wander]")
        userInput = input()
        if userInput == "enter":
            spooky()
        if userInput == "wander":
            forest()
    else:
        print("You cannot pick that option")

# def left():

intro()



def template():
    print("stuff")
    userInput = input()
    if userInput == "yes":
        print("""stuff""")
        death("dying")
    elif userInput == "no":
        print("""stuff""")
    else: 
        print("sorry i didnt understand. Let me explain once more.")
        template()
