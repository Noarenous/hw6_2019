from Board import *
from Submarine import *
from Destroyer import *
from General import *
from Jet import *


#
# Get User input + validation. Returns coordinates
#
def get_input(prompt, b: Board):
    while (True):
        user_input = input(prompt + " Please enter coordinates (x,y,z) ? ")


        #Print show
        if(user_input == "show"):
            b.print()
            continue
        #Quit Game
        if(user_input == "quit"):
            quit()

        #Get Coordinates
        coor = user_input.replace("(","").replace(")","").split(",")
        if len(coor) != 3:
            print("Invalid entry, too few/many coordinates.")
            continue

        #Validate int 
        try:
            x = int(coor[0])
            y = int(coor[1])
            z = int(coor[2])
        except ValueError:
            print("Invalid entry - only numbers allowed")
            continue

        #Check boundaries
        if(x < 0 or x >= b.x or y < 0 or y >= b.y or z < 0 or z >= b.z):
            print("Invalid coordinates. Values must be 0 < x < {0}. 0 < y < {1}. 0 < z < {2} ".format(b.x,b.y,b.z))
            continue

        #Good
        return(x,y,z)

# Randomly put vessels
def generate_boards(b: Board):
    
    #Add 1 General
    g = General()
    b.insert(g)

    #Add other vessels
    for i in range(5):
        ship = Submarine()
        b.insert(ship)
        
        ship = Jet()
        b.insert(ship)

        ship = Destroyer()
        b.insert(ship)

# Start the game
def start():
    b = user2Board
    while(True):

        #switch users
        if(b == user1Board):
            b = user2Board
            prompt = "Player 2> "
        else:
            b = user1Board
            prompt = "Player 1> "
        
        print("-------------------")

        #Get coordinates
        (x,y,z) = get_input(prompt, b)

        #Check if hit
        res = b.check(x,y,z)

        #Print the result
        print(res)

        #check if game over
        if(b.General == 0 or (b.Submarine == 0 and b.Destroyer == 0 and b.Jet == 0)):
            print("GAME OVER")
            input("Click Enter to end game")
            quit()


if __name__=="__main__":

    #create boards
    user1Board = Board(6,6)
    user2Board = Board(6,6)

    #add some ships randomly
    generate_boards(user1Board)
    generate_boards(user2Board)

    start()

    #pickle.dump(generate_boards(user1Board), open("trial.dat", "wb"))
    
    


    
