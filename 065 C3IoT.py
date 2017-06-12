"""
Balanced Sum question asked in c3Iot hackerRank test

"""

def checkIfEqualOption(arr):

    sumTotal = 0
    for i in range(len(arr)):
        sumTotal += arr[i]

    sumRight = 0
    sumLeft = 0
    for i in range(1, len(arr)):
        sumLeft += arr[i-1]
        sumRight = sumTotal - arr[i] - sumLeft

        if sumRight == sumLeft:
            return i

arr = [1,2,3,6,3,3]

print(checkIfEqualOption(arr))
