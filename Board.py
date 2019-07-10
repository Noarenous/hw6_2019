import numpy as np


class Board:

    #
    # __init - Keep the dimensions of the board
    #
    def __init__(self, x, y, z=3):
        self.x= x
        self.y= y
        self.z= z

        # create_board - Initialize a board of objects, and set default values to 0 (free cell)
        self.board= np.zeros((self.x, self.y, self.z), dtype= object)

        #Number of vessels on the board
        self.General = 0
        self.Submarine = 0
        self.Jet = 0
        self.Destroyer = 0



    #
    # check - a cell and see if there is a hit
    #
    def check(self,x,y,z):
        cell = self.board[x,y,z]
        # cell is free -- this is a miss
        if(cell == 0 ):
            return "MISS"

        # There is a ship - hit it.
        return cell.hit(self, x, y, z)

    #
    # insert -- add a ship randomly on the board
    #
    def insert(self, ship: object):
        # tell the ship to add itself
        ship.add_to_board(self)

    #
    # print -- nice  print of the board
    #
    def print(self):
        for z in range(self.z):
            print("")
            print(["Deep:", "Sea-level:", "Air:"][z])
            for y in range(self.y):
                print( "[", end =" ")
                for x in range(self.x):
                    cell = self.board[x,y,z]
                    if(cell == 0):
                        print( "free", end =" ")
                    else:
                        print(cell, end = " ")
                print("]")








