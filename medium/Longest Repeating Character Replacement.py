class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        left = right = counter = 0
        while right < len(s):
            window[s[right]] = window.get(s[right], 0) + 1
            window_len = right - left + 1
            spaces = window_len - max(window.values(),default = 1)
            while spaces > k:
                window[s[left]] = window.get(s[left],1) - 1
                if window[s[left]] <= 0 :
                    window.pop(s[left])
                left += 1
                window_len -= 1
                spaces = window_len - max(window.values(), default=1)
            counter = max(counter, window_len)
            right += 1
        return counter