from art import logo
import random
import os

def hard():
    # presets
    lives = 5
    computer_number = random.randint(1,100)
    
    # loop
    while lives > 0:
        print(f"You have {lives} lives remaining.")
        guess = int(input("Make a guess. "))
        
        if guess > computer_number:
            print("too high")
            lives -= 1
        elif guess < computer_number:
            print("too low")
            lives -= 1
        else:
            print("You are victorious")
            break
        
    if lives == 0:
        print(f"You lost, number was {computer_number} :(")
    

    
def easy():
     # presets
    lives = 10
    computer_number = random.randint(1,100)
    
    # loop
    while lives > 0:
        print(f"You have {lives} lives remaining.")
        guess = int(input("Make a guess. "))
        
        if guess > computer_number:
            print("too high")
            lives -= 1
        elif guess < computer_number:
            print("too low")
            lives -= 1
        else:
            print("You are victorious")
            break
        
    if lives == 0:
        print(f"You lost, number was {computer_number} :(")




replay = True
while replay == True:

    os.system("cls")
    print(logo)
    print("Guess a number between 1 and 100")
    difficulty = input("Welcome to the guessing game. Choose a difficulty: type 'easy' or 'hard'")

    if difficulty == "easy":
        easy()
    else:
        hard()
        
    play_again = input("Would you like to play again? Type 'y' or 'n' ")
    
    if play_again == "n":
        replay = False
    

