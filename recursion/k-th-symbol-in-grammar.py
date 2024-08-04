# https://leetcode.com/problems/k-th-symbol-in-grammar/submissions/
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def depthSearch(n, k, root):
            if n == 1:
                return root
            nextRoot = 0
            digitCount = 2 ** (n - 1)
            
            if k > digitCount / 2:
                if root == 0:
                    nextRoot = 1
                return depthSearch(n - 1, k - (digitCount / 2), nextRoot)
            else:
                if root == 1:
                    nextRoot = 1
                return depthSearch(n - 1, k, nextRoot)
        return depthSearch(n, k, 0)

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        symbol = 0
        
        while n > 1:
            length = 2 ** (n - 1)
            mid = length // 2
            
            if k > mid:
                symbol = 1 - symbol
                k -= mid
            
            n -= 1
        
        return symbol
