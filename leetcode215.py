'''
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
'''
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        end = len(nums) - 1
        return self.quick_search(nums, 0, end, k - 1)

    def partition(self, nums, start, end):
        import random

        random_idx = random.randint(start, end)
        self.swap(nums, random_idx, end)

        i = start - 1
        for j in range(start, end):
            if nums[j] > nums[end]:
                i = i + 1
                self.swap(nums, i, j)
        self.swap(nums, i + 1, end)
        return i + 1

    def quick_search(self, nums, start, end, k):
        idx = self.partition(nums, start, end)
        if idx == k:
            return nums[idx]

        if idx > k:
            return self.quick_search(nums, start, idx - 1, k)
        elif idx < k:
            return self.quick_search(nums, idx + 1, end, k)

    def swap(self, nums: List[int], i: int, j: int):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp


if __name__ == '__main__':
    num = [2,3]
    k=1
    solution = Solution()
    print(solution.findKthLargest(num, k))