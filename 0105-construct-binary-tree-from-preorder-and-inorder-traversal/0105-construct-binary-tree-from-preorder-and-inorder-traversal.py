# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # do some vaild check.
        if not preorder or not inorder:
            return
        rootVal = preorder[0]
        node = TreeNode(rootVal)
        idxOfInorder = inorder.index(rootVal)

        leftPreOrder = preorder[1 : idxOfInorder + 1]
        leftInOrder = inorder[:idxOfInorder]
        node.left = self.buildTree(leftPreOrder, leftInOrder)

        rightPreOrder = preorder[idxOfInorder + 1 :]
        rightInOrder = inorder[idxOfInorder + 1 :]
        node.right = self.buildTree(rightPreOrder, rightInOrder)
        return node
