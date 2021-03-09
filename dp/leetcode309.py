from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        import numpy as np
        dp = np.zeros((len(prices), 3),dtype=int)
        dp[0, 1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i, 0] = max(dp[i-1, 0], dp[i-1,2])
            dp[i, 1] = max(dp[i-1,0]-prices[i], dp[i-1, 1])
            dp[i, 2] = dp[i-1, 1]+prices[i]


        return int(max(dp[-1, 0], dp[-1, 2]))



if __name__ == '__main__':
    prices = [1,2,3,0,2]
    solution = Solution()
    print(solution.maxProfit(prices))