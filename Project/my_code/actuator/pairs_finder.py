import actuator
from actuator import smap
from actuator.square_map import traverse, edgeless

import loader


class SquareOccupied(Exception):
    pass

class Pair():
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class BFS():
    def __init__(self):
        self.map = None
        self.size = smap.size
        self.start = None
        self.debug_print = False
        self.mcount = 0

    def start_from(self, start):
        self.map = smap.map.copy()
        self.start = start
        if self.map[self.start].number == None and self.map[self.start].color == None:
            return self
        for (x, y) in smap.map:
            try:
                assert smap.map[(x, y)].moves == None
            except AssertionError:
                smap.map[(x, y)].moves = None
        self.map[start].moves = 0
        for i in range(3):
            self.mcount = 0
            self.move()
            if self.mcount == 0: break
        return self

    @traverse
    def move(self, x = None, y = None):
        if self.map[(x, y)].moves != None and self.map[(x, y)].moves <= 4:
            for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                poz = (x, y)
                while True:
                    poz = (poz[0] + direction[0], poz[1] + direction[1])
                    try:
                        if self.debug_print:
                            smap._debug_print_map()
                            print("\n\n\n\n\n", file = loader.stdout)
                        if self.map[poz].number != None and self.map[poz].color != None or self.map[poz].moves != None and self.map[poz].moves != self.map[(x, y)].moves + 1:
                            raise SquareOccupied("OOF")
                        else:
                            self.map[poz].moves = self.map[(x, y)].moves + 1
                            self.mcount += 1
                    except KeyError:
                        break
                    except SquareOccupied:
                        if poz != self.start:
                            if self.map[poz].number == self.map[self.start].number and self.map[poz].color == self.map[self.start].color:
                                if [poz, self.start] not in actuator.pfinder.update_pl() and [self.start, poz] not in actuator.pfinder.update_pl():
                                    actuator.pfinder.pairs.append(Pair(self.start, poz, self.map[(x, y)].moves + 1))
                        break


class Pairs_finder():
    def __init__(self):
        self.pairs = []
        self.size = smap.size

    @edgeless
    @traverse
    def find_pairs(self, x = None, y = None):
        BFS().start_from((x, y))

    def update_pl(self):
        pl = []
        for p in self.pairs:
            pl.append([p.start, p.end])
        return pl
