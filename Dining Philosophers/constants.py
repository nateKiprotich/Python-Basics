from threading import Thread
import time
import random
from enum import Enum
from threading import Lock


NUMBER_OF_PHILOSOPHERS = 5
NUMBER_OF_CHOPSTICKS = 5
SIMULATION_RUNNING_TIME = 30


# Enum
# State of the chopsticks
class State(Enum):
    LEFT = 0
    RIGHT = 1


class ChopStick:

    def __init__(self, stick_id):
        self.stick_id = stick_id
        self.lock = Lock()

    def pick_up(self, phil, state):
        # Each philosopher will wait for the lock for 1 sec
        if self.lock.acquire(True, 1):
            print('Philosopher %s picked up chopstick %s ' % (phil, state))
            return True
        return False

    def put_down(self, phil, state):
        self.lock.release()
        print('The philosopher %s put down stick %s ' % (phil, state))

    def __str__(self):
        return 'Chopstick - ' + str(self.stick_id)


class Philosopher(Thread):

    def __init__(self, philosopher_id, left_stick, right_stick):
        Thread.__init__(self)
        self.philosopher_id = philosopher_id
        self.left_stick = left_stick
        self.right_stick = right_stick
        self.running = True
        self.eating_counter = 0

    def run(self):

        try:
            while self.running:
                self.think()

                if self.left_stick.pick_up(self, State.LEFT):
                    if self.right_stick.pick_up(self, State.RIGHT):
                        self.eat()
                        self.left_stick.put_down(self, State.RIGHT)
                    self.left_stick.put_down(self, State.LEFT)
        except Exception as e:
            print(e)

    def think(self):
        print(str(self) + ' is eating ...')
        time.sleep(random.random())

    def eat(self):
        print(str(self) + ' is eating ...')
        self.eating_counter += 1
        time.sleep(random.random())

    def stop(self):
        self.running = False

    def __str__(self):
        return 'Philosopher - ' + str(self.philosopher_id)


if __name__ == '__main__':

    chop_sticks = []
    philosophers = []

    for index in range(NUMBER_OF_CHOPSTICKS):
        chop_sticks.append(ChopStick(index))

    for index in range(NUMBER_OF_CHOPSTICKS):
        philosophers.append(Philosopher(index, chop_sticks[index], chop_sticks[(index+1) % NUMBER_OF_PHILOSOPHERS]))
        philosophers[index].start()

    time.sleep(SIMULATION_RUNNING_TIME)

    for p in philosophers:
        p.stop()
        p.join()

    for p in philosophers:
        print('Philosopher %s eats %s times ...' % (p, str(p.eating_counter)))
