'''
从大到小快排
'''
from typing import List
import random

class Solution:

    def partition(self, nums, start, end):


        random_idx = random.randint(start, end)

        self.swap(nums, random_idx, end)

        i = start - 1
        for j in range(start, end):
            if nums[j] < nums[end]:
                i +=1
                self.swap(nums, i, j)
        self.swap(nums, i+1, end)

        return i+1

    def quick_sort(self, nums, start, end):
        if start < end:
            k = self.partition(nums, start, end)
            self.quick_sort(nums, start, k-1)
            self.quick_sort(nums, k+1, end)



    def swap(self, nums: List[int], i: int, j: int):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp


if __name__ == '__main__':
    nums = [5,4,3,2,1]
    k=1
    solution = Solution()
    solution.quick_sort(nums, 0, len(nums)-1)

    print(nums)