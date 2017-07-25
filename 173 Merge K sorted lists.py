class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))

        temp = ListNode(-1)
        head = temp
        while heap:
            smallestNode = heapq.heappop(heap)[1]
            temp.next = smallestNode
            temp = temp.next
            if smallestNode.next:
                heapq.heappush(heap, (smallestNode.next.val, smallestNode.next))
        return head.next
