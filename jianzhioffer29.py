'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
'''
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        top = 0
        left = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1

        ret = []

        while top <= bottom and left <= right:
            for j in range(left, right+1):
                ret.append(matrix[top][j])

            for i in range(top+1, bottom+1):
                ret.append(matrix[i][right])

            if top <bottom and left < right:
                for j in range(right-1, left-1, -1):
                    ret.append(matrix[bottom][j])

                for i in range(bottom-1, top, -1):
                    ret.append(matrix[i][left])

            top = top+1
            bottom = bottom-1
            left = left+1
            right = right-1
        return ret





if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    # matrix = [[1, 2, 3]]
    print(solution.spiralOrder(matrix))