from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque([])
        d = deque([])
        senateMembers = len(senate)

        for index, s in enumerate(senate):
            if s == "D":
                d.append(index)
            else:
                r.append(index)
        
        print(r)
        print(d)

        while r and d:
            _r = r.popleft()
            _d = d.popleft()

            if _r < _d:
                r.append(_r + senateMembers)
            else:
                d.append(_d + senateMembers)

        print(r)
        print(d)
        if len(r) > 0:
            return "Radiant"
        else:
            return "Dire"
    

s = Solution()
print(s.predictPartyVictory("RD"))
print(s.predictPartyVictory("RDD"))
print(s.predictPartyVictory("RDDRDRRDDDDR"))