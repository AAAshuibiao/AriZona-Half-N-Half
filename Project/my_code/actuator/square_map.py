from loader import pictures
from actuator.square import Square

import loader

def edgeless(func):
    def inner(self):
        return func(self, True)
    return inner

def traverse(func):
    def inner(self, trim = False):
        if not trim:
            sizes = [ [ 0, self.size['X'] ], [ 0, self.size['Y'] ] ]
        else:
            sizes = [ [1, self.size['X']-1 ], [ 1, self.size['Y']-1 ] ]
        
        for y in range(*sizes[1]):
            for x in range(*sizes[0]):
                info = func(self, x, y)
                if info != None:
                    print(str(info), end = ", ", file = loader.stdout)
                    if x+1 == sizes[0][1]: print(file = loader.stdout)
        
        return self
    return inner


class Square_map(object):
    def __init__(self, size = (8, 8)):
        self.size = { 'X': size[0]+2, 'Y': size[1]+2 }
        self.edgeless_size = { 'X': size[0], 'Y': size[1] }

        self.length = self.size['X'] * self.size['Y']

        self.list = []
        self.map = {}

        self.image_vectors = []

        self.init_list().init_map().init_edge()

        self.simple_predictions = []

        #self.debug_print_ids()
        #self.debug_print_edgeless_ids()

    def init_list(self):
        for i in range( self.length ):
            self.list.append( Square(i) )
        return self

    @traverse
    def init_map(self, x = None, y = None):
        index = x + self.size['X'] * y
        self.map[(x, y)] = self.list[index]

    @traverse
    def init_edge(self, x = None, y = None):
        if x in [0, self.size['X']-1]: pass
        elif y in [0, self.size['Y']-1]: pass
        else: self.map[(x, y)].is_edge = False

    @edgeless
    @traverse
    def load_image_vectors(self, x = None, y = None):
        self.image_vectors.append(
            self.map[(x, y)].image_data.greyscale
        )

    @edgeless
    @traverse
    def print_color(self, x = None, y = None):
        return self.map[(x, y)].color

    @traverse
    def _debug_print_ids(self, x = None, y = None):
        return self.map[(x, y)].ID

    @edgeless
    @traverse
    def _debug_print_edgeless_ids(self, x = None, y = None):
        return self.map[(x, y)].ID

    @traverse
    def _debug_print_map(self, x = None, y = None):
        square = self.map[(x, y)]

        if square.is_edge:
            return "ED"
        else:
            return ['R', 'G', 'B'][square.color] + str(square.number)
            #return "IN"
