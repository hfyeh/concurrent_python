import sys
import time

from components import mul

if __name__ == '__main__':
    for i in range(2):
        start = time.time()

        print(mul(11), flush=True)

        end = time.time()
        sys.stderr.write(f'Time cost for mul {end - start}\n')
        sys.stderr.flush()

