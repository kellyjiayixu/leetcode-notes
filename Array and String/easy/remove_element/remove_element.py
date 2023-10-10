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
