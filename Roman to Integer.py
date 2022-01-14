
#https://leetcode.com/problems/roman-to-integer/

# I struggled with this more than I should have because I didn't realize things like LC were not valid roman numerals
# one of the constraints in the problem is 'It is guaranteed that s is a valid roman numeral in the range [1, 3999]
# So I didn't realize you could just subtract the one before adding the 5 for IV because that doesn't work for LC
# (an invalid roman numeral) LC doesn't subtract from 100 so in theory it's 150 but this program returns 50
# Long story short I briefly looked up solutions to this one before submitting.

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for numeral_index in range(0, len(s)):
            if numeral_index + 1 != len(s):
                if roman_numerals_dict.get(s[numeral_index]) >= roman_numerals_dict.get(s[numeral_index+1]):
                    result += roman_numerals_dict.get(s[numeral_index])
                else:
                    result -= roman_numerals_dict.get(s[numeral_index])
            else:
                result += roman_numerals_dict.get(s[numeral_index])
        return result


if __name__ == '__main__':
    # example test cases
    testCandidates = ['III', 'LVIII', 'MCMXCIV']
    for testCandidate in testCandidates:
        print(Solution.romanToInt(None, testCandidate))
