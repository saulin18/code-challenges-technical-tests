# 💣 Look for the Grinch's bombs
# The Grinch has been up to his tricks in the North Pole and has planted explosive coal bombs 💣 in the elves'
# toy factory. He wants all the toys to be rendered useless, and that's why he has left a grid where some cells
# have explosive coal (true) and others are empty (false).
#
# The elves need your help to map the dangerous areas. Each empty cell should display a number indicating how
# many explosive coal bombs there are in the adjacent positions, including diagonals.
#
# detectBombs([
#  [true, false, false],
#  [false, true, false],
#  [false, false, false],
# ]);
# // [
# //   [1, 2, 1],
# //   [2, 1, 1],
# //   [1, 1, 1]
# // ]
#
# detectBombs([
#  [true, false],
#  [false, false],
# ]);
# // [
# //   [0, 1],
# //   [1, 1]
# // ]
#
# detectBombs([
#  [true, true],
#  [false, false],
#  [true, true],
# ]);
#
# // [
# //   [1, 1],
# //   [4, 4],
# //   [1, 1]
# // ]
# Note: Want a hint? You've surely played the Minesweeper game before… 😉
def detectBombs(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]:  # If there's a bomb
                result[r][c] = 0
            else:
                count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]:
                        count += 1
                result[r][c] = count

    return result