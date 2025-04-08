# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node, leaf_arr):
            if not node:
                return
            if not node.left and not node.right:
                leaf_arr.append(node.val)
            dfs(node.left,leaf_arr)
            dfs(node.right,leaf_arr)
            return
        leaf_arr1 = []
        dfs(root1,leaf_arr1)
        leaf_arr2 = []
        dfs(root2,leaf_arr2)
        return leaf_arr1 == leaf_arr2
        
        