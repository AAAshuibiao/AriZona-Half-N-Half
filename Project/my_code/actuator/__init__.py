import loader

from . import square_map
smap = square_map.Square_map()

from . import pairs_finder
pfinder = pairs_finder.Pairs_finder()

ready = True


def begin():
    pfinder.find_pairs()
