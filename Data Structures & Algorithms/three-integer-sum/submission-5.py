from collections import defaultdict
from typing import DefaultDict
class Solution:
    def create_freq_map(self, nums: list[int]) -> DefaultDict[int, int]:
        freq_map = defaultdict(int) 
        for number in nums:
            freq_map[number] += 1
        return freq_map

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        freq_map = self.create_freq_map(nums = nums)
        array_len = len(nums)
        answers:list[list[int]] = []
        for i in range(array_len):
            for j in range(i+1, array_len):
                temp_sum = nums[i] + nums[j]
                temp_diff = target - temp_sum
                if temp_diff in freq_map:
                    temp_diff_index = nums.index(temp_diff)
                    if temp_diff_index != i and temp_diff_index != j:
                        answer = [nums[i], nums[j], target - temp_sum]
                        #print(f"answer prior sorting : {answer}")
                        answer.sort()
                        #print(f"answer after sorting : {answer}")
                        if answer not in answers:
                            answers.append(answer)
        return answers