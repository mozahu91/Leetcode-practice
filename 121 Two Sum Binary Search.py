def twoSumBinarySearch(numbers, target):
    for i in range(len(numbers)):
        l, r = i, len(numbers)-1
        tmp = target - numbers[i]
        while l <= r:
            mid = l + (r-l)//2
            if numbers[mid] == tmp:
                return [i, mid]
            elif numbers[mid] < tmp:
                l = mid+1
            else:
                r = mid-1
