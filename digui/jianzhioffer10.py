'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def numWays(self, n: int) -> int:
        '''
        递归
        :param n:
        :return:
        '''
        def jump(n):
            if n==1:
                return 1
            if n==2:
                return 2

            return jump(n-1)+jump(n-2)
        if n==0:
            return 1

        return jump(n)

    def numWays(self, n: int) -> int:
        if n==0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2

        pre1 = 1
        pre2 = 2

        for i in range(3, n+1):
            res = pre1+pre2
            pre1 = pre2
            pre2 = res

        return res

if __name__ == '__main__':
    n = 37

    solution = Solution()
    print(solution.numWays(n))