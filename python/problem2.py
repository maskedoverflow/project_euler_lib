from itertools import takewhile

from eulerlib import fibonacci


print(sum(x for x in takewhile(lambda x: x <= 4000000, fibonacci())
          if x & 1 == 0))
