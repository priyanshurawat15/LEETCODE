class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0  # if the list is empty, there are no duplicates
        
        o = 1  # index of the next unique element
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # check for uniqueness
                nums[o] = nums[i]  # move the unique element to the next position
                o += 1  # increment unique elements count
                
        return o