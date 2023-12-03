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
res = 0

while row < rows:
    col = 0
    while col < cols:
        if lines[row][col] in "123456789":
            num, start, end = extract_number(row, col)
            adjacent = False

            for i in range(start, end + 1):
                # check tops
                if row > 0 and i > 0:
                    adjacent = adjacent or (lines[row - 1][i - 1] not in "0123456789.")
                if row > 0:
                    adjacent = adjacent or (lines[row - 1][i] not in "0123456789.")
                if row > 0 and i < len(lines[0]) - 1:
                    adjacent = adjacent or (lines[row - 1][i + 1] not in "0123456789.")
                # check lefts
                if i > 0:
                    adjacent = adjacent or (lines[row][i - 1] not in "0123456789.")
                # check rights
                if i < len(lines[0]) - 1:
                    adjacent = adjacent or (lines[row][i + 1] not in "0123456789.")
                # check bottoms
                if row < len(lines) - 1 and i > 0:
                    adjacent = adjacent or (lines[row + 1][i - 1] not in "0123456789.")
                if row < len(lines) - 1:
                    adjacent = adjacent or (lines[row + 1][i] not in "0123456789.")
                if row < len(lines) - 1 and i < len(lines[0]) - 1:
                    adjacent = adjacent or (lines[row + 1][i + 1] not in "0123456789.")

            if adjacent:
                res += num
            col = end + 1
        else:
            col += 1
    row += 1

print(res)
