import random

option = ["Rock", "Paper", "Scissors"]

user_choice = input("Choose Rock, Paper or Scissors: ")
comp_choice = random.choice(option)

print("Your choice is: ", user_choice)
print("The computers choice is: ", comp_choice)

if (user_choice == comp_choice):
    print("It's a tie!")

elif(user_choice == "Rock" and comp_choice == "Scissors"):
    print("Rock smashed the Scissors! You win!")

elif(user_choice == "Rock" and comp_choice == "Paper"):
    print("Paper covered the Rock! You lose!")

elif(user_choice == "Scissors" and comp_choice == "Paper"):
    print("Scissors cut the Paper! You win!")

elif(user_choice == "Scissors" and comp_choice == "Rock"):
    print("Rock smashed the Scissors! You lose!")

elif(user_choice == "Paper" and comp_choice == "Rock"):
    print("Paper covered the Rock! You win!")

elif(user_choice == "Paper" and comp_choice == "Scissors"):
    print("Scissors cut the Paper! You lose!")