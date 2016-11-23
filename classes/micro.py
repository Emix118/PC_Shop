from components import components

class micro(components):

    def __init__(self,brand,model,price,serial,
                 socket,speed):

        components.__init__(self,brand,model,price,serial)
        self.socket = socket
        self.speed = speed
        return
