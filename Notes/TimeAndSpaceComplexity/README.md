When Can a Factor Be Ignored?
Asymptotic Analysis:

When analyzing algorithms for large inputs, only the most significant term matters, because it grows the fastest as input size (
𝑛
n) increases.
Lower-order terms or constant factors are ignored.
Example:
𝑂
(
𝑛
2
+
𝑛
)
O(n 
2
 +n): For large 
𝑛
n, 
𝑛
2
n 
2
  dominates, so the time complexity is simplified to 
𝑂
(
𝑛
2
)
O(n 
2
 ).
𝑂
(
5
𝑛
)
O(5n): The constant 
5
5 is ignored, leaving 
𝑂
(
𝑛
)
O(n).
Negligible Contribution:

If one factor grows much slower than another, its contribution can be considered negligible for large inputs.
Example:
𝑂
(
𝑛
+
log
⁡
𝑛
)
O(n+logn): For large 
𝑛
n, the 
𝑛
n term dominates, so this simplifies to 
𝑂
(
𝑛
)
O(n).
𝑂
(
𝑛
⋅
𝑚
+
𝑛
)
O(n⋅m+n): If 
𝑚
≫
1
m≫1, the 
𝑛
⋅
𝑚
n⋅m term dominates, and the complexity becomes 
𝑂
(
𝑛
⋅
𝑚
)
O(n⋅m).
Dominated by Another Operation:

If one part of the algorithm dominates the runtime, smaller contributions can be ignored.
Example:
A recursive function with 
𝑂
(
𝑛
⋅
𝑚
log
⁡
𝑚
)
O(n⋅mlogm) complexity (e.g., due to sorting within recursion) can ignore 
𝑂
(
𝑛
)
O(n) if 
𝑚
log
⁡
𝑚
≫
1
mlogm≫1.
When Should All Factors Be Considered?
For Small Inputs:

For small values of 
𝑛
n, lower-order terms or constants can have a significant impact on performance.
Practical performance for real-world use cases often requires considering these "ignored" factors.
Edge Cases or Special Scenarios:

In cases where ignored factors may dominate due to specific input sizes or conditions.
Example:
𝑂
(
𝑛
+
log
⁡
𝑛
)
O(n+logn): If 
𝑛
n is small, the 
log
⁡
𝑛
logn term might contribute significantly.
Balanced Growth Rates:

When two factors grow at comparable rates, neither can be ignored.
Example:
𝑂
(
𝑛
⋅
log
⁡
𝑛
+
𝑛
⋅
𝑚
)
O(n⋅logn+n⋅m): If 
𝑚
≈
log
⁡
𝑛
m≈logn, both terms contribute significantly.
Rules of Thumb for Simplifying Complexity
Retain the Dominant Term:

Focus on the term that grows fastest with input size.
Example: 
𝑂
(
𝑛
3
+
𝑛
2
+
𝑛
)
O(n 
3
 +n 
2
 +n) simplifies to 
𝑂
(
𝑛
3
)
O(n 
3
 ).
Drop Constants:

Ignore constant multipliers since they don't affect growth rates.
Example: 
𝑂
(
3
𝑛
2
)
O(3n 
2
 ) simplifies to 
𝑂
(
𝑛
2
)
O(n 
2
 ).
Consider Practical Scenarios:

For real-world performance, constants and lower-order terms can matter, so keep them in mind when implementing algorithms.
Examples of Ignoring Factors
Example 1: Large Input, Dominant Term Matters
Expression: 
𝑂
(
𝑛
2
+
100
𝑛
+
500
)
O(n 
2
 +100n+500)
Simplified: 
𝑂
(
𝑛
2
)
O(n 
2
 ) (for large 
𝑛
n, lower-order terms 
100
𝑛
100n and 
500
500 are negligible).
Example 2: Comparable Growth Rates
Expression: 
𝑂
(
𝑛
log
⁡
𝑛
+
𝑛
⋅
𝑚
)
O(nlogn+n⋅m)
If 
𝑚
≫
log
⁡
𝑛
m≫logn, simplify to 
𝑂
(
𝑛
⋅
𝑚
)
O(n⋅m).
If 
𝑚
≈
log
⁡
𝑛
m≈logn, retain both terms: 
𝑂
(
𝑛
⋅
log
⁡
𝑛
)
O(n⋅logn).
Example 3: Ignoring Constants
Expression: 
𝑂
(
3
𝑛
+
5
)
O(3n+5)
Simplified: 
𝑂
(
𝑛
)
O(n).
Conclusion
You can ignore factors in time complexity:

When performing asymptotic analysis for large inputs.
When constants or lower-order terms contribute negligibly.
When one term dominates another significantly.