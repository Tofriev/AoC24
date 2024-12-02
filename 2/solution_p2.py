import pandas as pd


def is_safe(row_list):
    diffs = [row_list[i + 1] - row_list[i] for i in range(len(row_list) - 1)]
    is_increasing = all(d > 0 for d in diffs)
    is_decreasing = all(d < 0 for d in diffs)
    diffs_valid = all(1 <= abs(d) <= 3 for d in diffs)
    return (is_increasing or is_decreasing) and diffs_valid


def is_safe_with_dampener(row_list):
    if is_safe(row_list):
        return True
    for i in range(len(row_list)):
        if is_safe(row_list[:i] + row_list[i + 1 :]):
            return True
    return False


def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_safe_with_dampener(report):
            safe_count += 1
    return safe_count


with open("2/input.csv") as f:
    data = pd.read_csv(f, header=None)

reports = []
for row in data.itertuples(index=False):
    row_list = [int(x) for x in row[0].split(" ")]
    reports.append(row_list)

print(count_safe_reports(reports))
