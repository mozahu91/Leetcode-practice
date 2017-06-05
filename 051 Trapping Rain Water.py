+"""
+Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
+
+For example, 
+Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
+
+
+"""
+
+def trap(arr):
+    
+    
+    height, left, right, water = [], 0, 0, []
+    for i in arr:
+        left = max(left, i)
+        height.insert(0,left)
+    #print(height)
+    #height.reverse()
+    print(height)
+    
+    for n, i in enumerate(reversed(arr)):
+        right = max(right, i)
+        res = min(height[n], right) - i
+        water.append(res)
+    return water
