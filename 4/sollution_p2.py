with open("4/input.txt", "r") as file:
    grid = [line.strip() for line in file.readlines() if line.strip()]

rows = len(grid)
cols = len(grid[0])

count = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "A":
            for word1 in ["MAS", "SAM"]:
                for word2 in ["MAS", "SAM"]:
                    match1 = True
                    positions1 = [(-1, -1), (0, 0), (1, 1)]
                    letters1 = list(word1)
                    for pos, letter in zip(positions1, letters1):
                        nr, nc = r + pos[0], c + pos[1]
                        if not (0 <= nr < rows and 0 <= nc < cols):
                            match1 = False
                            break
                        if grid[nr][nc] != letter:
                            match1 = False
                            break
                    match2 = True
                    positions2 = [(-1, 1), (0, 0), (1, -1)]
                    letters2 = list(word2)
                    for pos, letter in zip(positions2, letters2):
                        nr, nc = r + pos[0], c + pos[1]
                        if not (0 <= nr < rows and 0 <= nc < cols):
                            match2 = False
                            break
                        if grid[nr][nc] != letter:
                            match2 = False
                            break
                    if match1 and match2:
                        count += 1

print(count)
