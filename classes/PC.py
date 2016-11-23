from store import store
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
Test = user('Test','123','123')

Board = mother_board('brand','model',10.00,'1','socket','mem_type',['HD_connections'])
Chip = micro('brand','model',15.01,'2','socket', 'speed')
mem = mem_RAM('brand','model','20.50','3','capacity','mem_type')
drive = hard_drive('brand','model','13.45','4','capacity','con_Type')

Mac = PC(Test,'123',Board,Chip,mem,drive)

lst = []
for e in list(Mac.components):
    lst.append(e.serial)
print lst

print Mac.total_price
print Mac.print_()
