class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to store opening brackets
        stack = []
        # Mapping of closing brackets to their corresponding opening brackets
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        # Iterate through each character in the string
        for c in s:
            if c in closeToOpen:
                # Check if stack is non-empty and the top matches the expected opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()    # Match found, pop the top element
                else:
                    return False   # Mismatch or empty stack which is invalid
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(c)

        # valid if stack is empty
        return True if not stack else False