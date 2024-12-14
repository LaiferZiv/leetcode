from heapq import heapify, heappop, heappush

class Solution:

    def lastStoneWeight(self, stones: list[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapify(max_heap)
        while len(max_heap) > 1:
            diff = heappop(max_heap)-heappop(max_heap)
            if diff != 0:
                heappush(max_heap,diff)
        return -max_heap[0] if max_heap else 0
