class Solution:
    def sortColors(self, nums: List[int]) -> None:

        size = len(nums)
        for i in range(1, size):
            key = nums[i]
            j = i - 1
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
                nums[j + 1] = key
        print(nums)

numbers= [2,0,2,1,1,0]
sol =Solution()
sol.sortColors(numbers)
        
