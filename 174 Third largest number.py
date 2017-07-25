import heapq
def num(arr):
    return heapq.nlargest(3, set(arr)).pop()
