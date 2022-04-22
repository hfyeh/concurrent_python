import sys
import time

def add(n: int) -> int:
    result = 0

    for i in range(n):
        result += (i + 1)

    return result


def mul(n: int) -> None:
    # Run many times to get longer execution period
    for x in range(4000000):
        result = 1

        for i in range(n):
            result *= (i + 1)

    return result


def mul_with_time(q1, q2) -> int:
    round = 0
    while True and round < 2:
        n = q1.get()
        start = time.time()

        q2.put(mul(n))
        round += 1

        end = time.time()
        sys.stderr.write(f'Time cost for mul {end - start}\n')
        sys.stderr.flush()


def add_with_time(q) -> int:
    round = 0
    while True and round < 2:
        n = q.get()
        start = time.time()

        add(n)
        round += 1

        end = time.time()
        sys.stderr.write(f'Time cost for mul {end - start}\n')
        sys.stderr.flush()

