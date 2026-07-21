class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0   # Maximum valid window length
        l = 0   # Left pointer of the sliding window
        maxf = 0
        
        for r in range(len(s)):  # Right pointer expands the window
            # Add the new character to the window
            count[s[r]] = 1 + count.get(s[r], 0)
            # Update the maximum frequency
            maxf = max(maxf, count[s[r]])
            
            # If the number of characters to replace exceeds k, shrink the window from the left
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1 # Remove the leftmost character from the window
                l += 1  # Move left pointer forward
            
            # Update the answer with the current valid window size
            res = max(res, r - l + 1)
        
        return res