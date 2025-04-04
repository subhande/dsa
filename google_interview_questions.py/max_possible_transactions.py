# https://leetcode.com/discuss/post/5563819/google-onsite-l4-by-anonymous_user-a0uh/
"""
Max possible transactions - you are given an array which has transaction amounts.Along with a initial total 'T' . if tx amount < 0 , you are making deposit, if tx amount is positive you are withdrawing.
Once you reach a stage where you cant withdraw more you have to stop. Find max number of tx which can be done by you.
eg arr = [-2 -3 4 1 132 ] T =0
output - 4
arr = [ -2 5 1 3 2 -3 -1 4 1 ] T = 5
output - 5

"""
# Brute Force Approach
# Time Complexity: O(N^2) | Space Complexity: O(1)
class Solution:
    def maxPossibleTransactionsHelper(self, arr, T, idx):
        """
        Function to calculate the maximum number of transactions possible.
        """
        transactions = 0
        currBalance = T
        for amount_idx in range(idx, len(arr)):
            amount = arr[amount_idx]
            if amount < 0:
                # Deposit
                currBalance += abs(amount)
                transactions += 1
            else:
                # Withdrawal
                if currBalance >= amount:
                    currBalance -= amount
                    transactions += 1
                else:
                    break
        return transactions

    def maxPossibleTransactions(self, arr, T):
        """
        Function to find the maximum number of transactions possible.
        """
        max_transactions = 0
        for i in range(len(arr)):
            transactions = self.maxPossibleTransactionsHelper(arr, T, i)
            max_transactions = max(max_transactions, transactions)
        return max_transactions


if __name__ == "__main__":
    # Example usage
    arr = [-2, -3, 4, 1, 132]
    T = 0
    print(Solution().maxPossibleTransactions(arr, T))  # Output: 4

    arr = [-2, 5, 1, 3, 2, -3, -1, 4, 1]
    T = 5
    print(Solution().maxPossibleTransactions(arr, T))  # Output: 5
