# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pre_map = {}
        for idx, val in enumerate(preorder):
            pre_map[val] = idx                                          
        post_map = {}
        for idx, val in enumerate(postorder):
            post_map[val] = idx
        
        def buildTree(preorder,postorder):
            if not preorder and not postorder:
                return
            print(f"{preorder},{postorder}")
            node = TreeNode(preorder[0])
            if len(preorder) == 1:
                return node
            mid = postorder.index(preorder[1])
            pre_l = preorder[1:1+mid+1]
            post_l = postorder[:mid+1]
            
            node.left = buildTree(pre_l, post_l)

            pre_r = preorder[mid+2:]
            post_r = postorder[mid+1:-1]
            node.right = buildTree(pre_r, post_r)
            return node            

        return buildTree(preorder,postorder)