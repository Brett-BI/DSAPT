# Combinatorics
Combinatorics is an area of mathematics primarily concerned with counting, both as a means and as an end to obtaining results, and certain properties of finite structures. It is closely related to many other areas of mathematics and has many applications ranging from logic to statistical physics and from evolutionary biology to computer science.

Combinatorics, on their own, are typically not the solution to a problem. They are, generally, a solution to a small part of a problem. 

## Permutation
Permutation is an arrangement of objects from a set such that each object in the set is used once. Order matters. For example, the permutation of `[1,2,3]` is:

`[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`

Each object from the original set is used once. No repeats. Order is important.

The algorithm uses recursion and the backtracking pattern. See more below.

**Algorithm**

This is a basic permutation strategy using backtracking. Backtracking is a recursive approach wherein the recursive function knocks off the last item of your current string/list/etc. to try the next available character. The full function looks like this:

```python
# answer: List[int] = []
# nums: List[int]
def backtrack(current: List[int]) -> List[int]:
    # base case
    if len(current) == len(numbers):
        answer.append(current[:]) # value, not reference
        return # end the recursive call with this

    # recursion
    for num in numbers:
        if num not in current:
            num.append(current) # append the missing number
            backtrack(current) # recursive call
            current.pop() # remove the last item and try the next num
```

The `pop()` method call looks odd but it's important to the backtracking pattern. It allows the recursive function to operate on one valid value at a time, the remove it after the recursive function completes, and to try the next number without increasing the size of the string. Think about this in terms of just iterating through permutations, without a recursive function call:

```python
# numbers: List[int] = [1,2,3]
# current: List[int] = [1]
for num in numbers: # 1 doesn't work, try 2
    if num not in current:
        num.append(current) # add 2, current = [1,2]
        current.pop() # remove the last num, 2, and try the next number, 3
```