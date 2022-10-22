#Name: Aditya Pisharoty
#Assignment Name: Tic Tac Toe
#Date: March 5 2021
#Description: TicTacToe Player vs Player 3x3 grid
from colorama import Fore
import math
#important variables and lists:
game = [["*","*","*"],["*","*","*"],["*","*","*"]]
game2 = [["*","*","*", "*"],["*","*","*", "*"],["*","*","*", "*"], ["*","*","*", "*"]]
game3 = [["*","*","*", "*", "*"],["*","*","*", "*", "*"],["*","*","*", "*", "*"], ["*","*","*", "*", "*"], ["*","*","*", "*", "*"]] 
p1s = 0
p2s = 0
p1s4 = 0
p2s4 = 0
p1s5 = 0
p2s5 = 0
#Imporant Functions:
def drawBoard():
  for i in range(3):
    print("---".join("    "))
    for j in range(3):
      print("| "+game[i][j], end=" ")
    print("|")
  print("---".join("    "))
def isWinner():
  global p1Score
  global p2Score
  p1Score = 0
  p2Score = 0
  if (game[0][0]=="X" and game[0][1]=="X" and game[0][2]=="X"):
    print("Player 1 is the winner in the top row!")
    p1Score = p1Score + 1
    return True
  if (game[1][0]=="X" and game[1][1]=="X" and game[1][2]=="X"):
    print("Player 1 is the winner in the middle row!")
    p1Score = p1Score + 1
    return True
  if (game[2][0]=="X" and game[2][1]=="X" and game[2][2]=="X"):
    print("Player 1 is the winner in the bottom row!")
    p1Score = p1Score + 1
    return True
  if (game[0][0]=="X" and game[1][0]=="X" and game[2][0]=="X"):
    print("Player 1 is the winner in the left column!")
    p1Score = p1Score + 1
    return True
  if (game[0][1]=="X" and game[1][1]=="X" and game[2][1]=="X"):
    print("Player 1 is the winner in the middle column!")
    p1Score = p1Score + 1
    return True
  if (game[0][2]=="X" and game[1][2]=="X" and game[2][2]=="X"):
    print("Player 1 is the winner in the right column!")
    p1Score = p1Score + 1
    return True
  if (game[0][0]=="X" and game[1][1]=="X" and game[2][2]=="X"):
    print("Player 1 winner: top left bottom right diagnol!")
    p1Score = p1Score + 1
    return True
  if (game[2][0]=="X" and game[1][1]=="X" and game[0][2]=="X"):
    print("Player 1 winner: bottom left top right diagnol!")
    p1Score = p1Score + 1
    return True
  if (game[0][0]=="O" and game[0][1]=="O" and game[0][2]=="O"):
    print("Player 2 is the winner in the top row!")
    p2Score = p2Score + 1
    return True
  if (game[1][0]=="O" and game[1][1]=="O" and game[1][2]=="O"):
    print("Player 2 is the winner in the middle row!")
    p2Score = p2Score + 1
    return True
  if (game[2][0]=="O" and game[2][1]=="O" and game[2][2]=="O"):
    print("Player 2 is the winner in the bottom row!")
    p2Score = p2Score + 1
    return True
  if (game[0][0]=="O" and game[1][0]=="O" and game[2][0]=="O"):
    print("Player 2 is the winner in the left column!")
    p2Score = p2Score + 1
    return True
  if (game[0][1]=="O" and game[1][1]=="O" and game[2][1]=="O"):
    print("Player 2 is the winner in the middle column!")
    p2Score = p2Score + 1
    return True
  if (game[0][2]=="O" and game[1][2]=="O" and game[2][2]=="O"):
    print("Player 2 is the winner in the right column!")
    p2Score = p2Score + 1
    return True
  if (game[0][0]=="O" and game[1][1]=="O" and game[2][2]=="O"):
    print("Player 2 winner: top left bottom right diagnol!")
    p2Score = p2Score + 1
    return True
  if (game[2][0]=="O" and game[1][1]=="O" and game[0][2]=="O"):
    print("Player 2 winner: bottom left top right diagnol!")
    p2Score = p2Score + 1
    return True
  return False
def playGame():
  global game
  draw = 0
  for x in range(9):
    global row
    global col
    if (x%2==0):
      #Player1 is X
      row = int(input("Player 1 enter row: "))
      col = int(input("Player 1 enter column: "))
      if game[row][col] != "*":
        e = 0
        print()
        while e<1:
          print ("Oops! That spot is already taken, please try again.")
          row = int(input("Player 1 enter row: "))
          col = int(input("Player 1 enter column: "))
          if game[row][col] != "*":
            print()
          else:
            game[row][col] = "X"
            e+=1
      else:
        game[row][col] = "X"
    else:
      #Player2 is O
      row = int(input("Player 2 enter row: "))
      col = int(input("Player 2 enter column: "))
      if game[row][col] != "*":
        e = 0
        print()
        while e<1:
          print ("Oops! That spot is already taken, please try again.")
          row = int(input("Player 2 enter row: "))
          col = int(input("Player 2 enter column: "))
          if game[row][col] != "*":
            print()
          else:
            game[row][col] = "O"
            e+=1   
      else:
        game[row][col] = "O"
    draw+=1
    drawBoard()
    if (isWinner()):
      draw-=1
      break
  if draw == 9:
    print("It's a draw!")
  else:
    return   
def userWantsToQuit():
  global quit 
  x = int(input("Please type 1 to quit, or type 2 to continue: "))
  if x == 1:
    quit += 1
  else:
    print()
def resetGame():
  global game
  game = [["*","*","*"],["*","*","*"],["*","*","*"]]
def resetGame4b4():
  global game2
  game2 = [["*","*","*", "*"],["*","*","*", "*"],["*","*","*", "*"], ["*","*","*", "*"]]
def resetGame5b5():
  global game3
  game3 = [["*","*","*", "*", "*"],["*","*","*", "*", "*"],["*","*","*", "*", "*"], ["*","*","*", "*", "*"], ["*","*","*", "*", "*"]] 
def fourByfour():
  for k in range(4):
    print("---".join("     "))
    for l in range(4):
      print("| "+game2[k][l], end=" ")
    print("|")      
  print("---".join("     "))
