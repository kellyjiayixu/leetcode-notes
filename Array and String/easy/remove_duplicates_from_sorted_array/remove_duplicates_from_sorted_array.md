<span style="font-family:Cambria;">

# Remove Duplicates From Sorted Array

**Jiayi Xu**

## Problem

> Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
> 
> Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
> 
> - Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums
> 
> - Return k.

## Solution

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Initialize 'replace' pointer to 1. This pointer will indicate the position to place the next non-duplicate value.
        replace = 1
        
        # Start iterating from the second element of the list
        for i in range(1, len(nums)):
            # If the current element is not the same as the previous one, it's not a duplicate
            if nums[i - 1] != nums[i]:
                # Place the non-duplicate value in the position indicated by 'replace'
                nums[replace] = nums[i]
                
                # Increment the 'replace' pointer for the next non-duplicate value
                replace += 1
            
        # At the end of the loop, 'replace' will indicate the position just after the last non-duplicate element.
        # Thus, 'replace' also represents the new length of the list without duplicates.
        return replace
```

## Runtime Analysis

The provided `removeDuplicates` method is designed to remove duplicates from a sorted array in-place. The runtime analysis for this code is as follows:

### Time Complexity

- The code iterates over each element in the `nums` list exactly once with the `for` loop. 
- During each iteration, it performs a constant-time check (`if nums[i - 1] != nums[i]`) and, potentially, a constant-time assignment (`nums[replace] = nums[i]`), and an increment operation (`replace += 1`).
  
Given that the list contains `n` elements, the time complexity for the `removeDuplicates` method is linear, denoted as **O(n)**.

### Space Complexity

- The algorithm modifies the `nums` list in-place and does not utilize any additional data structures that would grow proportionally with the input size.
- Only a constant amount of additional space is used, specifically the `replace` pointer and loop index `i`.

As a result, the space complexity of the method is **O(1)**, representing constant space usage regardless of the input size.

In summary, the `removeDuplicates` method efficiently handles the task of de-duplicating a sorted array in terms of both time and space complexity.


</span>