'''
	Determine if a cycle exist on a given linked list
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            currentHead = head
            futureHead = head.next
            while currentHead is not futureHead:
                currentHead = currentHead.next
                futureHead = futureHead.next.next
            return True
        except:
            return False
        

