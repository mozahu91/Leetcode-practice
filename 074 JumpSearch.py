"""



Like Binary Search, Jump Search is a searching algorithm for sorted arrays. The basic idea is to check fewer elements 
(than linear search) by jumping ahead by fixed steps or skipping some elements in place of searching all elements.
For example, suppose we have an array arr[] of size n and block (to be jumped) size m. Then we search at the indexes arr[0],
arr[m], arr[2m]…..arr[km] and so on. Once we find the interval (arr[km] < x < arr[(k+1)m]), 
we perform a linear search operation from the index km to find the element x.
Time Complexity : O(√n) Auxiliary Space : O(1)
Important points: Works only sorted arrays. The optimal size of a block to be jumped is O(√ n). 
This makes the time complexity of Jump Search O(√ n). The time complexity of Jump Search is between Linear Search ( ( O(n) )
and Binary Search ( O (Log n) ). Binary Search is better than Jump Search, but Jump search has an advantage that we 
traverse back only once (Binary Search may require up to O(Log n) jumps, consider a situation where the element to be search
is the smallest element or smaller than the smallest). So in a systems where jumping back is costly, we use Jump Search.
"""
