from threading import Thread
from time import sleep

knights = []


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.pow = 100

    def run(self):
        if self.pow == 100:
            print(f'{self.name}, на нас напали')
        i = 1
        while self.pow > 0:
            self.pow -= self.power
            if self.pow <= 0:
                self.pow = 0
                print(f'{self.name}, сражается {i} день(дня)..., осталось {self.pow} воинов.'+'\n', end='')
            else:
                print(f'{self.name}, сражается {i} день(дня)..., осталось {self.pow} воинов.'+'\n', end='')
                i += 1
                sleep(1)
        print(f'{self.name} одержал победу спустя {i} дней(дня)!'+'\n', end='')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
