
from typing import List

# Recursive formula: 
# dp[k] = max(dp[k-1] + nums[k], nums[k])
def maxSubArray(nums: List[int]) -> int:
    dp = [k for k in nums]
    result = nums[0]
    for i in range(1, len(nums)):
        n = nums[i]
        dp[i] = max(dp[i - 1] + n, n)
        if result < dp[i]:
            result = dp[i]
    return result
