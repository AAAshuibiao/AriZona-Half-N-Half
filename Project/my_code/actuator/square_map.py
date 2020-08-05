from actuator.square import Square


class Square_map(object):
    def __init__(self, size = (8, 8)):
        self.real_size = size
        self.size = ( size[0]+2, size[1]+2 )
        self.list = []
        self.map = []

        self.init_list().init_map()

        self.print_ids()
        print(self.map)

    def init_list(self):
        for i in range( self.size[0] * self.size[1] ):
            self.list.append( Square(i) )
        return self

    def init_map(self):
        for y in range( self.size[1] ):
            line = []
            for x in range( self.size[0] ):
                i = x + y * self.size[0]
                line.append( self.list[i] )
            self.map.append(line)
        return self

    def print_ids(self):
        for y in range( self.size[1] ):
            for x in range( self.size[0] ):
                print(str(self.map[y][x].id) + ", ", end = '')
            print()
