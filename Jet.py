import numpy as np
from Board import *
import random



class Jet():
    #
    #Jet was hit - mark the sub as not floating anymore
    #
    def hit(self, board: Board, x, y, z):
        
        if(self.floating):
            self.floating = False
            #Remove total number of subs
            board.Jet = board.Jet - 1
            return "Jet" + str(self.id) + " SUNK"

        #was already hit
        return "Jet" + str(self.id) + " ALREADY SUNK"

    
    #
    #Add a Jet randomly on the board
    #
    def add_to_board(self, board: Board):

        #Get random x,y,z
        x = random.randint(1, board.x) - 1
        y = random.randint(1, board.y)-1
        z = random.randint(1, board.z)-1

        orgx = x
        orgy = y
        orgz = z
 
        #Loop until you can place the sub
        while True:
            if(self.add_horizontal(board, x, y, z)):
                return True
            
            if(self.add_vertical(board, x, y, z)):
                return True

            #You can not add, so increment coordinate
            x = x+1
            if(x >= board.x):
                x = 0
                y = y + 1
            if(y >= board.y):
                y = 0
                z = z + 1
            if(z >= board.z):
                z = 0
            #If we tried all options - return false
            if(x == orgx and y == orgy and z == orgz ):
                return False

    def add_horizontal(self,board,x,y,z):
        if(can_add_horizontal(board, x,y,z)):
            #We can add on the right - add yourself to the board
            board.board[x,y,z] = self
            board.board[x+1,y,z] = self
            board.board[x+2,y,z] = self
            board.board[x+3,y,z] = self
            board.board[x+2,y+1,z] = self
            board.board[x+2,y-1,z] = self

            #Give yourself an new id and increment the number of subs
            self.id = board.Jet
            board.Jet = board.Jet + 1   
            
            self.floating = True                     
            return True
        return False

    def add_vertical(self,board,x,y,z):
        if(can_add_vertical(board,x,y,z)):
            #We can add below - add yourself to the board
            board.board[x,y,z] = self
            board.board[x,y+1,z] = self
            board.board[x,y+2,z] = self
            board.board[x,y+3,z] = self
            board.board[x-1,y+2,z] = self
            board.board[x+1,y+2,z] = self

            #Give yourself an new id and increment the number of subs
            self.id = board.Jet
            board.Jet = board.Jet + 1                            

            self.floating = True                      
            return True
        return False

    #           
    #__str__  Print the Jet information
    #
    def __str__(self):
        if(self.floating):
            return "JET" + str(self.id)
        else:
            return "jet" + str(self.id)

  

#Check if we can add a Jet to the right
def can_add_horizontal(b, x,y,z):
    cell = b.board[x,y,z]
    
    if(cell != 0):
        return False

    if( x+1 >= b.x):
        return False
    
    if(b.board[x+1, y, z]!= 0):
        return False

    if(x+2 >= b.x):
        return False
    
    if(b.board[x+2,y,z]!= 0):
           return False

    if(x+3 >= b.x):
        return False
    
    if(b.board[x+3,y,z]!= 0):
           return False   

    if(y - 1 < 0):
        return False
    
    if(b.board[x+2,y-1,z] != 0):
        return False
    
    if(y + 1 >= b.y):
        return False

    if(b.board[x+2,y+1,z] != 0):
        return False
 
    return True

#Check if we can add a Jet below
def can_add_vertical(b,x,y,z):
   
    cell = b.board[x,y,z]
    
    if(cell != 0):
        return False

    if( y+1 >= b.y):
        return False
    
    if(b.board[x, y+1, z]!= 0):
        return False

    if(y+2 >= b.y):
        return False
    
    if(b.board[x,y+2,z]!= 0):
           return False

    if(y+3 >= b.y):
        return False
        
    if(b.board[x,y+3,z]!= 0):
           return False
    
    if(x - 1 < 0):
        return False

    if(b.board[x-1,y+2,z] != 0):
        return False

    if(x + 1 >= b.x):
        return False

    if(b.board[x+1, y+2, z] != 0):
        return False

    return True

