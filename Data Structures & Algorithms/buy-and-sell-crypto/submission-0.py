class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left pointer: potential buying day, right pointer: selling day
        l, r = 0, 1
        maxP = 0  # track the maximum profit

        # iterate until the selling pointer reaches the end
        while r < len(prices):
            # if buying price is lower than selling price, we have a profit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # if buying price >= selling price, move the buying pointer to the current day
                # because a lower or equal price at 'r' is a better candidate for future profits
                l = r
            # always move the selling pointer forward
            r += 1

        return maxP