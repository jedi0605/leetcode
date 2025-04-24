class DoubleLink:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None


class LRUCache:

    def __init__(self, capacity: int):
        self.Least = DoubleLink(-1, -1)
        self.Most = DoubleLink(-1, -1)
        self.Most.pre = self.Least
        self.Least.next = self.Most
        self.maps = {}  # key->int, node->DoubleLink
        self.capacity = capacity
    def remove(self,node): # remove 
        pre_node = node.pre
        next_node = node.next
        pre_node.next = next_node
        next_node.pre = pre_node
        return
    def insert(self,node): # insert at right
        pre_node = self.Most.pre
        pre_node.next = node
        node.next = self.Most
        node.pre = pre_node
        self.Most.pre = node

        return
    
    def get(self, key: int) -> int:
        if key in self.maps:
            # when get val, update most resent
            self.remove(self.maps[key])
            self.insert(self.maps[key])
            return self.maps[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.maps: # update val
            self.remove(self.maps[key])
        self.maps[key] = DoubleLink(key,value)
        # insert
        self.insert(self.maps[key])
        # check cap
        if len(self.maps)>self.capacity: # remove least node
            remove_target = self.Least.next
            self.remove(remove_target)
            del self.maps[remove_target.key]
            
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
