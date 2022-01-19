from typing import List

#https://leetcode.com/problems/concatenation-of-array/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            nums.append(nums[index])
        return nums


if __name__ == '__main__':
    # example test cases
    testCandidates = [[1, 2, 1], [1, 3, 2, 1]]
    for testCandidate in testCandidates:
        print(Solution.getConcatenation(None, testCandidate))