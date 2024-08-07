# https://leetcode.com/problems/group-anagrams/solution/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars = {}
        for word in strs:
            sorted_word = tuple(sorted(word))
            
            if sorted_word in chars:
                chars[sorted_word].append(word)
            else:
                chars[sorted_word] = [word]
                
        result = []
        for k in chars:
            result.append(chars[k])
        return result
# O(n w log w) O(nw)
