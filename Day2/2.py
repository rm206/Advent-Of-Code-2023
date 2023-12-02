with open("input.txt", "r") as f:
    lines = f.read().splitlines()

res = 0
for i in range(len(lines)):
    game_id = i + 1
    line = lines[i]

    id_part, game = line.split(":")[0], line.split(":")[1]
    reds, greens, blues = [], [], []

    for turn in game.split(";"):
        for cube in turn.split(","):
            qt, color = int(cube.split()[0]), cube.split()[1]
            if color == "red":
                reds.append(qt)
            elif color == "green":
                greens.append(qt)
            else:
                blues.append(qt)

    res += max(reds) * max(greens) * max(blues)

print(res)
