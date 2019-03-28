class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        l=1 
        r = len(A) - 2
        while l + 1 <  r:
            mid = l+( r -l) // 2
            if A[mid] < A[mid - 1]:
                r = mid
            elif A[mid] < A[mid + 1]:
                l = mid
            else:
                r = mid

        if A[l] < A[r]:
            return r
        else:
            return l
            
