# https://leetcode.com/problems/unique-paths/submissions/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = []
        for _ in range(m):
            d.append([1] * n)
        for col in range(1, m):
            for row in range(1, n):
                d[col][row] = d[col - 1][row] + d[col][row - 1]
        return d[m - 1][n - 1]
# O(col x row) O(col x row)
