class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        maps = defaultdict(list)

        for s, d, p in flights:
            maps[s].append((d, p))

        heap = []
        heappush(heap, (0, src, 0))  # cost, src, k
        res = math.inf
        dist = {}  # calculate the cheapest price

        while heap:
            cost, src_stop, times = heappop(heap)
            if src_stop == dst:
                return cost
            if times > k:
                continue
            for d, p in maps[src_stop]:  # get dst, price
                new_cost = cost + p
                if (d, times + 1) not in dist or new_cost < dist[(d, times + 1)]:
                    heappush(heap, (new_cost, d, times + 1))
                    dist[(d, times + 1)] = new_cost

        return res if res != math.inf else -1
