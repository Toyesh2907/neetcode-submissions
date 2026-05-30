class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_map_s = {}
        char_map_t = {}
        print(s[0])
        for index in range(len(s)):
            try:
                char_map_s[s[index]] += 1
            except KeyError:
                char_map_s[s[index]] = 1

            try:
                char_map_t[t[index]] += 1
            except KeyError:
                char_map_t[t[index]] = 1

        return char_map_t == char_map_s