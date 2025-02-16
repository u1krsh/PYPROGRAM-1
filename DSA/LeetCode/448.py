class Solution(object):
    def findDisappearedNumbers(self, nums):
        set1 = set(nums)
        res = []
        for i in range(1, len(nums)+1):
            if i not in set1:
                res.append(i)
        return res
sol = Solution()
print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))