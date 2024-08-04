# https://leetcode.com/problems/split-bst/submissions/
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if not root:
            return [None, None]
        
        if root.val > target:
            result = self.splitBST(root.left, target)
            root.left = result[1]
            return [result[0], root]
        else:
            result = self.splitBST(root.right, target)
            root.right = result[0]
            return [root, result[1]]
# O(h), O(h) h: height of tree

class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        ans = [None, None]
        if not root:
            return ans
        cur = root
        stack = []
        
        while cur:
            stack.append(cur)
            if cur.val > target:
                cur = cur.left
            else:
                cur = cur.right
        while stack:
            node = stack.pop()
            if node.val > target:
                node.left = ans[1]
                ans[1] = node
            else:
                node.right = ans[0]
                ans[0] = node
        return ans

# O(h), O(h) h: height of tree
