from random import choice

lst = ["rock", "paper", "scissors"]

while True:
    hidden_objeect = choice(lst)
    objct = input()
    if  hidden_objeect == objct:
        print("Continue")

    if hidden_objeect == "rock" and objct == "paper":
        print("You've won!")
        break
    elif hidden_objeect == "rock" and objct == "scissors":
        print("You've lose.")
        break

    if hidden_objeect == "paper" and objct == "scissors":
        print("You've won!")
        break
    elif hidden_objeect == "paper" and objct == "rock":
        print("You've lose.")
        break
    
    if hidden_objeect == "scissors" and objct == "rock":
        print("You've won!")
        break 
    elif hidden_objeect == "scissors" and objct == "paper":
        print("You've lose.")
        break 