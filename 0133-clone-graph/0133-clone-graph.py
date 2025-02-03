"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        clone = {}
        clone[node] = Node(node.val,[])
        queue = deque()
        queue.append(node)
        
        while queue:
            cur = queue.popleft()
            for n in cur.neighbors:
                if n not in clone:
                    clone[n] = Node(n.val)
                    queue.append(n)
                clone[cur].neighbors.append(clone[n])
        return clone[node]