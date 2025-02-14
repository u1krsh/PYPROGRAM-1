class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n*(n+1)//2
        a = sum(nums)
        return expected_sum - a 
                
sol = Solution()
print(sol.missingNumber([3,0,1]))