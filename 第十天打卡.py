class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        self.quickSort(A, 0, len(A)-1)
    
    def quickSort(self, A, start, end):
        if start >= end:
            return
        left, right = start, end
        mid = start+(end-start)//2
        p = A[mid]
        while left <= right:
            while left <= right and A[left] < p:
                left += 1
            while left <= right and A[right] > p:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        self.quickSort(A, start, right)
        self.quickSort(A, left, end)
