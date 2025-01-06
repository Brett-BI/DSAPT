from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for index, val in enumerate(order):
            order_map[val] = index

        for i in range(len(words) - 1): # for each word
            for j in range(len(words[i])): # for each letter in a word
                # If we do not find a mismatch letter between words[i] and words[i + 1],
                # we need to examine the case when words are like ("apple", "app").
                if j >= len(words[i + 1]): return False # if current letter is greater than length of next word

                if words[i][j] != words[i + 1][j]: # if char in word 1 != char in word 2
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]: return False
                    # if we find the first different character and they are sorted,
                    # then there's no need to check remaining letters
                    break

        return True

# T: O(n) or O(m * n); choose and explain
# S: O(1) because length of order is fixed

s = Solution()
a = s.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
print(a) # true
print("\n=====================\n")
a = s.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")
print(a) # false
print("\n=====================\n")
a = s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")
print(a) # false