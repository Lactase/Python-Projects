
import random


def RPS():
    options = {1: "rock", 2: "paper", 3: "scissors"}
    while True:
        player_op = input("Choose Rock, Paper or Scissors: ").lower()
        if (player_op == "rock" or player_op == "scissors" or player_op == "paper"):
            cpu_op = options[random.randint(1, 3)]
            if (player_op == cpu_op):
                return print(f"It was a tie! You both picked {player_op}")
                break
            elif (isWin(player_op, cpu_op)):
                return print(f"You won! The computer chose {cpu_op}")
                break
            elif (isLost(player_op, cpu_op)):
                return print(f"You lost! The computer chose {cpu_op}")
                break
        else:
            print("Invalid input, please check your spelling")
            break


def isWin(player, cpu):
    if (player == "rock" and cpu == "scissors"):
        return True
    if (player == "paper" and cpu == "rock"):
        return True
    if (player == "scissors" and cpu == "paper"):
        return True


def isLost(player, cpu):
    if (player == "paper" and cpu == "scissors"):
        return True
    if (player == "scissors" and cpu == "rock"):
        return True
    if (player == "rock" and cpu == "paper"):
        return True


RPS()
