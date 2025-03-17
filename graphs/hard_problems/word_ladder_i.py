# Word Ladder I
# https://takeuforward.org/plus/dsa/graph/hard-problems/word-ladder-i
# https://leetcode.com/problems/word-ladder/editorial/

from collections import deque

class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):

        queue = deque([(startWord, 1)])

        wordListSet = set(wordList)

        wordListSet.discard(startWord)

        while queue:
            currentWord, length = queue.popleft()

            if currentWord == targetWord:
                return length

            for i in range(len(currentWord)):

                currChar = currentWord[i]

                for ch in range(ord('a'), ord('z') + 1):
                    newChar = chr(ch)

                    if currChar == newChar:
                        continue

                    newWord = currentWord[:i] + newChar + currentWord[i + 1:]

                    if newWord in wordListSet:
                        queue.append((newWord, length + 1))
                        wordListSet.remove(newWord)

        return 0
