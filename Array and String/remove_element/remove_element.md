<span style="font-family:Cambria;">

# Remove Element

**Jiayi Xu**

## Problem

> Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.   
> 
> Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things: 
>   
> - Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.   
> 
> - Return k.   

## Solution

```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        # Initialize a pointer i at the beginning of the list
        i = 0
        
        # Iterate over each element in the nums list
        for x in nums:
            # If the current element is not equal to the given value 'val'
            if x != val:
                # Assign this element to the position pointed by 'i'
                nums[i] = x
                
                # Increment the 'i' pointer
                i += 1
                
        # At the end of the loop, 'i' will be pointing just past the last valid element
        # Return 'i' as it also represents the new length of the modified list
        return i

```

## Runtime Analysis

The provided code is a method `removeElement` that intends to remove all instances of a specified value from an array in-place. The analysis of the code's performance is as follows:

### Time Complexity

- The method iterates over each element in the `nums` list exactly once using the `for` loop. 
- Each iteration consists of a constant-time check (`if x != val`) and potentially a constant-time assignment (`nums[i] = x`) and an increment operation (`i += 1`).
  
Given that the list contains `n` elements, the time complexity of the `removeElement` method is linear, which can be denoted as **θ(n)**.

### Space Complexity

- The algorithm modifies the `nums` list in-place and does not use any additional data structures that grow with the input size. 
- Only a constant amount of extra space is used (like the `i` pointer and temporary variables).

Given this, the space complexity of the method is **θ(1)**, which means it uses constant space irrespective of the input size.

In summary, the `removeElement` method is efficient in its time and space complexity for the purpose of removing a specific element from an array in-place.


</span>