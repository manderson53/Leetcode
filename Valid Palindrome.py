
# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = s.lower()
        for char in s:
            if not char.isalnum():
                s = s.replace(char, '')
        if s[::-1] == s:
            return True
        else:
            return False



if __name__ == '__main__':
    # example test cases
    testCandidates = ['A man, a plan, a canal: Panama', 'race a car', ' ',]
    for testCandidate in testCandidates:
        print(Solution.validPalindrome(None, testCandidate))