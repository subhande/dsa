# Letter Combination

from typing import List
class Solution:
    def letterCombinationsRecursive(self, digits: str, index: int, currCombination: list, validCombinations: list, digitToChar: dict):
        if index == len(digits):
            validCombinations.extend(currCombination)
            return
        for ch in digitToChar[digits[index]]:
            tempCombinations = []
            for comb in currCombination:
                tempCombinations.append(comb + ch)
            self.letterCombinationsRecursive(digits, index+1, tempCombinations, validCombinations, digitToChar)

    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        validCombinations = []
        if not digits:
            return []
        self.letterCombinationsRecursive(digits, 1, digitToChar[digits[0]], validCombinations, digitToChar)
        return validCombinations
# Time Complexity: O(n * 4^n) | Space Complexity: O(n)
class Solution2:
    def letterCombinationsRecursive(self, digits: str, index: int, path: str, validCombinations: list, digitToChar: dict):
        if index == len(digits):
            validCombinations.append(path)
            return
        for ch in digitToChar[digits[index]]:
            self.letterCombinationsRecursive(digits, index+1, path + ch, validCombinations, digitToChar)

    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        validCombinations = []
        if not digits:
            return []
        self.letterCombinationsRecursive(digits, 0, "", validCombinations, digitToChar)
        return validCombinations
