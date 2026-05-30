class Solution:

    def create_index_map(self, temperatures: list[int]) -> dict[int, int]:
        temp_index_map = defaultdict()
        for index, temperature in enumerate(temperatures):
            temp_index_map[temperature] = index
        return temp_index_map

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        array_len = len(temperatures)
        if array_len < 2:
            return [0]
        temp_index_map = self.create_index_map(temperatures = temperatures)
        next_highest_temp = array_len * [0]
        temp_stack = deque()
        for ri in range(array_len - 1, -1 , -1):
            current_temp = temperatures[ri]
            while temp_stack:
                stack_top = temperatures[temp_stack[-1]]
                if current_temp < stack_top:
                    next_highest_temp[ri] = temp_stack[-1] - ri
                    #next_highest_temp[temp_index_map[current_temp]] = temp_index_map[temp_stack[-1]] - temp_index_map[current_temp]
                    break
                else:
                    temp_stack.pop()
            temp_stack.append(ri)
        return next_highest_temp
        