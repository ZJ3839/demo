#lintcode457
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        #数组为空，直接返回-1
        if len(nums)==0:
            return -1
        #两个指针
        start = 0 
        end = len(nums)-1
        while start + 1 < end :
            mid = start + (end-start)//2
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
                
                
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

      
            
                
