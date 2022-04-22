from threading import Thread
from multiprocessing import Process, Queue

from components import *


if __name__ == '__main__':
    q1 = Queue()
    q2 = Queue()

    p1 = Process(target=mul_with_time, args=(q1, q2), daemon=True)
    p2 = Process(target=add_with_time, args=(q2,), daemon=True)
    p1.start()
    p2.start()

    for i in range(2):
        q1.put(11)

    p1.join()
    p2.join()

