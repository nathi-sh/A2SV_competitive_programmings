class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1  
            right -= 1
            boats += 1

        return boats
people =[3,5,3,4]
limit  =3
solution  =Solution()
solution.numRescueBoats(people,limit)
        
