# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p,q = q,p
        print(f"{p.val}, {q.val}")
        while root:
            print(root.val)
            if root.val == p.val or root.val == q.val:
                return root
            elif root.val > p.val and root.val < q.val:
                return root
            elif root.val > q.val:
                root = root.left
            else:
                root = root.right
        return root