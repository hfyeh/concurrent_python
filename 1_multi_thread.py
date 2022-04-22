from threading import Thread
from queue import Queue

from components import *


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

