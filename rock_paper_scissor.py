#program to create the rock paper scissor game application.

import random
item_list=["Rock","Paper","Scissor"]

user_choice=input("Enter your move=Rock,Paper,Scissor=")
comp_choice=random.choice(item_list)

print("User choice=",user_choice,"Computer choice=",comp_choice)

if user_choice==comp_choice:
    print("Both have the same move= Match Tie")

elif user_choice=="Rock":
    if comp_choice=="Paper":
        print("Paper covers Rock=Computer Win")
    else:
        print("Rock Smashes scissor=You win")

elif user_choice=="Paper":
    if comp_choice=="Scissor":
        print("Scissor cuts paper=Compute win")
    else:
        print("Paper covers rock=You win")

elif user_choice=="Scissor":
    if comp_choice=="Paper":
        print("Scissor cuts paper=You win")
    else:
        print("Rock Smashes scissor=Computer win")