import sys
import time
from threading import Thread
from queue import Queue

from components import *


def mul_with_time(q1: Queue, q2: Queue) -> int:
    round = 0
    while True and round < 2:
        n = q1.get()
        start = time.time()

        q2.put(mul(n))
        round += 1

        end = time.time()
        sys.stderr.write(f'Time cost for mul {end - start}\n')
        sys.stderr.flush()

def add_with_time(q: Queue) -> int:
    round = 0
    while True and round < 2:
        n = q.get()
        start = time.time()

        add(n)
        round += 1

        end = time.time()
        sys.stderr.write(f'Time cost for mul {end - start}\n')
        sys.stderr.flush()

if __name__ == '__main__':
    q1 = Queue()
    q2 = Queue()

    t1 = Thread(target=mul_with_time, args=(q1, q2), daemon=True)
    t2 = Thread(target=add_with_time, args=(q2,), daemon=True)
    t1.start()
    t2.start()

    for i in range(2):
        q1.put(11)

    t1.join()
    t2.join()

