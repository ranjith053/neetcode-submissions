class Solution:
    def maxProfit(self,prices:List[int])->int:
        left = 0
        right = 1
        mp = 0
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                mp = max(profit,mp)
            right += 1
        return mp