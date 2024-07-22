# https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        queue = [['(', 1]]
        while queue:
            comb, left_count = queue.pop()
            if len(comb) == 2 * n:
               result.append(''.join(comb))
               continue
            if left_count < n:
                comb.append('(')
                queue.append([comb[:], left_count + 1])
                comb.pop()
            if 0 < left_count:
                comb.append(')')
                queue.append([comb, left_count - 1])
        return result

      def generateParenthesis(self, n: int) -> List[str]:
          def backtrack(comb, left_count, right_count):
              if len(comb) == 2 * n:
                  result.append(''.join(comb))
                  return
              if left_count < n:
                  comb.append('(')
                  backtrack(comb, left_count + 1, right_count)
                  comb.pop()
              if left_count < right_count
                  comb.append(')')
                  backtrack(comb, left_count, right_count + 1)
                  comb.pop()
          result = []
          backtrack([], 0, 0)
          return result

    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
           return [""]
        answer = []
        for left_count in range(n):
           for left_string in self.generateParenthesis(left_count):
               for right_string in self.generateParanthesis(n - 1 - left_count):
                   answer.append('(' + left_string + ')' + right_string)
        return answer
      
