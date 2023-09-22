from typing import List

# Approach: maintain an array where index is the amount and value is the minimum number of coins required that add up to that amount
# value at index k is determined as min(f(k - c1), f(k - c2), ..., f(k - cn)) + 1
def coinChange(coins: List[int], amount: int) -> int:
    memo = [0] * (amount + 1)

    for k in range(1, amount + 1):
        min = None
        for c in coins:
            if k >= c:
                n = memo[k - c]
                if n > -1 and (min == None or min > n):
                    min = n

        if min == None:
            memo[k] = -1
        else:
            memo[k] = min + 1

    return memo[amount]
