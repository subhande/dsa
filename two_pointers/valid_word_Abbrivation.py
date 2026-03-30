# Valid Word Abbrivation


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_ptr = 0
        abbr_ptr = 0
        while word_ptr < len(word) and abbr_ptr < len(abbr):
            if abbr[abbr_ptr].isalpha():
                if word[word_ptr] != abbr[abbr_ptr]:
                    return False
                word_ptr += 1
                abbr_ptr += 1
            else:
                digit = ""
                while abbr_ptr < len(abbr):
                    if abbr[abbr_ptr].isnumeric():
                        digit += abbr[abbr_ptr]
                        abbr_ptr += 1
                    else:
                        break
                if digit[0] == "0":
                    return False
                digit = int(digit)
                if digit > len(word) - word_ptr:
                    return False
                word_ptr += digit
        return True if abbr_ptr == len(abbr) and word_ptr == len(word) else False
