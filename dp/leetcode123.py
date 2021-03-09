'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        import numpy as np

        # 0代表不持有股票，1代表持有股票
        dp = np.zeros((len(prices), 3, 2), dtype=int)
        dp[0,2,1] = -prices[0]
        dp[0,1,1] = -prices[0]

        for i in range(1, len(prices)):
            # dp[i, 2, 0] = dp[i-1, 2, 0]
            dp[i, 2, 1] = max(-prices[i],dp[i-1, 2, 1])
            dp[i, 1, 0] = max(dp[i-1, 1, 0], dp[i-1, 2, 1]+prices[i])
            dp[i, 1, 1] = max(dp[i-1, 1, 0] - prices[i], dp[i-1, 1, 1])
            dp[i, 0, 0] = max(dp[i-1, 1, 1]+prices[i], dp[i-1, 0, 0])



        # print(dp)
        return dp[-1, 0, 0]

if __name__ == '__main__':
    prices = [1,2,3,4,5]
    solution = Solution()
    print(solution.maxProfit(prices))