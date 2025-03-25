class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        max = 0
        min = prices[0]
        for i in prices:
            if i <= min:
                min = i
            elif i - min > max:
                max = i - min
        return max
    
x = Solution()
print(x.maxProfit([7,1,5,3,6,4]))
        