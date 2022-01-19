
#https://leetcode.com/problems/longest-common-prefix/

# had to look up solutions, my initial solution was to have a prefix counter and then slice the correct amount off of
# strs[0]. This didn't work because of the case where a letter could match later in the word. example 'flower', 'fkow'
# the f would match but the o would also match giving a count of 2 instead of 1.

# solution was kind of similar to my initial thought of just testing each letter at once and appending until it doesn't
# match but I did not know about the all() function in python. So I did look up the solution before getting this correct
# but I learned about a new function.


class Solution:
    def longestPrefix(self, strs):
        if len(strs) == 0:
            return ''
        longest_prefix = ''

        for index in range(len(min(strs))):
            if len(strs[0]) > 0:
                character = strs[0][index]
                if all(a[index] == character for a in strs):
                    longest_prefix += character
                else:
                    break

        return longest_prefix


if __name__ == '__main__':
    # example test cases
    testCandidates = [['flower', 'flow', 'flight'], ['dog', 'racecar', 'car'], ['a'], ['flower', 'fkow'], [''], ['', ''], ['ab', 'a']]
    for testCandidate in testCandidates:
        print('' + str(testCandidate) + ' : ' + Solution.longestPrefix(None, testCandidate))