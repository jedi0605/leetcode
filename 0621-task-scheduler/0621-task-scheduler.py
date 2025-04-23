class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        heap = []
        for key, val in cnt.items():
            heappush(heap, val * -1)
        print(heap)
        queue = deque()
        time = 0
        while queue or heap:
            time += 1
            if heap:
                left_task = 1 + heappop(heap)
                print(left_task)
                if left_task != 0:
                    queue.append((left_task, time + n))
            if queue:
                if queue[0][1] == time:
                    left_task, time = queue.popleft()
                    if left_task != 0:
                        heappush(heap, left_task)
        return time
