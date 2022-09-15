# gol.py
# Saranii Muller
# CSCI 77800 Fall 2022
# collaborators: Shana Henry
# consulted: Kate Maschmeyer & Kiana Herr
# 
#  * Conway's Game of Life by Team AreWeSentientYet?

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
      for coln in range(c-1,c+2):
        if coln >=0 and coln<len(board[r]):
          if rown ==r and coln == c:
            continue
          else: #if there is a neighbor
               #count the neighbors IF it's alive
               #if (neighbor == alive) 
            if board[rown][coln]== 'X':
              count = count+1
  return count

def getNextGenCell(board,r,c):
  #mise en place
  currentCell=board[r][c] #target cell as indicated in the main
  count = countNeighbours(board, r, c)
  nextCell = board[r][c]


  if(currentCell == 'X'):
    if(count == 2 or count ==3):
      nextCell = 'X'
      #if neighbors is less than 2, or greater than 3 then DIE
    else:
      nextCell = '+'
      #DEAD
  else:
    # if neighbors is exactly 3, reborn alive
    if(count==3):
      nextCell = 'X'
    else: #not, stay dead
      nextCell = '+'

  return nextCell

def genNextBoard(board):
  # get rows and cols from the given board
  rows = len(board)
  cols = len(board[0])
  #assemble the board using the parts already created 
  newBoard = createNewBoard(rows,cols)
  nextCell = '@'

  #traverse
  for i in range(rows):
    for j in range(cols):
      nextCell = getNextGenCell(board,i,j)
      setCell(newBoard,i,j,nextCell)

  return newBoard

board = createNewBoard(25,25) #initializer
    
    
# print board
print("\nWelcome to the Game of Life")
printBoard(board)

    
    
# breathe life into some cells:
setCell(board, 0, 0, 'X')
setCell(board, 0, 1, 'X')
setCell(board, 1, 0, 'X')

print("\nbreathe life into the cells")
printBoard(board)


print("\nTesting Count Neighbors")
c11 = countNeighbours(board, 1, 1 )  # should return 3
c01 = countNeighbours(board, 0, 1 )  # should return 2
c02 = countNeighbours(board, 0, 2 )  # should return 1
c55 = countNeighbours(board, 5, 5 )  # should return 0
print("(1,1) returns ",c11)
print("(0,1) returns ",c01)
print("(0,2) returns " ,c02)
print("(5,5) returns ", c55)

#def getNextGenCell(board,r,c )
print("\nTesting getNextGenCell")
cell11 = getNextGenCell(board, 1, 1)   # should return X alive
print("(1,1) will turn ", cell11)
cell01 = getNextGenCell(board, 0, 1)  #should stay alive
print("(0,1) will turn ",cell01)
cell02 = getNextGenCell(board, 0, 2)  #should stay dead
print("(0,2) will turn " ,cell02)
cell55 = getNextGenCell(board, 5, 5)  #  should stay dead
print("(5,5) will turn ", cell55)

print("\nTesting generateNextBoard")
    
    
    
#      TASK:
#      Once your initial version is running,
#      try out different starting configurations of living cells...
#      (Feel free to comment out the above three lines.)

print("Gen X:")
printBoard(board)
print("--------------------------\n\n")
    
board = genNextBoard(board)


print("Gen X+1:")
printBoard(board)
print("--------------------------\n\n")

