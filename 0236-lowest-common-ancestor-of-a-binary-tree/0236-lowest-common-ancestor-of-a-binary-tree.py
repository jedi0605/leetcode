# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return
            if node == p:
                return node
            if node == q:
                return node

            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.left and node.right:
                return node
            elif node.left:
                return node.left
            else:
                return node.right            

        return dfs(root)