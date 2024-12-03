import re


def extract_mul_operations_and_instructions(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    # regex
    extracted = re.findall(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", content)

    return extracted


file_path = "3/input.txt"
output = extract_mul_operations_and_instructions(file_path)

enabled = True
results = []
for item in output:
    if item == "do()":
        enabled = True
    elif item == "don't()":
        enabled = False
    elif enabled and "mul" in item:
        digits = re.findall(r"\d{1,3}", item)
        result = int(digits[0]) * int(digits[1])
        results.append(result)

print(sum(results))
