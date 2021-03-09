'''
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ['.'*n for _ in range(n)]
        self.ret = []

        def back_track(board, row, n):
            if row == len(board):
                self.ret.append(board.copy())
                return

            for i in range(n):
                if self.is_valid(board, row, i):
                    board[row] = board[row][:i]+ 'Q' + board[row][i+1:]
                    back_track(board, row+1, n)
                    board[row] = board[row][:i]+ '.' + board[row][i+1:]

        back_track(board, 0, n)

        return self.ret



    def is_valid(self, board, row, col) -> bool:
        # 判断竖直方向是否有皇后
        for i in range(len(board)):
            if board[i][col] == 'Q' and i != row:
                return False

        # 检查右上方
        i = row
        j = col
        while i>0 and j<len(board[0])-1:
            i-=1
            j+=1
            if board[i][j] == 'Q':
                return False

        # 检查左上方
        i = row
        j = col
        while i>0 and j>0:
            i-=1
            j-=1
            if board[i][j] == 'Q':
                return False

        return True




if __name__ == '__main__':
    n = 8
    solution = Solution()
    ret = solution.solveNQueens(n)
    print(len(ret))
    print(ret)