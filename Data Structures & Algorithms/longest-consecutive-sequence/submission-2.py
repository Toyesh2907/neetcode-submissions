class Solution:

    def create_frequency_map(self, nums: List[int]) -> tuple(dict[int, int], int, int):
        freq_map = {}
        min_number = 1005
        max_number = 0
        for number in nums:
            min_number = min(min_number, number)
            max_number = max(max_number, number)
            try:
                freq_map[number] += 1
            except KeyError:
                freq_map[number] = 1
        return (freq_map, min_number, max_number)

    def calculate_longest_conseq_seq(
        self, 
        freq_map: dict[int, int], 
        nums: List[int],
        min_number: int,
        max_number: int
    ) -> int:
        longest_conseq_seq = 0
        current_longest_conseq_seq = 0
        for number in range(min_number, max_number + 1):
            try:
                temp = freq_map[number]
                current_longest_conseq_seq += 1
            except KeyError:
                longest_conseq_seq = max(longest_conseq_seq, current_longest_conseq_seq)
                current_longest_conseq_seq = 0
            longest_conseq_seq = max(longest_conseq_seq, current_longest_conseq_seq)
        return longest_conseq_seq
    
    def longestConsecutive(self, nums: List[int]) -> int:
        array_len = len(nums)
        if array_len == 0:
            return 0
        if array_len == 1:
            return 1

        freq_map, min_number, max_number = self.create_frequency_map(nums = nums)
        longest_conseq_seq = self.calculate_longest_conseq_seq(
            freq_map = freq_map, 
            nums = nums,
            min_number = min_number,
            max_number = max_number
        )
        return longest_conseq_seq