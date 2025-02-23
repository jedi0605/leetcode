# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder and not inorder:
            return 
        node = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        left_pre = preorder[1:mid+1]
        left_inorder = inorder[:mid]
        node.left = self.buildTree(left_pre,left_inorder)
        
        r_pre = preorder[mid+1:]
        r_inorder = inorder [mid+1:]
        node.right = self.buildTree(r_pre,r_inorder)
        return node