class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            return n 
        else:
            return n*2

solution =Solution()
result = solution.smallestEvenMultiple(10)
print(result)



