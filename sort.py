class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            left=i
            right=i+1    
            for j in range(i+1,len(nums)):
                if nums[left]>nums[right]:
                    nums[left],nums[right]=nums[right],nums[left]
                right+=1