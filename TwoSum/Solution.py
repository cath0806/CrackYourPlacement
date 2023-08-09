class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a={}
        l=len(nums)
        for i in range(0,l):
            d=target-nums[i]
            if d in a:
                return [i,a[d]] 
            a[nums[i]]=i        
