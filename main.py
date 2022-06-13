
import random

print("'R' for Rock\n 'S' for Scissors\n 'P' for Paper")
def game():
  possible_choices = ["R", "P", "S"]
  while True:
    choice = input("Please make your choice ('R', 'P' or 'S'):\n")
    player = choice.upper()
    if player not in possible_choices:
      print("Invalid pick, try again.")
      continue
    else:
      break
  CPU = random.choice(possible_choices)
  print(f"Player({player}) : CPU({CPU})")
  for item in player:
    if player != CPU:
      if player == "R":
        if CPU == "S":
          print("Rock smashes scissors. Player wins!")
        else:
          print("Paper covers rock. CPU wins!")
      elif player == "P":
        if CPU == "R":
          print("Paper covers rock. Player wins!")
        else:
          print("Scissors cuts paper. CPU wins!") 
      elif player == "S":
        if CPU == "P":
          print("Scissors cuts paper. Player wins!")
        else:
          print("Rock smashes scissors. CPU wins!")
    elif player == CPU:
      print("It's a tie.")
      game()
    else:
      print("Game terminated")
game()
     