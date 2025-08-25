# Top-down
def fn(arr):
    def dp(STATE):
        if BASE_CASE:
            return 0
        
        if STATE in memo:
            return memo[STATE]
        
        ans = RECURRENCE_RELATION(STATE)
        memo[STATE] = ans
        return ans

    memo = {}
    return dp(STATE_FOR_WHOLE_INPUT)


# Bottom-up, 1D array
def fn2(arr):
    dp = [VAL * len(array)] # of length arr or other state variable

    # base cases (before iteration)
    dp[...] = ...

    for i in range(NUMBER_OF_BASE_CASES, len(arr) + 1):
        dp[i] = RECCURENCE_RELATION # with potential additional logic before/after

    return dp[LAST_INDEX] # first or last index based on for-loop direction