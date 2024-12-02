import pandas as pd

with open("1/input.csv") as f:
    data = pd.read_csv(f, header=None)
data[["col1", "col2"]] = data[0].str.split(expand=True).astype(int)
data = data.drop(columns=[0])

for column in data.columns:
    print(data[column].dtype)
    data[column] = data[column].sort_values().reset_index(drop=True)

for idx, row in enumerate(data.itertuples(index=False)):
    distances = [abs(row[i] - row[i + 1]) for i in range(len(row) - 1)]
    data.loc[idx, "Distances"] = distances[0]

sum = data["Distances"].sum()
print(sum)
