class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # Initialize an empty stack 
        for c in tokens:  # Iterate through each token
            if c == "+":  #pop two numbers, push the sum
                stack.append(stack.pop() + stack.pop()) #order doesn't matter
            elif c == "-": # order matter
                a = stack.pop()  # a popped later
                b = stack.pop()  # b popped earlier
                stack.append(b - a)  
            elif c == "*":  # commutative
                stack.append(stack.pop() * stack.pop())
            elif c == "/":   # order matter
                a = stack.pop() # a is the divisor
                b = stack.pop() # b is the dividend
                # Use int(b / a) to truncate toward zero (not floor division)
                stack.append(int(b / a))
            else:      
                stack.append(int(c))   # convert to int 
        return stack[0]   