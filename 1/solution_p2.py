import pandas as pd

with open("1/input.csv") as f:
    data = pd.read_csv(f, header=None)
data[["col1", "col2"]] = data[0].str.split(expand=True).astype(int)
data = data.drop(columns=[0])

dict = {}
value_counts = data["col2"].value_counts()
for value, count in value_counts.items():
    dict[value] = count

similarity = data["col1"].apply(lambda x: x * dict.get(x, 0))
print(similarity.sum())
