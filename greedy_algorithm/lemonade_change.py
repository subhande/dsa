# Lemonade Change
from typing import List
from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        total_bills = defaultdict(int)
        for bill in bills:
            if bill == 5:
                total_bills[bill] += 1
            elif bill == 10:
                if total_bills[5] >= 1:
                    total_bills[5] -= 1
                else:
                    return False
                total_bills[bill] += 1
            elif bill == 20:
                if total_bills[10] >= 1 and total_bills[5] >= 1:
                    total_bills[10] -= 1
                    total_bills[5] -= 1
                elif total_bills[5] >= 3:
                    total_bills[5] -= 3
                else:
                    return False
                total_bills[bill] += 1
        return True


class Solution2:
    """ Function to find whether each customer can
    be provided with correct change """
    def lemonadeChange(self, bills):

        # Counter for $5
        five = 0

        # Counter for $10
        ten = 0

        # Iterate through each customer's bill
        for bill in bills:

            # If the customer's bill is $5
            if bill == 5:
                # Increment $5
                five += 1

            # If the customer's bill is $10
            elif bill == 10:
                # Check if there are $5 bills available to give change
                if five > 0:
                    # Use one $5
                    five -= 1
                    # Receive one $10
                    ten += 1
                else:
                    # If no $5 bill available, return false
                    return False

            # If the customer's bill is $20
            else:
                # Check if there are both $5 and $10 bills available to give change
                if five > 0 and ten > 0:
                    # Use one $5
                    five -= 1
                    # Use one $10
                    ten -= 1
                # If there are not enough $10 bills,
                # check if there are at least three $5 bills available
                elif five >= 3:
                    # Use three $5 bills
                    five -= 3
                else:
                    # If unable to give change, return false
                    return False

        # Return true
        return True
