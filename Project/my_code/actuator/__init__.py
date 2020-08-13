import loader

from . import square_map
smap = square_map.Square_map()

from . import pairs_finder
pfinder = pairs_finder.Pairs_finder()
p = pairs_finder.Pair

ready = True


class WhatThtFuck(Exception):
    pass

def CRAP():
    for (x, y) in smap.map:
        square = smap.map[(x, y)]
        if square.number != None:
            return False
    return True


def begin():
    ag = loader.autoGrader

    while True:
        pfinder.find_pairs()
        if len(pfinder.pairs) == 0 and not CRAP():
            anything = []
            red_s, green_s, blue_s = [[], [], []]
            for (x, y) in smap.map:
                square = smap.map[(x, y)]
                if square.number != None:
                    anything.append((x, y))
                    if square.psargs["is_known"] == False:
                        if square.color == 'R': red_s.append((x, y))
                        elif square.color == 'G': blue_s.append((x, y))
                        elif square.color == 'B': green_s.append((x, y))
            try:
                while red_s: pfinder.pairs.append(p(red_s.pop(), red_s.pop(), 4))
                while blue_s: pfinder.pairs.append(p(blue_s.pop(), blue_s.pop(), 4))
                while green_s: pfinder.pairs.append(p(green_s.pop(), green_s.pop(), 4))
                if len(pfinder.pairs) == 0: raise WhatThtFuck
            except Exception:
                try:
                    bruh = red_s + blue_s + green_s
                    pfinder.pairs.append(p(bruh.pop(), bruh.pop(), 4))
                    if len(pfinder.pairs) == 0: raise WhatThtFuck
                except Exception as ARE_U_REALLY:
                    pfinder.pairs.append(p(anything.pop(), anything.pop(), 4))
            continue
        for i in range(1, 5):
            for pair in pfinder.pairs:
                if pair.distance == i:
                    args = [pair.start[1]-1, pair.start[0]-1, pair.end[1]-1, pair.end[0]-1]
                    
                    r = ag.link(*args)
                    if type(r) != int:
                        smap.map[pair.start].number = r[0][1]
                        smap.map[pair.start].color = ['R', 'G', 'B'][r[0][0]]
                        smap.map[pair.end].number = r[1][1]
                        smap.map[pair.end].color = ['R', 'G', 'B'][r[1][0]]
                        smap.map[pair.start].psargs["is_known"] = True
                        smap.map[pair.end].psargs["is_known"] = True
                    else:
                        smap.map[pair.start].number = None
                        smap.map[pair.end].number = None
                        smap.map[pair.start].color = None
                        smap.map[pair.end].color = None
                    break
            else: continue
            break
        else:
            if CRAP(): break
            if CRAP(): print("DONE")
            else: print("FUCK IM OUT")
        pfinder.pairs = []
