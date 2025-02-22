# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        sepArr = []  # "-2", --3, --4 etc....

        tmpCnt = 0
        i = 0
        while i < len(traversal):
            if traversal[i] == "-":
                tmpCnt += 1
                i += 1
            digStr = ""
            if traversal[i].isdigit():
                while i < len(traversal) and traversal[i].isdigit():
                    digStr += traversal[i]
                    i += 1
                sepArr.append([tmpCnt, int(digStr)])
                tmpCnt = 0
        print(sepArr)
        root = TreeNode(sepArr[0][1])
        stack = []
        stack.append((0, root))

        for pair in sepArr[1:]:
            depth, val = pair
            node = TreeNode(val)
            # Pop nodes from stack until we find the parent
            while stack and stack[-1][0] >= depth:
                stack.pop()

            # Add node as left or right child
            parent = stack[-1][1]
            if not parent.left:
                parent.left = node
            else:
                parent.right = node

            stack.append((depth, node))

        return root