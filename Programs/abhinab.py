import random
print("\n\t\t\t******* Game of Snake, Water and Gun *******\n")
print("     There are some rules in this game.These are:-")
print("\tRule no.1:- You need to choose snake, water or gun")
print('\tRule no.2:- To choose snake type 1, to choose water type 2 and to choose gun type 3')
print("\tRule no.3:- If you want to quit type 5")
print("\n\t\t\t    Ok then, Have fun!")

a = True
while a == True:
    def game(comp,user):
        if comp == 3 and user == 2:
            print(f"You win because the computer choose Gun")
        elif comp == 2 and user == 3:
            print(f"You lose because the computer choose Water")
        elif comp == 3 and user == 1:
            print(f"You Lose because the computer choose gun")
        elif comp == 1 and user == 3:
            print(f"You Win because the computer choose Snake")
        elif comp == 1 and user == 2:
            print(f"You Lose because the computer choose Snake")
        elif comp == 2 and user == 1:
            print(f"You Win because the computer choose Water")
        elif user == 5:
            print("\n\t\tYou quit the game.Thanks for Playing this game!")
            quit()
        elif user == comp :
            print("The game is draw")
        else:
            print("Warring: Donot enter any wrong number.Please check the rules again")

    comp = random.randint(1, 3)
    user = int(input('Your turn: '))
    game(comp, user)
