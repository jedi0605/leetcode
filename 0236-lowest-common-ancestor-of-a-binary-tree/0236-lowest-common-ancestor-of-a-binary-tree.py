# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def search(cur):
            if not cur:
                return
            if cur == p or cur == q:
                return cur
            l = search(cur.left)
            r = search(cur.right)
            if l and r:
                return cur
            elif l:
                return l
            else:
                return r                
        return search(root)
                        