from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        startingCities: set = set()

        for i in range(len(paths)):
            startingCities.add(paths[i][0])

        for j in range(len(paths)):
            city = paths[j][0]
            if city not in startingCities:
                return city
            
        return ""