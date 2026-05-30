from collections import deque
class Solution:

    def evaluate_expression(self, n1: int, n2: int, expression):
        if expression == '+':
            return n2 + n1
        if expression == '-':
            return n2 - n1
        if expression == '*':
            return n2 * n1
        if expression == '/':
            return int(n2 / n1)

    def evalRPN(self, tokens: List[str]) -> int:
        number_stack = deque()
        for token in tokens:
            # 48 <= ord(char) <= 57
            if token not in "+/*-":
                number_stack.append(int(token))
            else:
                n1 = number_stack.pop()
                n2 = number_stack.pop()
                answer = self.evaluate_expression(n1 = n1 , n2 = n2, expression = token)
                number_stack.append(answer)
        return number_stack[0]