# https://leetcode.com/problems/max-area-of-island/solution/
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        i = len(grid)
        j = len(grid[0])
        maxLand = 0
        for y in range(i):
            for x in range(j):
                if grid[y][x] == 1:
                    landNum = 1
                    queue = [(y, x)]
                    grid[y][x] = 2
                    while queue:
                        row, col = queue.pop()
                        if 0 < row and grid[row - 1][col] == 1:
                            landNum += 1
                            queue.append((row - 1, col))
                            grid[row - 1][col] = 2
                        if row < i - 1 and grid[row + 1][col] == 1:
                            landNum += 1
                            queue.append((row + 1, col))
                            grid[row + 1][col] = 2
                        if 0 < col and grid[row][col - 1] == 1:
                            landNum += 1
                            queue.append((row, col - 1))
                            grid[row][col - 1] = 2
                        if col < j - 1 and grid[row][col + 1] == 1:
                            landNum += 1
                            queue.append((row, col + 1))
                            grid[row][col + 1] = 2
                    maxLand = max(maxLand, landNum)
        return maxLand
      
