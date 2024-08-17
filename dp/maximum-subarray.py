# https://leetcode.com/problems/maximum-subarray/solution/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        amount = curr = nums[0]
        for i in range(1, len(nums)):
            curr = max(curr + nums[i], nums[i])
            amount = max(amount , curr)
        return amount

