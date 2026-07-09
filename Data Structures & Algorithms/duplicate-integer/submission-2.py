class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        hashset = set() #create hashset
        for n in nums: #iterate all the int in nums
            if n in hashset:
                return True
            hashset.add(n)
        return False