import pandas as pd

with open("2/input.csv") as f:
    data = pd.read_csv(f, header=None)

report = []
for row in data.itertuples(index=False):
    row_list = [int(x) for x in row[0].split(" ")]
    is_increasing = all(
        row_list[i] < row_list[i + 1] and 1 <= row_list[i + 1] - row_list[i] <= 3
        for i in range(len(row_list) - 1)
    )
    is_decreasing = all(
        row_list[i] > row_list[i + 1] and 1 <= row_list[i] - row_list[i + 1] <= 3
        for i in range(len(row_list) - 1)
    )
    if is_increasing or is_decreasing:
        report.append(True)
    else:
        report.append(False)
print(sum(report))
