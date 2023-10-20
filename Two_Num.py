#Two Sum
#M-1:Brute Force

class Solution:
  def twoSum(self, nums, target):
    n=len(nums)
    for i in range(n-1):
      for j in range(i+1, n):
        if nums[i]+nums[j]==target :
          return [i,j]
nums=[2,7,11,15]
target=9
obj=Solution()
printt(obj.twoSum(nums,target))
