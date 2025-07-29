from collections import deque
from typing import List

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            return False
        

        adjacencyList = {} # or use defaultdict(list) to make it easier
        for i, v in edges:
            # or just this:
            # adjacencyList[i].append(v)
            # adjacencyList[v].append(i)
            if v in adjacencyList.keys():
                adjacencyList[v].append(i)
            else:
                adjacencyList[v] = [i]
            
            if i in adjacencyList.keys():
                adjacencyList[i].append(v)
            else:
                adjacencyList[i] = [v]

        print(adjacencyList)

        START_NODE = list(adjacencyList.keys())[0]
        queue = deque([START_NODE])
        visited = set()

        while queue:
            node = queue.popleft()
            for neighbor in adjacencyList[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print(len(visited))

        return len(visited) - 1 == len(edges)


s = Solution()
print(s.validTree(5, [[0,1],[0,2],[0,3],[1,4]]))


adjacencyList = defaultdict(list)
adjacencyList[i].append(v)
adjacencyList[v].append(i)