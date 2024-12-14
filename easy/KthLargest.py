from heapq import heapify, heappush, heappop

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.heap = nums
        self.k = k
        heapify(self.heap)
        for _ in range(len(nums)-k):
            heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap,val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]


