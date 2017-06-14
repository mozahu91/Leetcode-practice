Find and Sum 2 Closet Numbers in List to a Target Number
You are given a list of unique numbers and a target number. Return the sum of the two numbers that have the smallest diference to 
the target number.
You can assume the target number will not be in the list.

For example if you are given a list:
[-15, -14, -9, -28, -17, 0, 6, 7, -6, -29]
And a target number of 5.
The two numbers in the list with the smallest difference to the target number would be 6 and 7 so the function would return 13.

Or of the list was:
[21, 6, 27, 18]
And the target number was 15.
The two numbers in the list with the smallest difference to the target number would be 18 and 21 so the function would return 39.


arr = [-15, -14, -9, -28, -17, 0, 6, 7, -6, -29]
seen = []
k = 5

for num in arr:
    # Set target difference
    target = abs(k-num)
        
        # Add it to set if target hasn't been seen
    if target not in seen:
        seen.append((target,num))
l = sorted(seen)
sum = 0
for diff,num in l[:2]:
    sum += num
print(sum)


def twoClosehuh(arr, k):
    seen = {}
    for num in arr:
        target = abs(k-num)
    
        if target not in seen:
            seen[target] = num
    first2vals = [seen[k] for k in sorted(seen.keys())[:2]]
    sum =0
    for i in first2vals:
        sum +=i
    return sum
