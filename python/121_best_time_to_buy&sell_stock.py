class Solution:
    def maxProfit(self, prices) -> int:
        #brute force
        #O(N^2)
        # Time Limit Exceeded
        # minPriceindex= 0
        # maxVale=0
        # #print(len(price))
        # for i in range(len(price)-1,0, -1):
        #     for j in range(i-1,-1,-1):
        #         temp = price[i]-price[j]
        #         if temp > maxVale :
        #             maxVale = temp
        # print(maxVale)
        # return maxVale

        maxValue= 0
        if len(prices) ==0: return maxValue
        minPrice= prices[0]
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            maxValue = max(maxValue, prices[i]-minPrice)
        return maxValue
            
s = Solution()
m = s.maxProfit([0])
print(m)