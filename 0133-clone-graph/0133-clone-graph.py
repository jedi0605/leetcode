"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone_map = {}
        clone_map[node] = Node(node.val,[])
        queue = deque()
        queue.append(node)        

        while queue:
            cur_node = queue.popleft()
            for nei in cur_node.neighbors:
                if nei not in clone_map:
                    clone_map[nei] = Node(nei.val,[])
                    queue.append(nei)
                clone_map[cur_node].neighbors.append(clone_map[nei])
                
        return clone_map[node]