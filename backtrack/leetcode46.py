'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
'''
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        self.ret = []

        def back_track(nums, track):
            if len(track) == len(nums):
                self.ret.append(track.copy())
                return

            for i in nums:
                if i in track:
                    continue
                track.append(i)
                back_track(nums, track)
                track.pop()
        track = []
        back_track(nums, track)

        return self.ret




if __name__ == '__main__':
    nums = [1,2,3]
    solution = Solution()
    print(solution.permute(nums))

