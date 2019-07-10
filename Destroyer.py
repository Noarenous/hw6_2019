import numpy as np
from Board import *
import random



class Destroyer():
    
    #
    #Destroyer was hit - mark the sub as not floating anymore
    #
    def hit(self, board: Board, x, y, z):
        
        if(self.floating == False):
            return "Destroyer" + str(self.id) + " ALREADY SUNK"
        
        if((x,y,z) in self.hitted ):
            return "Destroyer" + str(self.id) + " hitted there already"

        self.hitted.append((x,y,z))

        if(sorted(self.hitted ) != sorted(self.coordinates)):
            return "Destroyer" + str(self.id) + " hit"
        
        self.floating = False
        board.Destroyer = board.Destroyer - 1
        return "Destroyer" + str(self.id) + " SUNK"

    
    #
    #Add a Destroyer randomly on the board
    #
    def add_to_board(self, board: Board):

        #Get random x,y,z
        x = random.randint(1, board.x) - 1
        y = random.randint(1, board.y) -1
        z = random.randint(1, board.z) -1

        orgx = x
        orgy = y
        orgz = z
 
        #Loop until you can place the sub
        while True:
            if(self.add_right(board, x, y, z)):
                return True
            
            if(self.add_below(board, x, y, z)):
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

    def add_right(self,board,x,y,z):
        if(can_add_right(board, x,y,z)):
            #We can add on the right - add yourself to the board
            board.board[x,y,z] = self
            board.board[x+1,y,z] = self
            board.board[x+2,y,z] = self
            board.board[x+3,y,z] = self

            #Give yourself an new id and increment the number of subs
            self.id = board.Destroyer
            board.Destroyer = board.Destroyer + 1   
            
            #Keep the coorrdinates of this sub, and mark that you are floating 
            self.coordinates =   [(x,y,z), (x+1,y,z), (x+2,y,z), (x+3,y,z)] 
            self.hitted = []
            self.floating = True                     
            return True
        return False

    def add_below(self,board, x,y,z):
        if(can_add_below(board,x,y,z)):
            #We can add below - add yourself to the board
            board.board[x,y,z] = self
            board.board[x,y+1,z] = self
            board.board[x,y+2,z] = self
            board.board[x,y+3,z] = self

            #Give yourself an new id and increment the number of subs
            self.id = board.Destroyer
            board.Destroyer = board.Destroyer + 1                            

            #Keep the corrdinates of this sub, and mark that you are floating 
            self.coordinates =   [(x,y,z), (x,y+1,z), (x,y+2,z), (x, y+3, z)] 
            self.hitted = []
            self.floating = True                      
            return True
        return False


    #           
    #__str__  Print the Destroyer information
    #
    def __str__(self):
        if(self.floating):
            return "DST" + str(self.id)
        else:
            return "dst" + str(self.id)

  

#Check if we can add a Destroyer to the right
def can_add_right(b, x,y,z):
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
    
    return True

#Check if we can add a Destroyer below
def can_add_below(b,x,y,z):
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
        
    return True

