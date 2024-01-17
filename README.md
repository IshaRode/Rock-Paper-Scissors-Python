# Rock, Paper & Scissors

 Pseudocode : 

 
// Function to play the game 

RockPaperScissor(player)

// Computer function to generate random (rock / paper / scissor )

computer = randomSelect( )

// Winner 

winner = whoWins (player, computer)

// Display result 

Display (player, computer, winner)

// Randomly selected (rock / paper / scissor )

Function randomSelect( ):

// Generate a random number between 1 & 3

randomNum = randomNumberBetween1And3()

// Assign rock, paper, or scissors based on the random number

if randomNum == 1 :
   return "rock"
elif randomNum == 2 :
   return "paper"
else:
   return "scissors"

// Checking the winner

Function whoWins( player, computer ):

if player == computer:
        return "tie"
else if ( player == "rock" and computer == "scissors") or
           ( player == "paper" and computer == "rock") or
           (player == "scissors" and computer == "paper" ) :
        return "player"
else:
        return "computer"

// Function to display the results:

Function displayResult( player, computer, winner ) :
 print("Player :", player)
    print("Computer :", computer)

   if winner == "tie" :
        print("It's a tie!")
    elif winner == "player" :
        print("Player wins!")
    else:
        print("Computer wins!")


