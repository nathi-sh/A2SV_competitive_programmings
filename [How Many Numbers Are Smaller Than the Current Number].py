class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        num_to_smaller_count = {}
        for i, num in enumerate(sorted_nums):
            if num not in num_to_smaller_count:
                num_to_smaller_count[num] = i
        result = [num_to_smaller_count[num] for num in nums]
        
        return result

sol = Solution()
print(sol.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))  
