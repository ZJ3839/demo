class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        l=0
        r=len(nums)-1
        while l<r:
            mid = l + (r-l)//2
            if nums[mid]<=nums[r]:
                r=mid
            else:
                l=mid+1 
        return nums[l]
