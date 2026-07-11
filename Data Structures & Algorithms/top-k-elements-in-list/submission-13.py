class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 

        # Count frequency of each number
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        freq = [[] for i in range(len(nums) + 1)] # Create buckets, each bucket stores numbers with frequency

        # Place each number into its frequency bucket
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1): # skip index 0
            for n in freq[i]:
                res.append(n)
                if len(res) == k: # stop once have k elements
                    return res
        return res  