def fiveByfive():
  for m in range(5):
    print("---".join("      "))
    for n in range(5):
      print("| "+game3[m][n], end=" ")
    print("|")      
  print("---".join("      "))
#Challenge 1: Giving users different options of how big they want the grid to be (3x3, 4x4 or 5x5)
#Also gives them the option to change the colour of grids (red, green, blue or white)
def customizeGrid():
  print ()
  print ("There are three different grids available.")
  print ("Type 3 to choose a 3x3 grid, type 4 to choose a 4x4 grid or type 5 to choose a 5x5 grid.")
  global cgrid
  cgrid = 0
  size=int(input("Choose your grid size: "))
  if size == 3:
    cgrid+=3
    print("There are four different colour grids available.") 
    print ("Type 1 to choose a red grid, type 2 to choose a green grid, type 3 to choose a blue grid  type 4 to choose a white grid.")
    colour=int(input("Choose your grid colour: "))
    if colour == 1:
      print(Fore.RED + " ")
      print("Here is your customized grid:")
      drawBoard()
      print ("Let's play!")
    elif colour == 2:
      print(Fore.GREEN + "")
      print("Here is your customized grid:")
      drawBoard()
      print ("Let's play!")
    elif colour == 3:
      print(Fore.BLUE + "")
      print("Here is your customized grid:")
      drawBoard()
      print ("Let's play!")
    elif colour == 4:
      print(Fore.WHITE + "")
      print("Here is your customized grid:")
      drawBoard()
      print ("Let's play!")
    else:
      print("You entered an invalid colour, please try again.")
  elif size == 4:
    cgrid+=4
    print("There are four different colour grids available: type 1 to choose a red grid, type 2 to choose a green grid, type 3 to choose a blue grid and type 4 to choose a white grid.")
    colour=int(input("Choose your grid colour: "))
    if colour == 1:
      print(Fore.RED + " ")
      print("Here is your customized grid:")
      fourByfour()
      print ("Let's play!")
    elif colour == 2:
      print(Fore.GREEN + "")
      print("Here is your customized grid:")
      fourByfour()
      print ("Let's play!")
    elif colour == 3:
      print(Fore.BLUE + "")
      print("Here is your customized grid:")
      fourByfour()
      print ("Let's play!")
    elif colour == 4:
      print(Fore.WHITE + "")
      print("Here is your customized grid:")
      fourByfour()
      print ("Let's play!")
    else:
      print("You entered an invalid colour, please try again.")
  elif size == 5:
    cgrid+=5
    print("There are four different colour grids available: type 1 to choose a red grid, type 2 to choose a green grid, type 3 to choose a blue grid and type 4 to choose a white grid.")
    colour=int(input("Choose your grid colour: "))
    if colour == 1:
      print(Fore.RED + " ")
      print("Here is your customized grid:")
      fiveByfive()
      print ("Let's play!")
    elif colour == 2:
      print(Fore.GREEN + "")
      print("Here is your customized grid:")
      fiveByfive()
      print ("Let's play!")
    elif colour == 3:
      print(Fore.BLUE + "")
      print("Here is your customized grid:")
      fiveByfive()
      print ("Let's play!")
    elif colour == 4:
      print(Fore.WHITE + "")
      print("Here is your customized grid:")
      fiveByfive()
      print ("Let's play!")
    else:
      print("You entered an invalid colour, please try again.")
  else:
    print ("You entered an invalid size, please try again.")
def choosetoCustomize():
  print("Would you like to customize your grid before playing?")
  yesorno = int(input("Type 1 for Yes, or 2 for No: "))
  if yesorno == 1:
    customizeGrid()
    print()
  elif yesorno == 2:
    print()
