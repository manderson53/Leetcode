# doesn't pass completely not efficient enough for a really long string


# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # My solution - fails on very long strings (not efficient enough) n^3
        max_palindrome = ''
        length = len(s)
        substrings = []
        if length == 1:
            return s

        for i in range(0, length):
            temp = ''
            for j in range(i, length):
                temp += s[j]
                substrings.append(temp)

        for string in substrings:
            if Solution.isPalindrome(None, string):
                if len(string) > len(max_palindrome):
                    max_palindrome = string

        return max_palindrome


    def isPalindrome(self, s):
        reverse = s[::-1]
        if reverse == s:
            return True
        else:
            return False


if __name__ == '__main__':
    # example test cases
    testCandidates = ['babad', 'toyota', 'cbbd', 'aaaa', 'aaaaa', 'a']
    for testCandidate in testCandidates:
        print(Solution.longestPalindrome(None, testCandidate))