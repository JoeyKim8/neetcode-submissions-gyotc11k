class Solution:
    def isValid(self, s: str) -> bool:
        # "Most recent first" is LIFO and thats a stack
        stack = []

        # initiates the brackets, mapping the closer as the key and the opener as the value
        pairs = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in pairs: # if char is a closing bracket
                # "if stack" = if stack isnt empty and top of the stack matches the closer
                if stack and stack[-1] == pairs[char]: 
                    stack.pop()
                else: # if it doesnt match either case then the stack returns False
                    return False
            else: # if char is an opening bracket, push it onto the stack
                stack.append(char)

        # at the end, the program is only true if stack is fully empty
        return len(stack) == 0