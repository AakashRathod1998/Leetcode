class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l=0
        r= 1
        profit = 0
        maxprofit = 0
        while r < len(prices):
            if prices[r]>prices[l]:
                print("l: ",prices[l])
                print("r: ",prices[r])
                profit = prices[r] - prices[l]
                print("curprofit: ",profit)
                maxprofit = max(profit,maxprofit)   
            else:
                l = r
            r += 1          
        return maxprofit   
