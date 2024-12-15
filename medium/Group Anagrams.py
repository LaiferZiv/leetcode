class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        for str in strs:
            key_arr = [0] * (ord('z') - ord('a') + 1)
            for char in str:
                key_arr[ord(char)-ord('a')] += 1
            key = tuple(key_arr)
            if key in d:
                d[key].append(str)
            else:
                d[key] = [str]
        ans = []
        for key in d:
            ans.append(d[key])
        return ans