#to determine winner for 4x4 grid
#first list all possible winning outcomes
#then set it to add 1 to player score every time they get one of the winning outcomes
def isWinnerfor4():
  global p1Score4
  global p2Score4
  p1Score4 = 0
  p2Score4 = 0
  #horizontals
  if game2[0][0]=="X" and game2[0][1]=="X" and game2[0][2]=="X":
    print("Player 1 is the winner in the top row!")
    p1Score4 = p1Score4 + 1
    return True
  if game2[0][1]=="X" and game2[0][2]=="X" and game2[0][3] =="X":
    print("Player 1 is the winner in the top row!")
    p1Score4 = p1Score4 + 1
    return True
  if game2[1][0]=="X" and game2[1][1]=="X" and game2[1][2]=="X":
    print("Player 1 is the winner in the second row!")
    p1Score4 = p1Score4 + 1
    return True
  if game2[1][1]=="X" and game2[1][2]=="X" and game2[1][3] =="X":
    print("Player 1 is the winner in the second row!")
    p1Score4 = p1Score4 + 1
    return True  
  if game2[2][0]=="X" and game2[2][1]=="X" and game2[2][2]=="X":
    print("Player 1 is the winner in the third row!")
    p1Score4 = p1Score4 + 1
    return True
  if game2[2][1]=="X" and game2[2][2]=="X" and game2[2][3] =="X":
    print("Player 1 is the winner in the third row!")
    p1Score4 = p1Score4 + 1
    return True  
  if game2[3][0]=="X" and game2[3][1]=="X" and game2[3][2]=="X":
    print("Player 1 is the winner in the second row!")
    p1Score4 = p1Score4 + 1
    return True
  if game2[3][1]=="X" and game2[3][2]=="X" and game2[3][3] =="X":
    print("Player 1 is the winner in the second row!")
    p1Score4 = p1Score4 + 1
    return True  
  #verticals
  if game2[0][0]=="X" and game2[1][0]=="X" and game2[2][0]=="X":
    print("Player 1 is the winner in the left column!")
    p1Score4 = p1Score4 + 1
    return True
  if game2[1][0]=="X" and game2[2][0]=="X" and game2[3][0] =="X":
    print("Player 1 is the winner in the left column!")
    p1Score4 = p1Score4 + 1
    return True  
  if game2[0][1]=="X" and game2[1][1]=="X" and game2[2][1]=="X":
    print("Player 1 is the winner in the second column!")
    p1Score4 = p1Score4 + 1
    return True
  if game2[1][1]=="X" and game2[2][1]=="X" and game2[3][1] =="X":
    print("Player 1 is the winner in the second column!")
    p1Score4 = p1Score4 + 1
    return True  
  if game2[0][2]=="X" and game2[1][2]=="X" and game2[2][2]=="X":
    print("Player 1 is the winner in the third column!")
    p1Score4 = p1Score4 + 1
    return True
  if game2[1][2]=="X" and game2[2][2]=="X" and game2[3][2] =="X":
    print("Player 1 is the winner in the third column!")
    p1Score4 = p1Score4 + 1
    return True  
  if game2[0][3]=="X" and game2[1][3]=="X" and game2[2][3]=="X":
    print("Player 1 is the winner in the right column!")
    p1Score4 = p1Score4 + 1
    return True
  if game2[1][3]=="X" and game2[2][3]=="X" and game2[3][3] =="X":
    print("Player 1 is the winner in the right column!")
    p1Score4 = p1Score4 + 1
    return True 
  #diagnols
  if game2[0][0]=="X" and game2[1][1]=="X" and game2[2][2]=="X":
    print("Player 1 wins with a diagnol line!")
    p1Score4 = p1Score4 + 1
    return True
  if game2[0][1]=="X" and game2[1][2]=="X" and game2[2][3]=="X":
    print("Player 1 wins with a diagnol line!")
    p1Score4 = p1Score4 + 1
    return True
  if game2[0][3]=="X" and game2[1][2]=="X" and game2[2][1]=="X":
    print("Player 1 wins with a diagnol line!")
    p1Score4 = p1Score4 + 1
    return True
  if game2[0][2]=="X" and game2[1][1]=="X" and game2[2][0]=="X":
    print("Player 1 wins with a diagnol line!")
    p1Score4 = p1Score4 + 1
    return True
  if game2[3][0]=="X" and game2[2][1]=="X" and game2[1][2]=="X":
    print("Player 1 wins with a diagnol line!")
    p1Score4 = p1Score4 + 1
    return True
  if game2[3][1]=="X" and game2[2][2]=="X" and game2[1][3]=="X":
    print("Player 1 wins with a diagnol line!")
    p1Score4 = p1Score4 + 1
    return True
  if game2[3][3]=="X" and game2[2][2]=="X" and game2[1][1]=="X":
    print("Player 1 wins with a diagnol line!")
    p1Score4 = p1Score4 + 1
    return True
  if game2[3][2]=="X" and game2[2][1]=="X" and game2[1][0]=="X":
    print("Player 1 wins with a diagnol line!")
    p1Score4 = p1Score4 + 1
    return True
  #horizontals
  if game2[0][0]=="O" and game2[0][1]=="O" and game2[0][2]=="O":
    print("Player 2 is the winner in the top row!")
    p2Score4 = p2Score4 + 1
    return True
  if game2[0][1]=="O" and game2[0][2]=="O" and game2[0][3] =="O":
    print("Player 2 is the winner in the top row!")
    p2Score4 = p2Score4 + 1
    return True
  if game2[1][0]=="O" and game2[1][1]=="O" and game2[1][2]=="O":
    print("Player 2 is the winner in the second row!")
    p2Score4 = p2Score4 + 1
    return True
  if game2[1][1]=="O" and game2[1][2]=="O" and game2[1][3] =="O":
    print("Player 2 is the winner in the second row!")
    p2Score4 = p2Score4 + 1
    return True  
  if game2[2][0]=="O" and game2[2][1]=="O" and game2[2][2]=="O":
    print("Player 2 is the winner in the third row!")
    p2Score4 = p2Score4 + 1
    return True
  if game2[2][1]=="O" and game2[2][2]=="O" and game2[2][3] =="O":
    print("Player 2 is the winner in the third row!")
    p2Score4 = p2Score4 + 1
    return True  
  if game2[3][0]=="O" and game2[3][1]=="O" and game2[3][2]=="O":
    print("Player 2 is the winner in the second row!")
    p2Score4 = p2Score4 + 1
    return True
  if game2[3][1]=="O" and game2[3][2]=="O" and game2[3][3] =="O":
    print("Player 2 is the winner in the second row!")
    p2Score4 = p2Score4 + 1
    return True  
  #verticals
  if game2[0][0]=="O" and game2[1][0]=="O" and game2[2][0]=="O":
    print("Player 2 is the winner in the left column!")
    p2Score4 = p2Score4 + 1
    return True
  if game2[1][0]=="O" and game2[2][0]=="O" and game2[3][0] =="O":
    print("Player 2 is the winner in the left column!")
    p2Score4 = p2Score4 + 1
    return True  
  if game2[0][1]=="O" and game2[1][1]=="O" and game2[2][1]=="O":
    print("Player 2 is the winner in the second column!")
    p2Score4 = p2Score4 + 1
    return True
  if game2[1][1]=="O" and game2[2][1]=="O" and game2[3][1] =="O":
    print("Player 2 is the winner in the second column!")
    p2Score4 = p2Score4 + 1
    return True  
  if game2[0][2]=="O" and game2[1][2]=="O" and game2[2][2]=="O":
    print("Player 2 is the winner in the third column!")
    p2Score4 = p2Score4 + 1
    return True
  if game2[1][2]=="O" and game2[2][2]=="O" and game2[3][2] =="O":
    print("Player 2 is the winner in the third column!")
    p2Score4 = p2Score4 + 1
    return True  
  if game2[0][3]=="O" and game2[1][3]=="O" and game2[2][3]=="O":
    print("Player 2 is the winner in the right column!")
    p2Score4 = p2Score4 + 1
    return True
  if game2[1][3]=="O" and game2[2][3]=="O" and game2[3][3] =="O":
    print("Player 2 is the winner in the right column!")
    p2Score4 = p2Score4 + 1
    return True 
  #diagnols
  if game2[0][0]=="O" and game2[1][1]=="O" and game2[2][2]=="O":
    print("Player 2 wins with a diagnol line!")
    p2Score4 = p2Score4 + 1
    return True
  if game2[0][1]=="O" and game2[1][2]=="O" and game2[2][3]=="O":
    print("Player 2 wins with a diagnol line!")
    p2Score4 = p2Score4 + 1
    return True
  if game2[0][3]=="O" and game2[1][2]=="O" and game2[2][1]=="O":
    print("Player 2 wins with a diagnol line!")
    p2Score4 = p2Score4 + 1
    return True
  if game2[0][2]=="O" and game2[1][1]=="O" and game2[2][0]=="O":
    print("Player 2 wins with a diagnol line!")
    p2Score4 = p2Score4 + 1
    return True
  if game2[3][0]=="O" and game2[2][1]=="O" and game2[1][2]=="O":
    print("Player 2 wins with a diagnol line!")
    p2Score4 = p2Score4 + 1
    return True
  if game2[3][1]=="O" and game2[2][2]=="O" and game2[1][3]=="O":
    print("Player 2 wins with a diagnol line!")
    p2Score4 = p2Score4 + 1
    return True
  if game2[3][3]=="O" and game2[2][2]=="O" and game2[1][1]=="O":
    print("Player 2 wins with a diagnol line!")
    p2Score4 = p2Score4 + 1
    return True
  if game2[3][2]=="O" and game2[2][1]=="O" and game2[1][0]=="O":
    print("Player 2 wins with a diagnol line!")
    p2Score4 = p2Score4 + 1
    return True
  return False
