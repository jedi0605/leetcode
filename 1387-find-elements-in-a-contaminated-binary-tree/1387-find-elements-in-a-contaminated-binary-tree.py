# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.maps = set()
        def dfs(node):
            if not node:
                return
            if node.left:
                node.left.val = node.val *2 +1
                self.maps.add(node.left.val)
            if node.right:
                node.right.val = node.val *2 +2
                self.maps.add(node.val *2 +2)
            dfs(node.left)
            dfs(node.right)
        root.val = 0
        self.maps.add(0)
        dfs(root)

    def find(self, target: int) -> bool:
        return target in self.maps
        def find_target(node):
            if not node:
                return False
            if node.val == target:
                return True
            res_l = find_target(node.left)
            res_r = find_target(node.right)
            return res_l or res_r
        return find_target(self.root)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)