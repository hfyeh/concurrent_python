import sys
import time

from components import add

if __name__ == '__main__':
    round = 0
    while True and round < 2:
        stdin = sys.stdin.readline().rstrip()

        if (stdin == ''):
            continue
        else:
            start = time.time()

            result = add(int(stdin))

            end = time.time()
            sys.stderr.write(f'Time cost for add {end - start}\n')
            sys.stderr.flush()

            round += 1

