from typing import List

#https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = 0
        for sentence in sentences:
            words = sentence.split(' ')
            count = len(words)
            if count > result:
                result = count
        return result


if __name__ == '__main__':
    # example test cases
    testCandidates = [["alice and bob love leetcode", "i think so too", "this is great thanks very much"], ["please wait", "continue to fight", "continue to win"]]
    for testCandidate in testCandidates:
        print(Solution.mostWordsFound(None, testCandidate))