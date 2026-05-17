# Time Complexity: O(4^(n/3)) | Space Complexity: O(4^(n/3))
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prevRLE = self.countAndSay(n - 1)

        newRLE = ""
        count = 1
        for i in range(1, len(prevRLE)):
            if prevRLE[i - 1] != prevRLE[i]:
                newRLE += str(count) + str(prevRLE[i - 1])
                count = 1
            else:
                count += 1

        if count > 0:
            newRLE += str(count) + str(prevRLE[-1])

        return newRLE


# Iterative Solution | Time Complexity: O(4^(n/3)) | Space Complexity: O(4^(n/3))
class Solution2:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        rle = "1"
        for _ in range(2, n + 1):
            newRLE = ""
            count = 1
            for i in range(1, len(rle)):
                if rle[i - 1] != rle[i]:
                    newRLE += str(count) + str(rle[i - 1])
                    count = 1
                else:
                    count += 1

            if count > 0:
                newRLE += str(count) + str(rle[-1])

            rle = newRLE

        return rle
