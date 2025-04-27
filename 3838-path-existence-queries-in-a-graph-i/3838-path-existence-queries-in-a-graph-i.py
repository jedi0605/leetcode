class UnionFind:
    def __init__(self, n):
        """Initialize an Union-Find structure with n elements 0…n-1."""
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        """Find the root of x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union the sets containing x and y. Returns True if merged, False if already connected."""
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False

        # union by size: attach smaller tree under larger
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        return True

    def connected(self, x, y):
        """Check if x and y are in the same set."""
        return self.find(x) == self.find(y)

    def component_size(self, x):
        """Return the size of the set containing x."""
        return self.size[self.find(x)]

    def count_components(self):
        """Return the number of distinct sets."""
        # roots are those whose parent is itself
        return sum(1 for i in range(len(self.parent)) if self.find(i) == i)


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        un = UnionFind(n)

        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= maxDiff:
                un.union(i, i + 1)

        res = []
        for a, b in queries:
            if un.parent[a] == un.parent[b]:
                # if a not in pass_set and un.connected(a, b):
                res.append(True)
            else:
                # pass_set.add(a)
                res.append(False)
        return res
