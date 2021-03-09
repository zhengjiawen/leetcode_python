from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        import numpy as np
        dp = np.zeros((len(prices), 2),dtype=int)
        dp[0, 1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i, 0] = max(dp[i-1, 0], dp[i-1,1]+prices[i]-fee)
            dp[i, 1] = max(dp[i-1,0]-prices[i], dp[i-1, 1] )

        return int(dp[-1, 0])



if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    solution = Solution()
    print(solution.maxProfit(prices, fee))