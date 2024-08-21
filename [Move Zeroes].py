class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0 
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1


nums = [0,1,0,3,12]
solution =Solution()
solution.moveZeroes(nums)
