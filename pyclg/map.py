from random import randint
from random import seed as set_seed
from time import time
from typing import List

from .cell import Cell


class MapProperty:
    def __init__(self):
        self.height = 10
        self.width = 10


class Map:
    def __init__(self, matrix: List[List[Cell]], prop: MapProperty):
        self.prop = prop
        self.matrix = matrix

    def get(self, x: int, y: int) -> Cell:
        """
        :return: Cell in (x, y), if out of range, returns None.
        """
        if 0 <= y < self.prop.height:
            if 0 <= x < self.prop.width:
                return self.matrix[y][x]
        return None
    
    @staticmethod
    def from_seed(prop: MapProperty, seed: int=None) -> 'Map':
        if seed is None:
            seed = time()

        set_seed(seed)
        height = prop.height
        width = prop.width

        matrix = [[Cell(randint(0, 1)) for x in range(width)].copy() 
                  for y in range(height)]

        return Map(matrix, prop)

