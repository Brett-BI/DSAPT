# Recursion
Recursion is a method of solving problems that relies on using repeatable solutions to smaller parts of the problem. Two parts:
1. Base case
2. Work towards base case
3. The recursive call

Classic Fibonacci:
```python
def fib(n):
    if n <= 1:
        return n
    
    return fib(n - 1) + fib(n - 2)
```

Tail recursion:
- the very last statement is calling the recursive algorithm.
- every instance of tail recursion can be written in loops

Common corner cases:
- `n = 1` 
- `n = 0`

Things to try:
- figure out how to generate all permutions of a given sequence - this will only serve you later on
- There are limitations: recursion uses a call stack. If your recursion level goes too deep, you'll get a stack overflow (limit is 1000 by default in Python).

