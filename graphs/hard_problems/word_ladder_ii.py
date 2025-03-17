# Word Ladder II
# https://takeuforward.org/plus/dsa/graph/hard-problems/word-ladder-ii
# https://leetcode.com/problems/word-ladder-ii/description/

from collections import deque

class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        wordSet = set(wordList)
        sequences = []
        # Queue stores tuples of (currentWord, sequence)
        queue = deque()
        queue.append((startWord, [startWord]))

        foundLevel = None  # Level when we found the target first time

        while queue:
            # Process a full level at a time
            levelSize = len(queue)
            # To record words visited in this level
            levelVisited = set()

            for _ in range(levelSize):
                currentWord, sequence = queue.popleft()

                # If we've already found a sequence and this path is longer, we can skip
                if foundLevel is not None and len(sequence) > foundLevel:
                    continue

                if currentWord == targetWord:
                    # Record the level (length of the sequence) when we first encountered the target.
                    if foundLevel is None:
                        foundLevel = len(sequence)
                    if len(sequence) == foundLevel:
                        sequences.append(sequence)
                    # No need to explore further for this path.
                    continue

                # Try changing each letter of the currentWord
                for i in range(len(currentWord)):
                    for c in range(ord('a'), ord('z')+1):
                        c = chr(c)
                        if currentWord[i] == c:
                            continue
                        newWord = currentWord[:i] + c + currentWord[i+1:]
                        if newWord in wordSet:
                            levelVisited.add(newWord)
                            queue.append((newWord, sequence + [newWord]))

            # Remove all words visited in this level from wordSet
            wordSet -= levelVisited

            # If we found the target at this level, we are done.
            if foundLevel is not None:
                break

        return sequences


if __name__ == "__main__":
    sol = Solution()
    # Test 1
    startWord = "hit"
    targetWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    output = [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]
    print(f"Expected output: {output}")
    print(f"Actual output: {sol.findSequences(startWord, targetWord, wordList)}")

    # Test 2
    startWord = "hit"
    targetWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    output = []
    print(f"Expected output: {output}")
    print(f"Actual output: {sol.findSequences(startWord, targetWord, wordList)}")
