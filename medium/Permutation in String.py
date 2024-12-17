class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1:
            return True
        if len(s1) > len(s2):
            return False
        s1_letters = {}
        s2_window = {}
        for i in range(len(s1)):
            s1_letters[s1[i]] = s1_letters.get(s1[i],0) + 1
            s2_window[s2[i]] = s2_window.get(s2[i],0) + 1
        if s1_letters == s2_window:
            return True
        left,right = 0,len(s1)
        while right < len(s2):
            s2_window[s2[right]] = s2_window.get(s2[right], 0) + 1
            s2_window[s2[left]] -= 1
            if s2_window[s2[left]] == 0:
                del s2_window[s2[left]]
            if s1_letters == s2_window:
                return True
            left += 1
            right += 1
        return s1_letters == s2_window

if __name__ == "__main__":
    s = Solution()
    s1 = "a"
    s2 = "ab"
    print(s.checkInclusion(s1,s2))