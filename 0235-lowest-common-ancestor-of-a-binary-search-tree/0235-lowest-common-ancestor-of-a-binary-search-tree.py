# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        tmp = root

        while tmp:
            if p.val > tmp.val and q.val > tmp.val:
                tmp = tmp.right
            elif p.val < tmp.val and q.val < tmp.val:
                tmp = tmp.left
            else:
                return tmp

        # def dfs(node : 'TreeNode'):
        #     if not node:
        #         return
        #     if node == p:
        #         return node
        #     if node == q:
        #         return node

        #     left = dfs(node.left)
        #     right = dfs(node.right)
        #     if left and right:
        #         return node
        #     if left:
        #         return left
        #     if right:
        #         return right
        # low = dfs(root)

        # return low
