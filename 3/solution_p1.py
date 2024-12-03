import re


def extract_mul_operations(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    # regex
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, content)

    return matches


file_path = "3/input.txt"
mul_operations = extract_mul_operations(file_path)

results = []
for operation in mul_operations:
    digits = re.findall(r"\d{1,3}", operation)
    result = int(digits[0]) * int(digits[1])
    results.append(result)

sum = sum(results)
print(sum)
