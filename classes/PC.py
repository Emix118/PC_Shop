from user import user
from mother_board import mother_board
from micro import micro
from mem_RAM import mem_RAM
from hard_drive import hard_drive


class PC():

    def __init__(self, client, password, mother_board, micro, RAM, hard_drive):
        if not client.check(client.username,password):
            print "Wrong username or password"
            return
        self.client = client
        self.mother_board = mother_board
        self.micro = micro
        self.RAM = RAM
        self.hard_drive = hard_drive
        self.components =[self.mother_board,self.micro,self.RAM,self.hard_drive]
        self.total_price = 0
        for e in self.components:
            self.total_price+= float(e.price)
        return


    def print_(self):
        print "                   "
        print self.client.username
        print "=============="
        print self.total_price
        return "                  "


#TEST ZONE
#-------------------------------------------------------------------------------
