class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        mini_stock=prices[0]
        for i in range(1,len(prices)):
            cost=prices[i]-mini_stock
            if cost>profit:
                profit=cost
            mini_stock=min(mini_stock,prices[i])
        return profit
        