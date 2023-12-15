with open("input.txt", "r") as f:
    lines = f.read().splitlines()

res = 0

for line in lines:
    card, nums = line.split(":")
    winning, obtained = nums.split("|")
    winning = [int(x) for x in winning.split()]
    obtained = [int(x) for x in obtained.split()]

    common = list(set(winning).intersection(obtained))
    if pow(2, len(common) - 1) >= 1:
        res += pow(2, len(common) - 1)


print(res)
