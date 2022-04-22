import sys
import time

from components import *

if __name__ == '__main__':
    for i in range(2):
        start = time.time()
        x = mul(11)
        end = time.time()
        sys.stderr.write(f'Time cost for mul {end - start}\n')
        sys.stderr.flush()

        start = time.time()
        y = add(x)
        end = time.time()
        sys.stderr.write(f'Time cost for add {end - start}\n')
        sys.stderr.flush()

