from typing import List

#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force
        # length = len(nums)
        # for indexA in range(0, length):
        #     for indexB in range(1, length):
        #         if (nums[indexA] + nums[indexB] == target and indexA != indexB):
        #             return [indexA, indexB]

        length = len(nums)
        for indexA in range(0, length):
            targetValue = target - nums[indexA]
            if targetValue in nums:
                targetIndex = nums.index(targetValue)
                if (nums[indexA] + nums[targetIndex] == target and indexA != targetIndex):
                    return [indexA, targetIndex]


if __name__ == '__main__':
    # example test cases
    numsArr = [[2, 7, 11, 15], [3, 2, 4], [3, 3]]
    targetArr = [9, 6, 6]
    i = 0
    for nums in numsArr:
        print(Solution.twoSum(None, nums, targetArr[i]))
        i += 1