class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        dic = {}
        for i in sorted(nums):
            if i not in dic:
                dic[i] = len(dic)
        return [dic[i] for i in nums]
    
sol = Solution()
print(sol.smallerNumbersThanCurrent([8,1,2,2,3]))

        