#Version 1.1
#Author: Willy Martin
#May be copied and distributed without monetary gain.
import random
def character():
    playerInput = input("Enter your character : ")
    playerInput = playerInput.lower()
    return playerInput
def ai_character():
    player_list = ["rock","paper","scissors"]
    computerCharacter = (random.choice(player_list))
    return computerCharacter
def gameplay():
    print("Welcome to Rock, Paper, Scissors")    
    player_input = character()           
    computer_character = ai_character()
    if (player_input == computer_character):
        print("Tie Game")
    elif (player_input == "rock" and computer_character == "scissors" or player_input == "scissors" and computer_character == "paper" or player_input == "paper" and computer_character == "rock"):
        print(player_input + " beats " + computer_character)  
        print("You win!")  
    elif (player_input == "rock" and computer_character == "paper" or player_input == "scissors" and computer_character == "rock" or player_input == "paper" and computer_character == "scissors"):
        print(computer_character + " beats " + player_input)   
        print("The computer wins!")   
    else:
        print("ERROR: Invalid Game")        
gameplay()
