from collections import defaultdict, Counter
from functools import lru_cache
from itertools import *
from numpy import product, array
import re
import sys
from timeit import default_timer as timer


def main(inp, is_real):
    inp = inp.strip().split('\n')
    time = int(inp[0].replace(" ", "").split(':')[1])
    distance = int(inp[1].replace(" ", "").split(':')[1])

    start = 0
    for i in range(time):
        new_dist = i * (time - i)
        if new_dist > distance:
            start = i
            break
    stop = 0
    for i in range(time, 0, -1):
        new_dist = i * (time - i)
        if new_dist > distance:
            stop = i
            break
    print(f'start: {start}, stop: {stop}, res: {stop - start + 1}')

sample_input = r"""
Time:      7  15   30
Distance:  9  40  200
"""

real_input = r"""
Time:        42     89     91     89
Distance:   308   1170   1291   1467
"""


if len(sample_input.strip()) > 0:
    print("sample:")
    start = timer()
    main(sample_input, False)
    end = timer()
    print(f'sample: {(end-start)*1000_000:.0f}μs ({(end-start)*1000:.0f}ms)')


print("real:")
start = timer()
main(real_input, True)
end = timer()
print(f'sample: {(end-start)*1000_000:.0f}μs ({(end-start)*1000:.0f}ms)')