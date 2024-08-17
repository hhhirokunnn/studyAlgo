# https://leetcode.com/problems/longest-increasing-subsequence/solution/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums))
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        for num in nums:
            if sub[-1] < num:
                sub.append(num)
            else:
                i = 0
                while sub[i] < num:
                    i += 1
                sub[i] = num
        return len(sub)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        for num in nums:
            if sub[-1] < num:
                sub.append(num)
            else:
                i = self.binary_search(num, sub)
                sub[i] = num
        return len(sub)
    
    def binary_search(self, target, nums):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l
