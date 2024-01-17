import random

def RockPaperScissor(player):

    # Generating computer's choice
    computer = randomSelect()

    # Checking who wins the game
    winner = whoWins(player, computer)

    # Displaying the results
    display(player, computer, winner)

def randomSelect():
    
    # Generating random number between 1 & 3
    randomNum = random.randint(1, 3)

    # Giving names to random number generated (i.e. Rock, Paper & Scissors)
    if randomNum == 1:
        return "rock"
    elif randomNum == 2:
        return "paper"
    else:
        return "scissors"

# Comparing player's and computer's choice 
def whoWins(player, computer):
   
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

# Displaying the choices made by player & computer
def display(player, computer, winner):
    
    print("You chose:", player)
    print("Computer chose:", computer)

    # Checking the winner
    if winner == "tie":
        print("It's a tie!")
    elif winner == "player":
        print("Player wins!")
    else:
        print("Computer wins!")

# input 
player = input("Choose : (rock, paper, or scissors): ")
RockPaperScissor(player)