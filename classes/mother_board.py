from components import components

class mother_board(components):

    def __init__(self,brand,model,price,serial,
                 socket,mem_type,HD_connections):

        components.__init__(self,brand,model,price,serial)
        self.socket = socket
        self.mem_type = mem_type
        self.HD_connections = HD_connections
        return 
