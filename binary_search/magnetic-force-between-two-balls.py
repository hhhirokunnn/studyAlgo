# https://leetcode.com/problems/magnetic-force-between-two-balls/submissions/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def can_put_ball(distance):
            count = 1
            base = position[0]
            for i in range(1, len(position)):
                if position[i] - base >= distance:
                    count += 1
                    base = position[i]
                    if count == m:
                        return True
            return False
        
        low, high = 1, position[-1] - position[0]
        while low <= high:
            mid = (low + high) // 2
            if can_put_ball(mid):
                low = mid + 1
            else:
                high = mid - 1
                
        return high
