with open("input.txt", "r") as f:
    lines = f.read().splitlines()

s = 0
for line in lines:
    digits = []
    for c in line:
        if c.isdigit():
            digits.append(c)

    s += int(digits[0] + digits[-1])

print(s)
