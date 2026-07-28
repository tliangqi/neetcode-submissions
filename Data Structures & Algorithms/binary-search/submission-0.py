class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1  # Initialize left and right pointers

        while l <= r:  # Continue while search space is not empty
            m = l + (r - l) // 2  # Calculate the middle index 

            if nums[m] > target: # If middle value is greater than target, search left half
                r = m - 1
            elif nums[m] < target:   # If middle value is smaller, search right half
                l = m + 1
            else:
                return m  # Found the target, return its index

        return -1 # Target not found