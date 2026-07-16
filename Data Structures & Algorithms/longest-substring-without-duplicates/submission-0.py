class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Set to store characters in the current window 
        charSet = set()
        # Left pointer of the sliding window
        l = 0
        # Result: maximum length of substring without repeating characters
        res = 0

        # Right pointer expands the window to the right
        for r in range(len(s)):
            # If s[r] already exists in the window, shrink from the left
            while s[r] in charSet:
                # Remove the leftmost character from the set
                charSet.remove(s[l])
                # Move left pointer one step right
                l += 1
            # Now the window has all unique characters, add s[r]
            charSet.add(s[r])
            # Update the maximum length found
            res = max(res, r - l + 1)
        return res