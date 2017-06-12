"""
This question was asked in one of technical phone interview with eShares.
Find the N minimum and N maximum terms of an array, given an unsorted list
"""

def min_max(sequence, N):

    sequence.sort()
    min = []
    max = []
    min_max = []

    for i in range(N):
        min.append(sequence[i])
    min_max.append(min)

    for i in range(N+1, len(sequence)):
        max.append(sequence[i])

    min_max.append(max)

    return min_max

sequence = [1,2,3,4,5]
print(min_max(sequence,2))
