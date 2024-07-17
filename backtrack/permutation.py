# https://leetcode.com/problems/permutations/

# 順列だと、backtrackでできる
# time complexity n*2^n space n*2^n
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
      def backtrack(start):
        if start == len(nums):
          result.append(nums[:])
          return
        for i in range(start, len(nums)):
          nums[start], nums[i] = nums[i], nums[start]
          backtrack(start + 1)
          nums[start], nums[i] = nums[i], nums[start]
      result = []
      backtrack(0)
      return result
      
# numsを書き換えずにbacktrackを実装することもできる
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
      def backtrack(subset):
        if len(subset) == len(nums):
          result.append(subset[:])
          return
        for n in nums:
          subset.append(n)
          backtrack(subset)
          subset.pop()
      result = []
      backtrack([])
      return result
