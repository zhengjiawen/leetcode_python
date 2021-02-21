'''
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        反转数字，效率低
        :param x:
        :return:
        '''
        if x<0:
            return False
        if x < 10:
            return True

        cur_x = x
        rev_n = 0

        while cur_x>0:
            n = cur_x%10
            cur_x = cur_x//10
            rev_n  = rev_n*10+n

        if rev_n == x:
            return True
        else:
            return False
    def isPalindrome2(self, x: int) -> bool:
        '''
        将一半的数字反转
        :param x:
        :return:
        '''
        if x<0 or (x%10==0 and x!= 0):
            return False
        if x < 10:
            return True

        cur_x = x
        rev_n = 0

        while cur_x>rev_n:
            n = cur_x%10
            cur_x = cur_x//10
            rev_n  = rev_n*10+n

        return cur_x==rev_n or cur_x == rev_n//10


if __name__ == '__main__':
    x = 10
    solution = Solution()
    print(solution.isPalindrome2(x))