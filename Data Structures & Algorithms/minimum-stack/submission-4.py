from collections import deque
class MinStack:

    def __init__(self):
       self.min_stack = deque() 
       self.min_list = []
       self.min_list_len = 0

    def push(self, val: int) -> None:
        self.min_stack.appendleft(val)
        if  self.min_list_len == 0:
            self.min_list.append(val)
        else:
            self.min_list.append(min(val, self.min_list[-1]))
        self.min_list_len +=1 

    def pop(self) -> None:
        self.min_stack.popleft()
        self.min_list.pop()
        self.min_list_len -= 1


    def top(self) -> int:
        print(self.min_stack)
        return self.min_stack[0]

    def getMin(self) -> int:
        return self.min_list[-1]
