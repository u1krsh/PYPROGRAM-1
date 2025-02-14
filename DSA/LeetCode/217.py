class Solution(object):
    def containsDuplicate(self, nums):
        dic = {}
        for i in nums:
            if i in dic:
                return True
            else:
                dic[i] = 1
        return False

sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))