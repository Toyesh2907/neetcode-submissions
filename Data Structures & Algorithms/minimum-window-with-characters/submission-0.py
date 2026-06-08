from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        dict_t = defaultdict(int)
        dict_s = defaultdict(int)

        for character in t:
            dict_t[character] += 1
        have = 0
        need = len(dict_t)

        i = 0
        curr_min = (-1, float('inf'))

        for j in range(len(s)):
            if s[j] in dict_t:
                dict_s[s[j]] += 1
                if dict_s[s[j]] == dict_t[s[j]]:
                    have += 1
            while have == need:
                if (j - i) < (curr_min[1] - curr_min[0]):
                    curr_min = (i, j)
                if s[i] in dict_t:
                    if dict_s[s[i]] == dict_t[s[i]]:
                        have -= 1
                    dict_s[s[i]] -= 1

                i += 1

        if curr_min[0] == -1:
            return ""
        return s[curr_min[0]:curr_min[1] + 1]