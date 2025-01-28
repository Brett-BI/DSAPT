from collections import Counter, deque
import heapq
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dive(item: NestedInteger, depth: int) -> None:
            nonlocal ans
            # base case
            if item.isInteger():
                ans += item.getInteger() * depth
            else:
                for i in item.getList():
                    dive(i, depth + 1)

        ans: int = 0
        
        for n in nestedList:
            dive(n, 1)

        return ans

    def topKFrequentCounter(self, nums: List[int], k: int) -> List[int]:
        c = Counter([nums])

        if len(nums) == k:
            return nums
        
        return heapq.nlargest(k, c.keys(), key=c.get)

    def uniquePathsTD(self, m: int, n: int) -> int:
        board = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                board[i][j] = board[i - 1][j] + board[i][j - 1]

        return board[m - 1][n - 1]

    def uniquePathsBU(self, m: int, n: int) -> int:
        board = [[1] * n for _ in range(m)]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                board[i][j] = board[i + 1][j] + board[i][j + 1]

        return board[0][0]

    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr) -> None:
            if len(curr) == len(nums):
                answer.append(curr[:])
                return
            
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    backtrack(curr)
                    curr.pop()

        answer = []
        backtrack([])
        return answer
        

    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(curr, nextItem):
            if len(curr) == k:
                answer.append(curr[:])
                return
            
            for i in range(nextItem, n + 1):
                if i not in curr:
                    curr.append(i)
                    backtrack(curr, i + 1)
                    curr.pop()
        
        answer = []

        backtrack([], 1)

        return answer
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, lowerBound, size):
            if len(curr) == size:
                answer.append(curr[:])
                return
            
            for n in range(lowerBound, len(nums)):
                if nums[n] not in curr:
                    curr.append(nums[n])
                    backtrack(curr, n + 1, size)
                    curr.pop()

        answer = []

        for i in len(nums):
            backtrack([], 0, i)

        return answer
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def traverse(node: Optional[TreeNode]) -> None:
            if not node:
                return
            else:
                if node.val >= low and node.val <= high:
                    ans += node.val

                traverse(node.left)
                traverse(node.right)
        
        ans: int = 0

        traverse(root)

        return ans

    def lcaRec(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def traverse(node: Optional[TreeNode]) -> bool:
            nonlocal ans
            currentNodeMatch: bool = False

            if not node:
                return False
            
            lFind = traverse(node.left)
            rFind = traverse(node.right)

            if node == p or node == q:
                currentNodeMatch = True

            if (currentNodeMatch and (lFind or rFind)) or (lFind and rFind):
                ans = node
                return True
            
            if currentNodeMatch or lFind or rFind:
                return True
            else:
                return False

        ans: TreeNode = None

        traverse(root)

        return ans
    
    def lcaStack(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        nodeQueue = deque([root])
        parentDict = {root: None}

        while nodeQueue:
            curr = nodeQueue.popleft()

            if curr.left:
                nodeQueue.append(curr.left)
                parentDict[curr.left] = curr

            if curr.right:
                nodeQueue.append(curr.right)
                parentDict[curr.right] = curr

            if p in parentDict and q in parentDict:
                break

        ancestors = set()

        while p:
            ancestors.add(p)
            p = parentDict[p]

        while q:
            if q in ancestors:
                return q
            q = parentDict[q]