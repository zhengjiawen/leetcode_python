'''
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
'''

from typing import List

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def quick_sort(arr, left, right, k):
            tmp_val = arr[left]
            p_left = left+1
            p_right = right





if __name__ == '__main__':
    solution = Solution()
    arr = [3,2,1]
    k = 2

    print(solution.getLeastNumbers(arr, k))