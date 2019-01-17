def get_pyramid():
    pyramid = []
    with open("triangle_small.txt") as file:
        for line in file:
            pyramid.append([int(x) for x in line.split()])
    return pyramid


pyramid = get_pyramid()
height = len(pyramid)
sums = {}
for path in (f"0{num:0{height - 1}b}" for num in range(2 ** (height - 1))):
    sum = 0
    index = 0
    for row, values in enumerate(pyramid):
        index += int(path[row])
        sum += values[index]
    sums[path] = sum
max_key = max(sums.keys(), key=(lambda key: sums[key]))
print(max_key, sums[max_key], sep=" : ")
