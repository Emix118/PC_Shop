from components import components

class micro(components):

    def __init__(self,brand,model,price,serial,
                 socket, speed):

        super().__init__(brand,model,price,serial)
        self.socket = socket
        self.mem_type = mem_type
        self.HD_connections = HD_connections
