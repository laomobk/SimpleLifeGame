from sys import argv

from os import get_terminal_size
from .game import Game
from .map import Map, MapProperty


def get_height_width_from_arg() -> tuple:
    if len(argv) == 3:
        return int(argv[1]), int(argv[2])
    else:
        print('pyclg [width] [height]')
    return None, None


if __name__ == '__main__':
    prop = MapProperty()
    
    h, w = get_height_width_from_arg()
    
    if h is not None:
        prop.height, prop.width = h, w
        Game(Map.from_seed(prop)).run()
