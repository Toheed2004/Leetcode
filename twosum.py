class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range (len(nums)):
         j=i
         temp=j+1
         while(temp<=len(nums)-1):
            if(nums[j]+nums[temp]==target):
                return (j,temp)
            temp=temp+1
            
        