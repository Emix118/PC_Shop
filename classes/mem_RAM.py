from components import components

class mem_RAM(components):

    def __init__(self,brand,model,price,serial,
                 capacity,mem_type):

        components.__init__(self,brand,model,price,serial)
        self.mem_type = mem_type
        self.capacity = capacity
        return
