class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimum:
            self.minimum.append(val)
            return
        if val <= self.minimum[-1]:
            self.minimum.append(val)

    def pop(self) -> None:
        if self.minimum[-1] == self.stack[-1]:
            self.minimum.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]