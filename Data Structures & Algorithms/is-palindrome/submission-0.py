class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1  # Initialize two pointers

        while l < r:
            # Skip non-alphanumeric characters from left
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # Skip non-alphanumeric characters from right
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            # Compare characters
            if s[l].lower() != s[r].lower():
                return False
            # Move pointers inward
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        # Check if character is alphanumeric 
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
    