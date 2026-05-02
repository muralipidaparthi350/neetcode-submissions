class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        emptyCount = 0
        freshCount = 0
        rottenCount = 0
        queue = []
        minutes = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    emptyCount += 1
                elif grid[i][j] == 1:
                    freshCount += 1
                else:
                    rottenCount += 1
                    queue.append((i, j))

        if freshCount == 0:
            return 0
        if rottenCount == 0:
            return -1

        while queue:
            for i in range(len(queue)):
                r, c = queue.pop(0)

                for dr, dc in directions:
                    if r + dr < 0 or c + dc < 0 or r + dr >= ROWS or c + dc >= COLS or grid[r + dr][c + dc] == 2 or grid[r + dr][c + dc] == 0:
                        continue
                    queue.append((r + dr, c + dc))
                    freshCount -= 1
                    grid[r + dr][c + dc] = 2


            minutes += 1

        if freshCount == 0:
            return minutes - 1
        return -1