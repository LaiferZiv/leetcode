class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapchar_s = {}
        mapchar_t = {}
        for char_s,char_t in zip(s,t):
            mapchar_s[char_s] = mapchar_s.get(char_s,0) + 1
            mapchar_t[char_t] = mapchar_t.get(char_t,0) + 1
        return mapchar_t == mapchar_s
