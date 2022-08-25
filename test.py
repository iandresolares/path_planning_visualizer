import pandas as pd
from matplotlib import pyplot


SIZE = 10

matrix = pd.DataFrame(
    [[0 for _ in range(0, SIZE)] for _ in range(0, SIZE)],
    index=[i for i in range(SIZE - 1, -1, -1)],
)

matrix[1][1] = 1
print(matrix)


pyplot.figure(figsize=(10, 10))
pyplot.imshow(matrix, origin="lower")
x = [0, 1, 2, 3, 4]
y = [0, 1, 2, 3, 4]
y = [SIZE - 1 - i for i in y]
c = [i for i in range(len(x))]
pyplot.scatter(x, y, s=len(x), c=c)
ay = pyplot.gca()
ay.set_ylim(ay.get_ylim()[::-1])

pyplot.show()
