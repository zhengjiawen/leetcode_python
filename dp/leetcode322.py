'''
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = dict()
        def dp(coins, amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1

            if amount in self.memo.keys():
                return self.memo[amount]

            res = float('INF')

            for coin in coins:
                val = dp(coins, amount - coin)
                if val == -1:
                    continue
                res = min(res, 1+val)

            self.memo[amount] = res if res != float('INF') else -1
            return self.memo[amount]


        return dp(coins, amount)


    def coinChange2(self, coins: List[int], amount: int) -> int:




        return dp(coins, amount)



if __name__ == '__main__':
    # coins = [1, 2, 5]
    coins = [ 5]
    amount = 2

    solution = Solution()
    print(solution.coinChange(coins, amount))