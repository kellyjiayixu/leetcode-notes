<span style="font-family:Cambria;">

# Merge Sorted Array

**Jiayi Xu**

## Problem:

> You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.   
> Merge nums1 and nums2 into a single array sorted in non-decreasing order.   
> The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

```python
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
```

## Runtime Analysis

The given code snippet is designed to merge two sorted arrays, `nums1` and `nums2`, in-place. The runtime analysis for this code is as follows:

### Time Complexity
- The while loop in the code iterates until `ptr2` reaches `-1`, processing each element from `nums1` and `nums2` at most once.
- During each iteration of the loop, the code performs a constant amount of work, including a comparison, an assignment, and updating the pointers (`ptr1`, `ptr2`, and `pMerge`).
- In the worst case, the number of iterations is equivalent to the total number of elements in the two arrays, which is `m + n`. Here, `m` represents the number of valid elements in `nums1`, and `n` represents the number of elements in `nums2`.
  
Given these points, the overall time complexity of the merge function is **θ(m + n)**.

### Space Complexity
- The algorithm modifies `nums1` in-place and does not use any additional data structures or allocate additional space based on the input size.
- Thus, the space complexity is **θ(1)**, representing constant space usage irrespective of the input size.

This analysis indicates that the algorithm is efficient in both time and space for merging two sorted arrays.




</span>