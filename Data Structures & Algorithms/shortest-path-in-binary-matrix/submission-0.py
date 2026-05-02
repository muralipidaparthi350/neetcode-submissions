class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        queue = [(0, 0)]
        pathLength = 0
        grid[0][0] = 1

        while queue:
            for i in range(len(queue)):
                r, c = queue.pop(0)

                if r == ROWS - 1 and c == COLS - 1:
                    return pathLength + 1

                for d in directions:
                    if r + d[0] < 0 or c + d[1] < 0 or r + d[0] >= ROWS or c + d[1] >= COLS or grid[r + d[0]][c + d[1]] == 1:
                        continue
                    queue.append((r + d[0], c + d[1]))
                    grid[r + d[0]][c + d[1]] = 1

                

            pathLength += 1

        return -1