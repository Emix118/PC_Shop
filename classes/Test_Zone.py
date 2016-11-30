from user import user
from store import store
from components import components
from mother_board import mother_board
from micro import micro
from mem_RAM import mem_RAM
from hard_drive import hard_drive
from PC import PC

Test = user('Test','123','123',admin=True)

users = {Test}
Shop = store(dics = [users])
print Shop.users
Bob = user('Bob','123','123')
print Shop.users

#Shop.add(Test,'123',Shop.HD,Board)
#Shop.mod(Test,'123',Shop.HD,Board,mem)

"""
Mac = PC(Test,'123',Board,Chip,mem,drive)

mem = mem_RAM('brand','model','20.50','3','capacity','mem_type')
Board = mother_board('brand','model',10.00,'1','socket','mem_type',['HD_connections'])
Chip = micro('brand','model',15.01,'2','socket', 'speed')
drive = hard_drive('brand','model','13.45','4','capacity','con_Type')

lst = []
for e in list(Mac.components):
    lst.append(e.serial)
print lst

print Mac.total_price
print Mac.print_()
"""
#dics = [self.MB,self.RAM,self.Micro,self.HD,self.bought_PCs,self.users]
