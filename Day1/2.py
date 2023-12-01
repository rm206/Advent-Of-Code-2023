import re

with open("input.txt", "r") as f:
    lines = f.read().splitlines()


mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
for n in range(1, 10):
    mapping[str(n)] = n

s = 0

for line in lines:
    extracted_digits = []
    for i in range(len(line)):
        for string, digit in mapping.items():
            if line[i:].startswith(string):
                extracted_digits.append(digit)

    s += (extracted_digits[0] * 10) + extracted_digits[-1]

print(s)
