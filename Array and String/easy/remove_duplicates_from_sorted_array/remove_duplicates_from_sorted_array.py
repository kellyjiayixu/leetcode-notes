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