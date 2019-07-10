import numpy as np
from Board import *
import random



class General():
    #
    #General was hit - mark the as not floating anymore
    #
    def hit(self, board: Board, x, y, z):
        self.floating = False
        board.General = 0
        return "General SUNK"
    
    #
    #Add a general randomly on the board
    #
    def add_to_board(self, board: Board):
        # Dont add more than 1 general
        if(board.General > 0):
            return

        #Get random x,y,z
        x = random.randint(1, board.x) - 1
        y = random.randint(1, board.y)-1
        z = random.randint(1, board.z)-1

        orgx = x
        orgy = y
        orgz = z
 
        #Loop until you can place the sub
        while True:
            if(board.board[x,y,z] == 0):
                board.board[x,y,z] = self
                board.General = 1
                self.floating = True
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

    #           
    #__str__  Print the submarine information
    #
    def __str__(self):
        if(self.floating):
            return "**GEN**"
        else:
            return "gen"

