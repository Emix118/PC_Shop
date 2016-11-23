from components import components

class hard_drive(components):

    def __init__(self,brand,model,price,serial,
                 capacity,con_Type):

        components.__init__(self,brand,model,price,serial)
        self.capacity = capacity
        self.con_Type = con_Type
        return 
