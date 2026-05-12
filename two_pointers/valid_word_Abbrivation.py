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


class Solution2:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        word_idx = 0
        abbr_idx = 0

        word_len = len(word)
        abbr_len = len(abbr)

        skip = 0

        if abbr_len > word_len:
            return False

        while word_idx < word_len and abbr_idx < abbr_len:
            while abbr_idx < abbr_len and abbr[abbr_idx].isnumeric():
                if skip == 0 and int(abbr[abbr_idx]) == 0:
                    return False
                skip = skip * 10 + int(abbr[abbr_idx])
                abbr_idx += 1

            word_idx += skip
            skip = 0

            if word_idx >= word_len or abbr_idx >= abbr_len:
                break

            if word[word_idx] != abbr[abbr_idx]:
                return False

            word_idx += 1
            abbr_idx += 1
        return word_idx == word_len and abbr_idx == abbr_len
