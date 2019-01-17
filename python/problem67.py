import itertools as it


def get_triangle():
    triangle = []
    with open("triangle.txt") as file:
        for line in file:
            triangle.append([int(x) for x in line.split()])
    return triangle


def optimal_sum(triangle):
    sums = triangle[-1]
    for row in it.islice(reversed(triangle), 1, None):
        temp_sums = []
        for x, y in zip(sums, sums[1:]):
            temp_sums.append(max(x, y))
        for i, x in enumerate(row):
            temp_sums[i] += x
        sums = temp_sums
    return sums[0]


triangle = get_triangle()
print(triangle)
sum = optimal_sum(triangle)
print(sum)
