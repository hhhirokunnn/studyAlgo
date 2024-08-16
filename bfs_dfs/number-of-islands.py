# https://leetcode.com/problems/number-of-islands/solution/
class Solution:            
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = []
        # init
        i = len(grid)
        j = len(grid[0])
        for y in range(i):
            visited.append([0] * j)
        
        # bfs
        queue = []
        landNum = 0
        for y in range(i):
            for x in range(j):
                if visited[y][x] == 0 and grid[y][x] == "1":
                    landNum += 1
                    queue = [(y, x)]
                    while queue:
                        _y, _x = queue.pop()
                        visited[_y][_x] = 1
                        if 0 < _y and visited[_y - 1][_x] == 0 and grid[_y - 1][_x] == "1":
                            queue.append((_y - 1, _x))
                        if _y < i - 1 and visited[_y + 1][_x] == 0 and grid[_y + 1][_x] == "1":
                            queue.append((_y + 1, _x))
                        if 0 < _x and visited[_y][_x - 1] == 0 and grid[_y][_x - 1] == "1":
                            queue.append((_y, _x - 1))
                        if _x < j - 1 and visited[_y][_x + 1] == 0 and grid[_y][_x + 1] == "1":
                            queue.append((_y, _x + 1))
        return landNum
# O(NM), O(NM)
