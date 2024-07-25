# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShipDays(cap):
            total, day_count = 0, 1
            for w in weights:
                if total + w > cap:
                    day_count += 1
                    total = 0
                    if day_count > days:
                        return False
                total += w
            return True
        low, high = max(weights), sum(weights)
        while low <= high:
            mid = (low + high) // 2
            if canShipDays(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
