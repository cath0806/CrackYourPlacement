class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]==nums[j]):
                    a=nums[j]
        return a
