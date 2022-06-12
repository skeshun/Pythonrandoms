#Rock, Paper, Scissors Game
import random
    
#list of available options
choices = ["R","P","S"]
#keep_playing = "true"
while True:
    # CPU makes choice at random 
    CPU = random.choice(choices)
    if CPU == "R":
        CPU = "(Rock)"
    elif CPU == "P":
        CPU = "(Paper)"
    elif CPU == "S":
        CPU = "(Scissors)"
    # prompt Player to pick an option between "R", "P" or "S"
    Player = input("Please select an option between between 'R','P','S', (type q to quit) :").upper()

    if Player=="Q":
        break

    if Player == "R":
        Player = "(Rock)"
    elif Player == "P":
        Player = "(Paper)"
    elif Player == "S":
        Player = "(Scissors)"
    
    elif Player not in choices:
        print("Error! Please select a valid response")
        continue
    print(f"\nPlayer {Player} : CPU {CPU}")
    
    # if CPU and Player pick same move, it is a tie
    # restart the game from step 3
    if Player == CPU:
        print("TIE")
        
    elif Player == "(Rock)" and CPU == "(Scissors)" :
       print("Rock beats Scissors! Player wins!")
        
    elif Player == "(Paper)" and CPU == "(Rock)":
       print("Paper beats Rock! Player wins!")
      
    elif Player == "(Scissors)" and CPU == "(Paper)":
       print("Scissors beats Paper! Player wins!")
   
    else:
       print("CPU wins!")
       break
       
   
      # if user input is invalid (not amongst choices), print an error, and ask for their input again
    #else:
#        print("Error! Please select a valid response: \n")
#        continue