# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(maxVal, node):
            if not node:
                return 0
            if node.val < maxVal:
                return dfs(maxVal, node.left) + dfs(maxVal, node.right)
            maxVal = max(maxVal, node.val)
            return dfs(maxVal, node.left) + dfs(maxVal, node.right) + 1
        return dfs(root.val, root)
