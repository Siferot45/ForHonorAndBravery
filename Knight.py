from collections.abc import Callable
from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name_knight, power_knight, total_enemies = 100): 

        super().__init__()
        self.name_knight = name_knight
        self.power_knight = power_knight
        self.total_enemies = total_enemies


    def run(self):
        print(f"{self.name_knight}, на нас напали!")

        current_day = 0

        while self.total_enemies > 0:
            time.sleep(1)
            current_day += 1
            self.total_enemies -= self.power_knight
            print(f"{self.name_knight} сражается {current_day} день(дня)..., осталось {self.total_enemies} воинов.")

        print(f"{self.name_knight} одержал победу спустя {current_day} дней(дня)!")



