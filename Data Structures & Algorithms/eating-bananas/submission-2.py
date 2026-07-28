class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) #minimum speed is 1, maximum is the largest pile
        res = r  # best valid speed found so far, initially set to the maximum

        while l <= r:
            k = (l + r) // 2  # test speed k

            # Calculate total hours needed to eat all piles at speed k
            hours = 0 
            for p in piles:
                hours += math.ceil(p / k) # hours needed for this pile

            # If total hours <= h, speed k is feasible
            if hours <= h: 
                res = min(res, k)   # update the minimum feasible speed
                r = k - 1  # try a slower speed
            else:
                l = k + 1   # increase speed

        return res