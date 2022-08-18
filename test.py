import pandas as pd

SIZE = 10


matrix = pd.DataFrame(
    [[0 for _ in range(0, SIZE)] for _ in range(0, SIZE)],
    index=[i for i in range(SIZE - 1, -1, -1)],
)

for i in range(SIZE):
    for j in range(SIZE):
        pass
