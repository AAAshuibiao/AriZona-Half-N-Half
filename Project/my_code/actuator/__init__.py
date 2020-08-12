import loader

from . import square_map
smap = square_map.Square_map()

from . import pairs_finder
pfinder = pairs_finder.Pairs_finder()

ready = True


def begin():
    ag = loader.autoGrader

    while True:
        pfinder.find_pairs()
        a = pfinder.pairs
        b = 0
        for i in range(1, 5):
            for pair in pfinder.pairs:
                if pair.distance == i:
                    args = [pair.start[1]-1, pair.start[0]-1, pair.end[1]-1, pair.end[0]-1]
                    
                    ag.link(*args)
                    smap.map[pair.start].number = None
                    smap.map[pair.end].number = None
                    smap.map[pair.start].color = None
                    smap.map[pair.end].color = None
                    break
            else: continue
            break
        pfinder.pairs = []
