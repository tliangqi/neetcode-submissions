class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1  # left pointer at smallest, right at largest

        while l < r:  # stop when pointers cross
            curr_sum = numbers[l] + numbers[r]   # sum of current pair

            if curr_sum == target:     # found the target pair
                return [l + 1, r + 1]       
            elif curr_sum < target:    # sum too small，need a larger sum
                l += 1   # move left pointer right to increase sum
            else:        
                r -= 1  # sum too large，move right pointer left to decrease sum

        return [0, 0] # no pair found 