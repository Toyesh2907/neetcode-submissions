class Solution:

    def calculate_eating_hours(self, piles: list[int], rate: int) -> int:
        hours = 0
        for bananas in piles:
            hours += math.ceil(bananas / rate)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        array_len = len(piles)
        if array_len > h:
            return -1 #min k not possible
        
        min_rate = 1
        max_rate = max(piles)
        while(min_rate <= max_rate):
            mid_rate = (max_rate + min_rate) // 2
            current_hours = self.calculate_eating_hours(piles = piles, rate = mid_rate)
            if current_hours > h:
                min_rate = mid_rate + 1
            else:
                max_rate = mid_rate - 1
        return min_rate