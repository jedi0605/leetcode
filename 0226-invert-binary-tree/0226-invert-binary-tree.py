# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            tmp = root.left
            root.left = root.right
            root.right = tmp
            # if root.left == None and root.right == None:
            #     return
            # if root.left == None and root.right:
            #     root.left = root.right
            #     root.right = None
            # elif root.left and root.right == None:
            #     root.right = root.left
            #     root.left = None
            # else:
            #     root.left, root.right = root.right, root.left
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return root
