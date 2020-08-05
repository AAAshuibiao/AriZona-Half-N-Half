from actuator.square import Square


def trimmed(func):
    
def traverse(func):
    def inner(self):
        for y in range(self.size['Y']):
            for x in range(self.size['X']):
                info = func(self, x, y)
                if info:
                    print(str(info), end = ", ")
                    if x+1 == self.size['X']: print()
    return inner


class Square_map(object):
    def __init__(self, size = (8, 8)):
        self.size = { 'X': size[0]+2, 'Y': size[1]+2 }
        self.edgeless_size = { 'X': size[0], 'Y': size[1] }

        self.length = self.size['X'] * self.size['Y']

        self.list = []
        self.map = {}

        self.init_list().init_map().init_edge()

        self.debug_print_ids()

    def init_list(self):
        for i in range( self.length ):
            self.list.append( Square(i) )
        return self

    @traverse
    def init_map(self, x = None, y = None):
        index = x + self.size['X'] * y
        self.map[(x, y)] = self.list[index]
        return None

    @traverse
    def init_edge(self, x = None, y = None):
        if not x == 0 and not x+1 == self.size['X']: pass
        elif not y == 0 and not y+1 == self.size['Y']: pass
        else: self.map[(x, y)].is_edge = False

    @traverse
    def debug_print_ids(self, x = None, y = None):
        return self.map[(x, y)].ID
