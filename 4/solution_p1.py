with open("4/input.txt", "r") as file:
    grid = [line.strip() for line in file.readlines() if line.strip()]

rows = len(grid)
cols = len(grid[0])

# define vectors for every direction
directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

# first, search for start point candidate then go from there

search_word = "XMAS"


def search_candidate(r, c, direction):
    for i in range(len("XMAS")):
        nr, nc = r + i * direction[0], c + i * direction[1]
        if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != search_word[i]:
            return False
    return True


count = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "X":
            for direction in directions:
                if search_candidate(r, c, direction):
                    count += 1
print(count)
