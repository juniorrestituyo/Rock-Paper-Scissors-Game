rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

play = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
robot_play = random.randint(0,2)
rps = [rock, paper, scissors]

if play == robot_play:
  print(rps[play])
  print("Computer chose:")
  print(rps[robot_play])
  print("Tie")
  
elif play == 0 and robot_play == 1:
  print(rps[play])
  print("Computer chose:")
  print(rps[robot_play])
  print("You lose")

elif play == 0 and robot_play == 2:
  print(rps[play])
  print("Computer chose:")
  print(rps[robot_play])
  print("You win")

elif play == 1 and robot_play == 0:
  print(rps[play])
  print("Computer chose:")
  print(rps[robot_play])
  print("You win")

elif play == 1 and robot_play == 2:
  print(rps[play])
  print("Computer chose:")
  print(rps[robot_play])
  print("You lose")

elif play == 2 and robot_play == 0:
  print(rps[play])
  print("Computer chose:")
  print(rps[robot_play])
  print("You lose")

elif play == 2 and robot_play == 1:
  print(rps[play])
  print("Computer chose:")
  print(rps[robot_play])
  print("You win")