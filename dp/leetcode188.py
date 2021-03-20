'''
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    def maxProfit(self, k: int,prices: List[int]) -> int:
        import numpy as np

        # 0代表不持有股票，1代表持有股票
        dp = np.zeros((len(prices), k+1, 2), dtype=int)
        for i in range(k):
            dp[0,i,1] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(k):
                dp[i, j, 0] = max(dp[i-1,j, 0], dp[i-1, ])



        # print(dp)
        return dp[-1, 0, 0]

if __name__ == '__main__':
    prices = [1,2,3,4,5]
    solution = Solution()
    k=2
    print(solution.maxProfit(prices))