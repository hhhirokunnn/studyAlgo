# https://leetcode.com/problems/subsets/

# bit全探索使えそう。
# bactktrackもつかえる。
# bit 全探索はbacktrackよりも計算量が多くなる。
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        for bitmask in range(1 << len(nums)):
            subset = []
            for n in range(len(nums)):
                if bitmask & (1 << n):
                    subset.append(nums[n])
            result.append(subset[:])
        return result

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(start, subset):
            if len(subset) == k:
                result.append(subset[:])
                return
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        
        for k in range(len(nums) + 1):
            backtrack(0, [])
        
        return result

# 上記はどれも O(n*2*n), O(n)
          
# 忘れちゃいけないのがcascade
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for n in nums:
            result += [r + [n] for r in result]
        
        return result
# O(n*2*n), O(n*2*n)
