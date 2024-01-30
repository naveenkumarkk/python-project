import random
import sys
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print('')
playerChoice = input("Enter your choice: \n 1 for Rock \n 2 for Scissors \n 3 for Paper \n\n")
player = int(playerChoice)

if player < 1 or player > 3 or player is None:
    sys.exit('You must enter value between 1,2,3 .')

computerChoice = random.choice('123')
computer = int(computerChoice)
print('')
print('You chose ' + str(RPS(player)).replace('RPS.', '') + '.')
print('Computer chose ' + str(RPS(computer)).replace('RPS.', '') + '.')
print('')

pythonWins = 'Python Wins'
humanWins = 'Human Wins'
if computer == 1 and player == 2:
    print(pythonWins)
elif computer == 2 and player == 1:
    print(humanWins)
elif computer == 3 and player == 2:
    print(humanWins)
elif computer == 2 and player == 3:
    print(pythonWins)
elif computer == 1 and player == 3:
    print(humanWins)
elif computer == 3 and player == 1:
    print(pythonWins)
elif computer == player:
    print('Draw')
