# https://leetcode.com/problems/minimum-size-subarray-sum/submissions/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        amount = 0
        count = len(nums) + 1
        while right < len(nums):
            amount += nums[right]
            while amount >= target:
                count = min(count, right - left + 1)
                amount -= nums[left]
                left += 1
            right += 1
        if count > len(nums):
            return 0
        return count
# O(n) O(1)
