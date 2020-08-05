from actuator.square import Square

class Square_map(object):
    def __init__(self, size = (8, 8)):
        self.real_size = size
        self.size = ( size[0]+1, size[1]+1 )
        self.list = []
        self.map = []

        self.init_list().init_map()

    def init_list(self):
        for i in range( self.size[0] * self.size[1] ):
            self.list.append( Square() )
        return self

    def init_map(self):
        for x in range( self.size[0] ):
            for y in range( self.size[1] ):
        return self
