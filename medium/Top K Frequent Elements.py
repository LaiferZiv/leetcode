class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        freq = [[] for _ in range(len(nums)+1)]
        for num,frq in count.items():
            freq[frq].append(num)
        res = []
        for i in range(len(freq)-1,-1,-1):
            if freq[i]:
                for num in freq[i]:
                    res.append(num)
            if len(res) == k:
                return res