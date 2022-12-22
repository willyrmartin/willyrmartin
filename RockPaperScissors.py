import random
print("Welcome to Rock, Paper, Scissors")
def character():
    playerInput = input("Enter your character : ")
    return playerInput
player_input = character()           
player_input = player_input.lower()
player_list = ["rock","paper","scissors"]
computer_character = (random.choice(player_list))
if (player_input == computer_character):
    print("Tie Game")
elif (player_input == "rock" and computer_character == "scissors"):
    print(player_input + " beats " + computer_character)    
elif (player_input == "scissors" and computer_character == "paper"):
    print(player_input + " beats " + computer_character) 
elif (player_input == "paper" and computer_character == "rock"):
    print(player_input + " beats " + computer_character)   
elif (player_input == "rock" and computer_character == "paper"):
    print(computer_character + " beats " + player_input)   
elif (player_input == "scissors" and computer_character == "rock"):
    print(computer_character + " beats " + player_input)    
elif (player_input == "paper" and computer_character == "scissors"):  
    print(computer_character + " beats " + player_input)  
else:
    print("ERROR: Invalid Game")        