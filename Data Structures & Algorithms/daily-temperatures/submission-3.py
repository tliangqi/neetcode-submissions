class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) # Result array initialized with 0, same length as input
        stack = []  
            
        for i, t in enumerate(temperatures):  # Iterate over each day with its temperature
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()  # pop the colder day
                res[stackInd] = i - stackInd   # waiting days = index difference
            # Push current day into stack
            stack.append([t, i])

        return res