import pickle
from HW1 import *

class TestGame:
    def check_submarine(self):
        b = Board(4,4)
        sub = Submarine()
        assert(sub.add_to_right(b,0,0,0)==True)
        assert(sub.add_to_right(b,1,0,0)==False)
        
        assert(sub.add_to_below(b,3,3,0)==False)
        assert(sub.add_to_below(b,0,0,1)==True)

        assert(b.check(0,0,0)!= "MISS")
        assert(b.check(1,1,1) == "MISS")

    def check_destroyer(self):
        b = Board (4,4)
        dst= Destroyer()
        assert(dst.add_right(b,0,0,0)==True)
        assert(dst.add_right(b,1,0,0)==False)

        assert(dst.add_below(b,0,0,1)==True)
        assert(dst.add_below(b,3,3,0)==False)

        assert(b.check(0,0,0)!="MISS")
        assert(b.check(1,1,1) == "MISS")

    def check_jet(self):
        b= Board(4,4)
        j= Jet()
        assert(j.add_horizontal(b,0,1,0)==True)
        assert(j.add_horizontal(b,0,1,0)==False)

        assert(j.add_vertical(b,1,0,1)==True)
        assert(j.add_vertical(b,3,3,0)==False)

        assert(b.check(0,1,0)!= "MISS")
        assert(b.check(0,0,0) == "MISS")


t =TestGame()
t.check_submarine()
t.check_destroyer()
t.check_jet()
print('pass')

        

