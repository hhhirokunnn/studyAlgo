# https://leetcode.com/problems/cutting-ribbons

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def can_cut(length):
            count = 0
            for r in ribbons:
                count += (r // length)
            return count >= k
        low, high = 1, max(ribbons)
        while low <= high:
            mid = (low + high) // 2
            if can_cut(mid):
                low = mid + 1
            else:
                high = mid - 1
        return high
            
