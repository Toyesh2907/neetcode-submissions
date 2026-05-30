from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        parenthesis_map = {
           "[": "]", 
           "{":  "}",
           "(" : ")"
        }
        stack = deque()
        for character in s:
            print(f"character before any operation{character}")
            if character in parenthesis_map:
                print("pushing")
                stack.append(character)
            else:
                if not stack:
                    return False
                if character == parenthesis_map[stack[-1]]:
                    print("popping")
                    stack.pop()
                else:
                    print(stack)
                    return False
        if stack:
            return False
        else:
            return True