#to determine winner for 5x5 grid
#first list all possible winning outcomes (horizontal, vertical and diagnoal)
#then set it to add 1 to player score every time they get one of the winning outcomes
def isWinnerfor5():
  global p1score5
  global p2score5
  p1score5 = 0
  p2score5 = 0
  #horizontals
  if game3[0][0]=="X" and game3[0][1]=="X" and game3[0][2]=="X":
    print("Player 1 is the winner in the top row!")
    p1score5 = p1score5 + 1
    return True
  if game3[0][1]=="X" and game3[0][2]=="X" and game3[0][3]=="X":
    print("Player 1 is the winner in the top row!")
    p1score5 = p1score5 + 1
    return True
  if game3[0][2]=="X" and game3[0][3]=="X" and game3[0][4]=="X":
    print("Player 1 is the winner in the top row!")
    p1score5 = p1score5 + 1
    return True
  if game3[1][0]=="X" and game3[1][1]=="X" and game3[1][2]=="X":
    print("Player 1 is the winner in the second row!")
    p1score5 = p1score5 + 1
    return True
  if game3[1][1]=="X" and game3[1][2]=="X" and game3[1][3]=="X":
    print("Player 1 is the winner in the second row!")
    p1score5 = p1score5 + 1
    return True
  if game3[1][2]=="X" and game3[1][3]=="X" and game3[1][4]=="X":
    print("Player 1 is the winner in the second row!")
    p1score5 = p1score5 + 1
    return True
  if game3[2][0]=="X" and game3[2][1]=="X" and game3[2][2]=="X":
    print("Player 1 is the winner in the third row!")
    p1score5 = p1score5 + 1
    return True
  if game3[2][1]=="X" and game3[2][2]=="X" and game3[2][3]=="X":
    print("Player 1 is the winner in the third row!")
    p1score5 = p1score5 + 1
    return True
  if game3[2][2]=="X" and game3[2][3]=="X" and game3[2][4]=="X":
    print("Player 1 is the winner in the third row!")
    p1score5 = p1score5 + 1
    return True
  if game3[3][0]=="X" and game3[3][1]=="X" and game3[3][2]=="X":
    print("Player 1 is the winner in the fourth row!")
    p1score5 = p1score5 + 1
    return True
  if game3[3][1]=="X" and game3[3][2]=="X" and game3[3][3]=="X":
    print("Player 1 is the winner in the fourth row!")
    p1score5 = p1score5 + 1
    return True
  if game3[3][2]=="X" and game3[3][3]=="X" and game3[3][4]=="X":
    print("Player 1 is the winner in the fourth row!")
    p1score5 = p1score5 + 1
    return True
  if game3[4][0]=="X" and game3[4][1]=="X" and game3[4][2]=="X":
    print("Player 1 is the winner in the bottom row!")
    p1score5 = p1score5 + 1
    return True
  if game3[4][1]=="X" and game3[4][2]=="X" and game3[4][3]=="X":
    print("Player 1 is the winner in the bottom row!")
    p1score5 = p1score5 + 1
    return True
  if game3[4][2]=="X" and game3[4][3]=="X" and game3[4][4]=="X":
    print("Player 1 is the winner in the bottom row!")
    p1score5 = p1score5 + 1
    return True
  #verticals:
  if game3[0][0]=="X" and game3[1][0]=="X" and game3[2][0]=="X":
    print("Player 1 is the winner in the left column!")
    p1score5 = p1score5 + 1
    return True
  if game3[1][0]=="X" and game3[2][0]=="X" and game3[3][0]=="X":
    print("Player 1 is the winner in the left column!")
    p1score5 = p1score5 + 1
    return True
  if game3[2][0]=="X" and game3[3][0]=="X" and game3[4][0]=="X":
    print("Player 1 is the winner in the left column!")
    p1score5 = p1score5 + 1
    return True
  if game3[0][1]=="X" and game3[1][1]=="X" and game3[2][1]=="X":
    print("Player 1 is the winner in the second column!")
    p1score5 = p1score5 + 1
    return True
  if game3[1][1]=="X" and game3[2][1]=="X" and game3[3][1]=="X":
    print("Player 1 is the winner in the second column!")
    p1score5 = p1score5 + 1
    return True
  if game3[2][1]=="X" and game3[3][1]=="X" and game3[4][1]=="X":
    print("Player 1 is the winner in the second column!")
    p1score5 = p1score5 + 1
    return True
  if game3[0][2]=="X" and game3[1][2]=="X" and game3[2][2]=="X":
    print("Player 1 is the winner in the third column!")
    p1score5 = p1score5 + 1
    return True
  if game3[1][2]=="X" and game3[2][2]=="X" and game3[3][2]=="X":
    print("Player 1 is the winner in the third column!")
    p1score5 = p1score5 + 1
    return True
  if game3[2][2]=="X" and game3[3][2]=="X" and game3[4][2]=="X":
    print("Player 1 is the winner in the third column!")
    p1score5 = p1score5 + 1
    return True
  if game3[0][3]=="X" and game3[1][3]=="X" and game3[2][3]=="X":
    print("Player 1 is the winner in the fourth column!")
    p1score5 = p1score5 + 1
    return True
  if game3[1][3]=="X" and game3[2][3]=="X" and game3[3][3]=="X":
    print("Player 1 is the winner in the fourth column!")
    p1score5 = p1score5 + 1
    return True
  if game3[2][3]=="X" and game3[3][3]=="X" and game3[4][3]=="X":
    print("Player 1 is the winner in the fourth column!")
    p1score5 = p1score5 + 1
    return True
  if game3[0][4]=="X" and game3[1][4]=="X" and game3[2][4]=="X":
    print("Player 1 is the winner in the right column!")
    p1score5 = p1score5 + 1
    return True
  if game3[1][4]=="X" and game3[2][4]=="X" and game3[3][4]=="X":
    print("Player 1 is the winner in the right column!")
    p1score5 = p1score5 + 1
    return True
  if game3[2][4]=="X" and game3[3][4]=="X" and game3[4][4]=="X":
    print("Player 1 is the winner in the right column!")
    p1score5 = p1score5 + 1
    return True
  #diagonals:
  if game3[0][0]=="X" and game3[1][1]=="X" and game3[2][2]=="X":
    print("Player 1 wins with a diagnoal line!")
    p1score5 = p1score5 + 1
    return True
  if game3[0][1]=="X" and game3[1][2]=="X" and game3[2][3]=="X":
    print("Player 1 wins with a diagnoal line!")
    p1score5 = p1score5 + 1
    return True
  if game3[0][2]=="X" and game3[1][3]=="X" and game3[2][4]=="X":
    print("Player 1 wins with a diagnoal line!")
    p1score5 = p1score5 + 1
    return True
  if game3[0][4]=="X" and game3[1][3]=="X" and game3[2][2]=="X":
    print("Player 1 wins with a diagnoal line!")
    p1score5 = p1score5 + 1
    return True
  if game3[0][3]=="X" and game3[1][2]=="X" and game3[2][1]=="X":
    print("Player 1 wins with a diagnoal line!")
    p1score5 = p1score5 + 1
    return True
  if game3[0][2]=="X" and game3[1][1]=="X" and game3[2][0]=="X":
    print("Player 1 wins with a diagnoal line!")
    p1score5 = p1score5 + 1
    return True
  if game3[1][0]=="X" and game3[2][1]=="X" and game3[3][2]=="X":
    print("Player 1 wins with a diagnoal line!")
    p1score5 = p1score5 + 1
    return True
  if game3[1][1]=="X" and game3[2][2]=="X" and game3[3][3]=="X":
    print("Player 1 wins with a diagnoal line!")
    p1score5 = p1score5 + 1
    return True
  if game3[1][2]=="X" and game3[2][3]=="X" and game3[3][4]=="X":
    print("Player 1 wins with a diagnoal line!")
    p1score5 = p1score5 + 1
    return True
  if game3[1][4]=="X" and game3[2][3]=="X" and game3[3][2]=="X":
    print("Player 1 wins with a diagnoal line!")
    p1score5 = p1score5 + 1
    return True
  if game3[1][3]=="X" and game3[2][2]=="X" and game3[3][1]=="X":
    print("Player 1 wins with a diagnoal line!")
    p1score5 = p1score5 + 1
    return True
  if game3[1][2]=="X" and game3[2][1]=="X" and game3[3][0]=="X":
    print("Player 1 wins with a diagnoal line!")
    p1score5 = p1score5 + 1
    return True
  if game3[2][0]=="X" and game3[3][1]=="X" and game3[4][2]=="X":
    print("Player 1 wins with a diagnoal line!")
    p1score5 = p1score5 + 1
    return True
  if game3[2][1]=="X" and game3[3][2]=="X" and game3[4][3]=="X":
    print("Player 1 wins with a diagnoal line!")
    p1score5 = p1score5 + 1
    return True
  if game3[2][2]=="X" and game3[3][3]=="X" and game3[4][4]=="X":
    print("Player 1 wins with a diagnoal line!")
    p1score5 = p1score5 + 1
    return True
  if game3[2][4]=="X" and game3[3][3]=="X" and game3[4][2]=="X":
    print("Player 1 wins with a diagnoal line!")
    p1score5 = p1score5 + 1
    return True
  if game3[2][3]=="X" and game3[3][2]=="X" and game3[4][1]=="X":
    print("Player 1 wins with a diagnoal line!")
    p1score5 = p1score5 + 1
    return True
  if game3[2][2]=="X" and game3[3][1]=="X" and game3[4][0]=="X":
    print("Player 1 wins with a diagnoal line!")
    p1score5 = p1score5 + 1
    return True
  #horizontals
  if game3[0][0]=="O" and game3[0][1]=="O" and game3[0][2]=="O":
    print("Player 2 is the winner in the top row!")
    p2score5 = p2score5 + 1
    return True
  if game3[0][1]=="O" and game3[0][2]=="O" and game3[0][3]=="O":
    print("Player 2 is the winner in the top row!")
    p2score5 = p2score5 + 1
    return True
  if game3[0][2]=="O" and game3[0][3]=="O" and game3[0][4]=="O":
    print("Player 2 is the winner in the top row!")
    p2score5 = p2score5 + 1
    return True
  if game3[1][0]=="O" and game3[1][1]=="O" and game3[1][2]=="O":
    print("Player 2 is the winner in the second row!")
    p2score5 = p2score5 + 1
    return True
  if game3[1][1]=="O" and game3[1][2]=="O" and game3[1][3]=="O":
    print("Player 2 is the winner in the second row!")
    p2score5 = p2score5 + 1
    return True
  if game3[1][2]=="O" and game3[1][3]=="O" and game3[1][4]=="O":
    print("Player 2 is the winner in the second row!")
    p2score5 = p2score5 + 1
    return True
  if game3[2][0]=="O" and game3[2][1]=="O" and game3[2][2]=="O":
    print("Player 2 is the winner in the third row!")
    p2score5 = p2score5 + 1
    return True
  if game3[2][1]=="O" and game3[2][2]=="O" and game3[2][3]=="O":
    print("Player 2 is the winner in the third row!")
    p2score5 = p2score5 + 1
    return True
  if game3[2][2]=="O" and game3[2][3]=="O" and game3[2][4]=="O":
    print("Player 2 is the winner in the third row!")
    p2score5 = p2score5 + 1
    return True
  if game3[3][0]=="O" and game3[3][1]=="O" and game3[3][2]=="O":
    print("Player 2 is the winner in the fourth row!")
    p2score5 = p2score5 + 1
    return True
  if game3[3][1]=="O" and game3[3][2]=="O" and game3[3][3]=="O":
    print("Player 2 is the winner in the fourth row!")
    p2score5 = p2score5 + 1
    return True
  if game3[3][2]=="O" and game3[3][3]=="O" and game3[3][4]=="O":
    print("Player 2 is the winner in the fourth row!")
    p2score5 = p2score5 + 1
    return True
  if game3[4][0]=="O" and game3[4][1]=="O" and game3[4][2]=="O":
    print("Player 2 is the winner in the bottom row!")
    p2score5 = p2score5 + 1
    return True
  if game3[4][1]=="O" and game3[4][2]=="O" and game3[4][3]=="O":
    print("Player 2 is the winner in the bottom row!")
    p2score5 = p2score5 + 1
    return True
  if game3[4][2]=="O" and game3[4][3]=="O" and game3[4][4]=="O":
    print("Player 2 is the winner in the bottom row!")
    p2score5 = p2score5 + 1
    return True
  #verticals:
  if game3[0][0]=="O" and game3[1][0]=="O" and game3[2][0]=="O":
    print("Player 2 is the winner in the left column!")
    p2score5 = p2score5 + 1
    return True
  if game3[1][0]=="O" and game3[2][0]=="O" and game3[3][0]=="O":
    print("Player 2 is the winner in the left column!")
    p2score5 = p2score5 + 1
    return True
  if game3[2][0]=="O" and game3[3][0]=="O" and game3[4][0]=="O":
    print("Player 2 is the winner in the left column!")
    p2score5 = p2score5 + 1
    return True
  if game3[0][1]=="O" and game3[1][1]=="O" and game3[2][1]=="O":
    print("Player 2 is the winner in the second column!")
    p2score5 = p2score5 + 1
    return True
  if game3[1][1]=="O" and game3[2][1]=="O" and game3[3][1]=="O":
    print("Player 2 is the winner in the second column!")
    p2score5 = p2score5 + 1
    return True
  if game3[2][1]=="O" and game3[3][1]=="O" and game3[4][1]=="O":
    print("Player 2 is the winner in the second column!")
    p2score5 = p2score5 + 1
    return True
  if game3[0][2]=="O" and game3[1][2]=="O" and game3[2][2]=="O":
    print("Player 2 is the winner in the third column!")
    p2score5 = p2score5 + 1
    return True
  if game3[1][2]=="O" and game3[2][2]=="O" and game3[3][2]=="O":
    print("Player 2 is the winner in the third column!")
    p2score5 = p2score5 + 1
    return True
  if game3[2][2]=="O" and game3[3][2]=="O" and game3[4][2]=="O":
    print("Player 2 is the winner in the third column!")
    p2score5 = p2score5 + 1
    return True
  if game3[0][3]=="O" and game3[1][3]=="O" and game3[2][3]=="O":
    print("Player 2 is the winner in the fourth column!")
    p2score5 = p2score5 + 1
    return True
  if game3[1][3]=="O" and game3[2][3]=="O" and game3[3][3]=="O":
    print("Player 2 is the winner in the fourth column!")
    p2score5 = p2score5 + 1
    return True
  if game3[2][3]=="O" and game3[3][3]=="O" and game3[4][3]=="O":
    print("Player 2 is the winner in the fourth column!")
    p2score5 = p2score5 + 1
    return True
  if game3[0][4]=="O" and game3[1][4]=="O" and game3[2][4]=="O":
    print("Player 2 is the winner in the right column!")
    p2score5 = p2score5 + 1
    return True
  if game3[1][4]=="O" and game3[2][4]=="O" and game3[3][4]=="O":
    print("Player 2 is the winner in the right column!")
    p2score5 = p2score5 + 1
    return True
  if game3[2][4]=="O" and game3[3][4]=="O" and game3[4][4]=="O":
    print("Player 2 is the winner in the right column!")
    p2score5 = p2score5 + 1
    return True
  #diagonals:
  if game3[0][0]=="O" and game3[1][1]=="O" and game3[2][2]=="O":
    print("Player 2 wins with a diagnoal line!")
    p2score5 = p2score5 + 1
    return True
  if game3[0][1]=="O" and game3[1][2]=="O" and game3[2][3]=="O":
    print("Player 2 wins with a diagnoal line!")
    p2score5 = p2score5 + 1
    return True
  if game3[0][2]=="O" and game3[1][3]=="O" and game3[2][4]=="O":
    print("Player 2 wins with a diagnoal line!")
    p2score5 = p2score5 + 1
    return True
  if game3[0][4]=="O" and game3[1][3]=="O" and game3[2][2]=="O":
    print("Player 2 wins with a diagnoal line!")
    p2score5 = p2score5 + 1
    return True
  if game3[0][3]=="O" and game3[1][2]=="O" and game3[2][1]=="O":
    print("Player 2 wins with a diagnoal line!")
    p2score5 = p2score5 + 1
    return True
  if game3[0][2]=="O" and game3[1][1]=="O" and game3[2][0]=="O":
    print("Player 2 wins with a diagnoal line!")
    p2score5 = p2score5 + 1
    return True
  if game3[1][0]=="O" and game3[2][1]=="O" and game3[3][2]=="O":
    print("Player 2 wins with a diagnoal line!")
    p2score5 = p2score5 + 1
    return True
  if game3[1][1]=="O" and game3[2][2]=="O" and game3[3][3]=="O":
    print("Player 2 wins with a diagnoal line!")
    p2score5 = p2score5 + 1
    return True
  if game3[1][2]=="O" and game3[2][3]=="O" and game3[3][4]=="O":
    print("Player 2 wins with a diagnoal line!")
    p2score5 = p2score5 + 1
    return True
  if game3[1][4]=="O" and game3[2][3]=="O" and game3[3][2]=="O":
    print("Player 2 wins with a diagnoal line!")
    p2score5 = p2score5 + 1
    return True
  if game3[1][3]=="O" and game3[2][2]=="O" and game3[3][1]=="O":
    print("Player 2 wins with a diagnoal line!")
    p2score5 = p2score5 + 1
    return True
  if game3[1][2]=="O" and game3[2][1]=="O" and game3[3][0]=="O":
    print("Player 2 wins with a diagnoal line!")
    p2score5 = p2score5 + 1
    return True
  if game3[2][0]=="O" and game3[3][1]=="O" and game3[4][2]=="O":
    print("Player 2 wins with a diagnoal line!")
    p2score5 = p2score5 + 1
    return True
  if game3[2][1]=="O" and game3[3][2]=="O" and game3[4][3]=="O":
    print("Player 2 wins with a diagnoal line!")
    p2score5 = p2score5 + 1
    return True
  if game3[2][2]=="O" and game3[3][3]=="O" and game3[4][4]=="O":
    print("Player 2 wins with a diagnoal line!")
    p2score5 = p2score5 + 1
    return True
  if game3[2][4]=="O" and game3[3][3]=="O" and game3[4][2]=="O":
    print("Player 2 wins with a diagnoal line!")
    p2score5 = p2score5 + 1
    return True
  if game3[2][3]=="O" and game3[3][2]=="O" and game3[4][1]=="O":
    print("Player 2 wins with a diagnoal line!")
    p2score5 = p2score5 + 1
    return True
  if game3[2][2]=="O" and game3[3][1]=="O" and game3[4][0]=="O":
    print("Player 2 wins with a diagnoal line!")
    p2score5 = p2score5 + 1
    return True
  return False
