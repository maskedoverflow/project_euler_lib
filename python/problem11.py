import operator

import eulerlib


def max_of_lines(lines):
    return max(max(eulerlib.segment_reduce(operator.mul, line, 4), default=0) for line in lines)


with open(r"11\grid.txt") as f:
    lines = [[int(n) for n in line.split(" ")] for line in f]

xlen = len(lines[0])
ylen = len(lines)
maxes = []

maxes.append(max_of_lines(lines))
maxes.append(max_of_lines(eulerlib.transpose(lines)))

top_diags = [
            [lines[coords[1]][coords[0]]
             for coords in zip(range(start_x, xlen), range(0, min(xlen - start_x, ylen)))]
            for start_x in range(xlen)
            ]
maxes.append(max_of_lines(top_diags))
side_diags = [
             [lines[coords[1]][coords[0]]
              for coords in zip(range(0, min(ylen - start_y, xlen)), range(start_y, ylen))]
             for start_y in range(ylen)
             ]
maxes.append(max_of_lines(side_diags))
rot = eulerlib.rotate(lines)
xlen, ylen = ylen, xlen
top_diags = [
            [rot[coords[1]][coords[0]]
             for coords in zip(range(start_x, xlen), range(0, min(xlen - start_x, ylen)))]
            for start_x in range(xlen)
            ]
maxes.append(max_of_lines(top_diags))
side_diags = [
             [rot[coords[1]][coords[0]]
              for coords in zip(range(0, min(ylen - start_y, xlen)), range(start_y, ylen))]
             for start_y in range(ylen)
             ]
maxes.append(max_of_lines(side_diags))
print(max(maxes))
