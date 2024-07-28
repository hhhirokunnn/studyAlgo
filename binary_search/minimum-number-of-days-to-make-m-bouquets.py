# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/submissions/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        def can_make_bouquet(day):
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m
        low, high = min(bloomDay), max(bloomDay)
        while low < high:
            mid = (low + high) // 2
            if can_make_bouquet(mid):
                high = mid
            else:
                low = mid + 1
        if can_make_bouquet(low):
            return low
        return -1
  
