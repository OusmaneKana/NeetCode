class Solution:
    def isValid(self, s: str) -> bool:
        char_stack = []

        open_closed = {"}":"{", "]":"[",")":"("}


        for char in s:
            if char_stack!=[] and char in open_closed.keys() and open_closed[char] == char_stack[-1]:
                char_stack.pop()
            else:
                char_stack.append(char)
        

        print(char_stack == [])



Solution().isValid("[]()[]()")