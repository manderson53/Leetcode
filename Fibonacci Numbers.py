# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            result = Solution.fib(None, n-1) + Solution.fib(None, n-2)
        return result


if __name__ == '__main__':
    # example test cases
    testCandidates = [2, 3, 4]
    for testCandidate in testCandidates:
        print(Solution.fib(None, testCandidate))