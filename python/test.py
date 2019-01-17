import operator

import eulerlib as e

print(list(e.segment_reduce(operator.add, [1, 2], 3)))