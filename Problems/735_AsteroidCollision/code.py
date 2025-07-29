from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        print("--START--")
        print(stack)

        for i in range(1, len(asteroids)):
            print("{} vs {}".format(asteroids[i], stack[-1]))
            if len(stack) == 0:
                stack.append(asteroids[i])
            else:
                if asteroids[i] < 0 and stack[-1] > 0: #(asteroids[i] < 0 and stack[-1] > 0) or (asteroids[i] > 0 and stack[-1] < 0): 
                    last = stack.pop()
                    if abs(asteroids[i]) > abs(last):
                        stack.append(asteroids[i])
                    elif abs(asteroids[i]) < abs(last):
                        stack.append(last)
                else:
                    stack.append(asteroids[i])
                
            print(stack)

        return stack


        print("-- ANSWER --")
        hasNeg = False
        hasPos = False
        mixed = False
        for s in stack:
            if s < 0:
                hasNeg = True

            if s > 0:
                hasPos = True

        mixed = hasNeg and hasPos

        if not mixed:
            return stack
        else:
            return self.asteroidCollision(stack)



s = Solution()
print(s.asteroidCollision([5,10,-5]))
print(s.asteroidCollision([8,-8]))
print(s.asteroidCollision([10,2,-5]))

print(s.asteroidCollision([-2,-1,1,2]))