def playfourByfour():
  global game2
  draw2 = 0
  for x in range(16):
    if (x%2==0):
      #Player1 is X
      row = int(input("Player 1 enter row: "))
      col = int(input("Player 1 enter column: "))
      if game2[row][col] != "*":
#used to determine if spot is already taken
#if spot is taken, loops until player chooses spot that is empty
#will not count towards x in range(16)        
        e = 0
        print()
        while e<1:
          print ("Oops! That spot is already taken, please try again.")
          row = int(input("Player 1 enter row: "))
          col = int(input("Player 1 enter column: "))
          if game2[row][col] != "*":
            print()
          else:
            game2[row][col] = "X"
            e+=1
      else:
        game2[row][col] = "X"
    else:
      #Player2 is O
      row = int(input("Player 2 enter row: "))
      col = int(input("Player 2 enter column: "))
      if game2[row][col] != "*":
        e = 0
        print()
        while e<1:
          print ("Oops! That spot is already taken, please try again.")
          row = int(input("Player 2 enter row: "))
          col = int(input("Player 2 enter column: "))
          if game2[row][col] != "*":
            print()
          else:
            game2[row][col] = "O"
            e+=1
      else:
        game2[row][col] = "O"
    draw2 += 1
    fourByfour()
    if (isWinnerfor4()):
      draw2-=1
      break
  if draw2 == 16:
    print("It's a draw!")
  else:
    return
