import random
print("Choose Rock , Paper or Scissor")
user_choice=str(input())
print("Your Choice ",user_choice)
lst=['Rock' , 'Paper' ,'Scissor']
comp_choice = random.choice(lst)
print("Computer Choice",comp_choice)

if user_choice =="Rock" or 'R' or 'r' or 'rock' and comp_choice=='Paper':
    print("You lost !")
elif  user_choice=="paper" or 'R' or 'r' or 'Paper' and comp_choice=='Rock':
    print("You win !")
elif  user_choice=="paper" or 'R' or 'r' or 'Paper' and comp_choice=='Scissor':
    print("You lost !")
elif  user_choice=="Scissor" or 'S' or 's' or 'scissor' and comp_choice=='paper':
    print("You win !")
elif user_choice =="Rock" or 'R' or 'r' or 'rock' and comp_choice=='Scissor':
    print("You win !")
elif  user_choice=="Scissor" or 'S' or 's' or 'scissor' and comp_choice=='Rock':
    print("You lost !")
