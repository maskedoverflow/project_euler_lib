from itertools import takewhile
from time import time

from eulerlib import fibonacci

t0 = time()

print(sum(x for x in takewhile(lambda x: x <= 4000000, fibonacci())
          if x & 1 == 0))

print(time() - t0)
