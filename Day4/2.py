with open("input.txt", "r") as f:
    lines = f.read().splitlines()

card_freq = [0]
for i in range(1, len(lines) + 1):
    card_freq.append(1)

for line in lines:
    card, nums = line.split(":")
    card_no = int(card.split()[1])
    winning, obtained = nums.split("|")
    winning = [int(x) for x in winning.split()]
    obtained = [int(x) for x in obtained.split()]
    common = len(list(set(winning).intersection(obtained)))
    for _ in range(card_freq[card_no]):
        for i in range(1, common + 1):
            card_freq[card_no + i] += 1

print(sum(card_freq[1:]))