def playfiveByfive():
  global game3
  draw3 = 0
  for x in range(25):
    if (x%2==0):
      #Player1 is X
      row = int(input("Player 1 enter row: "))
      col = int(input("Player 1 enter column: "))
      if game3[row][col] != "*":
#used to determine if sopt is already taken
#if spot is taken, loops until player chooses spot that is empty
#will not count towards x in range(25)  
        e = 0
        print ()
        while e<1:
          print ("Oops! That spot is already taken, please try again.")
          row = int(input("Player 1 enter row: "))
          col = int(input("Player 1 enter column: "))
          if game3[row][col] != "*":
            print()
          else:
            game3[row][col] = "X"
            e+=1
      else:
        game3[row][col] = "X"          
    else:
      #Player2 is O
      row = int(input("Player 2 enter row: "))
      col = int(input("Player 2 enter column: "))
      if game3[row][col] != "*":
        e = 0
        print()
        while e<1:
          print ("Oops! That spot is already taken, please try again.")
          row = int(input("Player 2 enter row: "))
          col = int(input("Player 2 enter column: "))
          if game3[row][col] != "*":
            print()
          else:
            game3[row][col] = "O"
            e+=1
      else:
        game3[row][col] = "O"
    draw3 += 1
    fiveByfive()
    if (isWinnerfor5()):
      draw3-=1
      break
  if draw3 == 25:
    print("It's a draw!")
  else:
    return
