class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hs = {}
        k = 0
        
        # Create a copy of nums
        x = nums[:]
        
        # Count occurrences of each element in x
        for i in x:
            hs[i] = 0
        
        # Iterate through x to remove duplicates and update counts
        for i in range(len(x)):
            if hs[x[i]] == 0:
                hs[x[i]] += 1
                nums[k] = x[i]  # Replace the element at index k with the unique element
                k += 1
                
        return k