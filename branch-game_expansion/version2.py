from random import choice

question = int(input("How many times you wanna play? "))
counter = 0 
win_counter = 0

object_list = ["rock", "paper", "scissors"]

while question > counter:
    hidden_object = choice(object_list)
    
    user_objcet = input("Enter: 'paper', 'rock' or 'scissors': ")

    if  hidden_object == user_objcet:
        print("Continue")

    if hidden_object == "rock" and user_objcet == "paper":
        print("You've won!")
        counter += 1
        win_counter += 1
    elif hidden_object == "rock" and user_objcet == "scissors":
        print("You've lose.")
        counter += 1

    if hidden_object == "paper" and user_objcet == "scissors":
        print("You've won!")
        counter += 1 
        win_counter += 1
    elif hidden_object == "paper" and user_objcet == "rock":
        print("You've lose.")
        counter += 1
    
    if hidden_object == "scissors" and user_objcet == "rock":
        print("You've won!")
        counter += 1
        win_counter += 1
    elif hidden_object == "scissors" and user_objcet == "paper":
        print("You've lose.")
        counter += 1

    if question == counter:
        try:
            all = round(win_counter / counter, 2) * 100
        except ZeroDivisionError:
            print(f"Game over, your winrate is 0 % for {question} games.")
        else:
            print(f"\nGame over, your winrate is {all}% for {question} games.")
        