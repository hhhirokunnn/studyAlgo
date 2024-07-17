# https://leetcode.com/problems/subsets-ii/

# backtrackがつかえる。
# bit 全探索も行ける
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(start, subset):
            if k == len(subset):
                result.append(subset[:])
                return
            for i in range(start, len(nums)):
                if start < i and nums[i - 1] == nums[i]:
                    continue
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
            
        result = []
        for k in range(len(nums) + 1):
            backtrack(0, [])
            
        return result

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for bitmask in range(1 << len(nums)):
            subset = []
            for i in range(len(nums)):
                if bitmask & (1 << i):
                    subset.append(nums[i])
            result.add(tuple(subset))
        
        return [list(r) for r in result]

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, subset):
            result.add(tuple(subset))
            for i in range(start, len(nums)):
                backtrack(i + 1, subset + [nums[i]])
            
        nums.sort()
        result = set()
        backtrack(0, [])

        return [list(r) for r in result]


# 以下要理解

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        last_size = 0 
        for i, num in enumerate(nums):
            size = len(result)
            if i > 0 and nums[i] == nums[i - 1]:
                start = last_size
            else:
                start = 0
            last_size = size

            for j in range(start, size):
                result.append(result[j] + [num])

        return result
      
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = [[]]
        start_index = 0
        
        for i in range(len(nums)):
            size = len(subsets)
            for j in range(start_index, size):
                subset = subsets[j] + [nums[i]]
                if subset not in subsets:
                    subsets.append(subset)
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                start_index = size
            else:
                start_index = 0
        
        return subsets
