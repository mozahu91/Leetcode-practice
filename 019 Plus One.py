"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
You may assume the integer do not contain any leading zero, except the number 0 itself.
"""

def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    if len(digits) == 0:
        digits = [1]
    elif digits[-1] == 9:
        digits = self.plusOne(digits[:-1])
        digits.extend([0])
    else:
        digits[-1] += 1
    return digits
