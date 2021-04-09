'''
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        ret = 1
        if x==0:
            return 0

        if n <0:
            x = (1/x)
            n = -n
        while n:
            if n%2==0:
                x = x*x
                n = n//2
            else:
                ret*=x
                n = n-1
        return ret

if __name__ == '__main__':
    solution = Solution()
    print(solution.myPow(2, -2))