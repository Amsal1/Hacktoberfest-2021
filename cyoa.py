name=input("What's your name?")
print("Treasure Hunter, a custom story by " + name )
print("You are a brave explorer that was recognized by the world and found an ancient Mayan temple!")
opt1=input("Do you walk in? y/n?")
opt2=""
opt3=""
opt4=""
if opt1=="y":
    print("You walk in, your footsteps echoing in the dark. You turn on a flashlight and came across two paths.")
    opt2=input("You look down the first path and see jewels glinting in the darkness. You look down the left and hear a low hissing sound like snakes. Which path did you take? r/l? ")

    if opt2=="r":
        print("You walk down the path and found a treasure box stuffed with gems! You stuff a few handfuls of diamond, ruby, and sapphire into your backpack, and come across another crossroad.")
   
    opt3=input("At the second intersection, you peer into the darkness and don't see anything. The choice is your's to make. r/l? ")
    
    if opt3=="l":
        print("You found the treasure room! You walked in and found ancient treasures!")

    opt4=input("The door closes on you! You're trapped! Do you give up hope or keep looking? give up/ keep looking? ")

    if opt4=="keep looking":
        print("You kept looking, and found a piston mechanism that led you up to a stairway out. You escaped with a ton of jewels, and a story to be told for generations to come!")

if opt1=="n":
    print("You return and report your findings. You are stripped of your rights as an adventurer and are looked down upon as a coward.")

if opt2=="l":
        print("You walk down the descending staircase and look up. A venomous spider thought to be long extinct bit you and as your vision faded, you were alone.")

if opt3=="r":
        print("You find the Emperor's tomb. You decided to take the coffin up for the museums. But as you did, the lid was pushed off, and the ankhet the emperor was wearing cursed you to be forever stuffed into a bottle.")

if opt4=="give up":
    print("The world forgot you and your name fades, as your bones turn to dust...")
    
