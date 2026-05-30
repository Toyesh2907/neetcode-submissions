class Solution:
    # def create_freq_map(self, numbers: list[int]) -> dict[int ,int]:
    #     freq_map = {}
    #     for number in numbers:
    #         try:
    #             freq_map[number] += 1
    #         except KeyError:
    #             freq_map[number] = 1
    #     return freq_map
# 
    # def return_sum_indeces(
    #     self, 
    #     numbers: list[int], 
    #     freq_map: dict[int, int],
    #     target: int
    # ) -> list[int]:
    #     for number in numbers:
    #         try:
    #             temp =

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        number_set = set(numbers)
        for number in numbers:
            print(f"number: {number}")
            print(f"target - number: {target - number}")
            if target - number in number_set:
                return [numbers.index(number) + 1, numbers.index(target - number) + 1]
    
