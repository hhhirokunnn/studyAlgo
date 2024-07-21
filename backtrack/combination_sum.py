# https://leetcode.com/problems/combination-sum
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(start, comb):
            if sum(comb) == target:
                result.append(comp[:])
                return
            if sum(comb) > target:
                return
            
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(i, comb)
                comb.pop()
        backtrack(0, [])
        
        return result

  # TODO: 
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]

        for candidate in candidates:
            for current_target in range(candidate, target + 1):
                for combination in dp[current_target - candidate]:
                    dp[current_target].append(combination + [candidate])

        return dp[target]
