import operator

import eulerlib

with open(r"8\number.txt") as file:
    num = file.read()

num = [int(l) for l in num]
print(max(eulerlib.segment_reduce(operator.mul, num, 13)))
