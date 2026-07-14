class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert list to a set 
        numSet = set(nums)
        longest = 0

        # Iterate through each number
        for n in nums:
            # If n-1 is not in the set, n has no left neighbour → it's a start
            if (n - 1) not in numSet:
                length = 0
                # Count how many consecutive numbers exist from n onward
                while (n + length) in numSet:
                    length += 1
                # Update the global maximum
                longest = max(length, longest)
        
        return longest