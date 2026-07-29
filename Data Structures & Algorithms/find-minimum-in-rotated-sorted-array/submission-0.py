class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]    # Initialize result with the first element 
        l, r = 0, len(nums) - 1 #left boundary l, right boundary r

        # Binary search loop
        while l <= r:
            if nums[l] < nums[r]:     # subarray already sorted
                res = min(res, nums[l])  # the minimum is nums[l], update res and break
                break

            m = (l + r) // 2  # Check the middle element.
            res = min(res, nums[m])   # update the min

            if nums[m] >= nums[l]:  # The left side is sorted.
                l = m + 1  # Move to the right half.
            else: 
                r = m - 1 # Move to the left half.

        return res