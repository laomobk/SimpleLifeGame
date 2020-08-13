from time import time

from .drawtools import puts, bgstr


class _FPSMonitor:
    def __init__(self):
        self.__last_mrsec = 0

    def update(self):
        now_mrsec = time() * 1000
        
        interval = now_mrsec - self.__last_mrsec
        self.__last_mrsec = now_mrsec

        fps = int(1 / (interval / 1000))

        puts(0, 0, bgstr('[fps: %s]' % fps))


FPS_MONITOR = _FPSMonitor()


def fps_update():
    FPS_MONITOR.update()
