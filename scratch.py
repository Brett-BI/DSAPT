


from collections import defaultdict, deque


def shortestPathGraph(edges, degreesBetween) -> int:
    # get the adjacency list
    adj = defaultdict(list)
    for e in edges:
        # print(e)
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])

    queue = deque([(degreesBetween[1], 0)])
    seen = set()
    degreesOfSeparation = 0
    foundDegreesOfSeparation = float("inf")

    # if neither of the items/companies are not in the adjacency list, fail
    if degreesBetween[1] not in adj or degreesBetween[0] not in adj:
        return -1

    # figure out degree of separation
    while queue:
        current = queue.popleft()
        for relation in adj[current[0]]:
            # print(relation)
            if relation == degreesBetween[0]:
                # print("found match")
                foundDegreesOfSeparation = min(foundDegreesOfSeparation, current[1])
                # print(f"sep: {foundDegreesOfSeparation}")
                
            
            if relation not in seen:
                # print(f"not found: {relation}")
                seen.add(relation)
                queue.append((relation, current[1] + 1))
                degreesOfSeparation += 1

    if foundDegreesOfSeparation == float("inf"):
        return -1
    else:
        return int(foundDegreesOfSeparation)



edges = [["a", "b"], ["b", "c"]]
degressBetween = ["a", "c"]
print(shortestPathGraph(edges, degressBetween))