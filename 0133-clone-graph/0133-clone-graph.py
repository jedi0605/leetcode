"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        clone = {}
        clone[node] = Node(node.val, [])
        queue = deque()
        queue.append(node)

        while queue:
            cur = queue.popleft()
            for i in cur.neighbors:
                if i not in clone:
                    clone[i] = Node(i.val)
                    queue.append(i)
                clone[cur].neighbors.append(clone[i])
        return clone[node]
