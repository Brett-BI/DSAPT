class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        window_start = 0
        last_seen = {}

        for window_end, ch in enumerate(s):
            if ch in last_seen:
                # window_start is the index + 1 of the last time we saw it
                # it's a lagging indicator of our current window
                # with respect to the current value, ch
                window_start = max(window_start, last_seen[ch])

            longest = max(longest, window_end - window_start + 1)
            last_seen[ch] = window_end + 1

        return longest