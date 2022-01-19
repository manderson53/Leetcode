from typing import List

#https://leetcode.com/problems/build-array-from-permutation/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        for index in nums:
            result.append(nums[index])
        return result



if __name__ == '__main__':
    # example test cases
    testCandidates = [[0, 2, 1, 5, 3, 4], [5, 0, 1, 2, 3, 4]]
    for testCandidate in testCandidates:
        print(Solution.buildArray(None, testCandidate))