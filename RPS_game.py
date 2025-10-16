import random as rnd
from art import text2art

is_running = True

def continue_playing():
    choice = input("Do you want to continue playing?").lower()
    if choice == 'no':
        global is_running 
        is_running = False

shapes_key = ['rock', 'paper', 'sizer']

shapes = {
'rock' : text2art('rock'),
'paper' : text2art('paper'),
'sizer' : text2art('sizer')
}
print("Welcome to rock paper sizer  game.")

while is_running:
    your_choice = input("rock or paper or sizer? :").lower()
    computer_choice = rnd.choice(shapes_key)
    print(f"computer {shapes[computer_choice]}")
    print(f"you{text2art(your_choice)}")

    if computer_choice == your_choice:
        print("Draw")
        continue_playing()

    elif computer_choice == 'rock' and your_choice == 'sizer' or computer_choice == 'paper' and your_choice == 'rock' or computer_choice == 'sizer' and your_choice == 'paper':
        print("You lose")
        continue_playing()

    elif computer_choice == 'paper' and your_choice == 'sizer' or computer_choice == 'sizer' and your_choice == 'rock' or computer_choice == 'rock' and your_choice == 'paper':
        print("You win")
        continue_playing()