'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

'''
from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:

        def recur(postorder, start, end):
            if start >= end:
                return True
            root_val = postorder[end]
            i = start
            while postorder[i] < root_val:
                i+=1
            m = i
            for i in range(m, end):
                if postorder[i] <= root_val:
                    return False

            return recur(postorder, start, m - 1) and recur(postorder, m, end - 1)

        return recur(postorder, 0, len(postorder) - 1)

if __name__ == '__main__':
    solution = Solution()
    num = [4, 8, 6, 12, 16, 14, 10]

    print(solution.verifyPostorder(num))