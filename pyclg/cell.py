from typing import List


STATE_DEAD = 0
STATE_ALIVE = 1


class Cell:
    def __init__(self, init_state: int=STATE_DEAD):
        self.__state = init_state

    @property
    def state(self):
        return self.__state

    def __get_alive_number(self, surround: List['Cell']) -> int:
        snum = 0

        for c in surround:
            if isinstance(c, Cell):
                snum += 1 if c.state else 0

        return snum

    def update(self, surround: List['Cell']) -> int:
        """
        :param surround: 8 cells surrounding this cell.
                       if not enough, fill it up with None.
        :return: state of this cell.
        """

        alive = self.__get_alive_number(surround)

        if self.__state:
            self.__case_alive(alive)
        else:
            self.__case_dead(alive)


    def __case_dead(self, alive: int):
        if alive == 3:
            self.__state = 1

    def __case_alive(self, alive: int):
        if alive < 2:
            self.__state = 0

        elif alive > 3:
            self.__state = 0
    
    def __str__(self) -> str:
        return '<Cell state = %s>' % (self.state)

    __repr__ = __str__
