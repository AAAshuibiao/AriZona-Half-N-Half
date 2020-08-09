from actuator import smap
from actuator.square_map import traverse

class SquareOccupied(Exception):
    pass

class Pair():
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class BFS():
    def __init__(self):
        self.map = smap.map.copy()
        self.size = smap.size
        self.pairs = []
        self.start = None

    def start_from(self, start):
        self.start = start
        self.move()

    @traverse
    def move(self, x = None, y = None):
        if self.map[(s, y)].moves != None:
            for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                while True:
                    try:
                        self.map.
                    except KeyError or SquareOccupied:
                        break


class Pairs_finder():
    def __init__(self):
        self.pairs = {}
        self.size = smap.size

    @traverse
    def find_pairs(self, x = None, y = None):
        square = smap.map[(x, y)]
        BFS().start_from(square)
