class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemyEnergies.sort()
        points = 0

        if currentEnergy < enemyEnergies[0]:
            return 0
        sumOfTotal = sum(enemyEnergies[1:]) +currentEnergy

        return sumOfTotal // enemyEnergies[0]


        
