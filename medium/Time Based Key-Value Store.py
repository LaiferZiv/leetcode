class TimeMap:

    def __init__(self):
        d = {}
        self.d = d

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        left = 0
        right = len(self.d[key])-1
        expected_index = -1
        while left <= right:
            mid = (left+right)//2
            values = self.d[key][mid]
            if values[0] == timestamp:
                return values[1]
            elif values[0] > timestamp:
                right = mid-1
            else:
                expected_index = mid
                left = mid+1
        return self.d[key][expected_index][1] if expected_index != -1 else ""