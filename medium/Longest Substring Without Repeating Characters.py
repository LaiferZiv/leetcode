class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        window = set()
        longest , current_len , left , right = 1,0,0,0
        while right < len(s):
            if s[right] not in window:
                window.add(s[right])
                current_len += 1
            else:
                while s[right] in window:
                    window.remove(s[left])
                    left += 1
                window.add(s[right])
                if left > right:
                    left = right
            current_len = right-left+1
            longest = max(longest,current_len)
            right += 1
        return longest
