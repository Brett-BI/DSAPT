import collections
from typing import List


class Solution:
    def overlap(self, a, b):
        return a[0] <= b[1] and b[0] <= a[1]

    # generate graph where there is an undirected edge between intervals u
    # and v iff u and v overlap.
    # if there is overlap, add them to the graph dictionary
    def buildGraph(self, intervals):
        graph = collections.defaultdict(list)

        for i, interval_i in enumerate(intervals):
            for j in range(i + 1, len(intervals)):
                if self.overlap(interval_i, intervals[j]):
                    graph[tuple(interval_i)].append(intervals[j])
                    graph[tuple(intervals[j])].append(interval_i)

        return graph

    # merges all of the nodes in this connected component into one interval.
    # find the lowest start and highest end; that's your full interval
    def mergeNodes(self, nodes):
        min_start = min(node[0] for node in nodes)
        max_end = max(node[1] for node in nodes)
        return [min_start, max_end]

    # gets the connected components of the interval overlap graph.
    # nodes_in_comp: key = component number, value = list of intervals
    # each key is the list of overlapping intervals
    # comp_number: only used as a key in the dict; otherwise len() could 
    # be used later
    def getComponents(self, graph, intervals):
        visited = set()
        comp_number = 0
        nodes_in_comp = collections.defaultdict(list)

        # use a stack to process each interval
        def markComponentDFS(start):
            stack = [start]
            while stack:
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    # if the interval has an overlap, add its overlapping
                    # interval; stops when you point back to a node that's 
                    # already been visited
                    stack.extend(graph[node])

        # mark all nodes in the same connected component with the same integer.
        for interval in intervals:
            if tuple(interval) not in visited:
                markComponentDFS(interval)
                comp_number += 1

        return nodes_in_comp, comp_number

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        graph = self.buildGraph(intervals) # only overlapping intervals
        nodes_in_comp, number_of_comps = self.getComponents(graph, intervals)

        # all intervals in each connected component must be merged.
        # list comprehension. call self.mergeNodes() for each list of 
        # intervals in the dictionary
        return [
            self.mergeNodes(nodes_in_comp[comp])
            for comp in range(number_of_comps)
        ]
    
s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))