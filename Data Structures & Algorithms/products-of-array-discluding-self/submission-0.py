class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) # Initialize result array with 1s, same length as nums

        # First pass: left to right, store prefix product in res[i]
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix          # res[i] now holds product of all elements to the left
            prefix *= nums[i]        # update prefix for next position

        # Second pass: right to left, multiply by postfix product
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix        # multiply res[i] by product of all elements to the right
            postfix *= nums[i]       # update postfix for the next element on the left

        return res