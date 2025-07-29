from typing import List


class Solution:
    def equalPairsHashMap(self, grid: List[List[int]]) -> int:
        matches = 0
        size = len(grid)
        rows = {}

        for i in range(0, size):
            key = tuple(grid[i])
            print(rows.keys())
            if key not in rows.keys():
                rows[key] = 0

        for i in range(0, size):
            col = []
            for j in range(0, size):
                col.append(grid[j][i])

            if tuple(col) in rows.keys():
                rows[tuple(col)] += 1

        for k in rows.keys():
            matches += rows[k]

        print(rows)
        return matches

    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = []
        cols = []
        # rows = set()
        matches = 0

        size = len(grid)


        # load rows in rows
        for i in range(0, size):
            print(grid[i])
            rows.append(grid[i])

        for j in range(0, size):
            row = []
            for g in grid:
                row.append(g[j])
            
            for r in rows:
                if row == r:
                    matches += 1

        return matches


s = Solution()
print(s.equalPairsHashMap([[3,2,1],[1,7,6],[2,7,7]])) 
print(s.equalPairsHashMap([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])) 

