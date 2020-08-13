from .drawtools import puts, clear, hide_cursor, show_cursor


CELL_DEAD = ' '
CELL_ALIVE = '■'

CELL_SHAPES = (CELL_DEAD, CELL_ALIVE)


def draw_cell(x: int, y: int, state: int):
    puts(x, y, CELL_SHAPES[state])

