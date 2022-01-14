class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev_x = str(x)[::-1]
        if str(x) == rev_x:
            return True
        else:
            return False


if __name__ == '__main__':
    # example test cases
    testCandidates = [121, -121, 10]
    for testCandidate in testCandidates:
        print(Solution.isPalindrome(None, testCandidate))