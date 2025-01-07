from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def backtracking(cur_string, left_count, right_count):
            # base case, when string has all 6 characters (3 open, 3 close)
            if len(cur_string) == 2 * n:
                answer.append("".join(cur_string))
                return
            
            # reduce the problem - these next two if statements are going to run 
            # in sequence with each change in backtrack
            # essentially: try "(", backtrack, pop it, try a ")", backtrack

            # if there aren't enough opening parentheses
            if left_count < n: # this is really important on the first pass through
                cur_string.append("(")
                backtracking(cur_string, left_count + 1, right_count)
                cur_string.pop()

            # if there aren't enough closing parentheses
            # always executed after the opening parenthese if-statement
            if right_count < left_count:
                cur_string.append(")")
                backtracking(cur_string, left_count, right_count + 1)
                cur_string.pop()

        backtracking([], 0, 0)
        return answer
    
s = Solution()
print(s.generateParenthesis(3))

'''
( > (( > ((( > ((() > ((()) > ((()))
cur_string.pop() on line 29 > ((())
previous ) backtrack()
cur_string.pop() on line 29 > ((()
previous ) backtrack()
cur_string.pop() on line 29 > (((
previous ( backtrack()
cur_string.pop() on line 22 > ((
move to ) if-statement and append > (()
call ) backtrack()
add ( > (()(
call ( backtrack()
go to ) if-statement
append ) > (()()
'''