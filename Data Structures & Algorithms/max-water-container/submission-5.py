class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0                     # Initialize maximum area to 0
        l, r = 0, len(heights) - 1   #left start, right end

        while l < r:   # Stop when pointers meet
            # Current area = width (r-l) * height (the shorter of two walls)
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)    # Update the global maximum

            # Move the pointer pointing to the shorter wall,
            if heights[l] < heights[r]:
                l += 1    # Left wall is shorter, move left pointer rightward
            else:
                r -= 1    # Right wall is shorter or equal, move right pointer leftward

        return res   # Return the maximum area found