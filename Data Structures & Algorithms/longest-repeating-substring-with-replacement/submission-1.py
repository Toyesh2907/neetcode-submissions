from collections import defaultdict
class Solution:

    def is_valid_window(self, freq_map: dict[str, int], k: int, left: int, right: int) -> bool:
        max_char_freq = max(freq_map.values())
        if right - left + 1 - max_char_freq <= k:
            print(True)
            return True
        else:
            print(False)
            return False

    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
            
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        if k == len(s) or k == len(s): return len(s)

        left, right = 0, 0
        maxi = 1
        curr_max = 1
        while(right < len(s)):
            print(left, right)
            print(freq_map)
            freq_map[s[right]] += 1
            if self.is_valid_window(freq_map = freq_map, k = k, left = left, right = right):
                maxi = right - left + 1
            else:
                freq_map[s[left]] -= 1
                left += 1
                maxi = 0
            right += 1
            curr_max = max(curr_max, maxi)
        return curr_max