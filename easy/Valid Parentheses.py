class Solution:
    def isValid(self, s: str) -> bool:
        d = { ')':'(' , '}':'{' , ']':'[' }
        stack = []
        for char in s:
            if char in d.values():
                stack.append(char)
            else:
                if not stack or d[char] != stack[-1]:
                    return False
                stack.pop()
        return not stack

