"""
Problem
Given a list of integers and a target number, write a function that returns a boolean indicating if its possible to sum two integers from the list to reach the target number

"""


def twoSumpossible(lst, target):

    seen = set()

    for num in lst:
        num2 = target - num

        if num2 in seen:
            return True
        seen.add(num)

    return False
print(twoSumpossible([1,3,5,1,7],4))
