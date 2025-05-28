# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(node, depth):
            if not node:
                return
            res[0] = max(depth, res[0])

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 1)
        return res[0]
