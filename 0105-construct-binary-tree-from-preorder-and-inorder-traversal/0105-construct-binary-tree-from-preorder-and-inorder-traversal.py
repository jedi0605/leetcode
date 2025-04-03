# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        def build_tree(pre_o, in_o):
            if not pre_o or not in_o:
                return
            rootVal = pre_o[0]
            node = TreeNode(rootVal)
            inoder_idx = in_o.index(rootVal)

            inoder_left = in_o[:inoder_idx]
            preoder_left = pre_o[1 : len(inoder_left) + 1]
            inoder_right = in_o[inoder_idx + 1 :]
            preorder_right = pre_o[1 + len(inoder_left) :]
            node.left = build_tree(preoder_left, inoder_left)

            node.right = build_tree(preorder_right, inoder_right)
            return node

        return build_tree(preorder, inorder)
