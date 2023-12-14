with open("input.txt", "r") as f:
    lines = f.read().splitlines()


def extract_number(row, col):
    extracted = ""
    j = col
    while j < len(lines[0]) and lines[row][j] in "0123456789":
        extracted = extracted + lines[row][j]
        j += 1

    return [int(extracted), col, j - 1]


row, col = 0, 0
rows, cols = len(lines), len(lines[0])
all_nums = {}

res = 0

# extract all numbers and their positions and store them in a hashmap
while row < rows:
    col = 0
    while col < cols:
        if lines[row][col].isdigit():
            num, start, end = extract_number(row, col)
            all_nums[(row, start, end)] = num
            col = end + 1
        else:
            col += 1
    row += 1

row, col = 0, 0
builder = []

while row < rows:
    col = 0
    while col < cols:
        if lines[row][col] == "*":
            adjacent = set()
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    else:
                        new_row, new_col = row + dy, col + dx
                        for m_row, m_start, m_end in all_nums.keys():
                            if m_row == new_row and m_start <= new_col <= m_end:
                                adjacent.add(all_nums[(m_row, m_start, m_end)])
            col += 1
            builder.append(adjacent)
        else:
            col += 1
    row += 1

res = 0
for b in builder:
    if len(b) == 2:
        res += list(b)[0] * list(b)[1]
print(builder)
print(res)
