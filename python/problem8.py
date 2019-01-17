import operator

from eulerlib import segment_reduce

with open(r"8\number.txt") as file:
    num = file.read()

num = [int(l) for l in num]
print(max(segment_reduce(operator.mul, num, 13)))
