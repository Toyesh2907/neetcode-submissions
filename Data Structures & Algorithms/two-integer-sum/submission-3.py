class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq_map = {}
        for index, number in enumerate(nums):
            freq_map[number] = index

        for index, number in enumerate(nums):
            difference = target - number
            if (difference) in freq_map and index != freq_map[difference]:
                return [index, freq_map[difference]]  