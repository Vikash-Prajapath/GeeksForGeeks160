class Solution:
    def maximumProfit(self, prices):
        # code here
        buyPrice = prices[0]
        maxProfit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > buyPrice:
                maxProfit = max(maxProfit,prices[i] - buyPrice)
            else:
                buyPrice = prices[i]
                
        return maxProfit

arr = [7, 10, 1, 3, 6, 9, 2]
print(Solution.maximumProfit(arr))
