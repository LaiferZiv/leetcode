class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        num = 0
        while num < len(s):
            sign = s.index('#', num)
            start = sign + 1
            word_len = int(s[num:sign])
            word = s[start:start+word_len]
            res.append(word)
            num = start + word_len
        return res