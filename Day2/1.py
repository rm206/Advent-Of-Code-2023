with open("input.txt", "r") as f:
    lines = f.read().splitlines()

res = 0
for i in range(len(lines)):
    game_id = i + 1
    line = lines[i]

    id_part, game = line.split(":")[0], line.split(":")[1]
    game_possible = True

    for turn in game.split(";"):
        for cube in turn.split(","):
            qt, color = int(cube.split()[0]), cube.split()[1]
            if (
                (color == "red" and qt > 12)
                or (color == "green" and qt > 13)
                or (color == "blue" and qt > 14)
            ):
                game_possible = False

    if game_possible:
        res += game_id

print(res)
