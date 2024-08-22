class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i, j = 0, len(skill) - 1
        target= skill[i] + skill[j]
        total_chemistry = 0
        
        while i < j:
            if skill[i] + skill[j] != target:
                return -1
            total_chemistry += skill[i] * skill[j]
            i += 1
            j -= 1
        
        return total_chemistry

solution = Solution()
print(solution.dividePlayers)
