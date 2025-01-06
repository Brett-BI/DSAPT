# Time Complexity
## Common Times (in order)
O(1)
- constant time, very fast, one operation to solve the problem

O(log n)
- Logarithmic time; base-b logarithm of a number, n, is the power to which b must be raised to product n: logb n = x is the same as b^x = n
- As time increases linearly, n goes up exponentially
- Ex.: 1 second for 10 elements, 2 seconds for 100 elements:
for 128, logn = 7; for n=64, logn = 6

O(n)
- Changes as n changes; essentially there is a single operation for each value of n
- Ok, as far as time complexity goes

O(nlogn)
- This is slower than O(n), especially as n grows

O(n^2)
- Exponential growth, quite slow
- Should generally try to find alternative solutions if time complexity is O(n^2)

## Ignoring Factors
In theory, time complexity is often very nuanced and can be much more granular than the 
commonly-accepted time complexities for various solutions.

*Constants*
Constants can generally be ignored because they matter less as N grows in size. Constants are an important consideration when comparing two algorithms for the same solution.

*Low Order Terms*
When multiple terms are involved, only the term with the highest growth matters. The reasoning behind this is that as N grows larger, the lower order terms matter less and less. Example: O(n^2 + n); n^2 dominates n so this can be simplified to O(n^2).

*Non-Dominant Factors*
Sometimes, when the complexity calculation involves a product of terms, multiple factors in the complexity calculation carry significant weight. The dominant factor(s) should NOT be ignored. For example: O(n^2 * logn * c); c can be ignored because it is a constant but the other two factors, n^2 and logn, are significant in the product so they must be included.

*A note on when **NOT** to ignore factors...*
1. Small input sizes. If n is sufficiently small, all terms in the complexity calculation matter.
2. Comparative analysis of algorithms for the same solution
3. Real-time or performance-critical systems. When milliseconds count, the size of constant factors and other implementation details may matter.

# Space Complexity
Space complexity is the measure of the amount of space that is used by an algorithm. It accounts for:
1. Input space - memory required to store the input to the algorithm (generally n)
2. Auxiliary space - the additional memory required during execution of the algorithm (temporary variables, recursion stack, data structures, etc.)

## Ignoring Factors
Like time complexity calculations, some factors can be ignored in space complexity calculations.

Ignore the following:
- Constants
- Lower-order terms: only the term with the largest space requirement matters, generally. This is NOT true for small values of n.
- Non-dominant structures: focus on the structure(s) that consume the most space.