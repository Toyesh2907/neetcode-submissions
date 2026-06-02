class Solution:
        
    def create_turns_array(self, target: int, position: list[int], speed: list[int]) -> list[int]:
        turns_array = []
        for i in range(len(position)):
            turns_array.append((target - position[i]) / speed[i])
        return turns_array
        
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        array_len = len(position)
        if array_len == 1:
            return 1
        turns_array = self.create_turns_array(target=target, position = position, speed = speed)
        turns_reverse_sorted = [x for _, x in sorted(zip(position, turns_array), reverse=True)]
        print(turns_reverse_sorted)
        fleet = 1
        max_time = -1
        for i in range(array_len - 1):
            current_element = turns_reverse_sorted[i]
            next_element = turns_reverse_sorted[i + 1]
            max_time = max(current_element, max_time)

            if max_time >= next_element:
                continue
            else:
                fleet += 1
            max_time = max(max_time, next_element)
        return fleet