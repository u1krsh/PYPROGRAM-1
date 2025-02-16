class Solution(object):
    def twoSum(self, nums, target):
        set1 = set(nums)
        for i in range(0,len(nums)):
            if target-nums[i] in set1:
                if i != nums.index(target-nums[i]):
                    return [i,nums.index(target-nums[i])]
                
sol = Solution()
print(sol.twoSum([3,2,4],6))
        