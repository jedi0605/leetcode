# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # using BFS and maps to memorize col
        maps = defaultdict(list)
        q = deque()
        q.append((root, 0))  # node and col
        maps[0].append(root)
        while q:
            node, col = q.popleft()
            if node.left:
                maps[col - 1].append(node.left)
                q.append((node.left, col - 1))
            if node.right:
                maps[col + 1].append(node.right)
                q.append((node.right, col + 1))
        res = []
        for k in sorted(maps):
            res.append([node.val for node in maps[k]])
        return res

