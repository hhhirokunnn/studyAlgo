# koko-eating-bananas

import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_banana(k):
            count = 0
            for p in piles:
                count += math.ceil(p / k)
            return count <= h
        
        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            if can_eat_banana(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
