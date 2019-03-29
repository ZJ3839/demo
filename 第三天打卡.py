class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        if len(nums)==0:
            return -1
        l=0
        r=len(nums)-1
        while l+1<r:
            mid = l+(r-l)//2
            if nums[mid]==target:
                r=mid
            elif nums[mid]<target:
                l=mid
            else:
                r=mid
        if nums[l]==target:
            return l
        if nums[r]==target:
            return r
        return -1
