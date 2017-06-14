"""
Given a binary tree of integers, print it in level order. The output will contain space between the numbers in the same level, and new line between different levels. For example, if the tree is:
The output should be:
1
2 3
4 5 6
ALgorithm:
Solved using a Double ended queue
Saved root in deque, currcount, nextcount =1,0
len(nodes) != 0, popped left, dec count, printted current node, if leftchild append, if right child append
Check if currcount = 0, tuple unpacking for exchanging the counts
"""

import collections
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val =  val 

def levelOrderPrint(tree):
    if not tree:
        return
    nodes=collections.deque([tree])
    currentCount, nextCount = 1, 0
    while len(nodes)!=0:
        currentNode=nodes.popleft()
        currentCount-=1
        #print(currentCount)
        print(currentNode.val,end=" ")
        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount+=1
        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount+=1
        if currentCount==0:
            #finished printing current level
            print('\n',end="")
            currentCount, nextCount = nextCount, currentCount
            
c = Node(1)
c.left = Node(2)
c.left.left = Node(4)
c.right = Node(3)
c.right.left = Node(5)
c.right.right = Node(6)
levelOrderPrint(c)
