# https://leetcode.com/problems/paint-fence/submissions/

class Solution:
    def numWays(self, n: int, k: int) -> int:
        def total_way(i):
            if i == 1:
                return k
            if i == 2:
                return k * k
            if i in memo:
                return memo[i]
            memo[i] = (k - 1) * (total_way(i - 1) + total_way(i - 2))
            return memo[i]
        memo = {}
        return total_way(n)

class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k
        ways = [0] * (n + 1)
        ways[1] = k
        ways[2] = k * k
        for i in range(3, n + 1):
            ways[i] = (k - 1) * (ways[i - 1] + ways[i - 2])
        return ways[n]

class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k
        two_back = k
        one_back = k * k
        for i in range(3, n + 1):
            curr = (k - 1) * (one_back + two_back)
            two_back = one_back
            one_back = curr
        return one_back
