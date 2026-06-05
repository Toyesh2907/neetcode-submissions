from abc import abstractproperty
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0

        array_len = len(s)
        if array_len == 1: return 1

        current_seen = defaultdict()
        #counter = 1
        current_max = 1
        i, j = 0, 1
        current_seen[s[i]] = 1
        while (j < array_len):
            print(i, j)
            if s[j] not in current_seen:
                current_seen[s[j]] = 1
            else:
                current_seen[s[j]] += 1
            if current_seen[s[j]] < 2:
                #counter += 1
                current_max = max(current_max, j - i + 1)
            else:
                while current_seen[s[j]] != 1:
                    current_seen[s[i]] -= 1
                    i += 1
            print(current_seen)
            j += 1
        return current_max