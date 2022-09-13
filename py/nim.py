# nim.py
# Saranii Muller
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: Kate Maschmeyer

print("Welcome to Nim!")

stones = 12
stonesTaken = 0
# loop til the end
while stones > 0:
  print("Please pick how many stones to remove - between 1 and 3")
  stonesTaken = input()
  stonesTaken = int(stonesTaken)
  #calc remaining stones 
  stones -= stonesTaken
  print(f"You picked {stonesTaken}")
  print(f"There are {stones} remaining.")
  #check for win
  if stones == 0:
    print("you win!")
   
    break
  else:
    print(f"There are {stones} left. Computer's turn!")
    
  stonesTaken = 4 - stonesTaken
  print(f"The computer took {stonesTaken}")
  stones -= stonesTaken
  if stones == 0:
    print("Computer wins!")
  