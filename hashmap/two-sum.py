# https://leetcode.com/problems/two-sum/solution/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        n = len(nums)
        for i in range(n):
            amount = target - nums[i]
            if amount in visited:
                return [i, visited[amount]]
            visited[nums[i]] = i
# O(n) O(1)
