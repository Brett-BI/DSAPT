# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

from collections import deque


class Solution:
    def depthSumIterative(self, nestedList: List[NestedInteger]) -> int:
        # starts as a list, add the first item or multiple items, if needed
        queue = deque([(n, 1) for n in nestedList])
        # or use a loop:
        # for n in nestedList:
        #   queue.append((n, 1))
        ans = 0

        while queue:
            item = queue.pop()

            if item[0].isInteger():
                ans += item[0].getInteger() * item[1]
            else:
                for i in item[0].getList():
                    queue.appendleft((i, item[1] + 1))

        return ans
    



    def depthSumRecursive(self, nestedList: List[NestedInteger]) -> int:
        # start the total sum at 0; use nonlocal to access the variable in this scope
        sum: int = 0

        # recursive function
        def calculateSum(item: NestedInteger, depth: int):
            nonlocal sum # initialize parent scope's sum here

            # Based on NestedInteger class above, the type of the item/element
            # needs to be checked. The item can only be two things: integer or List.
            if item.isInteger():
                # increment sum by item * depth
                sum += item.getInteger() * depth
            else:
                # Loop through the list, use recursion to evaluate each function.
                # Each loop with either add to sum variable or it will loop through
                # the next nested List
                for l in item.getList():
                    calculateSum(l, depth + 1)

        # depth can be 1 to start because of constraints
        for nl in nestedList:
            calculateSum(nl, 1)

        return sum

# T: O(n); this is only evaluating each element once even though there are two for loops
# S: O(n + 1) => O(n)