#Welcoming user to program
print(Fore.GREEN + "Welcome to Aditya's Tic-Tac-Toe!")
print(Fore.WHITE + "Here is your grid:")
drawBoard()
print ()
print(Fore.GREEN + "There are four gamemodes to choose from:")
print ()
#Challenge 2: Cool colours
print(Fore.RED + "(1) Showdown:")
print(Fore.RED + "Play one round!")
print(Fore.YELLOW + "(2) Best of X Games:")
print(Fore.YELLOW + "Whoever wins the most out of X games wins! ")
print(Fore.YELLOW + "Players can choose value of X." )
print(Fore.CYAN + "(3) X Number of Games:")
print(Fore.CYAN + "Players choose value of X, and play that many games.")
print(Fore.BLUE + "(4) Unlimited Play:")
print(Fore.BLUE + "Players can play unlimited times.")
print ()
gamemode = int(input(Fore.GREEN + "Please choose a gamemode: "))
print (Fore.WHITE + "")
#Challenge 3: Multiple different gamemodes
if gamemode == 1:
  print("You chose Showdown!")
  cgrid=0
  choosetoCustomize()
  if cgrid == 3:
    drawBoard()
    playGame()
  elif cgrid == 4:
    fourByfour()
    playfourByfour()
  elif cgrid == 5:
    fiveByfive()
    playfiveByfive()
  else:
    drawBoard()
    playGame()
