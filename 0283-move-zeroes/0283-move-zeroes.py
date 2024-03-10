class Solution(object):
    def moveZeroes(self, nums):
     
        x=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[x]=nums[i]
                x=x+1
            
        for i in range(x,len(nums)):
            nums[i]=0
            
        return nums