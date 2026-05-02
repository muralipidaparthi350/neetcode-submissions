class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c, currArea):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            area = currArea
            for d in directions:
                area += dfs(r + d[0], c + d[1], currArea)

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    islandArea = dfs(r, c, 1)
                    maxArea = max(maxArea, islandArea)

        return maxArea