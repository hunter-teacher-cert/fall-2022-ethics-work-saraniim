# gol.py
# Saranii Muller
# CSCI 77800 Fall 2022
# collaborators: Shana Henry
# consulted: Kate Maschmeyer
# 
#  * Conway's Game of Life by Team AreWeSentientYet?
#  * First Last
#  * collaborators: First Last, First Last
# 

# 
#    The Rules of Life:

#    Survivals:
#   * A living cell with 2 or 3 living neighbours will survive for the next generation.

#    Deaths:
#    * Each cell with >3 neighbours will die from overpopulation.
#    * Every cell with <2 neighbours will die from isolation.

#    Births:
#    * Each dead cell adjacent to exactly 3 living neighbours is a birth cell. It will come alive next generation.

#    NOTA BENE:  All births and deaths occur simultaneously. Together, they constitute a single generation.
#
def createNewBoard(rows, cols):
  #creates 2D board with a empty soace for each empty location
  board = [[" " for i in range(cols)] for j in range(rows)] 
  
  return board
#prints board
def printBoard(board):
 # how many rows
  rows = len(board)
 # how many columns 
  cols = len(board[0])
#loop that goes through rows and columns
  for x in range(rows):
    for y in range(cols):
      #end = - means end of line is " "
      print(board[x][y], end = " ")

  print()

#set values of r and c
def setCell(board, r, c, val):
#access elements using c and r
  board [r][c] = val
#Counts number of living neigbours of board[r][c] and returns it
def countNeighbours(board, r, c):
  count = 0 #initialize
  # First loop; start in the row above which is row-1 go through row until the   
  # row cvalue is less than or equal to row+1 which is the row below the target , 
  # increment up until stop point is reached
  # rown = row neighbor
  # coln = col neighbor
  for rown in range(r-1, r+2): #goes up to but doesn't include the last starts with the row above
    if rown >=0 and rown <len(board): #checks for in bound
    