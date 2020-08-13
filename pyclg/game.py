from copy import copy
from time import sleep, time
from typing import List

from .cell import Cell
from .map import Map
from .draw import draw_cell, clear, hide_cursor, show_cursor, CELL_SHAPES, puts
from .fps import fps_update


class Game:
    def __init__(self, map: Map):
        self.__map = map
        self.__buf_map = copy(map)

    def __get_surround(self, x: int, y: int) -> List[Cell]:
        mget = self.__buf_map.get

        return [mget(x-1, y-1), mget(x, y-1), mget(x+1, y-1),
                mget(x-1, y),   mget(x+1, y), 
                mget(x-1, y+1), mget(x, y+1), mget(x+1, y+1)]

    def update_map(self):
        matrix = self.__map.matrix
        get_surround = self.__get_surround

        self.__buf_map = copy(self.__map)

        for y, line in enumerate(matrix):
            for x, cell in enumerate(line):
                surround = self.__get_surround(x, y)
                cell.update(surround)

        self.__map.matrix = self.__buf_map.matrix.copy()

    def draw_map(self):
        matrix = self.__map.matrix

        buf = ''

        puts(0, 0, '')

        for y, line in enumerate(matrix):
            for x, cell in enumerate(line):
                buf += CELL_SHAPES[cell.state]
            buf += '\n'
        
        print(buf, end='')

    def run(self):
        iterc = 0
        stime = time()
        try:
            clear()
            hide_cursor()

            while True:
                self.draw_map()
                self.update_map()

                iterc += 1

                fps_update()
        except (KeyboardInterrupt, EOFError):
            clear()

            print('Simulation terminated.')
            print('Number of iterations: %s' % iterc)
            print('avg fps: %s' % int(iterc / int(time() - stime)))
        except:
            raise

        finally:
            show_cursor()