elif gamemode == 2:
  print("You chose Best of X Games!")
  bestx = int(input("What do you want to set as the X value? "))
  cgrid=0
  choosetoCustomize()
  if cgrid == 3:
    gamenum = 1
    while bestx > p1s and bestx > p2s:
      print ("Game {}:".format(gamenum))
      gamenum+=1
      drawBoard()
      playGame()
      p1s += p1Score
      p2s += p2Score
#Challenge 4: Keeping score in gamemodes that require it
#specifically gamemode 2, 3 and 4
      print ("Player 1 won {} games.".format(p1s))
      print ("Player 2 won {} games.".format(p2s))
      resetGame()
    if p1s == bestx:
      print ("Player 1 is the winner!")
    elif p2s == bestx:
      print ("Player 2 is the winner!")
  elif cgrid == 4:
    gamenum = 1
    while bestx > p1s4 and bestx > p2s4:
      print ("Game {}:".format(gamenum))
      gamenum+=1
      fourByfour()
      playfourByfour()
      p1s4 += p1Score4
      p2s4 += p2Score4
      print ("Player 1 won {} games.".format(p1s4))
      print ("Player 2 won {} games.".format(p2s4))
      resetGame4b4()
    if p1s4 == bestx:
      print ("Player 1 is the winner!")
    elif p2s4 == bestx:
      print ("Player 2 is the winner!")
  elif cgrid == 5:
    gamenum = 1
    while bestx > p1s5 and bestx > p2s5:
      print ("Game {}:".format(gamenum))
      gamenum+=1
      fiveByfive()
      playfiveByfive()
      p1s5 += p1score5
      p2s5 += p2score5
      print ("Player 1 won {} games.".format(p1s5))
      print ("Player 2 won {} games.".format(p2s5))
      resetGame5b5()
    if p1s5 == bestx:
      print ("Player 1 is the winner!")
    elif p2s5 == bestx:
      print ("Player 2 is the winner!")
  else:
    gamenum = 1
    while bestx > p1s and bestx > p2s:
      print ("Game {}:".format(gamenum))
      gamenum+=1
      drawBoard()
      playGame()
      p1s += p1Score
      p2s += p2Score
      print ("Player 1 won {} games.".format(p1s))
      print ("Player 2 won {} games.".format(p2s))
      resetGame()
    if p1s == bestx:
      print ("Player 1 is the winner!")
    elif p2s == bestx:
      print ("Player 2 is the winner!")
elif gamemode == 3:
  print ("You chose X Number of Games!")
  numx = int(input("What do you want to set as the X value? "))
  print()
  cgrid=0
  choosetoCustomize()
  if cgrid == 3:
    end2 = 0
    gamenum2 = 1
    while end2 != numx:
      print ("Game {}:".format(gamenum2))
      drawBoard()
      playGame()
      p1s += p1Score
      p2s += p2Score
      print ("Player 1 won {} games.".format(p1s))
      print ("Player 2 won {} games.".format(p2s))
      resetGame()
      gamenum2 += 1
      end2 += 1
  elif cgrid == 4:
    end2 = 0
    gamenum2 = 1
    while end2 != numx:
      print ("Game {}:".format(gamenum2))
      fourByfour()
      playfourByfour()
      p1s4 += p1Score4
      p2s4 += p2Score4
      print ("Player 1 won {} games.".format(p1s4))
      print ("Player 2 won {} games.".format(p2s4))
      resetGame4b4()
      gamenum2 += 1
      end2 += 1
  elif cgrid == 5:
    end2 = 0
    gamenum2 = 1
    while end2 != numx:
      print ("Game {}:".format(gamenum2))
      fiveByfive()
      playfiveByfive()
      p1s5 += p1score5
      p2s5 += p2score5
      print ("Player 1 won {} games.".format(p1s5))
      print ("Player 2 won {} games.".format(p2s5))
      resetGame5b5()
      gamenum2 += 1
      end2 += 1
  else:
    end2 = 0
    gamenum2 = 1
    while end2 != numx:
      print ("Game {}:".format(gamenum2))
      drawBoard()
      playGame()
      p1s += p1Score
      p2s += p2Score
      print ("Player 1 won {} games.".format(p1s))
      print ("Player 2 won {} games.".format(p2s))
      resetGame()
      gamenum2 += 1
      end2 += 1   
elif gamemode == 4:
  print ("You chose unlimited Play!")
  cgrid=0
  choosetoCustomize()
  if cgrid == 3:
    gamenum3 = 1
    quit = 0
    while quit != 1:
      print ("Game {}:".format(gamenum3))
      drawBoard()
      playGame()
      p1s += p1Score
      p2s += p2Score
      print ("Player 1 won {} games.".format(p1s))
      print ("Player 2 won {} games.".format(p2s))
      userWantsToQuit()
      resetGame()
      gamenum3 += 1
  elif cgrid == 4:
    gamenum3 = 1
    quit = 0
    while quit!= 1:
      print ("Game {}:".format(gamenum3))
      fourByfour()
      playfourByfour()
      p1s4 += p1Score4
      p2s4 += p2Score4
      print ("Player 1 won {} games.".format(p1s4))
      print ("Player 2 won {} games.".format(p2s4))
      userWantsToQuit()
      resetGame4b4()
      gamenum3 += 1
  elif cgrid == 5:
    gamenum3 = 1
    quit = 0
    while quit!= 1:
      print ("Game {}:".format(gamenum3))
      fiveByfive()
      playfiveByfive()
      p1s5 += p1score5
      p2s5 += p2score5
      print ("Player 1 won {} games.".format(p1s5))
      print ("Player 2 won {} games.".format(p2s5))
      userWantsToQuit()
      resetGame5b5()
      gamenum3 += 1
  else:
    gamenum3 = 1
    quit = 0
    while quit != 1:
      print ("Game {}:".format(gamenum3))
      drawBoard()
      playGame()
      p1s += p1Score
      p2s += p2Score
      print ("Player 1 won {} games.".format(p1s))
      print ("Player 2 won {} games.".format(p2s))
      userWantsToQuit()
      resetGame()
      gamenum3 += 1     
else:
  print ("You entered an invalid gamemode, please try again.")
