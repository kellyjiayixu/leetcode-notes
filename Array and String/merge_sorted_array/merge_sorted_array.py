# This python file intends to solve the merge sorted array problem.

# 2 Pointers
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
                
        # Initialize pointers for nums1 and nums2 arrays
        ptr1 = m - 1       # pointing to the end of valid elements in nums1
        ptr2 = n - 1       # pointing to the end of nums2
        pMerge = m + n - 1  # pointing to the end of nums1 where merged elements will be placed
        
        # While there are still elements to process in nums2
        while (ptr2 >= 0):
            # Compare elements of nums1 and nums2
            if ptr1 >= 0 and nums1[ptr1] > nums2[ptr2]:
                # If current element in nums1 is greater, place it in the correct position in nums1
                nums1[pMerge] = nums1[ptr1]
                ptr1 -= 1  # move the pointer in nums1
            else:
                # Else, place the element from nums2 in the correct position in nums1
                nums1[pMerge] = nums2[ptr2]
                ptr2 -= 1  # move the pointer in nums2
            pMerge -= 1  # move the merge pointer
