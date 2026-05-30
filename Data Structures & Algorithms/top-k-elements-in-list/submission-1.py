def create_freq_map(nums: List[int]) -> Dict:
    frequency_map = {}
    for number in nums:
        try:
            frequency_map [number] += 1
        except KeyError:
            frequency_map [number] = 1
        print(frequency_map)
    return frequency_map

def calculate_k_frequent(nums: List[int], frequency_map: Dict, k: int) -> List[int]:
    sorted_freq_map = dict(
        sorted(frequency_map.items(), 
        key=lambda item: item[1],
        reverse=True
        )
    )
    top_k_set = list(sorted_freq_map)[:k]
    return top_k_set

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = create_freq_map(nums = nums)
        return calculate_k_frequent(
            nums = nums,
            frequency_map = frequency_map,
            k = k
        ) 
