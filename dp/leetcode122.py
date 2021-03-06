'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        import numpy as np

        # 0代表不持有股票，1代表持有股票
        dp = np.zeros((len(prices), 2), dtype=int)
        dp[0,1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i, 0] = max(dp[i-1, 0], dp[i-1, 1]+prices[i])
            dp[i, 1] = max(dp[i-1, 0]-prices[i], dp[i-1, 1])

        return dp[-1, 0]

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    solution = Solution()
    print(solution.maxProfit(prices))