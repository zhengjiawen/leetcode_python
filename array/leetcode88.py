'''
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1

        p1 = m-1
        p2 = n-1

        last = m+n-1

        while last >=0 and p1>=0 and p2 >=0:
            if nums1[p1] > nums2[p2]:
                nums1[last] = nums1[p1]
                p1-=1
            else:
                nums1[last] = nums2[p2]
                p2-=1
            last -= 1

        # while p1 >= 0:
        #     nums1[last] = nums1[p1]
        #     p1-=1
        #     last-=1

        while p2 >= 0:
            nums1[last] = nums2[p2]
            last-=1
            p2-=1

        return nums1

if __name__ == '__main__':
    solution = Solution()
    # nums1 = [1,2,3,0,0,0]
    # nums2 = [2,5,6]
    nums1 = [0]
    nums2 = [1]

    solution.merge(nums1, 0,nums2,1)
    print(nums1)